#!/usr/bin/env python3
"""Sync ielab member publication records into _data/.

Ground truth: each member's **Google Scholar profile** (the `scholar` key in
their _people/ file). A snapshot of every profile lives in
_data/scholar_profiles.json; the member's site list contains exactly those
papers (from ielab's founding year onwards), enriched with rich metadata
(full author lists, venues, open-access PDF links) from **OpenAlex** via the
`openalex` author-ID key. Scholar papers with no OpenAlex match are shown as
stubs built from the Scholar data itself, so nothing is missing.

Modes:
  python3 _scripts/update_publications.py             # refresh _data/openalex.json
  python3 _scripts/update_publications.py --scholar   # refresh _data/scholar_profiles.json
  python3 _scripts/update_publications.py --discover  # suggest OpenAlex author IDs

--scholar backends:
  * SERPAPI_KEY set      -> SerpApi google_scholar_author API (use this in CI;
                            a full refresh of ~35 profiles costs ~50 of the
                            100 free searches/month, so run it monthly).
  * SERPAPI_KEY unset    -> direct fetch from scholar.google.com. Works from
                            residential IPs (run locally); Google blocks
                            datacenter IPs, so this path refuses to run in CI.

Members without a Scholar snapshot fall back to their full OpenAlex record
cleaned by an institution-based namesake filter (`openalex_filter: off`
disables it). Runs on the Python standard library only.
Be polite to the free OpenAlex API: set OPENALEX_MAILTO=you@example.com.
"""

import difflib
import html as html_mod
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = ROOT / "_people"
PUBS_DIR = ROOT / "_publications"
OUT_FILE = ROOT / "_data" / "openalex.json"
SCHOLAR_FILE = ROOT / "_data" / "scholar_profiles.json"

API = "https://api.openalex.org"
MAILTO = os.environ.get("OPENALEX_MAILTO", "").strip()
SERPAPI_KEY = os.environ.get("SERPAPI_KEY", "").strip()
IN_CI = os.environ.get("GITHUB_ACTIONS", "") == "true"

MIN_YEAR = 2019  # ielab founding year - earlier publications are not shown
MAX_WORKS_PER_MEMBER = 500
MAX_AUTHORS_PER_WORK = 12
SCHOLAR_PAGE_SIZE = 100
EXCLUDED_TYPES = {"paratext", "erratum", "retraction", "peer-review", "grant", "libguides"}
BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# ---------------------------------------------------------------- helpers


def get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "ielab.io publication sync"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                raise
            wait = 2 ** (attempt + 1)
            print(f"    retrying in {wait}s ({exc})", file=sys.stderr)
            time.sleep(wait)


def api_get(path, params):
    params = dict(params)
    if MAILTO:
        params["mailto"] = MAILTO
    return get_json(f"{API}{path}?{urllib.parse.urlencode(params)}")


