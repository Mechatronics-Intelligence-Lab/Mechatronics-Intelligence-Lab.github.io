---
layout: page
title: Projects
permalink: /project.html
tagline: Research Projects
main_image: /image/main/EV.jpg
---

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
