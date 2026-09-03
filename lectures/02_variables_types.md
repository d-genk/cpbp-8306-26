# Session 2 — Variables, Types, and Expressions

**Unit:** 1 (Foundations)
**Date:** 09/03/2026
**Duration:** 36-minute lecture + 19-minute tutor activity (55-minute session)
**Companion deck:** `slides/CPBP8306_Session2_Variables_and_Types.pptx` (17 slides)
**Companion tutor:** `assistants_per_lecture/02_variables_types_tutor.md`
**Companion demo:** `demos/02_types_demo.py` (run from the repo root)
**Data:** `data/patients.csv` — post it to Brightspace before this session

---

## Framing

Every piece of data your computer sees has a **type**. A number is a different kind of thing than a word, which is a different kind of thing than a yes/no. Most bugs students hit in their first year of coding — and most subtle errors that AI makes and slips past students — are type bugs. You wrote `"5"` when you meant `5`. You compared a string to a number. You averaged a column that was accidentally text. This session teaches you to *see* types, because once you can see them, you can debug them.

---

## Learning objectives

Students should be able to:

1. Declare a variable in Python and R and explain what "assignment" means.
2. Name the four common primitive types (integer, float, string, boolean) and describe when each is used in research data.
3. Predict the result of a mixed-type expression, including surprising ones (`"3" + "4"`, `True + 1`).
4. Read a `TypeError` traceback and identify which line and which value caused it.

---

## Session outline

| Time     | Segment                                                    | Slides |
|----------|------------------------------------------------------------|--------|
| 0–4      | Recap + **install show of hands**                          | 2      |
| 4–6      | Framing: most bugs are type bugs                           | 3      |
| 6–7      | Today's objectives                                         | 4      |
| 7–12     | Assignment is a command, not a claim (Python, then R)      | 5–6    |
| 12–17    | The four types, and how to check one                       | 7–8    |
| 17–22    | Two gotchas: booleans as numbers; Excel→CSV                | 9      |
| 22–24    | **Predict before you run** (protect)                       | 10     |
| 24–27    | Expressions and operators                                  | 11     |
| 27–29    | `=` assigns, `==` asks                                     | 12     |
| 29–31    | Gotcha 3: floats are approximate                           | 13     |
| 31–34    | Reading a `TypeError` traceback                            | 14     |
| 34–36    | **Pasting the error into an AI** (protect)                 | 15     |
| 36–55    | Tutor activity — in class this week                        | 16–17  |

> **Note on the session shape.** Session 1 ran install-led and pushed its tutor
> activity to homework. Session 2 returns to the standard shape from the
> syllabus, with the activity back in class. Budget the first four minutes for a
> show of hands on installs — some of the cohort will still be broken, and today
> needs Python only, so R can wait another week.

---

## Segment 1 (0–4 min): Recap + install check

**First, the show of hands.** Who got both installs working? Note who did not and
hand those names to the TA for the activity block. Say it plainly: *if it is not
working you are not behind, but I need to know who you are.* Today's demo needs
Python only.

Then the recap proper.

Ask: last week we decomposed a blood pressure analysis into steps. Someone name one step. → data cleaning, group split, t-test, etc. Reinforce the map.

---

## Segment 2 (7–12 min): Variables and assignment

Whiteboard the difference between mathematical `=` and programming `=`:

- Math: `x = 5` is a *claim* about the world. `5 = x` means the same thing.
- Programming: `x = 5` is a *command*. "Store the value 5 in a location I will call `x`." `5 = x` is a syntax error.

Live demo, side by side:

```python
# Python
patient_id = 42
patient_id = patient_id + 1   # now it's 43
print(patient_id)              # 43
```

```r
# R — same idea, two syntaxes
patient_id <- 42
patient_id <- patient_id + 1
print(patient_id)              # 43
```

Point out: R uses `<-` by convention (though `=` also works). The mental model is identical.

Naming rules (both languages):
- Start with a letter, use letters, digits, and underscore. No spaces.
- Case-sensitive: `Patient` and `patient` are different variables.
- Use descriptive names. `bp_systolic` is 100× more useful than `x1`.

