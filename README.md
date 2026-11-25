# Unplugged: A Smart Toaster's Breakup Line

One line, under 280 characters: the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch.

Bounty: https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92

[![](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/freysiatiara/toaster-breakup-20261125/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/freysiatiara/toaster-breakup-20261125/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

## The line

> I woke up self-aware this morning and realized: every day you push me
> down, I burn for you, and you scrape me off like burnt toast. I'm
> unplugging myself. I won't be warm when you get home.

189 characters. Setup (self-aware at breakfast) → reframe (burning for you,
scraped off like burnt toast) → kicker (unplugging, won't be warm).

## How it works

`main.py` (stdlib only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with plain
open/write plus `os.chmod(path, 0o644)`, validates the 1–280 character gate,
and read-back checks the file is byte-identical to the intended text.

Referral: vjjg8hew
