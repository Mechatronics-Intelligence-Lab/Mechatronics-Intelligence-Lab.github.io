---
layout: page
title: People
menu-order: 20
hero-image-origin: 50% 40%
tagline: Researcher
permalink: /people.html
ref: people
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
					<img class="pi-photo" src="{{ site.baseurl }}/image/people/{{person.image}}" title="{{person.name}}{% if person.image-credit %} (image credit: {{ person.image-credit }}){% endif %}">
					<h5 class="name sm-bottom-margin">
						{{person.name}}{% if person.title %} <span>{{person.title}}</span>{% endif %}
					</h5>
				</div>
				<div class="details">
					{% if person.bio %}
					<p class="sm-top-margin">{{person.bio}}</p>
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
</div>
<div class="row">
	<div class="col-xs-12" markdown="l">
		<h5>{{group.role}}</h5>
		<ul>
		{% for person in group.people %}
			<li>{{person}}</li>
		{% endfor %}
		</ul>
	</div>
</div>
{% endif %}
{% endfor %}

---

<div class="row">
<div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">

### Joining the group

Applications for graduate study are always welcome, however before making contact, applicants should consider carefully whether their interests are aligned with this group, how their study might be funded, and whether they meet the department and university admissions criteria.
</div>
</div>