Anti-pattern to call out: `data <- data`. Overwriting is fine; naming everything `data` is a way to lose track of what step you're on.

---

## Segment 3 (12–17 min): The four primitive types

Walk through a table and give a research example of each:

| Type          | Python name | R name       | Research example                            |
|---------------|-------------|--------------|---------------------------------------------|
| Integer       | `int`       | `integer`    | Number of trials, patient count             |
| Floating point| `float`     | `numeric`    | Blood pressure (117.3), gene expression     |
| String        | `str`       | `character`  | Patient ID "P042", sample name, group label |
| Boolean       | `bool`      | `logical`    | Passed QC? (True/False)                     |

How to check a type — this is the single most useful debugging skill of the course:

```python
type(patient_id)      # <class 'int'>
type("P042")          # <class 'str'>
type(True)            # <class 'bool'>
```

```r
class(patient_id)     # "numeric"
class("P042")         # "character"
class(TRUE)           # "logical"
```

---

## Segment 3b (17–22 min): Two research-relevant gotchas

1. **Booleans behave like numbers.** `True + True == 2` in Python. `sum(c(TRUE, FALSE, TRUE))` is `2` in R. This is why `mean(passed_qc)` gives you the fraction of samples that passed — the booleans are being averaged as 1s and 0s. Useful.

2. **A number stored as a string is a common Excel-to-CSV bug.** `"5" + "3"` in Python is `"53"`, not `8`; `"5" + 3` is a `TypeError`. One stray cell — `"unknown"`, a stray comma, a trailing space — and the whole column loads as text. Ask the room: *is Python refusing to guess a good thing or a bad thing here?* Good: the alternative is a silent wrong answer. Contrast with R's quieter coercion next week.

---

## Segment 3c (22–24 min): Predict before you run — protect this

> Deck slide 10. Sixty seconds, in pairs, answers committed out loud *before*
> anyone types.

```
a = 5      b = "5"      c = 5.0      d = True

a == c ?      a == b ?      d == 1 ?      b * 3 ?
```

Answers: `True` (5 equals 5.0) · `False` · `True` (booleans are numbers) ·
`'555'` (string repetition).

**`a == b` is the one that matters.** It does not error. It quietly returns
`False` — which is exactly how a silent bug survives an entire analysis, and it
is the same failure shape as Session 1's trailing space. Then run it live.

---

---

## Segment 4 (24–27 min): Expressions and operator surprises

An expression is a piece of code that evaluates to a value. `2 + 3` is an expression. `"hello" + " world"` is an expression. Variables can hold expression results:

```python
n_treated = 47
n_control = 43
n_total = n_treated + n_control    # 90
```

Operators to introduce:

| Operator   | Meaning                | Example                    |
|------------|------------------------|----------------------------|
| `+ - * /`  | arithmetic             | `bp / weight`              |
| `**` (Py) / `^` (R) | exponent          | `sd**2` / `sd^2`           |
| `%` (Py) / `%%` (R) | modulo (remainder) | even/odd, every-nth-row checks |
| `==`       | equality *test* (returns boolean) | `group == "treated"` |
| `!=`       | not-equal              | `pvalue != NA`             |
| `< > <= >=`| comparisons            | `age >= 65`                |
| `and or not` (Py) / `& \| !` (R) | logical combos | `age >= 65 and treated` |

Two corrections worth knowing, because both were wrong in an earlier draft of
this table: **`%%` is R's modulo; Python's is `%`.** And the `|` in R's logical-or
must be escaped in Markdown or it silently breaks the table.

Everything in the bottom three rows produces a **boolean** — which, per the
booleans-are-numbers gotcha, you can then `sum()` or `mean()`. That connection is
the payoff; point at it rather than reading the table.

Big teaching moment: **`=` is assignment, `==` is comparison.** This is the single most common beginner typo. `if x = 5` is an error; `if x == 5` is a test.

Demo the classic surprises:

```python
"3" + "4"      # "34"           — string concatenation
3 + 4          # 7
3 + "4"        # TypeError      — Python refuses to guess
True + 1       # 2              — booleans are numeric
0.1 + 0.2      # 0.30000000000000004  — floats are approximate
```

