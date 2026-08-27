"""Check every tutor's system prompt against ChatGPT's 8,000-character cap.

ChatGPT silently truncates a custom GPT's Instructions field past 8,000
characters, which is invisible until a student reports the tutor ignoring
rules that live near the end of the prompt. Run this after editing any file
in assistants_per_lecture/ or assistants_by_unit/.

    python instructor/check_prompt_length.py

Exits non-zero if anything is over, so it can go in a pre-commit hook.
"""

import glob
import io
import sys

CAP = 8000
WARN = 7500          # close enough that the next edit could push it over
FENCE = "`" * 3


def prompt_of(path):
    """Return the fenced system-prompt block, or None if the file has no marked block."""
    s = io.open(path, encoding="utf-8").read()
    try:
        i = s.index("## System prompt")
    except ValueError:
        return None
    b = s.index(FENCE, i) + len(FENCE)
    e = s.index(FENCE, b)
    return s[b:e].strip("\n")


def main():
    paths = sorted(glob.glob("assistants_per_lecture/*.md") + glob.glob("assistants_by_unit/*.md"))
    if not paths:
        print("No tutor files found - run this from the repo root.")
        return 1

    over, warn = [], []
    for p in paths:
        block = prompt_of(p)
        name = p.replace("\\", "/").split("/")[-1]
        if block is None:
            print("%-46s   no fenced prompt block" % name)
            continue
        n = len(block)
        if n > CAP:
            flag, bucket = "OVER CAP", over
        elif n >= WARN:
            flag, bucket = "close", warn
        else:
            flag, bucket = "ok", None
        if bucket is not None:
            bucket.append((name, n))
        print("%-46s %6d  %-9s %s" % (name, n, flag, "(-%d)" % (n - CAP) if n > CAP else ""))

    print("\ncap %d characters" % CAP)
    if over:
        print("\n%d file(s) OVER the cap - ChatGPT will truncate these silently:" % len(over))
        for name, n in over:
            print("   %s  needs %d characters cut" % (name, n - CAP))
        return 1
    if warn:
        print("\n%d file(s) within %d of the cap - trim before adding to them." % (len(warn), CAP - WARN))
    print("\nAll prompts fit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
