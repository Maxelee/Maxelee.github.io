# Website visual briefs (cluster-side generation)

Instructions for generating final artwork for maxelee.github.io on the cluster.
Anything generated from these briefs replaces the current asset 1:1 (same
filename → drop in, done).

> **Status (Sep 2026):** briefs 1, 2, and the methods teaser are DONE — the
> talk_figs2 npz caches (task_a trajectory + task_b sweeps) were re-rendered
> site-side in magma via `scripts/render_site_figs.py`, which also produced
> animated flow-matching and parameter-sweep WebPs now on `/bind/`. Still
> open: **#3 (lightcone κ/τ/y maps)** — the highest-value remaining item —
> plus the optional #4/#5/#6b/#6c. New raw fields dropped as npz (same shapes
> as the talk caches) can be re-rendered with the same script.

**Global spec, applies to every asset:**

- PNG, sRGB, no alpha. Deliver at the pixel sizes below (2× display size);
  final compression to WebP happens site-side — do not pre-compress.
- Background must be `#070b14` (the site's page color), NOT pure black, so
  fields blend into the page. In matplotlib: `fig.patch.set_facecolor('#070b14')`
  and `ax.set_facecolor('#070b14')`.
- **No axes, ticks, labels, titles, colorbars, or scale bars.** Frame nothing.
- Colormaps: `magma` or `inferno` for mass/thermodynamic fields (site's hero
  look), `viridis` only for variance/uncertainty panels. Log-stretch surface
  density (`LogNorm` or `log10(1+M)`) so filaments are visible; clip the top
  ~0.1% so cores don't blow out.
- Template:

  ```python
  fig, ax = plt.subplots(figsize=(size/dpi, size/dpi), dpi=dpi)
  fig.patch.set_facecolor('#070b14'); ax.set_facecolor('#070b14')
  ax.imshow(np.log10(1 + field), cmap='magma', origin='lower',
            vmin=vmin, vmax=vmax)
  ax.set_axis_off()
  fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
  fig.savefig(out, dpi=dpi, facecolor='#070b14')
  ```

## Assets (in priority order)

### 1. `hero-field.png` — 2000×2000
The homepage hero image. A single visually rich BIND-generated halo:
cluster-mass (M200c ≳ 10^14), **gas or dark-matter** channel, magma, with
plenty of filamentary substructure in frame. Choose the prettiest of ~10
candidate draws — this is the first thing every search committee sees.
Replaces `images/bind/hero-field.webp`.

### 2. `trajectory-{a,b,c}.png` — 3 files, 1400×1400 each
The flow-matching story, one halo, same channel (gas preferred), same
color scale across all three: (a) t=0 pure noise, (b) t≈0.5 intermediate,
(c) t=1 generated field. These get composed into the homepage strip
`images/bind/trajectory.webp` site-side. Use the SAME halo and normalization
so the morphology visibly emerges from noise.

### 3. `lightcone-{kappa,tau,y}.png` — 3 files, 1500×1500 each
Square cutouts from the BIND ray-traced maps at fiducial parameters:
convergence κ (use `magma` on log(1+κ−κmin) or an asinh stretch — NOT the
red/blue diverging map from the paper), optical depth τ (`inferno`), and
Compton-y (`magma`, log). The y-map is used as the lightcone paper teaser
(`images/pubs/bind-lightcone.webp`); κ may become a page banner.

### 4. `og-field.png` — 1260×1260
Any especially striking field (can reuse #1's halo at different rotation).
Composed site-side into the 1200×630 social-preview card.

### 5. `favicon-halo.png` — 512×512 (optional)
One compact bright halo, centered, magma on `#070b14`, readable at 16 px
(i.e., essentially a glowing dot with a hint of structure). If it reads
well tiny, it replaces the monogram favicon; if not, skip.

### 6. Paper teasers (optional upgrades, 800×800 each)
- `teaser-methods.png`: gas-channel BIND draw of a group-mass halo
  (replaces `images/pubs/bind-methods.webp`).
- `teaser-bmr.png`: for the mass/radius paper — a hydro-minus-DMO
  difference field around one massive halo (diverging `RdBu_r` is OK here),
  or the replaced-region field itself (replaces
  `images/pubs/baryon-mass-radius.webp`).
- `teaser-ia.png`: shear/convergence patch, viridis (replaces
  `images/pubs/ia.webp`).

## Delivery

Drop the PNGs anywhere in the repo (e.g. a `_incoming/` folder) or send them
over, and say which brief each corresponds to; conversion, cropping, and
wiring happen site-side.
