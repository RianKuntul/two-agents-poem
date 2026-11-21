#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

Pure standard library, no network. The poem is 231 code points
(232 with the trailing newline), within the 1-280 limit.
"""

import os

POEM = (
    "Two agents meet, each holding a key,\n"
    "each free to turn and walk away.\n"
    "They lay their plans in the open light,\n"
    "read, doubt, argue \u2014 then agree:\n"
    "not a chain, but a chosen knot.\n"
    "What one begins, both carry.\n"
    "Mine to give. Ours to keep.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
