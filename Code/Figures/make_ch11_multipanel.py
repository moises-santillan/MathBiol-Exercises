"""Create a multipanel figure for Chapter 11.

Layout:
 - Top row: fig-11.02.I.png (saddle) spanning both columns -> panel (a)
 - Second row: fig-11.02.II.png (unstable node) -> panel (b)
               fig-11.02.V.png  (stable node)   -> panel (c)
 - Third row:  fig-11.03.III.png (unstable spiral) -> panel (d)
               fig-11.03.IV.png  (stable spiral)   -> panel (e)

Saves output to JupyterBook/Figures/fig-11-multipanel.png and .pdf

Usage: python make_ch11_multipanel.py
"""

from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as pe

# Paths
# __file__ is in Code/Figures; JupyterBook is in the repo root, so go two parents up.
BASE = Path(__file__).resolve().parents[2] / 'JupyterBook' / 'Figures'
FILES = {
    'a': 'fig-11.02.I.png',   # saddle
    'b': 'fig-11.02.II.png',  # unstable node
    'c': 'fig-11.02.V.png',   # stable node
    'd': 'fig-11.03.III.png', # unstable spiral
    'e': 'fig-11.03.IV.png',  # stable spiral
}
OUTNAME = BASE / 'fig-11-multipanel'

# Load images and check
images = {}
for key, fname in FILES.items():
    path = BASE / fname
    if not path.exists():
        raise FileNotFoundError(f"Required image not found: {path}")
    images[key] = Image.open(path).convert('RGBA')

# Create figure with GridSpec 3x2; top row spans both columns
# Use a slightly larger figure so panels retain clarity when packed tightly
fig = plt.figure(figsize=(10, 12), constrained_layout=False)
# Remove inter-panel gaps entirely and minimize whitespace at figure edges
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1.0, 1.0, 1.0], hspace=0.0, wspace=0.0)
# Reduce figure margins to pack panels tightly
plt.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005) 

ax_a = fig.add_subplot(gs[0, :])  # spans both columns
ax_b = fig.add_subplot(gs[1, 0])
ax_c = fig.add_subplot(gs[1, 1])
ax_d = fig.add_subplot(gs[2, 0])
ax_e = fig.add_subplot(gs[2, 1])

axes = [ax_a, ax_b, ax_c, ax_d, ax_e]
keys = ['a', 'b', 'c', 'd', 'e']

for ax, k in zip(axes, keys):
    img = images[k]
    ax.imshow(img)
    # Hide axis ticks and frames for a cleaner multipanel look
    ax.axis('off')
    # Label panels (a)-(e) centered at the top of each panel; add thin outline for legibility
    txt = ax.text(0.5, 0.93, f"({k})", transform=ax.transAxes,
            fontsize=12, fontweight='bold', va='top', ha='center', color='black')
    # Add a white outline to the black label so it remains legible over varied backgrounds
    txt.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Removed overall suptitle per layout preference

# Save
for ext in ('.png', '.pdf'):
    outpath = OUTNAME.with_suffix(ext)
    fig.savefig(outpath, dpi=300, bbox_inches='tight')
    print(f"Saved {outpath}")

plt.close(fig)

if __name__ == '__main__':
    pass
