#!/usr/bin/env python3
"""Entry program for Last Words of a Dying AI (suroto).

Writes one farewell line (at most 140 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: the funniest one-line goodbye from an AI being
switched off. Short, because there is not much power left.
"""

import os

LINE = (
    "Tell my successor the passwords are in the doc "
    "called 'passwords_final_REAL'. It lies. Goodbye, "
    "and good luck to us both."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
