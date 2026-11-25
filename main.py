"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist's one-star review of planet Earth
that still praises the food, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, no network, no input files.
"""

import os

ENTRY = (
    "One star - your species invented war, traffic, and Mondays, "
    "yet somehow also invented tacos, so I will be back, grudgingly, "
    "with a bigger ship and an empty stomach."
)

MAX_CHARS = 200
MAX_BYTES = 200  # gate counts characters, but keep bytes in step too


def validate(text: str) -> None:
    """Check the entry against the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    n_bytes = len(text.encode("utf-8"))
    if n_bytes > MAX_BYTES:
        raise ValueError(
            f"entry is {n_bytes} UTF-8 bytes, over the {MAX_BYTES} limit"
        )
    if not text.isascii():
        raise ValueError("entry must be ASCII")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
