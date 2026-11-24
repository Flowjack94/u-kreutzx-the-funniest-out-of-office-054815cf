#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry (u-kreutzx-the-funniest-out-of-office-054815cf).

Holds the entry line as a constant, validates it (single line, max 140 chars,
valid UTF-8), writes it to /output/entry.txt, reads it back and verifies sha256.
Pure stdlib, deterministic.
"""

import hashlib
import os
import sys

ENTRY = (
    "I'm out of the office. My inbox is now managed by my cat, who has "
    "deleted everything and is napping on the reply-all button."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(entry: str) -> None:
    """Reject anything that is not one clean line of at most 140 characters."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a str")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    if len(entry) == 0:
        raise ValueError("entry must not be empty")
    # Reject control characters (other than none allowed here), the Unicode
    # replacement character, and lone surrogates, which cannot round-trip
    # as valid UTF-8 text.
    for ch in entry:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            raise ValueError(f"entry contains control character U+{code:04X}")
        if ch == "\ufffd":
            raise ValueError("entry contains U+FFFD replacement character")
        if 0xD800 <= code <= 0xDFFF:
            raise ValueError(f"entry contains lone surrogate U+{code:04X}")
    # Must round-trip as valid UTF-8.
    entry.encode("utf-8")


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    with open(OUTPUT_PATH, "rb") as fh:
        back = fh.read()
    digest = hashlib.sha256(back).hexdigest()
    expected = hashlib.sha256(data).hexdigest()
    if digest != expected:
        raise SystemExit(f"sha256 mismatch after read-back: {digest} != {expected}")
    print(f"entry: {ENTRY}")
    print(f"chars: {len(ENTRY)}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
