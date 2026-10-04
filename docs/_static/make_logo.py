# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py"]
# ///
"""Draw the zeroth logo: ``[0]``.

Index zero between square brackets: the first element, for any iterable, in
GalacticDynamics' navy and purple. The shapes are vector, so the logo is written
as an SVG, sharp at any size; for a bitmap, name a .png and give its size::

    uv run docs/_static/make_logo.py                     # favicon.svg
    uv run docs/_static/make_logo.py --size 2048 big.png
"""

import argparse
from pathlib import Path

NAVY, PURPLE = "#030a23", "#7738eb"  # GalacticDynamics' colours

# In a 64-unit square: the brackets' left and right x, their top and bottom, and
# how far their ends turn in; the zero's centre and half-width and half-height.
BRACKETS = (10, 54, 10, 54, 8)
ZERO = (32, 32, 10, 16)

SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512">
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="{brackets}" stroke="{navy}" stroke-width="4.5"/>
    <ellipse cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}"
      stroke="{purple}" stroke-width="5"/>
  </g>
</svg>
"""


def brackets() -> str:
    """Return the square brackets as an SVG path."""
    left, right, top, bottom, end = BRACKETS
    return (
        f"M{left + end:g} {top:g}H{left:g}V{bottom:g}H{left + end:g}"
        f"M{right - end:g} {top:g}H{right:g}V{bottom:g}H{right - end:g}"
    )


def svg() -> str:
    """Return the logo as SVG text."""
    cx, cy, rx, ry = ZERO
    return SVG.format(
        brackets=brackets(),
        navy=NAVY,
        purple=PURPLE,
        cx=cx,
        cy=cy,
        rx=rx,
        ry=ry,
    )


def main() -> None:
    """Parse the command line and save the logo."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "out",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("favicon.svg"),
        help="output file, SVG or PNG by its extension (default: favicon.svg)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="pixels per side, for a PNG",
    )
    args = parser.parse_args()

    if args.out.suffix == ".svg":
        args.out.write_text(svg())
    else:
        import resvg_py  # noqa: PLC0415  # only a PNG needs a renderer

        png = resvg_py.svg_to_bytes(svg_string=svg(), width=args.size)
        args.out.write_bytes(bytes(png))


if __name__ == "__main__":
    main()
