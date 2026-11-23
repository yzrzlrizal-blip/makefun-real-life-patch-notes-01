#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in real life /
human biology -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space. The program validates the line against that gate
before writing, and reads the file back to confirm what was written.
"""

import os
import sys

ENTRY = (
    "v3.1.4: fixed a bug where the brain remembered every lyric "
    "from 2009 but not why you walked into the kitchen."
)

MAX_CHARS = 160


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    # The entry is a fixed string: every run writes the same bytes,
    # so the two grading runs are deterministic by construction.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