def http_text(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": BROWSER_UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "CONSENT=YES+cb; SOCS=CAESEwgDEgk0ODE3Nzk3MjQaAmVuIAEaBgiA_LyaBg",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def load_json_file(path):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


# Jekyll parses _data/*.json with its YAML parser, which rejects raw
# control/C1 characters AND \uXXXX surrogate-pair escapes (produced by
# ensure_ascii for emoji/math symbols). So: strip control characters and
# write plain UTF-8.
_CTRL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")


def sanitize(obj):
    if isinstance(obj, str):
        return _CTRL_CHARS.sub("", obj)
    if isinstance(obj, list):
        return [sanitize(item) for item in obj]
    if isinstance(obj, dict):
        return {key: sanitize(value) for key, value in obj.items()}
    return obj


def write_data_file(path, payload, **dump_kwargs):
    path.parent.mkdir(exist_ok=True)
    path.write_text(
        json.dumps(sanitize(payload), ensure_ascii=False, sort_keys=True, **dump_kwargs) + "\n",
        encoding="utf-8",
    )


def front_matter(path):
    """Parse simple `key: value` pairs from a file's YAML front matter."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip("\"'")
    return fields


def scholar_user_id(url):
    match = re.search(r"user=([\w-]+)", url or "")
    return match.group(1) if match else ""


def members():
    out = []
    for path in sorted(PEOPLE_DIR.glob("*.md")):
        fm = front_matter(path)
        role = (fm.get("role") or "").lower()
        is_alumni = "alumni" in role or (fm.get("alumni") or "").lower() == "true"
        is_external = "external" in role
        out.append({
            "slug": path.stem,
            "path": path,
            "name": fm.get("name", path.stem),
            "openalex": (fm.get("openalex") or "").strip(),
            "scholar_id": scholar_user_id(fm.get("scholar", "")),
            # Core members are current staff/students. Alumni and external
            # members' papers appear on their own pages and via search, but
            # not in the default lab-wide listings or headline counts.
            "core": not (is_alumni or is_external),
            # `openalex_filter: off` disables namesake filtering for members
            # with distinctive names whose careers span many institutions.
            "filter_off": (fm.get("openalex_filter") or "").strip().lower() == "off",
        })
    return out


def local_pub_titles(slug, limit=4):
    """Titles of local _publications that list this member slug as an author."""
    titles = []
    for path in sorted(PUBS_DIR.glob("*.md")):
        fm_text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---", fm_text, re.DOTALL)
        if not match:
            continue
        block = match.group(1)
        authors = re.search(r"^authors:\s*\[(.*?)\]\s*$", block, re.MULTILINE)
        title = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", block, re.MULTILINE)
        if not authors or not title:
            continue
        if re.search(rf"(^|[,\s\[]){re.escape(slug)}([,\s\]]|$)", authors.group(1)):
            titles.append(title.group(1))
            if len(titles) >= limit:
                break
    return titles


def surname(name):
    return name.split()[-1].lower() if name.split() else ""


def norm_title(title):
    return re.sub(r"\W+", "", title.lower())


# ---------------------------------------------------------------- discover


def discover():
    """Suggest an OpenAlex author ID for each member that doesn't have one.

    Strategy: look up the member's local publications by title on OpenAlex and
    take the author ID that recurs in matching authorships (precise even for
    very common names). Fall back to an author name search.
    """
    print(f"{'slug':28} {'suggested ID':14} {'works':>5}  matched name / note")
    print("-" * 90)
    for member in members():
        if member["openalex"]:
            continue
        votes = {}
        for title in local_pub_titles(member["slug"]):
            clean = re.sub(r"[^\w\s]", " ", title)
            try:
                data = api_get("/works", {"search": clean, "per-page": "3"})
            except Exception as exc:
                print(f"{member['slug']:28} ERROR searching works: {exc}")
                continue
            for work in data.get("results", []):
                for auth in work.get("authorships", []):
                    disp = (auth.get("author") or {}).get("display_name") or ""
                    if surname(disp) == surname(member["name"]):
                        aid = ((auth.get("author") or {}).get("id") or "").rsplit("/", 1)[-1]
                        if aid:
                            votes.setdefault(aid, {"n": 0, "name": disp})
                            votes[aid]["n"] += 1
            time.sleep(0.15)

        if votes:
            best = max(votes.items(), key=lambda kv: kv[1]["n"])
            aid, info = best
            try:
                author = api_get(f"/authors/{aid}", {})
                count = author.get("works_count", "?")
            except Exception:
                count = "?"
            print(f"{member['slug']:28} {aid:14} {count:>5}  {info['name']} "
                  f"(matched in {info['n']} title lookup(s))")
            continue

        # No local publications matched - try a plain author search.
        try:
            data = api_get("/authors", {"search": member["name"], "per-page": "3"})
            results = data.get("results", [])
        except Exception as exc:
            print(f"{member['slug']:28} ERROR searching authors: {exc}")
            continue
        if not results:
            print(f"{member['slug']:28} {'-':14} {'-':>5}  no match found - set manually")
            continue
        top = results[0]
        aff = ((top.get("last_known_institutions") or [{}])[0] or {}).get("display_name", "?")
        print(f"{member['slug']:28} {top['id'].rsplit('/', 1)[-1]:14} {top.get('works_count', '?'):>5}  "
              f"{top.get('display_name')} @ {aff}  [NAME SEARCH - verify!]")
        time.sleep(0.15)


# ------------------------------------------------- Google Scholar snapshot


def fetch_scholar_serpapi(user_id):
    """All publications on a Scholar profile, via the SerpApi author API.
    Returns (pubs, number_of_api_requests_used)."""
    pubs, start, used = [], 0, 0
    while True:
        params = urllib.parse.urlencode({
            "engine": "google_scholar_author",
            "author_id": user_id,
            "api_key": SERPAPI_KEY,
            "num": SCHOLAR_PAGE_SIZE,
            "start": start,
            "hl": "en",
        })
        data = get_json(f"https://serpapi.com/search.json?{params}")
        used += 1
        if data.get("error"):
            raise RuntimeError(f"SerpApi: {data['error']}")
        articles = data.get("articles") or []
        for art in articles:
            year_str = str(art.get("year") or "")
            pubs.append({
                "title": (art.get("title") or "").strip(),
                "year": int(year_str) if year_str.isdigit() else 0,
                "authors": (art.get("authors") or "").strip(),
                "venue": (art.get("publication") or "").strip(),
                "url": art.get("link") or "",
                "cited": ((art.get("cited_by") or {}).get("value")) or 0,
            })
        if len(articles) < SCHOLAR_PAGE_SIZE:
            break
        start += SCHOLAR_PAGE_SIZE
        time.sleep(1.0)
    return pubs, used


def fetch_scholar_direct(user_id):
    """All publications on a Scholar profile, scraped from the public profile
    page. Low-volume and throttled; works from residential IPs only."""
    pubs, cstart = [], 0
    while True:
        url = (f"https://scholar.google.com/citations?user={user_id}"
               f"&hl=en&cstart={cstart}&pagesize={SCHOLAR_PAGE_SIZE}")
        page = http_text(url)
        if "gsc_a_tr" not in page:
            if cstart == 0:
                raise RuntimeError("profile empty/private, or Google served a block page")
            break
        rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.DOTALL)
        added = 0
        for row in rows:
            tag = re.search(r'(<a\b[^>]*class="gsc_a_at"[^>]*>)(.*?)</a>', row, re.DOTALL)
            if not tag:
                continue  # placeholder row ("there are no articles")
            title = html_mod.unescape(re.sub(r"<[^>]+>", "", tag.group(2))).strip()
            href = re.search(r'href="([^"]+)"', tag.group(1))
            link = html_mod.unescape(href.group(1)) if href else ""
            if link.startswith("/"):
                link = "https://scholar.google.com" + link
            grays = [html_mod.unescape(re.sub(r"<[^>]+>", " ", g)).strip()
                     for g in re.findall(r'<div class="gs_gray">(.*?)</div>', row, re.DOTALL)]
            year_m = re.search(r'<span class="gsc_a_h[^"]*">(\d{4})</span>', row)
            cited_m = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d+)', row)
            venue = grays[1] if len(grays) > 1 else ""
            venue = re.sub(r"[,\s]*\d{4}\s*$", "", venue).rstrip(" ,…").strip()
            pubs.append({
                "title": title,
                "year": int(year_m.group(1)) if year_m else 0,
                "authors": grays[0] if grays else "",
                "venue": venue,
                "url": link,
                "cited": int(cited_m.group(1)) if cited_m else 0,
            })
            added += 1
        if added < SCHOLAR_PAGE_SIZE:
            break
        cstart += SCHOLAR_PAGE_SIZE
        time.sleep(1.5)
    return pubs


def scholar_mode():
    existing = load_json_file(SCHOLAR_FILE)
    if not SERPAPI_KEY and IN_CI:
        print("ERROR: refreshing Scholar profiles in CI needs the SERPAPI_KEY secret -\n"
              "Google blocks direct Scholar requests from datacenter IPs.\n"
              "Add the secret (Settings -> Secrets -> Actions) or run this locally.",
              file=sys.stderr)
        sys.exit(1)

    targets = [m for m in members() if m["scholar_id"]]
    backend = "SerpApi" if SERPAPI_KEY else "direct fetch (residential IP)"
    print(f"Refreshing Google Scholar profiles for {len(targets)} members via {backend}…")

    out, failures, api_requests = {}, [], 0
    today = time.strftime("%Y-%m-%d")
    for member in targets:
        try:
            if SERPAPI_KEY:
                pubs, used = fetch_scholar_serpapi(member["scholar_id"])
                api_requests += used
            else:
                pubs = fetch_scholar_direct(member["scholar_id"])
                time.sleep(2.0)
            out[member["slug"]] = {
                "user": member["scholar_id"],
                "fetched": today,
                "count": len(pubs),
                "pubs": pubs,
            }
            print(f"  {member['slug']:28} {len(pubs):>4} publications on profile")
        except Exception as exc:
            failures.append(member["slug"])
            kept = " - keeping previous snapshot" if member["slug"] in existing else ""
            print(f"  {member['slug']:28} FAILED ({exc}){kept}", file=sys.stderr)
            if member["slug"] in existing:
                out[member["slug"]] = existing[member["slug"]]

    write_data_file(SCHOLAR_FILE, out, indent=1)
    print(f"Wrote {SCHOLAR_FILE.relative_to(ROOT)} ({len(out)} members)")
    if SERPAPI_KEY:
        print(f"SerpApi requests used this run: {api_requests}")
    if failures:
        print(f"WARNING: failed members: {', '.join(failures)}", file=sys.stderr)
        if len(failures) == len(targets):
            sys.exit(2)


# ---------------------------------------------------------------- fetch


_GRAPHIC_MARKER = re.compile(r"\[inline-graphic[^\]]*\]", re.IGNORECASE)
_EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF"
                    "\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F\U0001F1E6-\U0001F1FF]+")


def clean_title(title):
    """Normalise messy titles from OpenAlex and Google Scholar:
    - drop "[inline-graphic …]" placeholders and emoji (a paper with an emoji
      in its title renders differently on every source - alt text, a
      placeholder, or the raw emoji - creating spurious variants of one work);
    - for very long multi-sentence titles (figure alt-text that OpenAlex and
      Scholar sometimes prepend, e.g. 'A sketch of a coffee cup ... detail.
      Starbucks: Improved Training…') keep only the final sentence, since
      real titles of that shape are vanishingly rare."""
    title = _GRAPHIC_MARKER.sub(" ", title)
    title = _EMOJI.sub(" ", title)
    title = re.sub(r"\s+", " ", title).strip()
    if len(title) > 160 and ". " in title:
        candidate = title.rsplit(". ", 1)[-1].lstrip("—–- ").strip()
        if len(candidate) >= 15:
            return candidate
    return title


def authorship_of(work, author_id):
    for auth in work.get("authorships") or []:
        aid = ((auth.get("author") or {}).get("id") or "").rsplit("/", 1)[-1]
        if aid == author_id:
            return auth
    return None


def slot_institutions(authorship):
    if not authorship:
        return set()
    return {((inst or {}).get("id") or "").rsplit("/", 1)[-1]
            for inst in authorship.get("institutions") or [] if inst}


def filter_namesakes(raw_works, author_id, lab_ids):
    """Drop works that belong to a namesake merged into the same OpenAlex
    author cluster (fallback path for members without a Scholar snapshot).
    Trust is calibrated per member: institutions seen on works co-authored
    with other ielab members are trusted; works whose member-slot
    institutions are all outside that set are dropped. Works with another
    ielab co-author are always kept. If no trusted institutions can be
    derived, keep everything."""
    others = lab_ids - {author_id}

    def coauthor_ids(work):
        return {((a.get("author") or {}).get("id") or "").rsplit("/", 1)[-1]
                for a in work.get("authorships") or []}

    def coauthor_names(work):
        """Display names of every author on the work EXCEPT the member."""
        names = set()
        for a in work.get("authorships") or []:
            author = a.get("author") or {}
            aid = (author.get("id") or "").rsplit("/", 1)[-1]
            if aid != author_id and author.get("display_name"):
                names.add(author["display_name"])
        return names

    trusted_insts = set()
    trusted_names = set()
    for work in raw_works:
        if coauthor_ids(work) & others:
            trusted_insts |= slot_institutions(authorship_of(work, author_id))
            trusted_names |= coauthor_names(work)
    if not trusted_insts:
        return raw_works

    kept = []
    for work in raw_works:
        if coauthor_ids(work) & others:
            kept.append(work)
            continue
        insts = slot_institutions(authorship_of(work, author_id))
        if insts:
            if insts & trusted_insts:
                kept.append(work)
        # No parsed affiliation (common for preprints): trust the work only
        # if it shares a co-author with the member's verified papers.
        elif coauthor_names(work) & trusted_names:
            kept.append(work)
    return kept


def clean_work(work):
    wtype = work.get("type") or ""
    title = clean_title((work.get("display_name") or "").strip())
    year = work.get("publication_year") or 0
    if not title or wtype in EXCLUDED_TYPES or year < MIN_YEAR:
        return None
    source = ((work.get("primary_location") or {}).get("source") or {})
    venue = (source.get("display_name") or "").strip()
    authorships = work.get("authorships") or []
    authors = []
    for auth in authorships[:MAX_AUTHORS_PER_WORK]:
        disp = ((auth.get("author") or {}).get("display_name") or "").strip()
        if disp:
            authors.append(disp)
    oa = work.get("open_access") or {}
    doi = work.get("doi") or ""
    landing = (work.get("primary_location") or {}).get("landing_page_url") or ""
    return {
        "title": title,
        "year": year,
        "venue": venue,
        "type": wtype,
        "url": doi or landing,
        "pdf": oa.get("oa_url") or "",
        "authors": authors,
        "etal": len(authorships) > MAX_AUTHORS_PER_WORK,
        "cited": work.get("cited_by_count") or 0,
    }


def scholar_stub(pub):
    """Site entry built from Scholar profile data alone (no OpenAlex match)."""
    url = pub.get("url") or ""
    return {
        "title": pub["title"],
        "year": pub["year"],
        "venue": (pub.get("venue") or "").rstrip(" ,…"),
        "type": "scholar",
        "url": url,
        "pdf": "",
        "authors": [pub["authors"]] if pub.get("authors") else [],
        "etal": False,
        "cited": pub.get("cited") or 0,
    }


def match_scholar(scholar_pubs, raw_works):
    """Build a member's publication list with their Google Scholar profile as
    ground truth: every Scholar entry from MIN_YEAR onwards appears exactly
    once - enriched with OpenAlex metadata when a title match exists,
    otherwise as a stub from the Scholar data itself. Scholar profiles
    occasionally list the same work twice (typically emoji-in-title variants);
    rows that resolve to an already-matched work are dropped as duplicates."""
    cleaned, raw_index = [], []
    for raw in raw_works:
        work = clean_work(raw)
        if work:
            cleaned.append(work)
            raw_index.append((norm_title(raw.get("display_name") or ""), work))
    buckets = {}
    for work in cleaned:
        buckets.setdefault(norm_title(work["title"]), []).append(work)
    keys = list(buckets)

    out, used = [], set()
    for pub in scholar_pubs:
        raw_title = (pub.get("title") or "").strip()
        title = clean_title(raw_title)
        if not title or pub.get("year", 0) < MIN_YEAR:
            continue
        pub = dict(pub)
        pub["title"] = title
        key = norm_title(title)
        cands = buckets.get(key)
        if not cands:
            close = difflib.get_close_matches(key, keys, n=1, cutoff=0.9)
            # digit guard: "… Lab 2019" must never fuzzy-match "… Lab 2020"
            # (series papers differ only in the year digit)
            if close and re.findall(r"\d+", close[0]) == re.findall(r"\d+", key):
                cands = buckets.get(close[0])
        if not cands and raw_title.endswith(("…", "...")):
            # Scholar truncated the title mid-way; match it as a prefix of
            # the raw (pre-cleaning) OpenAlex titles instead.
            prefix = norm_title(raw_title)
            if len(prefix) >= 30:
                cands = [w for nraw, w in raw_index if nraw.startswith(prefix)] or None
        pick = None
        scholar_dupe = False
        if cands:
            avail = [w for w in cands if id(w) not in used]
            if avail:
                avail.sort(key=lambda w: (w["year"] != pub["year"],
                                          w["venue"].lower().startswith("arxiv"),
                                          -w["cited"]))
                pick = avail[0]
            else:
                scholar_dupe = True  # profile lists the same work again
        if pick is not None:
            used.add(id(pick))
            # keep a meaningfully different Scholar title searchable
            # (e.g. "Evalugator — …" matched to the OpenAlex "Rapid, Agile …")
            if norm_title(pick["title"]) != key and not pick.get("alt"):
                pick["alt"] = title
            out.append(pick)
        elif not scholar_dupe:
            out.append(scholar_stub(pub))
    return out


def fetch():
    existing = load_json_file(OUT_FILE)
    scholar_cache = load_json_file(SCHOLAR_FILE)

    out = {}
    failures = []
    today = time.strftime("%Y-%m-%d")
    all_members = members()
    core_by_slug = {m["slug"]: m["core"] for m in all_members}
    targets = [m for m in all_members
               if m["openalex"] or (scholar_cache.get(m["slug"]) or {}).get("pubs")]
    lab_ids = {m["openalex"] for m in targets if m["openalex"]}
    print(f"Building publication records for {len(targets)} members "
          f"({len([t for t in targets if t['slug'] in scholar_cache])} with Scholar ground truth)…")

    for member in targets:
        aid = member["openalex"]
        profile = scholar_cache.get(member["slug"]) or {}
        raw_works = []
        if aid:
            cursor = "*"
            try:
                while cursor and len(raw_works) < MAX_WORKS_PER_MEMBER:
                    data = api_get("/works", {
                        "filter": f"author.id:{aid}",
                        "per-page": "200",
                        "cursor": cursor,
                        "select": "display_name,publication_year,type,doi,primary_location,"
                                  "open_access,authorships,cited_by_count",
                    })
                    raw_works.extend(data.get("results", []))
                    cursor = (data.get("meta") or {}).get("next_cursor")
                    time.sleep(0.12)
            except Exception as exc:
                failures.append(member["slug"])
                print(f"  {member['slug']:28} FAILED ({exc}) - keeping previous data", file=sys.stderr)
                if member["slug"] in existing:
                    out[member["slug"]] = existing[member["slug"]]
                continue

        if profile.get("pubs"):
            works = match_scholar(profile["pubs"], raw_works)
            ground = "scholar"
            note = f" (Scholar ground truth; {profile.get('count', '?')} on profile)"
        else:
            ground = "openalex"
            n_raw = len(raw_works)
            if not member["filter_off"]:
                raw_works = filter_namesakes(raw_works, aid, lab_ids)
            n_dropped = n_raw - len(raw_works)
            works = [w for w in (clean_work(r) for r in raw_works) if w]
            note = f" ({n_dropped} namesake works filtered)" if n_dropped else ""

        # Collapse duplicate (title, year) pairs, keeping the most-cited copy.
        seen = {}
        for work in works:
            key = (norm_title(work["title"]), work["year"])
            if key not in seen or work["cited"] > seen[key]["cited"]:
                seen[key] = work
        works = list(seen.values())
        works.sort(key=lambda w: (-w["year"], -w["cited"], w["title"]))
        works = works[:MAX_WORKS_PER_MEMBER]

        record = {
            "id": aid,
            "name": member["name"],
            "updated": today,
            "count": len(works),
            "works": works,
            "ground_truth": ground,
        }
        if ground == "scholar":
            record["scholar_fetched"] = profile.get("fetched", "")
        out[member["slug"]] = record
        print(f"  {member['slug']:28} {len(works):>4} works{note}")

    # Site-wide metadata: the deduplicated union of every member's works.
    # Members legitimately share papers, and the same paper can arrive in
    # different shapes per member (arXiv vs published year, Scholar title
    # variants), so the union clusters works: same paper = within one year
    # AND titles that are identical, contained in one another, or >= 93%
    # similar - with matching digit sequences, so series papers such as
    # "TREC 2023 …" / "TREC 2024 …" never merge. The best copy represents
    # the cluster (enriched > Scholar stub, published > arXiv, most cited);
    # core=1 if ANY contributing member is current (non-alumni/external).
    # Default listings and headline counts use core works only; the rest
    # stay hidden on /publications until a visitor searches.
    candidates = []
    for slug, record in out.items():
        member_core = 1 if core_by_slug.get(slug) else 0
        for work in record["works"]:
            entry = dict(work)
            entry["core"] = member_core
            entry["_norm"] = norm_title(work["title"])
            entry["_digits"] = "/".join(re.findall(r"\d+", entry["_norm"]))
            candidates.append(entry)

    def quality(work):
        return (work["type"] != "scholar",
                not (work["venue"] or "").lower().startswith("arxiv"),
                work["cited"], work["year"])

    def same_paper(a, b):
        # arXiv year vs published year can drift by up to two years
        if abs(a["year"] - b["year"]) > 2:
            return False
        na, nb = a["_norm"], b["_norm"]
        if na == nb:
            return True
        short, longer = (a, b) if len(na) <= len(nb) else (b, a)
        if len(short["_norm"]) >= 25 and short["_norm"] in longer["_norm"]:
            if short["_digits"] == longer["_digits"] or not short["_digits"]:
                return True
        if a["_digits"] == b["_digits"] and min(len(na), len(nb)) >= 25:
            # long shared prefix: the same paper with a renamed subtitle
            # or different separator ("- Tutorial" vs ": A Tutorial")
            shared = 0
            limit = min(len(na), len(nb))
            while shared < limit and na[shared] == nb[shared]:
                shared += 1
            if shared >= 40:
                return True
            matcher = difflib.SequenceMatcher(None, na, nb)
            if matcher.quick_ratio() >= 0.93 and matcher.ratio() >= 0.93:
                return True
        return False

    candidates.sort(key=quality, reverse=True)  # best copy becomes the representative
    clusters, reps_by_year = [], {}
    for cand in candidates:
        rep_found = None
        for year in range(cand["year"] - 2, cand["year"] + 3):
            for rep in reps_by_year.get(year, ()):
                if same_paper(rep, cand):
                    rep_found = rep
                    break
            if rep_found:
                break
        if rep_found:
            rep_found["core"] = rep_found["core"] or cand["core"]
            # keep a differing variant title searchable on the merged entry
            if cand["_norm"] != rep_found["_norm"] and not rep_found.get("alt"):
                rep_found["alt"] = cand.get("alt") or cand["title"]
        else:
            clusters.append(cand)
            reps_by_year.setdefault(cand["year"], []).append(cand)

    for cluster in clusters:
        del cluster["_norm"], cluster["_digits"]
    all_works = sorted(clusters, key=lambda w: (-w["year"], -w["cited"], w["title"]))
    core_works = [w for w in all_works if w["core"]]
    n_extended = len(all_works) - len(core_works)
    out["_meta"] = {
        "updated": today,
        "min_year": MIN_YEAR,
        "unique_works": len(core_works),
        "unique_works_display": f"{len(core_works):,}",
        "extended_works": n_extended,
        "extended_works_display": f"{n_extended:,}",
        "recent": core_works[:6],
        # Full union: rendered (searchable) on the lab-wide /publications page.
        "works": all_works,
    }
    print(f"Union across members since {MIN_YEAR}: {len(core_works)} works by current members "
          f"+ {n_extended} alumni/external-only works (search-only)")

    write_data_file(OUT_FILE, out, separators=(",", ":"))
    size_kb = OUT_FILE.stat().st_size // 1024
    print(f"Wrote {OUT_FILE.relative_to(ROOT)} ({size_kb} KB, {len(out)} members)")
    if failures:
        print(f"WARNING: failed members: {', '.join(failures)}", file=sys.stderr)
        sys.exit(2 if len(failures) == len(targets) else 0)


if __name__ == "__main__":
    if "--discover" in sys.argv:
        discover()
    elif "--scholar" in sys.argv:
        scholar_mode()
    else:
        fetch()
