# ielab website — [ielab.io](https://ielab.io)

The website of the **Information Engineering Lab (ielab)** at The University of Queensland.

The site is a static [Jekyll](https://jekyllrb.com) site hosted on **GitHub Pages**: any commit
pushed to the `master` branch is automatically built and published to
[ielab.io](https://ielab.io) within a couple of minutes. There is no separate deploy step.

---

## 1. Running the site locally

You should always preview changes locally before pushing. The site builds with the
[`github-pages`](https://github.com/github/pages-gem) gem, which pins the exact same Jekyll
version GitHub uses in production — what you see locally is what gets published.

### 1.1 Prerequisites

You need **Ruby 3.x** (3.2–3.4) and **Bundler**.

> ⚠️ **Ruby 4 does not work**: the `github-pages` gem requires `Ruby < 4.0`. If `ruby -v`
> prints 4.x, install a versioned Ruby 3 alongside it as shown below.

**macOS** (recommended setup — avoid the system Ruby):

```bash
# Install Ruby 3.4 with Homebrew (plain `brew install ruby` now installs Ruby 4 — too new)
brew install ruby@3.4

# Use it for this project (zsh) — or add this line to ~/.zshrc to make it permanent
export PATH="/opt/homebrew/opt/ruby@3.4/bin:$PATH"

# Verify (should print 3.4.x)
ruby -v
```

> Alternatively use a version manager such as [`rbenv`](https://github.com/rbenv/rbenv)
> (`brew install rbenv && rbenv install 3.4.9 && rbenv local 3.4.9`) — useful if you work
> on multiple Ruby projects.

**Ubuntu / Debian:**

```bash
sudo apt-get install ruby-full build-essential zlib1g-dev
gem install bundler
```

**Windows:** install Ruby+Devkit from [rubyinstaller.org](https://rubyinstaller.org/), then
`gem install bundler` in a new terminal.

### 1.2 Install dependencies

From the repository root (first time, and again whenever `Gemfile` changes):

```bash
bundle install
```

If `bundle install` fails against the old `Gemfile.lock`, refresh it with
`bundle update github-pages`.

### 1.3 Serve the site

```bash
bundle exec jekyll serve --livereload
```

Then open **<http://127.0.0.1:4000>**. The site rebuilds automatically when you save a file,
and `--livereload` refreshes the browser for you. Press `Ctrl-C` to stop.

Useful variants:

```bash
bundle exec jekyll serve --livereload --drafts   # also render _drafts/
bundle exec jekyll build                          # one-off build into _site/ (no server)
JEKYLL_ENV=production bundle exec jekyll build    # build exactly as production
```

> **Note:** one feature does not work locally: `site.github.build_revision` (used for CSS/JS
> cache-busting) is only available on GitHub's servers — locally it falls back to a timestamp.
> Everything else renders identically.

### 1.4 Troubleshooting

| Symptom | Fix |
|---|---|
| `github-pages … requires Ruby >= 2.6, < 4.0` | You are on Ruby 4 — install `ruby@3.4` and put it first in `PATH` (see 1.1) |
| `cannot load such file -- csv` (or `base64`) | Run `bundle install` — these gems are in the Gemfile for Ruby ≥ 3.4 |
| `Invalid US-ASCII character` during the Sass build | Your shell locale is not UTF-8: `export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8` |
| `cannot load such file -- webrick` | `bundle install` (webrick is in the Gemfile) |
| Permission errors installing gems | You are using the system Ruby — install Ruby via Homebrew/rbenv as above |
| `GitHub Metadata: No GitHub API authentication` warning | Harmless locally; ignore |
| Stale styles after pulling | Hard-refresh the browser (`Cmd-Shift-R`) |

---

## 2. How publishing works

1. Commit your changes on `master` (or merge a PR into `master`).
2. `git push origin master`.
3. GitHub Pages builds the site automatically (Settings → Pages → "Deploy from a branch").
4. The result is live at [ielab.io](https://ielab.io) (custom domain configured via `CNAME`)
   after ~1–2 minutes. Check the repository's **Actions** tab for the `pages-build-deployment`
   workflow if something doesn't appear.

Because GitHub builds the site itself, **only plugins on the
[GitHub Pages whitelist](https://pages.github.com/versions/) can be used** (we use
`jekyll-feed`, `jekyll-redirect-from`, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-paginate`).
Custom Ruby plugins will not run.

---

## 3. Site structure

```
.
├── _config.yml          # site config, collections, plugins
├── index.html           # homepage
├── publications.md      # publications list (search + year filter)
├── people.md            # team page
├── projects.md          # projects grid
├── grants.md            # grants list
├── tutorials.md         # tutorials grid
├── posts/index.html     # news archive (paginated)
├── student-projects.md  # "Join Us" page
├── _people/             # one .md per lab member
├── _publications/       # one .md per publication (curated ielab record)
├── _projects/           # one .md per project
├── _grants/             # one .md per grant
├── _tutorials/          # one .md per tutorial
├── _posts/              # news posts (YYYY-MM-DD-title.md)
├── _layouts/            # page templates (default, page, people, publications, …)
├── _includes/           # reusable components (header, footer, cards, icons, …)
├── _data/openalex.json            # auto-synced member publication records (do not edit)
├── _data/scholar_profiles.json    # Google Scholar ground-truth snapshot (do not edit)
├── _scripts/update_publications.py             # the sync script (Scholar + OpenAlex)
├── .github/workflows/update-publications.yml      # weekly metadata sync
├── .github/workflows/update-scholar-profiles.yml  # monthly Scholar refresh (SerpApi)
├── assets/css/main.scss # the entire design system (light + dark theme)
├── assets/js/main.js    # theme toggle, mobile nav, publication search, etc.
└── images/              # photos, logos, project images
```

### Design system notes

- All styling lives in `assets/css/main.scss`. Colours/typography are defined as CSS custom
  properties at the top — there is a light and a dark theme (`html[data-theme]`).
- Icons are inline SVGs in `_includes/icon.html`; use them with
  `{% raw %}{% include icon.html name="github" size=16 %}{% endraw %}`.
- Cards and grids: `{% raw %}{% include person-card.html person=… %}{% endraw %}`,
  `project-card.html`, `post-card.html`, `pub-item.html`.
- No CSS/JS frameworks — plain Liquid + SCSS + vanilla JS, all GitHub Pages-safe.

---

## 4. Editing content

### 4.0 How member publication lists work (auto-synced)

Member publication lists are generated, not hand-written. **Ground truth: each member's
Google Scholar profile.** Metadata (full author lists, venues, open-access PDF links)
comes from [OpenAlex](https://openalex.org), a free open scholarly index. Only papers
from **2019 onwards** (ielab's founding year) are shown — the cutoff is `MIN_YEAR` in
`_scripts/update_publications.py`.

The pieces:

1. Each file in `_people/` carries two keys: `scholar` (the member's Google Scholar
   profile URL — this defines *which* papers they have) and `openalex: A…` (their OpenAlex
   author ID — this provides rich metadata). Find OpenAlex IDs at
   [openalex.org/authors](https://openalex.org/authors?search=their+name) or via
   `python3 _scripts/update_publications.py --discover`.
2. `_data/scholar_profiles.json` is a committed **snapshot of every member's Scholar
   profile** (title/year/venue/citations per paper). It is refreshed **monthly** by
   `.github/workflows/update-scholar-profiles.yml` using **SerpApi** (see below), or
   locally with `python3 _scripts/update_publications.py --scholar` (no key needed from a
   home/office network; Google blocks cloud IPs).
3. The **weekly** workflow (`.github/workflows/update-publications.yml`) rebuilds
   `_data/openalex.json`: for each member it takes exactly the papers on their Scholar
   snapshot (≥ 2019), enriches each with OpenAlex metadata by title match, and keeps
   Scholar-only papers as plain entries linking back to Scholar — so the site count
   always equals the member's Scholar count (minus pre-2019 papers).
4. **Fallbacks:** members with no Scholar profile use their OpenAlex record cleaned by an
   institution-based namesake filter (`openalex_filter: off` disables it); members with
   neither fall back to the curated `_publications/` list, so pages never go blank.

**SerpApi setup (one-time):** Google Scholar has no API and blocks scrapers on cloud IPs,
so the monthly workflow uses [SerpApi](https://serpapi.com)'s `google_scholar_author`
engine. Create a free account, copy the API key, and add it as the repository secret
`SERPAPI_KEY` (*Settings → Secrets and variables → Actions → New repository secret*).
Quota math: a full refresh of ~30 profiles costs ~45–55 searches; the free tier allows
**100/month**, which is why the refresh is monthly — do not schedule it weekly. (The
Python `scholarly` package was considered instead, but it scrapes Scholar directly and
needs a paid proxy to work from CI — strictly worse than SerpApi here.)

New papers appear automatically once they are on the member's Scholar profile and the
monthly refresh has run — or run the two commands locally and commit for an immediate
update. If a member's page shows a wrong paper, fix their Scholar profile (it's the
ground truth) and refresh. Never edit the two `_data/*.json` files by hand.

**Whose papers appear where:** the homepage stats/recent list and the default
[/publications](https://ielab.io/publications) listing only count papers with at least
one **current member** as author (anyone whose `_people/` file is not `alumni` and not
`external`). Papers authored only by alumni or external members are still rendered on
the publications page but stay hidden until a visitor types a search query, and they
always appear in full on the member's own profile page. This is driven by a `core` flag
the sync script computes per paper — change a member's `role`/`alumni` front matter and
re-run the sync to move their papers in or out of the default view.

> The **lab-wide [/publications](https://ielab.io/publications) page renders the
> deduplicated union of all member records since 2019** (`_meta.works` in
> `_data/openalex.json`), searchable and filterable by year — the same source as the
> homepage stats. The curated
> `_publications/` collection still exists and matters: it provides the per-paper detail
> pages (abstract, self-hosted PDF), powers project cross-links and old news posts, and is
> the fallback if the synced data is ever unavailable. Keep adding flagship lab papers
> there (§4.2) when you want a proper landing page for them.

### 4.1 Add or edit a person

Create `_people/firstname-lastname.md` (the filename becomes the URL,
e.g. `/people/firstname-lastname`):

```yaml
---
name: Person Display Name
image: /images/firstname-lastname.jpg   # add the photo to images/ (square crop looks best)
role: phd                # staff | phd | mphil | external | alumni — or a list: [staff, alumni]
alumni: true             # optional, marks the person as alumni regardless of role
description: PhD student, UQ. One-line bio shown on cards and the profile page.
website: //example.com
scholar: //scholar.google.com/citations?user=XXXX   # ground truth for their publication list (§4.0)
openalex: A0000000000          # OpenAlex author ID — supplies rich publication metadata (§4.0)
github: //github.com/username
twitter: //twitter.com/username
orcid: 0000-0000-0000-0000
links:                   # optional extra links
  - url: //example.com/thesis.pdf
    name: Download PhD Thesis
---

An optional longer bio in Markdown goes here. It appears on the profile page, which also
automatically lists the person's projects and publications.
```

People appear automatically on `/people/`, grouped by role; anyone with `alumni: true` (or
`role` containing `alumni`) is listed under Alumni only.

### 4.2 Add a publication

Create `_publications/author-year-keyword.md`:

```yaml
---
title: "A Very Good Paper About Search"
authors: [hang-li, guido-zuccon, "External Coauthor"]
venue: "Proceedings of the 48th International ACM SIGIR Conference"
year: 2026
pdf: /publications/pdfs/li2026verygood.pdf   # optional; put the file in publications/pdfs/
projects: [systematic-reviews]               # optional; links the paper to project pages
links:                                       # optional extra buttons
  - url: https://github.com/ielab/verygood
    name: Code
---

## Abstract

The abstract goes here.
```

- Entries in `authors` that match a filename in `_people/` (e.g. `hang-li`) are linked to that
  person's profile automatically; anything else is rendered as plain text — use quoted full
  names for external co-authors.
- The publication appears automatically on `/publications/` (searchable, filterable by year),
  on each author's profile, and on any project page listed in `projects`.

### 4.3 Add a project

Create `_projects/project-name.md`:

```yaml
---
name: Title of the Project
image: /images/projects/project-name.jpg   # 16:9 image used on cards
people: [guido-zuccon, hang-li]
featured: true                             # featured projects appear on the homepage
---

Describe the project here in Markdown.
```

Publications tagged with this project (via their `projects` key) are listed on the project
page automatically.

### 4.4 Add a news post

Create `_posts/YYYY-MM-DD-short-title.md`:

```yaml
---
layout: post
title: "Three papers accepted at SIGIR 2026"
date: 2026-04-01
categories: posts
author: ielab
tags: [publications]
publications:            # optional: render a list of publication entries in the body
  - li-2026-verygood
---

The first paragraph is used as the excerpt on the news page and homepage.

{% raw %}{% include publications.html publications=page.publications %}{% endraw %}
```

### 4.5 Add a grant

Create `_grants/grant-name.md`:

```yaml
---
name: ARC Discovery Project 2026        # the funding scheme
description: Project title goes here    # shown as the headline
value: $675,000
years: 2026-2029
image: /images/arc-logo.png             # optional logo
people: [guido-zuccon]
---

Longer description of the funded project.
```

### 4.6 Add a tutorial

Create `_tutorials/tutorial-name.md`:

```yaml
---
name: Retrieval and Ranking with LLMs
venues: [SIGIR2026]
description: One-paragraph description shown on the tutorials page.
people:
  - name: guido-zuccon
links:
  - url: https://example.com/slides.pdf
    name: Slides
---

Agenda, materials, and other details go here.
```

---

## 5. Standalone project pages

Supplementary content for a paper or a tool with its own website should live in **its own
repository** with GitHub Pages enabled (e.g. [ielab.io/searchrefiner](https://ielab.io/searchrefiner)
→ [github.com/ielab/searchrefiner](https://github.com/ielab/searchrefiner)), not in this repo.

---

## 6. Conventions

- Image files: lowercase, hyphenated (`firstname-lastname.jpg`); people photos roughly square;
  project images 16:9; keep files under ~500 KB (resize/compress before committing).
- Publication slugs: `author-year-keyword` (e.g. `scells-2018-searchrefiner`).
- Don't edit files in `_layouts/` or `_includes/` for content changes — content lives in the
  collections (`_people/`, `_publications/`, …) and is templated automatically.
