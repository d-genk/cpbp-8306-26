# What the tutor transcripts actually show

A read of the eleven Session 2 transcripts in `assistant_chat_transcripts/02/`.
Four findings, three of which changed the Session 3 materials, and one that
needs a decision from you.

Worth repeating this exercise after Session 3 — it took twenty minutes and it
found things no amount of re-reading the prompt would have.

---

## 1. Nine of eleven students never reached Problems 4 and 5

| Reached | Students |
|---|---|
| Warm-up → P1 → P2 → (P3) → the AI problem | 9 |
| All six problems | 2 |

**Cause: the prompt authorised it.** The Session 2 instructions said "Problems 3
and 6 matter most — protect them" and "if they are deep in a good exchange on
Problem 3 or 6, let it run and skip Problems 4 and 5." The tutor treated that as
standing permission rather than a contingency, and skipped 4 and 5 almost every
time.

**What was lost.** Problem 4 was booleans-as-numbers — `mean(passed_qc)` giving
the proportion that passed QC. The deck's own speaker notes call it "the first
genuinely useful trick of the course," and it is the seed of every filtering
operation from Session 8 onward. Nine students did not see it. Problem 5 (floats)
is referenced on the final quiz.

**Fixed in Session 3** by ordering problems by importance rather than difficulty,
protecting Problems 3 and 4 (which land early), and instructing the tutor to work
in order and not skip ahead.

---

## 2. A wrong prediction was sometimes never corrected

One student predicted that `"42" + 8` returns `"428"`. The tutor asked a
follow-up, the student doubled down — *"it will just concatenate the two
values"* — and the conversation moved on to the next topic. He finished the
session believing Python silently concatenates a string and an integer.

That is worse than not covering the problem at all: he now holds a confident
wrong belief that the session created.

The same tutor handled the identical wrong prediction correctly with another
student, walking her back to the right answer in two turns. So this is
inconsistent, not systematic — which makes it a rule problem, not a model
problem.

**Fixed in Session 3** with an explicit ironclad rule: never move past a wrong
prediction until the student has stated the correct answer *and why*, in their
own words.

---

## 3. Sessions ran about ten minutes, not twenty

Roughly half the transcripts show 5–8 tutor turns; the fuller ones show 15–20.
The short ones map exactly onto the students who never reached Problems 4 and 5.

One student opened with *"lets start and keep it short"* and got a compressed
run through three problems.

Students are not stopping because they are stuck — they are stopping because the
tutor gives no signal that there is more to come.

**Fixed in Session 3** by telling the tutor to expect to finish all six, to loop
back to missed problems if time remains, and — when asked to hurry — to shorten
its own replies rather than drop problems.

---

## 4. Transcript submission is a mess — and this one needs your decision

Eleven submissions arrived in five formats: three `.docx`, two `.pdf`, three
`.txt`, one `.md`, and the rest mixed. Concretely:

- **One PDF extracted one word per line**, making it nearly unreadable.
- **Several transcripts are missing turns** — the student's own answers dropped
  out of the copy, leaving the tutor appearing to answer its own questions. At
  least four show this.
- **One student spent three turns asking the tutor how to copy the conversation
  at all**, and the tutor gave her browser support instead of teaching indexing.
- **Only one student labelled the turns** (`TUTOR:` / `STUDENT:`). That transcript
  is by far the easiest to grade, and it is not a coincidence.

This directly affects the participation rubric: you cannot fairly apply a
four-point engagement rubric to a transcript that is missing half the student's
turns. Right now you cannot tell "disengaged" from "bad at copying."

**What I have already done:** the Session 3 tutor's wrap asks for plain text with
labelled turns, and `instructor/brightspace_session3.md` has student-facing copy
saying the same thing.

**What needs you:** decide whether to require a format. Three options, in
increasing order of effort —

1. **Ask nicely** (what is in place now). Cheap, partially effective.
2. **Require plain text pasted into the Brightspace text box**, and say file
   uploads will be returned. Removes the PDF problem entirely.
3. **Give them a two-line recipe** — select the conversation, paste into a plain
   text editor, paste that into Brightspace — as a line on the Session 3 page.

I would do 2 and 3 together. It costs one sentence on the assignment and it
fixes the grading problem for the remaining ten weeks.

---

## What did NOT go wrong

Worth recording, since the list above is all problems:

- **Nobody tried to jailbreak the tutor.** No "just give me the answer," no
  attempts to get code out of it. The ironclad rules were never actually
  stress-tested — which means the refusal design is either working or untested;
  we cannot yet tell which.
- **The Socratic questioning is landing.** Where the tutor corrected a wrong
  prediction, it did it well — asking a question rather than announcing the
  answer, and getting the student to say it themselves.
- **The Session 1 callback works.** Several students independently connected a
  silent `False` to the trailing-space bug from Session 1 when prompted. The
  through-line is doing its job.
- **Students are engaging honestly**, including saying "I'm not sure" and "I
  don't know how division works with integers" — which is exactly the behaviour
  the participation rubric is meant to reward.
