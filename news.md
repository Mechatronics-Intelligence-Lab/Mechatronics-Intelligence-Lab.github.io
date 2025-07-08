---
layout: page
title: News
tagline: 최신소식
permalink: /news.html
ref: news
order: 2
main_image: /image/main/EV.jpg
---

<div>
  {% for post in site.posts %}
    <div style="margin-bottom: 30px;">
      <a href="{{ post.url }}" style="display: flex; align-items: flex-start; gap: 20px; text-decoration: none;">
        {% if post.main_image %}
          <img src="{{ post.main_image }}" alt="{{ post.title }}" style="height: 100px; flex-shrink: 0;">
        {% endif %}
        <div>
          <h3 style="margin: 0; color: #007acc;">{{ post.title }}</h3>
          <p style="margin: 0; color: #333;">{{ post.excerpt }}</p>
        </div>
      </a>
    </div>
  {% endfor %}
</div>
