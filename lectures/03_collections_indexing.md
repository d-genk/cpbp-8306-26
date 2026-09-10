# Session 3 — Collections: Lists, Vectors, and Dictionaries

**Unit:** 1 (Foundations)
**Date:** 09/10/2026
**Duration:** 36-minute lecture + 19-minute tutor activity (55-minute session)
**Companion deck:** `slides/CPBP8306_Session3_Collections_and_Indexing.pptx` (13 slides)
**Companion tutor:** `assistants_per_lecture/03_collections_indexing_tutor.md`
**Companion demos:** `demos/03_collections_demo.py` **and** `demos/03_collections_demo.R` — run side by side, in two visible consoles

---

## Framing

Real research data is never one value. It is a column of blood pressures, a set of patient IDs, a table of gene expressions. Before we can analyze data, we need containers to hold *many* values, and a way to reach in and grab the ones we want. This session covers the three most important containers you will use every day this semester: lists (Python) / vectors (R), and dictionaries — the container that maps names to values.

---

## Learning objectives

Students should be able to:

1. Create a list/vector and access an element by its position.
2. Explain the difference between Python's **0-indexed** and R's **1-indexed** conventions and why this matters when translating code.
3. Create a dictionary (Python) or named list (R) mapping keys to values.
4. Predict the result of common slicing operations (`nums[2:5]`, `nums[c(2,3,4)]`).
5. Recognize when to reach for each container: sequence of values → list/vector; key→value map → dict/named list.

---

## Session outline

| Time     | Segment                                                       | Slides |
|----------|---------------------------------------------------------------|--------|
| 0–4      | Recap: a container's type is not its contents' type           | 2      |
| 4–5      | Today's objectives                                            | 3      |
| 5–10     | Lists and vectors                                             | 4      |
| 10–14    | R vectors are homogeneous — and silent about it               | 5      |
| 14–19    | Indexing: 0 vs 1, and the `-1` divergence *(whiteboard)*      | 6      |
| 19–23    | Slicing: exclusive vs inclusive stop                          | 7      |
| 23–26    | **Predict — ninety seconds** *(protect)*                      | 8      |
| 26–30    | **Boolean masks — the idiom that runs the semester** *(protect)* | 9   |
| 30–33    | Dictionaries, named lists, and choosing a container           | 10     |
| 33–36    | **Where AI gets this wrong** *(protect)*                      | 11     |
| 36–55    | Tutor activity — in class                                     | 12–13  |

> **This is the side-by-side week.** Have a Python REPL and an R console open in
> two visible windows and alternate between them, saying which language you are
> in *out loud, every single time you type*. Students who lose track of which
> console they are watching leave more confused than they arrived. The whiteboard
> index ruler on slide 6 is not optional.

---

## Segment 1 (0–4 min): Recap

Ask the room: what's the type of `[1, 2, 3]`? Anyone who says "int" — good chance to point out that a container's type is *not* its contents. `type([1, 2, 3])` is `list`. The contents are ints. This distinction matters.

---

## Segment 2 (5–10 min): Lists and vectors

Motivation: a research dataset column is a sequence of values. We need a container.

Python **list**:

```python
bp_systolic = [117, 122, 141, 130, 118]
patient_ids = ["P001", "P002", "P003", "P004", "P005"]
mixed = [117, "high", True]           # legal but bad style
len(bp_systolic)                      # 5
```

R **vector** — created with `c()` (short for "combine"):

```r
bp_systolic <- c(117, 122, 141, 130, 118)
patient_ids <- c("P001", "P002", "P003", "P004", "P005")
length(bp_systolic)                   # 5
```

Two conceptual points:

1. **Both are ordered.** Position matters. `bp_systolic[1]` in R is 117 (the first element).
2. **R vectors are homogeneous.** All elements are the same type. `c(1, "two")` will silently convert everything to strings. Python lists are heterogeneous but you should still keep them homogeneous in practice.

The R silent-coercion behavior is a bug source. Show it live:

```r
c(1, 2, "three")     # returns "1" "2" "three" — all strings, no warning
```

Foreshadow: this is exactly what happens when your CSV has one row where "age" is `"unknown"`. The whole column becomes a string. Then `mean(age)` fails.

---

## Segment 2b (10–14 min): R's silent coercion

> Deck slide 5. **Run this live** — the silence is the lesson.

```r
c(1, 2, "three")
# "1"  "2"  "three"   — everything became text. No warning, no error.
```

