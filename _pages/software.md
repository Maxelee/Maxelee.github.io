---
layout: page
title: "Software"
eyebrow: "Open source"
lede: "Most of my research code is publicly available on GitHub. These are the main projects."
permalink: /software/
wide: true
description: "Research software by Max E. Lee: emulators, baryon correction pipelines, and simulation tools for cosmology."
---

<div class="software-grid software-grid--3">
{% for sw in site.data.software %}
<div class="software-card">
<h3><a href="{{ sw.repo }}">{{ sw.name }}</a></h3>
<p>{{ sw.tagline }}</p>
<div class="software-card__links">
<a href="{{ sw.repo }}">code ↗</a>
{% if sw.paper_url %}<a href="{{ sw.paper_url }}">{{ sw.paper_label | default: "paper" }}</a>{% endif %}
</div>
</div>
{% endfor %}
</div>
