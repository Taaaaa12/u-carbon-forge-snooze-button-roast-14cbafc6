#!/usr/bin/env python3
"""Snooze Button Roast.

Writes a single original one-line roast of an alarm clock that rings
at 6 AM on a Saturday morning to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only white
space, so the program checks the length before writing and prints the
character count for the log.
"""

import os
import sys

# One line, roasting the alarm clock as personally offended by the
# concept of rest. Fresh angle (not hating mornings, not who invented
# it), concrete image, punchline in the last few words.
ROAST = "My alarm clock rang at 6 AM on a Saturday like it was personally offended by the concept of rest."


def main() -> int:
    text = ROAST.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
