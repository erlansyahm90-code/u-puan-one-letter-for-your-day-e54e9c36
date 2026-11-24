[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/erlansyahm90-code/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/erlansyahm90-code/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

A make.fun entry that answers the whole prompt with a single letter.

## The entry

**U** — for **"unhinged"**.

One letter, one word behind it: a day so chaotic it came clean off its hinges. The brief's own example word points at a letter everyone else will reach for first, so this entry sidesteps the crowd and picks the sharper, fresher one. "Unhinged" is vivid, funny, and honest about what a genuinely wild day feels like — and U is the only letter that opens it.

## How it works

Running `main.py` writes exactly one character — the letter `U`, with no trailing newline — to `/output/entry.txt`. Before writing, the program asserts the entry is exactly one character long, so a broken entry can never slip through silently. That is the whole program: one letter, one byte, one file.

## Run it

```bash
python3 main.py
```

Then check the result:

```bash
wc -c /output/entry.txt   # 1
cat /output/entry.txt     # U
```
