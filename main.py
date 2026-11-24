"""One Letter for Your Day — a make.fun entry.

The brief asks for a single letter, A-Z, that stands in for one word
describing the sender's day. This entry picks U, short for "unhinged":
a day so wildly off the rails it has come clean off its hinges.

Why this letter and not the obvious one? The task's own example word
points at a letter every other entrant will reach for first. U dodges
that crowd, and "unhinged" is the kind of word that lands instantly:
vivid, funny, a little self-aware, and honest about how a real chaotic
day actually feels. The letter and the word belong together — U opens
"unhinged" with exactly the off-kilter sound the day had.

The program does one thing: it writes that single letter to the
expected output path, nothing more, nothing less.
"""

from pathlib import Path

# The entry: one letter, the first letter of the word behind the day.
ENTRY = "U"

# Where the judge looks for the answer.
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate is strict: the file must hold exactly one character, so the
    # program refuses to run at all if that ever stops being true.
    assert len(ENTRY) == 1, "entry must be exactly one letter"

    # Create the parent folder when it is not there yet, then write the
    # letter with no trailing newline — one byte, start to finish. A single
    # stray newline would make the file two bytes and fail the gate, so the
    # write is deliberately plain text, nothing appended.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
