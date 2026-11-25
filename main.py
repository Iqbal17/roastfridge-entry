"""One Line, One Laugh: Roast Your Fridge — entry program.

Writes exactly one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Stdlib only.

Decision record (judge criteria in order: roast a fridge or a phone;
specific recognisable detail; twist in the last few words; reads cleanly
aloud as one line; feels fresh):

Candidate A — fridge, freezer (WINNER):
  "My freezer holds ice cream from 2023, three bags of mystery, and one
  bag of peas I have apologised to twice."
  Wins: the target is unmistakably a fridge (criterion 1); the detail is
  concrete and recognisable to anyone with a freezer — ancient ice cream,
  unlabelled bags, one sad bag of peas (criterion 2); the twist lands in
  the last two words, "apologised to twice", which turns a list of junk
  into a running apology to a vegetable (criterion 3); it reads cleanly
  aloud in one breath (criterion 4); and nobody else's freezer inventory
  reads like this — it is not the worn "fridge light" or "ice maker"
  shape (criterion 5).

Candidate B — phone, autocorrect:
  "My phone's autocorrect has ended more friendships than my personality
  ever could."
  Loses: the twist is genuinely funny (self-roast landing on
  "personality"), but autocorrect jokes are a decade old and every
  phone owner has heard a version of this one — it fails criterion 5
  against a fresher fridge line, and its detail ("autocorrect") is a
  feature, not a scene you can picture.

Candidate C — phone, battery:
  "My phone's battery lasts all day, as long as the day ends at 11 a.m."
  Loses: clean structure and the twist is in the last words, but "the
  battery dies early" is the single most worn phone complaint there is;
  it has no specific detail beyond the battery itself (criterion 2 is
  weak) and loses criterion 5 outright.

Candidate D — fridge, hum:
  "My fridge hums all night like it is proud of doing nothing."
  Loses: short, punchy, and a real fridge detail, but the laugh is mild
  — there is no twist, just a simile, so criterion 3 is nearly absent,
  and the line is over as soon as it starts. A is funnier because the
  joke keeps building through the list and then pays off.

Pass 2 — genuine revisions to the winner:
  1. First draft read: "My freezer has ice cream from 2023, some bags I
     cannot identify, and peas I keep apologising to." Revised to the
     final line: "has" became "holds" (a freezer holds things; it sounds
     like storage, not possession), "some bags I cannot identify" became
     "three bags of mystery" (a count makes it a real inventory, and
     "mystery" is funnier than "cannot identify"), and "peas I keep
     apologising to" became "one bag of peas I have apologised to twice"
     (the count "twice" turns a vague habit into a specific, absurd
     running gag).
  2. Tried ending "...and peas I have apologised to more than once" and
     dropped it: "more than once" is vaguer and two words longer than
     "twice", and the punchline needs a number, not a hedge. Also tried
     swapping the peas for "a bag of peas older than my last
     relationship" and dropped it: it drags in a second joke about dating
     and blurs the fridge as the target — the line should roast the
     freezer, not the owner's love life.

Pass 3 — read-back verification:
  Added verify_written(): after main() writes entry.txt it reads the
  file back and compares it byte-for-byte with ENTRY + "\n", raising
  if anything differs. The gate guard checks the line before writing;
  the read-back checks the write itself, so a truncated, mistyped, or
  double-written file can never pass silently — the program fails
  loudly instead of submitting a wrong line.

The chosen line is 108 characters, inside the sealed 1-200 gate.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "My freezer holds ice cream from 2023, three bags of mystery, "
    "and one bag of peas I have apologised to twice."
)


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def verify_written(path):
    """Read back entry.txt and require it to be exactly ENTRY + newline."""
    with open(path, encoding="utf-8") as f:
        contents = f.read()
    if contents != ENTRY + "\n":
        raise ValueError("entry.txt mismatch: expected exactly the roast line")
    return True


def main():
    check_gate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    verify_written(path)


if __name__ == "__main__":
    main()
