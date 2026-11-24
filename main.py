#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes exactly one line to /output/entry.txt: a one-sentence pitch for a
bizarre startup idea that sounds absurd until you see the business logic.
No network, no randomness, no environment secrets. Deterministic, exit 0.
"""

import os
import sys

# The pitch: professional mourners are a real profession (hired criers at
# funerals exist in China, the Middle East, parts of Africa and Victorian
# England). Bizarre at first glance, plainly a paid service on second look.
LINE = (
    "Professional mourners for hire: trained criers weep at strangers' "
    "funerals, because grieving families pay $300 a head to make a small "
    "service look deeply loved."
)


def main() -> int:
    """Write the single pitch line to the grader's output directory."""
    # Guard the gate: the entry must be 1-200 characters of real text.
    if not (1 <= len(LINE) <= 200):
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
