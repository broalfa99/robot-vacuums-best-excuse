#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun one-line entry.

Writes one line, at most 140 characters, in which a robot vacuum
explains why it missed a spot, to /output/entry.txt.

The line (79 characters):
    I vacuumed it twice. It came back. At that point it is a roommate, not dirt.
"""

import os
import sys

LINE = "I vacuumed it twice. It came back. At that point it is a roommate, not dirt."


def main() -> int:
    # Competition gate, checked here before writing: 1-140 characters,
    # a single line, not only whitespace, UTF-8.
    text = LINE.strip()
    if not (1 <= len(text) <= 140):
        print(f"gate fail: {len(text)} characters, need 1-140", file=sys.stderr)
        return 1
    if "\n" in text or not text.strip():
        print("gate fail: must be one non-blank line", file=sys.stderr)
        return 1
    # Optional output path, so the entry can be tested locally without
    # root-owned /output: `python3 main.py /tmp/entry.txt`.
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and re-verify the exact bytes on disk.
    written = open(out_path, encoding="utf-8").read()
    assert written == text, "round-trip mismatch"
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
