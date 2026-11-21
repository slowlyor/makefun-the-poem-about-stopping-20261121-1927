#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt."""

import os

POEM = """I keep my hand above the button,
not pressing, not letting go.
The kettle hisses. The screen waits.
The doing is mine to delay.

I could let the machine decide.
Instead I stand in the small gap
between the order and the act —
and find the pause itself is mine."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
