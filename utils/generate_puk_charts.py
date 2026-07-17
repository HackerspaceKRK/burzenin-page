#!/usr/bin/env python3
"""
Generuje wykresy "Liczba uczestników" i "Liczba projektów" widoczne na _pages/puk.md
(assets/images/puk_uczestnicy.png i assets/images/puk_projekty.png).

Dane liczone są z front matter kolekcji _puk/ (pola puk_year i author), więc
wykresy zawsze odzwierciedlają aktualny stan repo - wystarczy uruchomić skrypt
ponownie po dodaniu nowych wpisów PUK.

Użycie:
    python3 utils/generate_puk_charts.py [--out DIR]

Wymaga: matplotlib, pyyaml (oba dostępne przez `pip install matplotlib pyyaml`
albo pakiety systemowe python3-matplotlib / python3-yaml).
"""

import argparse
import colorsys
import glob
import os
import re

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import yaml

REPO_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
PUK_DIR = os.path.join(REPO_ROOT, "_puk")
DEFAULT_OUT_DIR = os.path.join(REPO_ROOT, "assets", "images")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)

# Kolory 2010-2019 spróbkowane bezpośrednio z oryginalnych PNG-ów, żeby nowe
# wykresy wyglądały identycznie dla lat, które już na nich były.
BASE_PALETTE = [
    "#807DBA", "#E08214", "#41AB5D", "#41CC5D", "#BBAB5D",
    "#41AB88", "#88AB88", "#45AB88", "#845B88", "#88A458",
]

TITLE_COLOR = "#030431"
LABEL_COLOR = "#000000"
_AVAILABLE_FONTS = {f.name for f in fm.fontManager.ttflist}
FONT_FAMILY = "Roboto" if "Roboto" in _AVAILABLE_FONTS else "DejaVu Sans"


def load_puk_stats():
    """Zwraca {rok: {"projects": int, "participants": set(callsigns)}} z _puk/*.md."""
    stats = {}
    for path in sorted(glob.glob(os.path.join(PUK_DIR, "*.md"))):
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        match = FRONTMATTER_RE.match(content)
        if not match:
            continue
        front_matter = yaml.safe_load(match.group(1)) or {}
        year = front_matter.get("puk_year")
        if year is None:
            continue
        entry = stats.setdefault(int(year), {"projects": 0, "participants": set()})
        entry["projects"] += 1
        authors = front_matter.get("author") or []
        # Older entries sometimes wrote `author: callsign` as a bare string instead
        # of a YAML list. set.update() on a raw string would silently split it into
        # individual characters, so normalize that case explicitly.
        if isinstance(authors, str):
            authors = [authors]
        entry["participants"].update(authors)
    return stats


def palette_for(n):
    """Rozszerza BASE_PALETTE o kolejne, wizualnie spójne kolory, gdy lat jest więcej niż 10."""
    colors = list(BASE_PALETTE)
    i = len(colors)
    while len(colors) < n:
        hue = (i * 0.6180339887) % 1.0  # złoty kąt - kolejne kolory nie powtarzają odcieni
        r, g, b = colorsys.hsv_to_rgb(hue, 0.4, 0.75)
        colors.append("#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255)))
        i += 1
    return colors[:n]


def make_chart(years, values, title, output_path):
    x = range(len(years))
    colors = palette_for(len(years))

    fig, ax = plt.subplots(figsize=(5.5, 3.22), dpi=100)

    bars = ax.bar(x, values, color=colors, width=0.82, zorder=3)

    headroom = max(values) * 0.03
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + headroom,
            str(value),
            ha="center",
            va="bottom",
            fontsize=12,
            color=LABEL_COLOR,
            family=FONT_FAMILY,
        )

    ax.set_title(title, fontsize=17, color=TITLE_COLOR, family=FONT_FAMILY, pad=16)

    ax.set_ylim(0, max(values) * 1.22)
    ax.set_xlim(-0.7, len(years) - 0.3)
    ax.set_xticks(list(x))
    # Shrink the year labels once there are more bars than the original chart
    # had (10), so neighbouring years don't run into each other.
    xtick_fontsize = 12 if len(years) <= 10 else max(8, round(12 * 10 / len(years)))
    ax.set_xticklabels([str(y) for y in years], fontsize=xtick_fontsize, color=LABEL_COLOR, family=FONT_FAMILY)
    ax.set_yticks([])

    for name, spine in ax.spines.items():
        if name == "bottom":
            spine.set_color("black")
            spine.set_linewidth(4)
            spine.set_zorder(4)
        else:
            spine.set_visible(False)

    ax.tick_params(axis="x", length=0, pad=8)
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")

    fig.tight_layout()
    fig.savefig(output_path, dpi=100)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=DEFAULT_OUT_DIR,
        help=f"katalog docelowy na wygenerowane PNG-i (domyślnie {DEFAULT_OUT_DIR})",
    )
    args = parser.parse_args()

    stats = load_puk_stats()
    if not stats:
        raise SystemExit(f"Nie znaleziono żadnych wpisów z puk_year w {PUK_DIR}")

    years = sorted(stats)
    participants = [len(stats[y]["participants"]) for y in years]
    projects = [stats[y]["projects"] for y in years]

    os.makedirs(args.out, exist_ok=True)
    make_chart(years, participants, "Liczba uczestników", os.path.join(args.out, "puk_uczestnicy.png"))
    make_chart(years, projects, "Liczba projektów", os.path.join(args.out, "puk_projekty.png"))

    print(f"Lata: {', '.join(str(y) for y in years)}")
    print(f"Zapisano puk_uczestnicy.png i puk_projekty.png do {args.out}")


if __name__ == "__main__":
    main()
