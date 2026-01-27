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
      <a href="{{ post.url }}" style="
          display: flex;
          align-items: flex-start;
          gap: 20px;
          text-decoration: none;
        ">
        <div style="flex: 1;">
          <h3 style="
              margin: 0 0 5px 0;
              color: #007acc;
              font-weight: normal;
          ">
            {{ post.date | date: "%Y-%m-%d" }} {{ post.title }}
          </h3>
          <p style="margin: 0; color: #333;">
            {{ post.excerpt }}
          </p>
        </div>
        {% if post.main_image %}
        <div class="post-thumb">
        <img src="{{ post.main_image }}" alt="{{ post.title }}">
        </div>
      {% endif %}

      </a>
    </div>
  {% endfor %}
</div>
