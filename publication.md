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
<ol reversed style="padding-left: 1.5em;">
  {% for paper in publications %}
    <li style="margin-bottom: 10px;">
      {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i> [{{ paper.date | date:"%Y.%m.%d }}]
    </li>
  {% endfor %}
</ol>

<hr>

### Conference

{% assign conference = site.data.conference | sort: "start_date" | reverse %}
<ol reversed style="padding-left: 1.5em;">
{% for conf in conference %}
  <li style="margin-bottom: 10px;">
    {{ conf.title }}, {{ conf.organization }}, {{ conf.location }}
    [
    {{ conf.start_date | date: "%Y.%m.%d" }}
    ~
    {% if conf.end_date %}
      {{ conf.end_date | date: "%Y.%m.%d" }}
    {% else %}
      Present
    {% endif %}
    ]
  </li>
{% endfor %}
</ol>

<hr>

### Patent

{% assign patent = site.data.patent | sort: "date" | reverse %}
<ol style="padding-left: 1.5em;">
  {% for paper in patent %}
    <li style="margin-bottom: 10px;">
      ({{ paper.state }}) {{ paper.title }}, {{ paper.author }}
      [{{ paper.date | date: "%Y.%m.%d" }}]
    </li>
  {% endfor %}
</ol>

<hr>

### Project

{% assign project = site.data.project | sort: "start_date" | reverse %}
<ol reversed style="padding-left: 1.5em;">
{% for paper in project %}
  <li style="margin-bottom: 10px;">
    ({{ paper.state }}) {{ paper.title }}, {{ paper.author }}
    [
    {{ paper.start_date | date: "%Y.%m.%d" }}
    ~
    {% if paper.end_date %}
      {{ paper.end_date | date: "%Y.%m.%d" }}
    {% else %}
      Present
    {% endif %}
    ]
  </li>
{% endfor %}
</ol>

