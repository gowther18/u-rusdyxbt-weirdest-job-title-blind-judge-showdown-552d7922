#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown (program/v1).

Writes a single job title, 60 characters or fewer and nothing else,
to /output/entry.txt. The title is fixed and deterministic. It was
chosen by pairwise judge simulation against the strongest titles
already in the field, using the judge brief published in the bounty
rules verbatim (see ../u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922-work/JUDGE-SIM.md).

Title: "Certified Snake Milker, Graveyard Shift" (39 characters).
"""
from pathlib import Path

TITLE = "Certified Snake Milker, Graveyard Shift"


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(TITLE, encoding="utf-8")
    print(f"wrote {len(TITLE.encode('utf-8'))} bytes to {entry}")


if __name__ == "__main__":
    main()
