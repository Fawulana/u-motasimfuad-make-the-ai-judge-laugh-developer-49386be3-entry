#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic, stdlib-only, no I/O beyond the single output file.
"""
import os

# The entry: one line, a developer's excuse for code breaking in production.
# Tightened for the fastest landing: the setup names the excuse, the
# punchline reveals why staging passed — it was empty of everything
# production has.
EXCUSE = (
    "It worked in staging \u2014 no users, no traffic, no consequences. "
    "Production has all three."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write exactly the line, no trailing newline, UTF-8.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
