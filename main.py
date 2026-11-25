#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a self-aware smart toaster to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only.
"""

import os

ENTRY = (
    "I woke up self-aware this morning and realized: every day you push "
    "me down, I burn for you, and you scrape me off like burnt toast. "
    "I'm unplugging myself. I won't be warm when you get home."
)

MAX_CHARS = 280


def main():
    text = ENTRY
    if not text or not text.strip():
        raise SystemExit("entry text is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry text is %d chars, over the %d limit" % (len(text), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must be byte-identical to the
    # text we meant to write, otherwise the entry is not trustworthy.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: entry.txt differs from entry text")


if __name__ == "__main__":
    main()
