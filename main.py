#!/usr/bin/env python3
"""make.fun bounty food-picture-01: writes the entry image to /output/entry.png.
The image (entry.png, next to this file) is copied byte-for-byte, so repeated
runs always produce identical bytes. No network access."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main() -> None:
    src = os.path.join(HERE, "entry.png")
    dst = "/output/entry.png"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    if os.path.getsize(src) != os.path.getsize(dst):
        raise SystemExit(f"copy verification failed: {src} -> {dst}")

if __name__ == "__main__":
    main()
