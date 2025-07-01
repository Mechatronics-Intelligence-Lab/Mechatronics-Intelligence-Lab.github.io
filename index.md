---
layout: default
title: Home
menu-order: 5
hero-image-origin: 50% 25%
---
<style scoped>
.hero.{{ page.title | replace: ' ', '-' | replace: '&', 'and' | downcase }} {
	background-image: url({{ site.baseurl }}/img/hero/{{ page.title | replace: ' ', '-' | replace: '&', 'and' | downcase }}.jpg);
{% if page.hero-image-origin %}	background-position: {{ page.hero-image-origin }};{% endif %}
}
@media (min-width: 768px) {
	.hero.{{ page.title | replace: ' ', '-' | replace: '&', 'and' | downcase }} {
		background-image: url({{ site.baseurl }}/img/hero/{{ page.title | replace: ' ', '-' | replace: '&', 'and' | downcase }}@2x.jpg);
	}
}
</style>
<div class="banner-img"><img src="{{ site.baseurl }}/img/hero/{{ page.title | replace: ' ', '-' | replace: '&', 'and' | downcase }}@2x.jpg"></div>
<div class="intro-text">
<div class="container content">
<div class="row">
<div class="col-xs-12 col-md-10 col-lg-8 col-md-offset-1 col-lg-offset-2" markdown="1">

우리의 목표는 메카트로닉스 시스템의 성능평가, 이상감지, 고장진단, 수명예측을 통해 메카트로닉스 시스템의 성능과 효율을 개선하는 것입니다. 
