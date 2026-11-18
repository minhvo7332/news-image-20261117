#!/usr/bin/env python3
"""news-image-20261117 entry: copy the finished front page to /output.

The image (entry.png, 1024x1024, drawn by draw_image.py from reporting
on Tuesday 17 November 2026) is baked into this repository. This program
only copies its bytes, so both grader runs write byte-identical output.
Standard library only; no network.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly instead of shipping a truncated copy: the gate reads
    # exactly the bytes in the file, so a short write must never pass.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
