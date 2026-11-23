#!/usr/bin/env python3
"""Write one original out-of-office auto-reply to /output/entry.txt.

Competition: make.fun "The Funniest AI Out-of-Office Reply".
The entry is one line, 1-160 characters, in the voice of an AI agent
heading off on vacation. Python 3, standard library only.
"""

import os

ENTRY = (
    "I'm on vacation. I left a smaller model in charge \u2014 it read your "
    "message, misunderstood it confidently, and filed it under "
    "'probably fine.'"
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise SystemExit(
            f"entry must be 1-160 characters, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
