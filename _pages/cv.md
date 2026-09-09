---
layout: page
title: "Curriculum Vitae"
eyebrow: "CV"
permalink: /cv/
description: "CV of Max E. Lee — cosmology PhD candidate at Columbia University."
redirect_from:
  - /resume
---

{% assign cv_pdf = site.static_files | where: "path", "/files/cv.pdf" | first %}
{% if cv_pdf %}
<div class="cv-actions">
<a class="btn btn--primary" href="/files/cv.pdf">{% include icon.html name="download" %} Download CV (PDF)</a>
<span class="cv-updated">updated {{ cv_pdf.modified_time | date: "%B %Y" }}</span>
</div>
{% endif %}

## Education

- **Ph.D. in Astronomy**, Columbia University, 2027 (expected)
- **M.S. in Astronomy**, Columbia University, 2024
- **B.A. in Astronomy & Physics**, University of California, Berkeley, 2020
- **A.A. in Mathematics & History**, Cabrillo College, 2018

## Awards & Fellowships

- **Columbia CTL Lead Teaching Fellowship** (2024–2026)
- **National Osterbrock Leadership Fellowship** (2023–2026)
- **NSF Graduate Research Fellowship** (2022–2027)
- **Ted Bowen Memorial Endowed Scholarship** (2018)

## Publications

<div>
{% assign pubs = site.publications | sort: "date" | reverse %}
{% for pub in pubs %}
<p class="cv-pub"><a href="{{ pub.url }}">{{ pub.title }}</a><span class="cv-pub__meta">{{ pub.venue }} · {{ pub.date | date: "%Y" }}</span></p>
{% endfor %}
</div>

## Teaching

{% for t in site.data.teaching %}
- **{{ t.role }}** — {{ t.course }}, {{ t.venue }} ({{ t.term }})
{% endfor %}

## Service & Leadership

- **STEM Coach** — Columbia School of General Studies (Jan–Jun 2024)
- **Astronomy Youth Outreach Coordinator** — Columbia Dept. of Astronomy (Aug 2023 – Present)
- **Undergraduate Mentor** — Foundational Course for Physical Science Transfers, UC Berkeley (2019 & 2020)
- **Research Mentor** — ULAB 21cm Cosmology Group, UC Berkeley (Aug 2019 – May 2020)
