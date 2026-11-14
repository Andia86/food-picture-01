#!/usr/bin/env python3
"""make.fun bounty food-picture-01: writes the entry image to /output/entry.png.
The image (entry.png, next to this file) is copied byte-for-byte, so repeated
runs always produce identical bytes. No network access."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")

if __name__ == "__main__":
    main()
