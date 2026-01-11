"""Create a 2x2 multipanel figure for Chapter 13 from four saved images.

Files expected in this directory:
 - fig-13.01.A.png
 - fig-13.01.B.png
 - fig-13.01.C.png
 - fig-13.01.D.png

Output:
 - JupyterBook/Figures/fig-13-multipanel.png and .pdf

Usage: python make_ch13_multipanel.py
"""

from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as pe

HERE = Path(__file__).resolve().parent
FILES = {
    'a': 'fig-13.01.A.png',
    'b': 'fig-13.01.B.png',
    'c': 'fig-13.01.C.png',
    'd': 'fig-13.01.D.png',
}
OUTDIR = Path(__file__).resolve().parents[2] / 'JupyterBook' / 'Figures'
OUTNAME = OUTDIR / 'fig-13-multipanel'

# Load images from the project's JupyterBook/Figures directory
images = {}
for k, fname in FILES.items():
    p = OUTDIR / fname
    if not p.exists():
        raise FileNotFoundError(f"Missing image in JupyterBook/Figures: {p}")
    images[k] = Image.open(p).convert('RGBA')

# Create figure
fig = plt.figure(figsize=(8.5, 8.5))
gs = gridspec.GridSpec(nrows=2, ncols=2, hspace=0.02, wspace=0.02)
axes = [fig.add_subplot(gs[0,0]), fig.add_subplot(gs[0,1]), fig.add_subplot(gs[1,0]), fig.add_subplot(gs[1,1])]
keys = ['a','b','c','d']

for ax, k in zip(axes, keys):
    ax.imshow(images[k])
    # Hide axes for a clean multipanel layout (no labels)
    ax.axis('off')

# Minimal margins
plt.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)

# Ensure output directory exists
OUTDIR.mkdir(parents=True, exist_ok=True)

for ext in ('.png', '.pdf'):
    out = OUTNAME.with_suffix(ext)
    fig.savefig(out, dpi=300, bbox_inches='tight')
    print(f"Saved {out}")

plt.close(fig)

if __name__ == '__main__':
    pass
