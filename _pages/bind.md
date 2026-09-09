---
layout: page
title: "BIND"
eyebrow: "Featured project"
lede: "Baryonic INpainting with Deep learning — a conditional flow-matching model that paints baryons onto dark-matter-only simulations."
permalink: /bind/
description: "BIND (Baryonic INpainting with Deep learning): a conditional flow-matching model mapping dark-matter-only halos to full hydrodynamical fields, with a live GPU-backed explorer."
teaser: /images/bind/hero-field.webp
---

<figure class="bind-hero">
<img src="/images/bind/trajectory.webp" alt="Three panels showing the dark-matter-only input field, a BIND draw, and the mean over 100 BIND draws" width="1954" height="646">
<figcaption>DMO input → a BIND draw → the mean over 100 draws, for a cluster-mass halo.</figcaption>
</figure>

**BIND** (Baryonic INpainting with Deep learning) is a conditional flow-matching model trained on the 1024 paired hydrodynamical and dark-matter-only simulations of the CAMELS SB35 suite. Given a dark-matter-only halo, it generates the corresponding dark matter, gas, and stellar mass fields — conditioned on the full 35-dimensional ΛCDM and IllustrisTNG galaxy formation parameter space, in about a second per halo on one GPU.

Applied halo-by-halo to full N-body volumes and ray-traced, BIND produces convergence, optical depth, and Compton-y maps whose statistics match full hydrodynamical simulations to within the precision of upcoming surveys. The trained models, generated halos, and map suites are released as open-source tools.

## The papers

- [BIND (Baryonic INpainting with Deep learning): A Field-level Emulator for Galaxy Groups and Clusters](/publication/2026-09-09-BIND-methods) — the model: training, validation, and halo-level performance. [Download PDF](/files/BIND_methods.pdf)
- [BINDing the lightcone: A suite of astrophysical ray-traced weak lensing and SZ maps](/publication/2026-09-09-BIND-lightcone) — the maps: 1000 pseudo-independent realizations across the IllustrisTNG galaxy formation prior. [Download PDF](/files/BINDing_the_lightcone.pdf)

## Try it live

The explorer lets you tune cosmological and astrophysical parameters with sliders and watch BIND generate halo projections in real time, running inference on a live GPU.

<div class="bind-notice">
<span>⚠️</span><span><strong>Note:</strong> the app runs on a cloud GPU and may take up to a minute to wake on first visit.</span>
</div>

<p><a href="https://maxelee--halo-explorer-haloserver-web.modal.run" target="_blank" rel="noopener noreferrer" class="btn btn--primary">Launch the BIND Explorer ↗</a></p>
