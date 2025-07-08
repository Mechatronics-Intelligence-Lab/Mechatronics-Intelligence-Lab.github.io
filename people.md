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
<div class="image-grid {{group.role | downcase | replace: ' ', '-'}}">
<h3>{{group.role}}</h3>
<ul class="no-bullet">
  {% for person in group.people %}
    <li id="{{person.name | downcase | replace: ' ', '-'}}">
      <div class="person-row">
        <div class="photo">
          {% if person.image %}
  <img class="pi-photo" src="{{ site.baseurl }}/image/people/{{person.image}}" alt="{{person.name}}">
{% endif %}{% if person.image-credit %} (image credit: {{ person.image-credit }}){% endif %}">
          <h5 class="name sm-bottom-margin">
            {{person.name}}{% if person.title %} <span>{{person.title}}</span>{% endif %}
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
<div class="image-grid {{group.role | downcase | replace: ' ', '-'}}">
  <h3>{{group.role}}</h3>
  <ul class="no-bullet">
    {% for person in group.people %}
      <li id="{{person.name | downcase | replace: ' ', '-'}}">
        <div class="person-row">
          <div class="photo">
            <!-- Alumni는 사진이 없으므로 비워 두거나 빈 이미지 사용 -->
            <img class="pi-photo" src="{{ site.baseurl }}/image/people/Blank.jpg" alt="{{person.name}}">
            <h5 class="name sm-bottom-margin">
              {{person.name}}
              {% if person.title %}
                <span>{{person.title}}</span>
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

Applications for graduate study are always welcome, however before making contact, applicants should consider carefully whether their interests are aligned with this group, how their study might be funded, and whether they meet the department and university admissions criteria.
</div>
</div>
