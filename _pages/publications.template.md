# Publications

Publications ordered by year.

<ul>{{ range .Entries }}
<li>
    <span>{{ index .Fields "Author" }}</span>.
    <span>{{index .Fields "Year"}}</span>.
    <span>{{ index .Fields "Title"}}</span>.
    {{ if index .Fields "Booktitle"}}
    <span>In <em>{{ index .Fields "Booktitle"}}</em></span>.
    {{ end }}
    {{ if index .Fields "Journal" }}
    <span><em>{{ index .Fields "Journal"}}</em></span>.
    {{ end }}
</li>{{ end }}
</ul>