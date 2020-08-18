<img src="images/ielab-page001.png" width="120px" height="120px" style="float: right;">

# ielab website

welcome to the README file of the ielab website. This file will get you set up and running to develop the ielab website locally and explain how to add and edit content to the website.

## Edit locally
 
 Rather than guessing to see if your changes look good on the website without testing them, you can render the website locally with jekyll. **please follow [this tutorial](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) to set this up**. Building the site locally gives you "hot-reloading" so you just need to refresh your browser to see changes.
 
## Organisation of Website 

The organisation of the ielab website is currently broken down into the following collections:

 - people
 - publications
 - projects
 - posts
 
Each of these files (`people.md`, `publications.md`, `projects.md`, and `posts.md`) **should not be touched** unless you know what you are doing with [liquid templates](https://jekyllrb.com/docs/liquid/). These files are automatically templates with content from the collections. 
 
Collections are a feature built into [jekyll](https://jekyllrb.com/docs/collections/). Aspects of a particular collection are modified using the [front matter](https://jekyllrb.com/docs/front-matter/) of a page. All front matter on a page is contained between two `---` tags. The data format of the front matter is YAML.
 
Collections, configured in `_config.yml`, are used to group common pages together. For example, the `people` collection (found in `_people`) is used to create a page (indicated by the name of the file) for each person in ielab, as well as to template pages such as the publications page, where each author of a publication can be linked to an existing person in the people collection. The following sections describe how to configure variables in the front matter of collection pages.
 
### People

Example: [http://ielab.io/people/harry-scells](http://ielab.io/people/harry-scells)

People pages are located in the `_people` folder. The name of each file should correspond the the name of the person: e.g., `harry-scells.md`.

A person has the following variables (with example values):

```yaml
name: Person Display Name
image: /images/example.png
description: This is an example description.
role: role
twitter: //twitter.com/username
twitter-timeline: true
orcid: 0000-0000-0000-0000
github: //github.com/username
website: //example.com
scholar: //scholar.google.com.au/citations?user=EXAMPLE
``` 

The `name`, `image`, and `description` are used in most places in the website (e.g., home page and publications). The `role` determines where the person should fit in the home page. The values of `role` can either be `staff`, `phd`, `alumni`, or `external` (it is possible to have multiple roles by creatng a list, e.g. `[staff, alumni]`). The `twitter-timeline` variable will place a timeline of tweets using the `twitter` variable on the profile page.

Content inside each person page can be anything that you wish to mention about yourself. Add content to your people page underneath the front matter. This content will appear after your name, links, and description, but before your publications.
 
### Publications

Example: [http://ielab.io/publications/scells-2018-searchrefiner](http://ielab.io/publications/scells-2018-searchrefiner)

Publication pages are located in the `_publications` folder. The name of each file should correspond to `author-year-keyword.md`.

A publication has the following variables (with example values):

```yaml
authors: [harry-scells, "Billy Bob"]
title: "READMEs Considered Useful: You Should Read Them"
venue: "Proceedings of the 1st ielab README file"
year: 2019
pdf: /publications/pdfs/scells2019readme.pdf
``` 

The `authors` variable must correspond to either an existing person in the people collection (i.e., `harry-scells`), or a string indicating an external author. When templated, publications use this author list to link to a page from the people collection. The `pdf` variable, when filled, will produce a download link next to the sharing buttons on a publication page.

Content inside each publication page should be external links and an abstract. 
 
### Projects

Example: [http://ielab.io/projects/systematic-reviews](http://ielab.io/projects/systematic-reviews)

Project pages are located in the `_projects` folder. The name of each file should be the name of the project.

A project has the following variables (with example values):

```yaml
name: Title of the Project
image: /images/project.png
people: [person-one, "Billy Bob"]

```

The `name` and `image` variables are used in the templating process on the home page and on the projects overview page. The `people` variable controls who is associated with the page and will be displayed on the project page.

Enter content about the project underneath the front matter.

### Posts

Example: [http://localhost:4000/posts/2019/01/30/journal-accepted-jmir.html](http://localhost:4000/posts/2019/01/30/journal-accepted-jmir.html)

Post pages are located in the `_posts` folder. The name of each file **must** adhere to the [jekyll specification](https://jekyllrb.com/docs/posts/) (i.e., `YEAR-MONTH-DAY-title.MARKUP`).

A post has the following variables:

```yaml
layout: post
title: "We have a README! You should read it!"
date: 2019-02-06
categories: posts
author: ielab team
tags: [publications]
```

The `layout` variable must be `post`. The `title`, `date` and `author` are displayed when templating the page. Enter content of the post underneath the front matter. The first paragraph of a post is used as an except in templating.

## Unrelated Pages

If you have a requirement for a page at the top-level of the ielab website, e.g., supplemental content for a paper, project page for code, etc., **this should be a separate repository**. It is [very easy](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/) to set up if you have an existing repository and removes clutter from this repository.

Example:

 - Project page: [https://ielab.io/searchrefiner/](https://ielab.io/searchrefiner/)
 - GitHub repo: [https://github.com/ielab/searchrefiner](https://github.com/ielab/searchrefiner)


## Data Files

If you want to do something a bit more complicated, you can use [data files](https://jekyllrb.com/docs/datafiles/). The [Systematic Reviews](http://ielab.io/projects/systematic-reviews) project page uses a data file (located at `_data/projects/systematic-reviews.yml`) contains the structure of the publications on the page. If I wanted to add another publication to my project page, I would only need to update the data file with a reference to the new publication, rather than editing my project page. 

For anything else, check out the [jekyll documentation](https://jekyllrb.com/docs/).
