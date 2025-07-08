---
layout: page
title: News
tagline: 최신소식
permalink: /news.html
ref: news
order: 2
main_image: /image/main/EV.jpg
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">
        {% if post.main_image %}
          <img src="{{ post.main_image }}" alt="{{ post.title }}" style="height: 100px;">
        {% endif %}
        <h3>{{ post.title }}</h3>
      </a>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