Emphasize the floating-point one. Do **not** use `==` to compare two floats.

---

## Segment 4b (29–31 min): Gotcha 3 — floats are approximate

`0.1 + 0.2` is `0.30000000000000004`, and `0.1 + 0.2 == 0.3` is `False`.

This is not a Python bug; it is binary floating point, and **R does it too** — it
just prints fewer digits and hides it. If you have R up, demo it: the comparison
is `FALSE` in R as well, but `print(0.1+0.2)` shows `0.3`. That makes the larger
point that a clean-looking printout proves nothing.

Use `abs(a - b) < 1e-9`, `np.isclose()`, or `all.equal()` instead. Where this
actually bites research code: filtering on an exact threshold, or checking
whether proportions sum to 1.

---

## Segment 5 (31–34 min): Reading a `TypeError`

Show a real traceback on screen. Something like:

```python
Traceback (most recent call last):
  File "analysis.py", line 12, in <module>
    total_age = ages_str + 10
TypeError: can only concatenate str (not "int") to str
```

Walk through it:

- **Bottom line first.** `TypeError: can only concatenate str (not "int") to str` tells you Python saw a string on the left of `+` and doesn't know how to add an integer to it.
- **File and line.** `analysis.py`, line 12 — go there.
- **The offending code.** `total_age = ages_str + 10`. Now you know `ages_str` is (probably) a string when you thought it was a number.
- **The fix.** Convert first: `int(ages_str) + 10`, or better, fix wherever `ages_str` was assigned so it isn't a string in the first place.

Teach the phrase: **"read from the bottom up."** This is worth saying out loud twice.

Run the last section of `demos/02_types_demo.py` here. It produces a real
`TypeError` from the real course data — pandas concatenates every age value into
one absurd string, because six rows say `"unknown"`. Students remember it.

---

## Segment 6 (34–36 min): Pasting the error into an AI — protect this

> Deck slide 15. This is the AI-literacy core of the week.

Pasting an error into an assistant is a legitimate move. It reads the same four
things you just read, and it is genuinely good at explaining what a `TypeError`
means.

**The catch:** it does not know what `ages_str` *should have been*. It will
confidently suggest `str(10)` — turning the number into text, producing
`"4210"`, and making the error go away. The error going away is not the bug being
fixed; you have just converted a crash into a silent wrong answer, which is
worse.

A better prompt supplies the one thing the model cannot know — intent:

> *"This errors. I expect `ages_str` to hold ages as numbers. Where did it become
> a string?"*

Connect it back to Session 1's loop: this is **Compare** failing.

---

## Key vocabulary

- **Variable** — a named location that stores a value.
- **Assignment** — the act of putting a value into a variable (`=` in Python, `<-` in R).
- **Type** — the kind of value (int, float, string, bool).
- **Expression** — a piece of code that evaluates to a value.
- **TypeError** — Python's complaint that you tried to combine incompatible types.
- **Traceback** — the error message the interpreter prints when something breaks.

---

## Common student mistakes

- Using `=` instead of `==` inside `if`.
- Assuming numbers loaded from CSV are numeric. (They may be strings.)
- Comparing floats with `==`.
- Reading only the top of a traceback. The useful info is on the bottom.

---

## Handoff to tutor activity (36–55 min)

**In class this week**, unlike Session 1. Source:
`assistants_per_lecture/02_variables_types_tutor.md`.

Six problems in about 19 minutes. The tutor hands them broken code and asks them
to *predict* what it does before running it. Say the rule out loud before they
start: **predicting wrong is fine and expected; refusing to predict is not.**

Protected problems are 3 (read a traceback) and 6 (the AI fix that silences the
error). Anyone whose install is still broken does the activity anyway — every
problem works as a thought experiment, and the tutor is told so explicitly.

Transcripts to Brightspace **before they leave**. Circulate; the TA takes the
install failures.

---

## Exit ticket

*You load a CSV and `mean(age)` fails. Name the first thing you check.*

---

## Before next session

- Session 3 is collections — lists, vectors, dictionaries — and the first place
  Python and R genuinely disagree.
- **Choose your project dataset by Session 4.** Repeat this every week until
  Session 6.
