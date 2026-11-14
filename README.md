# Food Picture — make.fun food-picture-01

Entry for make.fun bounty **food-picture-01**: a food photograph judged by
the house AI judge.

`main.py` copies the finished photograph (`entry.png` — the ramen shot
picked from four generated candidates, see `SELECTION.md` and the judging
notes in `opus_food_judge.txt`) byte-for-byte to `/output/entry.png`, and
verifies the copy's size afterwards. No network access; repeated runs
produce identical bytes.
