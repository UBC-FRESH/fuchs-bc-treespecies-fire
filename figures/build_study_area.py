"""Build the TSA24 study-area map for the manuscript.

Environment: needs geopandas, pyogrio, matplotlib. Run from the repository root:

    python figures/build_study_area.py

Inputs are the public FEMIC TSA24 instance layers. Set FEMIC_TSA24 to the instance
directory if it is not in the default location.
"""

from __future__ import annotations

import os
from pathlib import Path

import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import pyogrio

matplotlib.use("Agg")

INSTANCE = Path(os.environ.get("FEMIC_TSA24", "/data/femic-tsa24-instance"))
STANDS = INSTANCE / "data/shp/tsa24.shp/stands.shp"
BOUNDARY = INSTANCE / "data/tsa_boundaries.feather"
OUTPUT = Path(__file__).with_name("studyArea_map.pdf")

# Leading-species crosswalk from the stand species code to a display group.
GROUPS = {
    "SX": "Spruce",
    "SE": "Engelmann spruce",
    "PLI": "Lodgepole pine",
    "BL": "Subalpine fir",
    "AT": "Deciduous",
    "ACT": "Deciduous",
    "AC": "Deciduous",
    "DR": "Deciduous",
    "EP": "Deciduous",
    "MB": "Deciduous",
}
COLOURS = {
    "Spruce": "#14532d",
    "Lodgepole pine": "#d99a2b",
    "Subalpine fir": "#1f6f80",
    "Engelmann spruce": "#6aa832",
    "Deciduous": "#c94a22",
    "Other": "#cccccc",
}


def load_stands() -> gpd.GeoDataFrame:
    """Read the stand polygons with the columns needed for the map.

    Returns
    -------
    geopandas.GeoDataFrame
        Stand polygons with a ``group`` column.
    """
    stands = gpd.read_file(STANDS, columns=["SPECIES_CD", "geometry"])
    code = stands["SPECIES_CD"].astype(str).str.upper().str.strip()
    stands["group"] = code.map(GROUPS).fillna("Other")
    return stands


def draw() -> None:
    """Draw and write the map."""
    stands = load_stands()
    boundary = gpd.read_feather(BOUNDARY)
    boundary = boundary.to_crs(stands.crs)

    fig, ax = plt.subplots(figsize=(6.4, 5.6))
    for group, colour in COLOURS.items():
        subset = stands[stands["group"] == group]
        if subset.empty:
            continue
        subset.plot(ax=ax, color=colour, linewidth=0, rasterized=True, label=group)
    boundary.boundary.plot(ax=ax, color="black", linewidth=0.9)

    ax.set_axis_off()
    ax.set_aspect("equal")
    handles, labels = ax.get_legend_handles_labels()
    order = [labels.index(k) for k in COLOURS if k in labels]
    ax.legend(
        [handles[i] for i in order],
        [labels[i] for i in order],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.01),
        ncol=3,
        fontsize=7,
        frameon=False,
        title="Leading species",
        title_fontsize=7,
    )
    # Scale bar: 100 km, drawn in the projected CRS (metres).
    x0, y0 = ax.get_xlim()[0], ax.get_ylim()[0]
    span = ax.get_xlim()[1] - x0
    length = 100_000
    ax.plot([x0 + 0.03 * span, x0 + 0.03 * span + length], [y0 + 0.04 * span, y0 + 0.04 * span],
            color="black", linewidth=1.2)
    ax.text(x0 + 0.03 * span, y0 + 0.055 * span, "100 km", fontsize=7)

    fig.tight_layout()
    fig.savefig(OUTPUT, bbox_inches="tight", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    draw()
    print(f"wrote {OUTPUT}")
