---
layout: page
title: Student
menu-order: 20
hero-image-origin: 50% 40%
tagline: Students
permalink: /student.html
main_image: /image/main/EV.jpg
---

<div class="row">

{% assign people = site.data.people -%}

{% for group in people %}

  <div class="image-grid {{ group.role | downcase | replace: ' ', '-' }}">

    <h3>{{ group.role }}</h3>

    <ul class="no-bullet">

      {% for person in group.people %}

        <li id="{{ person.name | downcase | replace: ' ', '-' }}">

          <div class="person-row">

            <!-- Photo -->
            <div class="photo">

              {% if group.role == 'Alumni' %}
                <img class="pi-photo"
                     src="{{ site.baseurl }}/image/people/Blank.jpg"
                     alt="{{ person.name }}">

              {% elsif person.image %}
                <img class="pi-photo"
                     src="{{ site.baseurl }}/image/people/{{ person.image }}"
                     alt="{{ person.name }}">
              {% endif %}

              {% if person.image-credit %}
                <p class="image-credit">
                  (image credit: {{ person.image-credit }})
                </p>
              {% endif %}

            </div>


            <!-- Name & Details -->
            <div class="details">

              <h5 class="name sm-bottom-margin">
                {{ person.name }}

                {% if person.title %}
                  <span>{{ person.title }}</span>
                {% endif %}
              </h5>


              {% if person.scholar_url %}
                <p class="scholar-link">
                  <a href="{{ person.scholar_url }}"
                     target="_blank">
                    Google Scholar
                  </a>
                </p>
              {% endif %}


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
    <hr style="border: none;
               border-top: 2px solid #157878;
               margin: 40px 0;">
  {% endunless %}

{% endfor %}

</div>


---

<div class="row">
  <div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">

### Joining the group

Students who are interested in our graduate program and Internship are very welcome.<br>
If you have any questions about admission or research topics, please feel free to contact Professor Youngsun Hong at any time.<br>
You may reach out by phone or email, and we will be happy to provide detailed information.

  </div>
</div>
