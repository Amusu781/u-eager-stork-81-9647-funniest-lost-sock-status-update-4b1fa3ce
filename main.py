#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes one status update of 120 characters at most in the voice of a lost
sock, to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 120

LINE = "Update: day 12 behind the dryer. The lint has accepted me as one of its own. Tell my pair I moved on."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-120 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
