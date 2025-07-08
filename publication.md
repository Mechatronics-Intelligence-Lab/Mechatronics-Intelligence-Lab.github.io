---
layout: page
title: Publication
tagline: 논문 및 학술대회
permalink: /publication.html
ref: publication
order: 0
main_image: /image/main/EV.jpg
---

### Paper


{% assign publications = site.data.publications | sort: "date" | reverse %}
<ul style="list-style: none; padding-left: 0;">
  {% for paper in publications %}
    <li>
      [{{ forloop.index }}] {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i> [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ul>

<hr>

### Conference

{% assign conference = site.data.conference | sort: "date" | reverse %}
<ul style="list-style: none; padding-left: 0;">
  {% for paper in conference %}
    <li>
      [{{ forloop.index }}] {{ paper.title }}, {{ paper.location }} [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ul>

<hr>

### Patent

{% assign patent = site.data.patent | sort: "date" | reverse %}
<ul style="list-style: none; padding-left: 0;">
  {% for paper in patent %}
    <li>
      [{{ forloop.index }}] ({{ paper.state }}) {{ paper.title }}, {{ paper.author }} [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ul>
