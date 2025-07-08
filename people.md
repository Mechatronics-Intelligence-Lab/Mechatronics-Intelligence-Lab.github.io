---
layout: page
title: People
menu-order: 20
hero-image-origin: 50% 40%
tagline: Researcher
permalink: /people.html
ref: people
main_image: /image/main/EV.jpg
---

<div class="row">
{% assign people = site.data.people -%}
{% for group in people %}
  {% if group.role != 'Alumni' %}
    <div class="image-grid {{ group.role | downcase | replace: ' ', '-' }}">
      <h3>{{ group.role }}</h3>
      <ul class="no-bullet">
        {% for person in group.people %}
          <li id="{{ person.name | downcase | replace: ' ', '-' }}">
            <div class="person-row">
              <div class="photo">
                {% if person.image %}
                  <img class="pi-photo" src="{{ site.baseurl }}/image/people/{{ person.image }}" alt="{{ person.name }}">
                  {% if person.image-credit %}
                    <p class="image-credit">(image credit: {{ person.image-credit }})</p>
                  {% endif %}
                {% endif %}
                <h5 class="name sm-bottom-margin">
                  {{ person.name }}{% if person.title %} <span>{{ person.title }}</span>{% endif %}
                </h5>
                {% if person.scholar_url %}
                  <p style="margin-top: 10px;">
                    <a href="{{ person.scholar_url }}" target="_blank">Google Scholar</a>
                  </p>
                {% endif %}
              </div>
              <div class="details">
                {% if person.bio %}
                  <div class="sm-top-margin">
                    {{ person.bio | markdownify }}
                  </div>
                {% endif %}
              </div>
            </div>
          </li>
        {% endfor %}
      </ul>
    </div>
    {% unless forloop.last %}
      <hr style="border: none; border-top: 2px solid #157878; margin: 40px 0;">
    {% endunless %}
  {% else %}
    <div class="image-grid {{ group.role | downcase | replace: ' ', '-' }}">
      <h3>{{ group.role }}</h3>
      <ul class="no-bullet">
        {% for person in group.people %}
          <li id="{{ person.name | downcase | replace: ' ', '-' }}">
            <div class="person-row">
              <div class="photo">
                <img class="pi-photo" src="{{ site.baseurl }}/image/people/Blank.jpg" alt="{{ person.name }}">
                <h5 class="name sm-bottom-margin">
                  {{ person.name }}
                  {% if person.title %}
                    <span>{{ person.title }}</span>
                  {% endif %}
                </h5>
              </div>
              <div class="details">
                {% if person.bio %}
                  <div class="sm-top-margin">
                    {{ person.bio | markdownify }}
                  </div>
                {% endif %}
              </div>
            </div>
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endif %}
{% endfor %}
</div>

---

<div class="row">
  <div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">
### Joining the group

대학원과정에 관심있는 학생들을 환영합니다. 진학이나 연구 내용에 대해 궁금한 점이 있으면 언제든지 홍영선 교수에게 연락바랍니다.<br>
전화나 이메일을 통해 편하게 문의주시면 자세히 알려드리겠습니다. 

  </div>
</div>