Python lists happily hold mixed types (`[117, "high", True]` is legal), but you
should still keep them homogeneous: a column of one kind of thing is the whole
idea.

**Contrast with Session 2 explicitly.** Python *refused* to mix types and raised
a `TypeError`. R *silently converts*. **Loud failure beats quiet wrongness** — a
crash tells you where to look; a silent conversion does not.

Ask the room: *which behaviour would you rather have?* There is no clean answer,
and that is a good discussion — it is the deepest philosophical difference
between the two languages, and it shapes how you debug in each.

Tie it to the real data: six rows of `patients.csv` say `"unknown"` in the `age`
column. That is this bug, in the dataset they met last week.

---

---

## Segment 3 (14–23 min): Indexing and slicing

This is the segment where students most often get confused. Draw it on the board.

**Python is 0-indexed. R is 1-indexed. This will bite you.**

```python
# Python: index 0 = first element
bp_systolic = [117, 122, 141, 130, 118]
bp_systolic[0]        # 117  (first)
bp_systolic[1]        # 122  (second)
bp_systolic[-1]       # 118  (last — negative indices count from end)
```

```r
# R: index 1 = first element
bp_systolic <- c(117, 122, 141, 130, 118)
bp_systolic[1]        # 117
bp_systolic[2]        # 122
bp_systolic[length(bp_systolic)]   # 118 — no negative-from-end shortcut
```

**Slicing** — grab a range of elements:

```python
bp_systolic[1:4]      # [122, 141, 130] — indices 1, 2, 3. Stop is EXCLUSIVE.
bp_systolic[:3]       # [117, 122, 141] — first three
bp_systolic[-2:]      # [130, 118]      — last two
```

```r
bp_systolic[2:4]      # 122 141 130 — indices 2, 3, 4. Stop is INCLUSIVE.
bp_systolic[c(1, 3, 5)]  # 117 141 118 — grab specific indices
bp_systolic[-1]       # 122 141 130 118 — negative means DROP element 1 (very different from Python!)
```

Emphasize: **the same syntax means completely different things.** `-1` in Python = "last element". `-1` in R = "everything except the first." When you paste code from ChatGPT written for one language into the other, this is a common silent bug.

**Boolean indexing** — the single most useful research idiom:

```python
bp = [117, 122, 141, 130, 118]
high = [x > 130 for x in bp]           # [False, False, True, False, False]
# with numpy or pandas this is much cleaner — Session 7
```

```r
bp <- c(117, 122, 141, 130, 118)
high <- bp > 130                       # FALSE FALSE TRUE FALSE FALSE
bp[high]                               # 141 — the high values only
bp[bp > 130]                           # same thing, inline
```

The R idiom `bp[bp > 130]` is the seed of every filter operation you will do this semester. Ring that bell.

---

## Segment 3b (23–26 min): Predict — ninety seconds — protect this

> Deck slide 8. In pairs, all eight answers written down *before* anyone runs
> anything.

```
bp  = [117, 122, 141, 130, 118]     # Python
bp <- c(117, 122, 141, 130, 118)    # R

Python:   bp[2]     bp[1:3]     bp[-2]     bp[:0]
R:        bp[2]     bp[1:3]     bp[-2]     bp[0]
```

| | Python | R |
|---|---|---|
| `bp[2]` | `141` | `122` |
| `bp[1:3]` | `[122, 141]` | `117 122 141` |
| `bp[-2]` | `130` | `117 141 130 118` *(drops the 2nd)* |
| `bp[:0]` / `bp[0]` | `[]` | `numeric(0)` |

**Dwell on the two empty results.** An empty result is *not* an error. An
analysis that quietly runs on zero rows is a real failure mode — and it is the
same shape of bug as Session 1's trailing space.

---

---

## Segment 3c (26–30 min): Boolean masks — protect this

> Deck slide 9. **The most important slide in the deck. Three minutes, not one.**

Build it in stages, live, in R. The mask is invisible to students until you print
it by itself:

```r
bp <- c(117, 122, 141, 130, 118)
bp > 130            # FALSE FALSE TRUE FALSE FALSE   <- print this ALONE first
bp[bp > 130]        # 141                            <- then use it
sum(bp > 130)       # 1                              <- then count with it
```

Read `bp[bp > 130]` out loud as: **"the elements of `bp`, where `bp` is over
130."**

Ring the bell: *every* filtering operation for the rest of this course is this.
`dplyr::filter()` is this. `df[df.age > 65]` is this. Learn it here, in five
elements, before it arrives with fifty thousand rows.

