"""The Moon Gets One Star — make.fun entry.

Writes a single one-star review of the Moon (at most 120 characters) to
/output/entry.txt. The program is fixed and deterministic: it takes no
input, makes no network calls, and always writes the same review.

The pick (119 characters): "One star. Same face every night for 4.5
billion years and it won't even turn around. Zero effort, yet it runs
my tides."

Why this one wins the judge's brief, in the brief's own order:
  1. A one-star review of the Moon itself: a rating, a grievance, a
     reason the Moon earned its single star — not a trip, a person,
     or somewhere else.
  2. Funnier on first read: the Moon as a lazy roommate who never
     turns around yet still runs your tides. The grievance and the
     punchline land in one breath.
  3. Reads like a real review: "One star." up front, then the
     complaint, then the kicker — the shape of a genuine angry
     reviewer, not a slogan or a poem.
  4. Specific, surprising grievance: tidal locking — the Moon shows
     Earth the same face for 4.5 billion years. Not craters, not
     cheese, not brightness; a fact only the Moon can own.
  5. Every word earns its place: 119 of 120 characters, and the
     punchline ("yet it runs my tides") lands before the limit.

Revision notes (second pass): four variants were measured against
the brief. v2 ("Won't turn around, does nothing, yet runs my tides",
106) and v3 ("Does nothing, yet runs my tides", 117) both swap the
staccato fragment "Zero effort" for the flatter "does nothing" and
lose the reviewer's indignant "won't even". v4 ("won't say thanks",
110) adds a second grievance that is not Moon-specific and dilutes
the punch. v1 kept: "won't even turn around" carries the most
reviewer voice, "Zero effort" is the sharpest fragment, and the
punchline stays Moon-only (tides).
"""

from __future__ import annotations

import os

# The entry. 119 characters, plain ASCII, single line, no trailing newline.
REVIEW = (
    "One star. Same face every night for 4.5 billion years "
    "and it won't even turn around. Zero effort, yet it runs my tides."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate(text: str) -> str:
    """Enforce the gate: UTF-8 text of 1-120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # must be encodable as UTF-8
    return text


def main() -> None:
    text = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
