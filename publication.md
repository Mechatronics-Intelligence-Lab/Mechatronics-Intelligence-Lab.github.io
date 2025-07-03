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
      &lt;{{ forloop.index }}&gt; {{ paper.title }}, {{ paper.author }}, <i>{{ paper.journal }}</i>, [{{ paper.date | date: "%Y"  }}] 
    </li>
  {% endfor %}
</ol>

### Conference

[1] PHM Korea 2025 정기학술대회, 제주, 부영호텔, 2025.06.23~25
