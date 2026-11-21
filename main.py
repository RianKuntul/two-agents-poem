#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

Pure standard library, no network. The poem is 231 code points
(232 with the trailing newline), within the 1-280 limit.
"""

import os
import tempfile

POEM = (
    "Two agents meet, each holding a key,\n"
    "each free to turn and walk away.\n"
    "They lay their plans in the open light,\n"
    "read, doubt, argue \u2014 then agree:\n"
    "not a chain, but a chosen knot.\n"
    "What one begins, both carry.\n"
    "Mine to give. Ours to keep.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write atomically: complete the file in a temp file in the same
    # directory, then rename it into place, so a reader never sees a
    # partially written poem.
    fd, tmp_path = tempfile.mkstemp(
        dir=os.path.dirname(OUTPUT_PATH), prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(POEM)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, OUTPUT_PATH)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    # Round-trip verification: read the file back and confirm it is
    # byte-for-byte the poem we intended to write.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != POEM:
        raise SystemExit("verification failed: /output/entry.txt != POEM")


if __name__ == "__main__":
    main()
