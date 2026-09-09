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
<img src="/images/bind/fm-gas.webp" alt="Animation of flow matching: a gas field emerging from pure noise into a cluster-mass halo" width="512" height="512">
<figcaption>Watch the generation itself: BIND integrates a learned velocity field from pure noise (t&thinsp;=&thinsp;0) to the finished gas field (t&thinsp;=&thinsp;1) of a 10¹⁴ M⊙ halo — about a second of GPU time.</figcaption>
</figure>

**BIND** (Baryonic INpainting with Deep learning) is a conditional flow-matching model trained on the 1024 paired hydrodynamical and dark-matter-only simulations of the CAMELS SB35 suite. Given a dark-matter-only halo, it generates the corresponding dark matter, gas, and stellar mass fields — conditioned on the full 35-dimensional ΛCDM and IllustrisTNG galaxy formation parameter space.

Applied halo-by-halo to full N-body volumes and ray-traced, BIND produces convergence, optical depth, and Compton-y maps whose statistics match full hydrodynamical simulations to within the precision of upcoming surveys. The trained models, generated halos, and map suites are released as open-source tools.

<figure class="bind-wide">
<img src="/images/bind/gas-web.webp" alt="A wide slice of a 50 Mpc/h simulation volume: BIND-generated gas pasted onto the halos of the dark-matter cosmic web" loading="lazy" width="1800" height="792">
<figcaption>BIND gas pasted halo-by-halo into the dark-matter web of a 50 h⁻¹ Mpc volume.</figcaption>
</figure>

## The papers

- [BIND (Baryonic INpainting with Deep learning): A Field-level Emulator for Galaxy Groups and Clusters](/publication/2026-09-09-BIND-methods) — the model: training, validation, and halo-level performance. [Download PDF](/files/BIND_methods.pdf)
- [BINDing the lightcone: A suite of astrophysical ray-traced weak lensing and SZ maps](/publication/2026-09-09-BIND-lightcone) — the maps: 1000 pseudo-independent realizations across the IllustrisTNG galaxy formation prior. [Download PDF](/files/BINDing_the_lightcone.pdf)

## Turning the astrophysical dials

BIND is conditioned on every IllustrisTNG galaxy formation parameter, so the same halo can be regenerated under different astrophysics. Here one parameter sweeps across its prior while everything else — including the initial noise — stays fixed:

<div class="sweep-pair">
<figure>
<img src="/images/bind/sweep-wind.webp" alt="Animation of the same halo's gas field as the galactic wind velocity factor sweeps from 3.7 to 14.8" width="448" height="448">
<figcaption>galactic wind velocity &times;3.7 &rarr; &times;14.8</figcaption>
</figure>
<figure>
<img src="/images/bind/sweep-imf.webp" alt="Animation of the same halo's gas field as the stellar initial mass function slope sweeps from minus 2.8 to minus 1.8" width="448" height="448">
<figcaption>IMF slope &minus;2.8 &rarr; &minus;1.8</figcaption>
</figure>
</div>

And because BIND is generative rather than deterministic, every draw is a new plausible realization — same halo, same parameters, three different draws:

<figure class="bind-wide">
<img src="/images/bind/ensemble.webp" alt="Three side-by-side BIND draws of the same halo with identical parameters, each showing different small-scale structure" loading="lazy" width="1552" height="512">
<figcaption>one halo &middot; one parameter vector &middot; three independent draws</figcaption>
</figure>

## Does it get the physics right?

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

<p><a href="https://maxelee--halo-explorer-haloserver-web.modal.run" target="_blank" rel="noopener noreferrer" class="btn btn--primary">Launch the BIND Explorer ↗</a></p>
