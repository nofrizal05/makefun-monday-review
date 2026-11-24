#!/usr/bin/env python3
"""Monday: One Star, Would Not Recommend.

Writes a one-line review of Monday, as if Monday were a product,
to /output/entry.txt.

Standard library only. Deterministic: every run writes the same line.
"""

import os

REVIEW = (
    "Monday: one star. It arrived before the coffee did, stole my weekend, "
    "and charged me a full week for the dread."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The review must stay exactly one line: no newline may sneak in.
    assert "\n" not in REVIEW and "\r" not in REVIEW
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(REVIEW + "\n")
    print(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
