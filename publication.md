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
<ol style="padding-left: 1.5em;">
  {% for paper in publications %}
    <li style="margin-bottom: 10px;">
      {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i> [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ol>

<hr>

### Conference

{% assign conference = site.data.conference | sort: "date" | reverse %}
<ol style="padding-left: 1.5em;">
  {% for paper in conference %}
    <li style="margin-bottom: 10px;">
      {{ paper.title }}, {{ paper.location }} [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ol>

<hr>

### Patent

{% assign patent = site.data.patent | sort: "date" | reverse %}
<ol style="padding-left: 1.5em;">
  {% for paper in patent %}
    <li style="margin-bottom: 10px;">
      ({{ paper.state }}) {{ paper.title }}, {{ paper.author }} [{{ paper.date | date: "%Y" }}]
    </li>
  {% endfor %}
</ol>
