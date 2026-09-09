---
title: "BIND (Baryonic INpainting with Deep learning): A Field-level Emulator for Galaxy Groups and Clusters"
collection: publications
permalink: /publication/2026-09-09-BIND-methods
excerpt: 'A conditional flow-matching model that maps dark-matter-only halos to their hydrodynamical counterparts across the full 35-dimensional CAMELS SB35 parameter space.'
date: 2026-09-09
venue: 'Submitted'
selected: true
selected_order: 1
teaser: /images/pubs/bind-methods.webp
authors: 'M. E. Lee, S. Genel, Z. Haiman, G. L. Bryan, C. C. Lovell, B. Hadzhiyska'
paperurl: 'https://maxelee.github.io/files/BIND_methods.pdf'
citation: 'M. E. Lee, S. Genel, Z. Haiman, G. L. Bryan, C. C. Lovell, B. Hadzhiyska (2026) &quot;BIND (Baryonic INpainting with Deep learning): A Field-level Emulator for Galaxy Groups and Clusters.&quot; <i>submitted</i>.'
---

Baryonic feedback is a dominant source of systematic uncertainty for upcoming weak-lensing surveys, but current tools for modeling its effect rely on spherical approximations and density profiles calibrated almost entirely on two-point statistics. We introduce BIND (Baryonic INpainting with Deep learning), a conditional flow-matching model that learns a field-level mapping from dark-matter-only halos to their hydrodynamical counterparts. BIND is trained on halos from the 1024 paired hydrodynamical and dark-matter-only simulations of the CAMELS 50 h⁻¹ Mpc SB35 suite and samples dark matter, gas, and stellar mass fields over redshift across the full 35-dimensional ΛCDM and IllustrisTNG galaxy formation parameter space. BIND recovers dark matter, gas, and stellar masses at the percent level, reproduces azimuthally averaged profiles to ≲10% at all radii, and matches halo shape distributions with high fidelity. The learned parameter dependence captures the rank correlations between the generated fields and the subgrid parameters, and the field-level response to individual parameter variations is recovered in both sign and morphology. Halo mass is never supplied as conditioning, yet the baryon fraction, stellar-to-halo mass relation, inter-component scaling relations, and the joint covariance of their residuals are all reproduced. We finally show that, applied halo-by-halo to a (50 h⁻¹ Mpc)³ N-body volume with 512³ particles, BIND reproduces the projected matter power spectrum suppression to the accuracy ceiling set by pasting in the hydrodynamical halos themselves, in minutes on one GPU. We release the trained BIND models and all generated halos as open-source tools. A companion paper extends BIND to thermodynamic fields and non-Gaussian weak-lensing statistics.
