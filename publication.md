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
      {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i> [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>

<div class="row">
<div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">

### Conference

{% assign conference = site.data.conference | sort: "date" | reverse %}
<ol>
  {% for paper in conference %}
    <li>
      {{ paper.title }}, {{ paper.location }} [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>

<div class="row">
<div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">

###  Patent

{% assign patent = site.data.patent | sort: "date" | reverse %}
<ol>
  {% for paper in patent %}
    <li>
      ({{ paper.state }}) {{ paper.title }}, {{ paper.author }} [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>
