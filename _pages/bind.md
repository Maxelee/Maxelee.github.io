---
layout: page
title: "BIND"
eyebrow: "Featured project"
lede: "Baryonic INpainting with Deep learning — a conditional flow-matching model that paints baryons onto dark-matter-only simulations."
permalink: /bind/
description: "BIND (Baryonic INpainting with Deep learning): a conditional flow-matching model mapping dark-matter-only halos to full hydrodynamical fields, with a live GPU-backed explorer."
teaser: /images/bind/gas-web.webp
---

<figure class="bind-hero">
<img src="/images/bind/fm-gas.webp" alt="Animation of flow matching: a gas field emerging from pure noise into a cluster-mass halo" width="560" height="560">
<figcaption>Watch the generation itself: BIND integrates a learned velocity field from pure noise (t&thinsp;=&thinsp;0) to the finished gas field (t&thinsp;=&thinsp;1) of a cluster-mass halo — about a second of GPU time.</figcaption>
</figure>

**BIND** (Baryonic INpainting with Deep learning) is a conditional flow-matching model trained on the 1024 paired hydrodynamical and dark-matter-only simulations of the CAMELS SB35 suite. Given a dark-matter-only halo, it generates the corresponding dark matter, gas, and stellar mass fields — conditioned on the full 35-dimensional ΛCDM and IllustrisTNG galaxy formation parameter space.

Applied halo-by-halo to full N-body volumes and ray-traced, BIND produces convergence, optical depth, and Compton-y maps whose statistics match full hydrodynamical simulations to within the precision of upcoming surveys. The trained models, generated halos, and map suites are released as open-source tools.

<figure class="bind-wide">
<img src="/images/bind/gas-web.webp" alt="A wide slice of a 50 Mpc/h simulation volume: BIND-generated gas pasted onto the halos of the dark-matter cosmic web" loading="lazy" width="1800" height="792">
<figcaption>BIND gas pasted halo-by-halo into the dark-matter web of a 50 h⁻¹ Mpc volume.</figcaption>
</figure>

## One input, seven fields

From a single dark-matter-only conditioning field, BIND generates every baryonic channel at once — masses and thermodynamics — for the same halo in one draw:

<div class="field-grid">
<figure><img src="/images/bind/fields/dmo-input.webp" alt="Dark-matter-only input field" loading="lazy" width="420" height="420"><figcaption>DMO input</figcaption></figure>
<figure><img src="/images/bind/fields/dm.webp" alt="Generated dark matter field" loading="lazy" width="420" height="420"><figcaption>dark matter</figcaption></figure>
<figure><img src="/images/bind/fields/gas.webp" alt="Generated gas field" loading="lazy" width="420" height="420"><figcaption>gas</figcaption></figure>
<figure><img src="/images/bind/fields/stars.webp" alt="Generated stellar field" loading="lazy" width="420" height="420"><figcaption>stars</figcaption></figure>
<figure><img src="/images/bind/fields/y.webp" alt="Generated Compton-y field" loading="lazy" width="420" height="420"><figcaption>Compton-y</figcaption></figure>
<figure><img src="/images/bind/fields/temperature.webp" alt="Generated temperature field" loading="lazy" width="420" height="420"><figcaption>temperature</figcaption></figure>
<figure><img src="/images/bind/fields/pressure.webp" alt="Generated pressure field" loading="lazy" width="420" height="420"><figcaption>pressure</figcaption></figure>
<figure><img src="/images/bind/fields/entropy.webp" alt="Generated entropy field" loading="lazy" width="420" height="420"><figcaption>entropy</figcaption></figure>
</div>

## The papers

- [BIND (Baryonic INpainting with Deep learning): A Field-level Emulator for Galaxy Groups and Clusters](/publication/2026-09-09-BIND-methods) — the model: training, validation, and halo-level performance. [Download PDF](/files/BIND_methods.pdf)
- [BINDing the lightcone: A suite of astrophysical ray-traced weak lensing and SZ maps](/publication/2026-09-09-BIND-lightcone) — the maps: 1000 pseudo-independent realizations across the IllustrisTNG galaxy formation prior. [Download PDF](/files/BINDing_the_lightcone.pdf)

## Turning the astrophysical dials

BIND is conditioned on every IllustrisTNG galaxy formation parameter, so the same halo can be regenerated under different astrophysics. Here the same dark-matter-only halo is painted while one feedback parameter sweeps across the full SB35 prior (cyan tick) with everything else — including the initial noise — held fixed:

<div class="sweep-pair">
<figure>
<img src="/images/bind/sweep-sn.webp" alt="Animation of the same halo's gas field as the supernova wind energy parameter sweeps across its prior, with a position indicator below" loading="lazy" width="600" height="634">
<figcaption>A<sub>SN1</sub> &middot; galactic wind energy &middot; prior low &rarr; high</figcaption>
</figure>
<figure>
<img src="/images/bind/sweep-agn.webp" alt="Animation of the same halo's gas field as the AGN radio feedback parameter sweeps across its prior, with a position indicator below" loading="lazy" width="600" height="634">
<figcaption>A<sub>AGN1</sub> &middot; AGN radio feedback &middot; prior low &rarr; high</figcaption>
</figure>
</div>

And because BIND is generative rather than deterministic, every draw is a new plausible realization — same halo, same parameters, four different draws:

<figure class="bind-wide">
<img src="/images/bind/ensemble.webp" alt="Four side-by-side BIND draws of the same halo with identical parameters, each showing different small-scale structure" loading="lazy" width="2072" height="512">
<figcaption>one halo &middot; one parameter vector &middot; four independent draws</figcaption>
</figure>

## Does it get the physics right?

Start with the eye test — the same merging cluster, once from the full IllustrisTNG-300 simulation and once drawn by BIND from the dark-matter-only input alone, on a shared color scale:

<div class="sweep-pair">
<figure>
<img src="/images/bind/truth-gas.webp" alt="Gas field of a merging cluster from the IllustrisTNG-300 hydrodynamical simulation" loading="lazy" width="640" height="640">
<figcaption>IllustrisTNG-300 truth</figcaption>
</figure>
<figure>
<img src="/images/bind/bind-gas.webp" alt="Gas field of the same merging cluster generated by BIND from the dark-matter-only input" loading="lazy" width="640" height="640">
<figcaption>BIND draw from the DMO input</figcaption>
</figure>
</div>

Beyond looking right, the generated halos reproduce the target statistics. Pasted back into an N-body volume, BIND recovers the projected matter power-spectrum suppression to the accuracy ceiling set by pasting in the true hydrodynamical halos themselves:

<figure class="bind-validation">
<img src="/images/bind/validation-ps.webp" alt="Power spectrum ratio P(k) over P DMO of k, showing BIND tracking the truth and the hydro-replaced ceiling" loading="lazy" width="1059" height="1100">
<figcaption>Projected matter power-spectrum suppression: BIND (red) against the IllustrisTNG truth (black) and the hydro-replacement ceiling (dashed).</figcaption>
</figure>

## Try it live

The explorer lets you tune cosmological and astrophysical parameters with sliders and watch BIND generate halo projections in real time, running inference on a live GPU.

<div class="bind-notice">
<span>⚠️</span><span><strong>Note:</strong> the app runs on a cloud GPU and may take up to a minute to wake on first visit.</span>
</div>

<p><a href="/explorer/" target="_blank" rel="noopener" class="btn btn--primary">Launch the BIND Explorer ↗</a></p>
