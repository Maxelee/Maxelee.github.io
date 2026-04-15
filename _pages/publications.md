---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">Google Scholar</a> and <a href="{{site.author.arxiv}}">arXiv</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  <div class="pub-card">
    <h3><a href="{{ base_path }}{{ post.url }}">{{ post.title }}</a></h3>
    <div class="pub-meta">
      {% if post.venue %}<span class="pub-venue">{{ post.venue }}</span>{% endif %}
      {% if post.date %}<span class="pub-year">{{ post.date | date: "%Y" }}</span>{% endif %}
    </div>
    {% if post.excerpt %}<p class="pub-excerpt">{{ post.excerpt }}</p>{% endif %}
    <div class="pub-links">
      {% if post.paperurl %}<a href="{{ post.paperurl }}"><i class="fas fa-external-link-alt"></i> Paper</a>{% endif %}
      <a href="{{ base_path }}{{ post.url }}"><i class="fas fa-info-circle"></i> Details</a>
    </div>
  </div>
{% endfor %}
