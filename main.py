#!/usr/bin/env python3
"""One-Liner Marathon — writes one one-line comedy joke to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version, revised):
#   "I told my therapist my phone listens to me; she said that's the
#    most stable relationship I've ever had."
# Why it was revised: "that's the" is slack — the punchline lands
# harder when the sentence is as tight as the joke. Cutting it to
# "it's the" drops two words and puts the turn ("most stable
# relationship") one beat sooner, with no meaning lost.
#
# REVISION (final): the scene is specific and modern — therapy, a phone
# that listens — and the turn flips the complaint into a compliment:
# the surveillance device is your most stable relationship. Deadpan,
# retellable, needs no explanation, and the punchline is the last
# clause, so the joke lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "I told my therapist my phone listens to me; she said it's the "
    "most stable relationship I've ever had."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 280 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert 1 <= len(written) <= 280 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