**Be honest about the Python asymmetry.** Plain Python lists do *not* vectorise —
`bp > 130` is a `TypeError`. It needs numpy, which is Session 7. That is
genuinely why numpy and pandas exist. Do **not** teach the list-comprehension
version; comprehensions are Session 4.

---

---

## Segment 4 (30–33 min): Dictionaries and named lists

Motivation: sometimes you don't want position-based lookup. You want name-based lookup. "Give me the sample with ID P042."

Python **dict**:

```python
patient = {
    "id": "P042",
    "age": 61,
    "systolic": 141,
    "treated": True
}
patient["age"]              # 61
patient["age"] = 62         # update
patient["diagnosis"] = "HTN"  # add
patient.keys()              # dict_keys(['id', 'age', ...])
```

R **named list** (closest equivalent):

```r
patient <- list(
    id = "P042",
    age = 61,
    systolic = 141,
    treated = TRUE
)
patient$age                 # 61
patient[["age"]]            # same thing
patient$diagnosis <- "HTN"  # add a field
names(patient)              # "id" "age" "systolic" "treated" "diagnosis"
```

When to use a dict vs a list:

| Situation                                                       | Reach for              |
|-----------------------------------------------------------------|------------------------|
| A column of measurements (all one kind of thing)                | list / vector          |
| A single subject's attributes (mixed types, named fields)       | dict / named list      |
| A lookup table (gene name → chromosome, ID → group)             | dict / named list      |
| A stack of columns you want to line up as a table               | dataframe (Session 7)  |

The dataframe row from Session 7 onward is essentially a dict-per-row. Foreshadow this.

---

## Segment 5 (33–36 min): Where AI gets this wrong — protect this

> Deck slide 11. The AI-literacy core of the week.

You have Python, and you ask an AI to translate it to R:

```python
last_reading = bp[-1]        # Python: the last element
```

```r
last_reading <- bp[-1]       # R: everything EXCEPT the first
```

It runs perfectly. It never errors. Your "last reading" is now most of the
dataset. The correct R is `bp[length(bp)]` or `tail(bp, 1)`.

**Be honest with them:** current models often get this one *right* if asked
carefully. The point is not that AI is stupid — it is that when it is wrong here,
**nothing signals it**. No error, no warning, plausible-looking output.

Tie back to Session 1's loop: this is caught at step 3, **Compare** — and only if
you had an expectation in the first place.

---

## Segment 6 (36–55 min): Preview activity

The tutor will hand students small lists/vectors and ask them to *predict* the result of various indexing operations before running them. This forces the mental model. Point out that ChatGPT can *run* the code for them but only they can *predict* it.

---

## Key vocabulary

- **List / vector** — ordered container of values.
- **Element** — one item in a list.
- **Index** — the position of an element. Python starts at 0, R starts at 1.
- **Slice** — a sub-range of a list.
- **Boolean mask** — a list of True/False the same length as the data, used to select elements.
- **Dictionary / named list** — a container mapping keys (names) to values.

---

## Common student mistakes

- Off-by-one: forgetting Python starts at 0.
- Assuming Python and R slice syntax means the same thing (`-1` is the classic trap).
- Using position when they mean name, or vice versa.
- Silently coercing an R vector to strings by including one string element.

---

## Exit ticket

*In R, `xs <- c(10, 20, 30)`. What does `xs[-1]` give you, and why?*

---

## Before next session

- **Bring a candidate project dataset next week.** Even a bad one — a mediocre
  chosen dataset beats an unchosen perfect one, and they can switch by Session 6.
- Session 4 is control flow: conditionals, loops, and vectorisation.

---

## Handoff to tutor activity

**In class**, minutes 36–55. Source:
`assistants_per_lecture/03_collections_indexing_tutor.md`.

Six problems in about nineteen minutes: indexing puzzles that get progressively
nastier, plus the cross-language translation trap. Say the rule out loud before
they start — **the tutor will not move on until you commit to a prediction.
Predicting wrong is fine and expected; refusing to predict is not.**

Protected problems are 3 (boolean masks) and 4 (the AI translation trap).

**Two things to say about transcripts,** both learned from last week's
submissions: ask for **plain text** with the turns labelled, and tell them to
expect to reach all six problems — most of last week's cohort stopped at about
ten minutes, believing they were done.

Transcripts to Brightspace **before they leave**.
