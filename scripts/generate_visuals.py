"""
Northstar HealthTech — NIST CSF 2.0 Gap Assessment
Visual generation script.

Produces three consistently styled figures:
  1. maturity-heatmap.png   — Current maturity + Gap, using two semantically
                               distinct colormaps (sequential blue for a score,
                               sequential red for a deficit) rather than one
                               shared scale across unlike quantities.
  2. maturity-by-finding.png — Current vs Target bars, sorted by gap size
                               (largest gap first) so the reader sees the
                               worst findings without hunting.
  3. risk-matrix.png        — The 5x5 likelihood/impact reference matrix with
                               the assessment's actual 12 findings overlaid as
                               markers, so this is *this* organization's risk
                               profile rather than a generic reference chart.

Run from the project root (script lives in scripts/ or similar); output goes
to ../visuals/ relative to this file's parent directory.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

BASE = Path(__file__).resolve().parents[1]
VISUALS = BASE / "visuals"
VISUALS.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# Shared style
# ---------------------------------------------------------------------------

plt.rcParams.update({
    "font.size": 11,
    "font.family": "sans-serif",
    "axes.titlesize": 15,
    "axes.titleweight": "medium",
    "axes.edgecolor": "#444444",
    "axes.labelsize": 11,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

FIG_WIDTH = 12  # unify figure width across all three charts

COLOR_CURRENT = "#2E5C8A"   # muted blue  — "where we are"
COLOR_TARGET = "#F2A541"    # amber       — "where we need to be"
COLOR_GAP = "#C0392B"       # brick red   — "the deficit"

CMAP_CURRENT = "Blues"      # sequential — current maturity is a level (0-5)
CMAP_GAP = "Reds"           # sequential — gap is a deficit, bigger = worse

# ---------------------------------------------------------------------------
# Data — 12 core findings
# ---------------------------------------------------------------------------

findings = [f"GRC-{i:03d}" for i in range(1, 13)]
current = np.array([1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2])
target = np.array([4] * 12)
gap = target - current

# Likelihood / Impact per finding, from the risk register (1-5 scale each)
# Likelihood: Rare=1, Unlikely=2, Possible=3, Likely=4, Almost Certain=5
# Impact:     Insignificant=1, Minor=2, Moderate=3, Major=4, Severe=5
likelihood = np.array([4, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3])
impact = np.array([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4])

# ---------------------------------------------------------------------------
# 1. Maturity heatmap — Current (blue) + Gap (red), separate scales
# ---------------------------------------------------------------------------

fig, (ax_cur, ax_gap) = plt.subplots(
    2, 1, figsize=(FIG_WIDTH, 5), sharex=True,
    gridspec_kw={"height_ratios": [1, 1], "hspace": 0.35},
)

fig.suptitle(
    "Northstar HealthTech — Current Maturity and Maturity Gap by Finding",
    fontsize=15, fontweight="medium", y=1.02,
)

# --- Current maturity row (0-4 scale, Blues) ---
im1 = ax_cur.imshow(
    current.reshape(1, -1), aspect="auto", cmap=CMAP_CURRENT, vmin=0, vmax=4,
)
ax_cur.set_yticks([0])
ax_cur.set_yticklabels(["Current\nMaturity"])
ax_cur.set_xticks(range(12))
ax_cur.set_xticklabels([])  # shared x-axis, labels on bottom subplot only
for j in range(12):
    val = current[j]
    text_color = "white" if val >= 2.5 else "black"
    ax_cur.text(j, 0, str(val), ha="center", va="center",
                color=text_color, fontsize=11, fontweight="bold")
cbar1 = fig.colorbar(im1, ax=ax_cur, fraction=0.025, pad=0.02)
cbar1.set_label("Score (0–5)", fontsize=9)
cbar1.ax.tick_params(labelsize=8)

# --- Gap row (deficit, Reds — bigger = worse) ---
im2 = ax_gap.imshow(
    gap.reshape(1, -1), aspect="auto", cmap=CMAP_GAP, vmin=0, vmax=4,
)
ax_gap.set_yticks([0])
ax_gap.set_yticklabels(["Maturity\nGap"])
ax_gap.set_xticks(range(12))
ax_gap.set_xticklabels(findings, rotation=45, ha="right")
for j in range(12):
    val = gap[j]
    text_color = "white" if val >= 2.5 else "black"
    ax_gap.text(j, 0, str(val), ha="center", va="center",
                color=text_color, fontsize=11, fontweight="bold")
cbar2 = fig.colorbar(im2, ax=ax_gap, fraction=0.025, pad=0.02)
cbar2.set_label("Gap (Target − Current)", fontsize=9)
cbar2.ax.tick_params(labelsize=8)

fig.text(
    0.5, -0.04,
    "All findings target Level 4 (Managed). Current maturity and the resulting gap "
    "are shown separately since they measure different things: a level vs. a deficit.",
    ha="center", fontsize=9, style="italic", color="#555555",
)

fig.savefig(VISUALS / "maturity-heatmap.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# 2. Current vs Target bar chart — sorted by gap size (largest first)
# ---------------------------------------------------------------------------

order = np.argsort(-gap)  # descending gap
findings_sorted = [findings[i] for i in order]
current_sorted = current[order]
target_sorted = target[order]
gap_sorted = gap[order]

x = np.arange(12)
w = 0.38

fig, ax = plt.subplots(figsize=(FIG_WIDTH, 6))
bars_cur = ax.bar(x - w / 2, current_sorted, w, label="Current",
                   color=COLOR_CURRENT)
bars_tgt = ax.bar(x + w / 2, target_sorted, w, label="Target",
                   color=COLOR_TARGET)

# Annotate gap above each pair
for xi, c, t, g in zip(x, current_sorted, target_sorted, gap_sorted):
    ax.text(xi, t + 0.12, f"gap {g}", ha="center", va="bottom",
            fontsize=8.5, color="#555555")

ax.set_title("Northstar HealthTech — Current vs Target Maturity\n(sorted by largest gap first)")
ax.set_ylabel("Maturity Score (0–5)")
ax.set_xticks(x)
ax.set_xticklabels(findings_sorted, rotation=45, ha="right")
ax.set_ylim(0, 5.3)
ax.legend(frameon=False, loc="upper right")
ax.grid(axis="y", alpha=0.25)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(VISUALS / "maturity-by-finding.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# 3. Risk matrix — reference grid + actual findings overlaid
# ---------------------------------------------------------------------------

risk_scores = np.array([[lik * imp for imp in range(1, 6)] for lik in range(5, 0, -1)])

import textwrap
from collections import defaultdict

fig, (ax, ax_legend) = plt.subplots(
    1, 2, figsize=(FIG_WIDTH, 7.5),
    gridspec_kw={"width_ratios": [2.1, 1]},
)

im = ax.imshow(risk_scores, aspect="equal", cmap="viridis", alpha=0.55)

ax.set_title("Northstar HealthTech — 5×5 Risk Matrix\nwith Assessed Findings Overlaid")
ax.set_xlabel("Impact")
ax.set_ylabel("Likelihood")
ax.set_xticks(range(5), ["1\nInsig.", "2\nMinor", "3\nModerate", "4\nMajor", "5\nSevere"])
ax.set_yticks(range(5), ["5\nAlmost\nCertain", "4\nLikely", "3\nPossible", "2\nUnlikely", "1\nRare"])

for i in range(5):
    for j in range(5):
        s = int(risk_scores[i, j])
        r = "L" if s <= 4 else "M" if s <= 9 else "H" if s <= 16 else "C"
        ax.text(j, i, f"{s}\n{r}", ha="center", va="center",
                fontsize=9, color="#333333")

# --- Overlay actual findings ---
# Row index 0 = Likelihood 5 (top) ... row 4 = Likelihood 1 (bottom).
# Col index 0 = Impact 1 ... col 4 = Impact 5.
plot_rows = 5 - likelihood
plot_cols = impact - 1

cell_groups = defaultdict(list)
for name, r, c in zip(findings, plot_rows, plot_cols):
    cell_groups[(r, c)].append(name)

# Marker + a compact count badge on the chart itself (no long text labels
# on-chart — full listing goes in the side panel instead, so nothing
# overflows regardless of how many findings share a cell).
for (r, c), names in cell_groups.items():
    n = len(names)
    ax.scatter(c, r, s=340, color="white", edgecolor="#111111",
               linewidth=1.6, zorder=5, marker="o")
    ax.text(c, r, str(n), ha="center", va="center",
            fontsize=11, fontweight="bold", color="#111111", zorder=6)

legend_handle = mpatches.Patch(
    facecolor="white", edgecolor="#111111",
    label="● = assessed finding(s); number = count in that cell"
)
ax.legend(handles=[legend_handle], loc="upper center",
          bbox_to_anchor=(0.5, -0.12), frameon=False, fontsize=8.5)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Risk Score (Likelihood × Impact)", fontsize=9)

# --- Side panel: full finding-to-cell listing, wrapped to fit ---
ax_legend.axis("off")
ax_legend.set_title("Findings by Risk Cell", fontsize=12, loc="left", pad=10)

# Sort cells by risk score descending so the worst appears first
sorted_cells = sorted(
    cell_groups.items(),
    key=lambda kv: risk_scores[kv[0][0], kv[0][1]],
    reverse=True,
)

y = 1.0
line_height = 0.09
for (r, c), names in sorted_cells:
    score = int(risk_scores[r, c])
    rating = "L" if score <= 4 else "M" if score <= 9 else "H" if score <= 16 else "C"
    lik_label = 5 - r
    imp_label = c + 1
    header = f"Score {score} ({rating}) — Likelihood {lik_label} × Impact {imp_label}"
    ax_legend.text(0, y, header, fontsize=9, fontweight="bold",
                    color="#111111", transform=ax_legend.transAxes, va="top")
    y -= line_height * 0.75

    wrapped = textwrap.fill(", ".join(names), width=42)
    n_lines = wrapped.count("\n") + 1
    ax_legend.text(0.02, y, wrapped, fontsize=8.5, color="#333333",
                    transform=ax_legend.transAxes, va="top")
    y -= line_height * (0.55 * n_lines + 0.45)

fig.tight_layout()
fig.savefig(VISUALS / "risk-matrix.png", dpi=180, bbox_inches="tight")
plt.close(fig)

print("Generated: maturity-heatmap.png, maturity-by-finding.png, risk-matrix.png")
