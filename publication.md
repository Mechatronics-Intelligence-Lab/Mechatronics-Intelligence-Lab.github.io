---
layout: page
title: Publication
tagline: 논문 및 학술대회
permalink: /publication.html
ref: publication
order: 0
main_image: /image/main/EV.jpg
---


<style>
.publication-item {
  text-indent: -2em;         /* 번호만큼 내어쓰기 */
  padding-left: 2em;         /* 들여쓰기 */
  margin-bottom: 10px;
}
</style>

### Paper

{% assign publications = site.data.publications | sort: "date" | reverse %}
<div>
  {% for paper in publications %}
    <div class="publication-item">
      [{{ forloop.index }}] {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i> [{{ paper.date | date: "%Y" }}]
    </div>
  {% endfor %}
</div>

<hr>

### Conference

{% assign conference = site.data.conference | sort: "date" | reverse %}
<div>
  {% for paper in conference %}
    <div class="publication-item">
      [{{ forloop.index }}] {{ paper.title }}, {{ paper.location }} [{{ paper.date | date: "%Y" }}]
    </div>
  {% endfor %}
</div>

<hr>

### Patent

{% assign patent = site.data.patent | sort: "date" | reverse %}
<div>
  {% for paper in patent %}
    <div class="publication-item">
      [{{ forloop.index }}] ({{ paper.state }}) {{ paper.title }}, {{ paper.author }} [{{ paper.date | date: "%Y" }}]
    </div>
  {% endfor %}
</div>
