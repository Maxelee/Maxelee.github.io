---
layout: page
title: "Launching the BIND Explorer"
eyebrow: "Live demo"
permalink: /explorer/
description: "Warming up a cloud GPU for the BIND halo explorer — live flow-matching inference on demand."
sitemap: false
---

<div id="launch-status" class="launch-status">
  <div class="launch-status__bar"><div class="launch-status__fill" id="launch-fill"></div></div>
  <p id="launch-msg">Waking up a dedicated GPU for you — this usually takes 30&ndash;60 seconds. You'll be redirected automatically.</p>
</div>

While you wait: this is what the explorer does. The same dark-matter-only halo, re-painted by BIND as one
feedback parameter sweeps across its full prior (cyan tick) — everything else, including the initial noise, held fixed:

<div class="sweep-pair">
<figure>
<img src="/images/bind/sweep-sn.webp" alt="Animation of the same halo's gas field as the supernova wind energy parameter sweeps across its prior" width="600" height="634">
<figcaption>supernova wind energy</figcaption>
</figure>
<figure>
<img src="/images/bind/sweep-agn.webp" alt="Animation of the same halo's gas field as the AGN radio feedback parameter sweeps across its prior" width="600" height="634">
<figcaption>AGN radio feedback</figcaption>
</figure>
</div>

In the explorer you get sliders for these parameters — and the rest of the 35-dimensional space — with a live
GPU generating each halo in about a second.

<p id="launch-manual" hidden><a id="launch-link" class="btn btn--primary" href="https://maxelee--halo-explorer-haloserver-web.modal.run">Open the explorer now ↗</a></p>

<script>
(function () {
  var URL_ = "https://maxelee--halo-explorer-haloserver-web.modal.run";
  var msg = document.getElementById("launch-msg");
  var fill = document.getElementById("launch-fill");
  var manual = document.getElementById("launch-manual");
  var t0 = Date.now();

  // Progress bar eases toward ~90% over a minute; jumps to 100% on ready.
  var timer = setInterval(function () {
    var t = (Date.now() - t0) / 60000;
    fill.style.width = Math.min(90, 100 * (1 - Math.exp(-2.2 * t))) + "%";
  }, 250);

  // Modal's ingress holds the request open while the container cold-starts,
  // so this resolves (opaque) the moment the app is actually serving.
  fetch(URL_, { mode: "no-cors", cache: "no-store" }).then(function () {
    clearInterval(timer);
    fill.style.width = "100%";
    msg.textContent = "GPU is up — taking you to the explorer.";
    setTimeout(function () { window.location.href = URL_; }, 400);
  }).catch(function () {
    clearInterval(timer);
    msg.textContent = "Couldn't reach the explorer automatically — try the button below.";
    manual.hidden = false;
  });

  // Safety net: after 75 s, surface the manual link either way.
  setTimeout(function () { manual.hidden = false; }, 75000);
})();
</script>
