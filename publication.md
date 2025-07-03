---
layout: page
title: Publication
tagline: 논문 및 학술대회
permalink: /publication.html
ref: publication
order: 0
---

### Paper

{% assign publications = site.data.publications | sort: "date" | reverse %}
<ol>
  {% for paper in publications %}
    <li>
      {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i>, [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>

### Conference

{% assign conference = site.data.conference | sort: "date" | reverse %}
<ol>
  {% for paper in conference %}
    <li>
      {{ paper.title }}, {{ paper.location }}, [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>
