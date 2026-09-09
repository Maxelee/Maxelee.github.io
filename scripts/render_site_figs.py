#!/usr/bin/env python3
"""Render BIND field caches into site-styled assets (magma on #070b14).

Inputs: the npz caches produced by talk_figs task_a_fm_frames.py /
task_b_param_sweep.py (frames/fields arrays of shape [N, 7, 128, 128];
channels 0=dm, 1=gas, 2=stars). Point CACHE at that directory and run with
any python that has numpy + matplotlib + Pillow.

Outputs (drop into images/ and convert to webp as noted in VISUALS.md):
  hero-gas-t1.png       homepage hero          -> images/bind/hero-field.webp
  trajectory-strip.png  noise->t.5->BIND->truth -> images/bind/trajectory.webp
  fm-gas.webp           flow-matching animation -> images/bind/fm-gas.webp
  sweep-*.webp          parameter sweep loops   -> images/bind/sweep-*.webp
  teaser-dm.png         methods paper teaser    -> images/pubs/bind-methods.webp

Normalization matches the talk figures: log10 stretch from the 5th percentile
of positive pixels to the 99.9th, fixed per channel from the t=1 frame;
nearest-neighbor upsample keeps the native 128^2 pixels crisp.
"""
import os
import numpy as np
from matplotlib import colormaps
from PIL import Image

CACHE = os.path.expanduser('~/Downloads/talk_figs2/cache')
OUT = os.path.expanduser('~/Desktop/site_renders')
BG = (7, 11, 20)
CMAP = colormaps['magma']
DM, GAS, STAR = 0, 1, 2


def stretch_from(ref):
    pos = ref[ref > 0]
    return np.percentile(pos, 5), np.percentile(pos, 99.9)


def render(img, lo, hi, size=512):
    a = np.log10(np.clip(img, lo, hi))
    a = (a - np.log10(lo)) / (np.log10(hi) - np.log10(lo))
    rgb = (CMAP(a)[..., :3] * 255).astype(np.uint8)
    return Image.fromarray(rgb).resize((size, size), Image.NEAREST)


def main():
    os.makedirs(OUT, exist_ok=True)
    za = np.load(f'{CACHE}/task_a_trajectory.npz')
    frames, truth, ts = za['frames'], za['truth'], za['ts']
    lo_g, hi_g = stretch_from(frames[-1, GAS])
    lo_d, hi_d = stretch_from(frames[-1, DM])

    # 4-panel trajectory strip (gas): noise -> t=0.5 -> BIND -> truth
    i_half = int(np.argmin(np.abs(ts - 0.5)))
    panels = [render(frames[0, GAS], lo_g, hi_g),
              render(frames[i_half, GAS], lo_g, hi_g),
              render(frames[-1, GAS], lo_g, hi_g),
              render(truth[GAS], lo_g, hi_g)]
    gap, size = 8, 512
    strip = Image.new('RGB', (size * 4 + gap * 3, size), BG)
    for i, p in enumerate(panels):
        strip.paste(p, (i * (size + gap), 0))
    strip.save(f'{OUT}/trajectory-strip.png')

    # Flow-matching animation (gas), long hold on the finished field
    anim = [render(frames[i, GAS], lo_g, hi_g) for i in range(len(frames))]
    dur = [60] * len(anim)
    dur[-1] = 1800
    anim[0].save(f'{OUT}/fm-gas.webp', save_all=True, append_images=anim[1:],
                 duration=dur, loop=0, quality=55, method=4)

    # Parameter sweeps (gas), ping-pong loops with holds at the ends
    for name, fn in [('sweep-imf', 'task_b_IMFslope'),
                     ('sweep-wind', 'task_b_VarWindVelFactor')]:
        zb = np.load(f'{CACHE}/{fn}.npz')
        flds = zb['fields']
        lo, hi = stretch_from(flds[len(flds) // 2, GAS])
        seq = [render(flds[i, GAS], lo, hi, 448) for i in range(len(flds))]
        pp = seq + seq[-2:0:-1]
        d = [90] * len(pp)
        d[0] = 700
        d[len(seq) - 1] = 700
        pp[0].save(f'{OUT}/{name}.webp', save_all=True, append_images=pp[1:],
                   duration=d, loop=0, quality=55, method=4)

    render(frames[-1, GAS], lo_g, hi_g, 1024).save(f'{OUT}/hero-gas-t1.png')
    render(frames[-1, DM], lo_d, hi_d, 640).save(f'{OUT}/teaser-dm.png')
    print('done ->', OUT)


if __name__ == '__main__':
    main()
