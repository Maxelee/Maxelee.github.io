---
layout: splash
title: "BIND Halo Explorer"
permalink: /bind/
author_profile: false
---

## BIND Halo Explorer

**BIND** (Baryonification and Intrinsic alignment Neural Diffusion model) is a field-level generative model trained on IllustrisTNG simulations. It maps dark matter-only fields to full hydrodynamical fields — including gas, stars, and dark matter — conditioned on IllustrisTNG's astrophysical and cosmological parameters.

The explorer below lets you tune the 28-dimensional IllustrisTNG parameter space with sliders and watch BIND generate halo projections in real time, running inference on a live GPU.

<div class="bind-notice">
  ⚠️ <strong>Note:</strong> The app runs on a cloud GPU and may take up to a minute to load on first visit. If the frame is blank, wait a moment and refresh.
</div>

<div class="bind-embed">
  <iframe
    src="https://maxelee--halo-explorer-haloserver-web.modal.run"
    title="BIND Halo Explorer"
    allowfullscreen
    loading="lazy"
  ></iframe>
</div>
