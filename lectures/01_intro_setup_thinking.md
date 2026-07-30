# Session 1 — Course Intro, Setup, and Thinking Like a Coder

**Unit:** 1 (Foundations)
**Duration:** 30-minute lecture + 20-minute activity
**Companion tutor:** `assistants_per_lecture/01_intro_setup_thinking_gpt.md`

---

## Framing

Every student in this room will, at some point this semester, ask ChatGPT to write code for them. That is fine. The problem is not *that* they use AI — it is that most first-time programmers cannot tell whether the code the AI produced does what they need. This course exists to fix that. We are going to teach you how to *think* like a programmer, so that when you paste code out of an AI, you can look at it and know whether to trust it.

---

## Learning objectives

By the end of this session, students should be able to:

1. Open a Python `.py` file in VS Code, a Jupyter notebook, and an R script in RStudio, and run a one-line program in each.
2. State — in one sentence, in their own words — what a program *is*.
3. Take an English research question and break it into a numbered list of sub-tasks a computer could do.
4. Name one thing AI coding assistants are reliably good at, and one thing they are reliably bad at.

---

## 30-minute outline

| Time     | Segment                                             |
|----------|-----------------------------------------------------|
| 0–5      | Why this course exists (the AI honesty conversation) |
| 5–12     | Tool tour + everyone runs hello world               |
| 12–22    | Decomposition demo (research question → steps)      |
| 22–28    | What AI is (and is not) good at                     |
| 28–30    | Preview the tutor activity                          |

---

## Segment 1 (0–5 min): Why this course exists

Talking points:

- The old version of this course taught syntax. That is now free — an LLM will produce syntactically valid Python in a second. So teaching syntax is no longer the job.
- The new job is teaching the *logic* underneath the syntax, because that is what an LLM cannot do reliably. LLMs are word-completion engines. They do not know what your data means. They will happily run a t-test on ordinal data.
- Corollary: **you** are the scientist. The code has your name on it. If an AI wrote a bug and the paper is wrong, that is your bug and your paper.
- One-sentence contract: *in this course we do not care whether you memorize syntax. We care whether you can read a block of code and tell us what it does and whether it is right.*

---

## Segment 2 (5–12 min): Tool tour + hello world

Everyone should have installed the following before class (pre-work). Confirm:

- **Python 3.11+** — https://www.python.org/downloads/
- **VS Code** — https://code.visualstudio.com/
- **VS Code extensions:** Python, Jupyter, GitHub Copilot (free for students)
- **R** — https://cran.r-project.org/
- **RStudio Desktop** — https://posit.co/download/rstudio-desktop/
- **GitHub Copilot in RStudio** — Tools → Global Options → Copilot

Walk through each tool and *what problem it solves*:

| Tool             | What it is                                                             | When you use it                                   |
|------------------|------------------------------------------------------------------------|---------------------------------------------------|
| Python           | The interpreter (the thing that runs `.py` files)                      | Anywhere you run Python code                      |
| R                | The interpreter for R                                                  | Anywhere you run R code                           |
| VS Code          | A text editor. That is all.                                            | Writing/editing Python files, notebooks           |
| RStudio          | An editor + console + plot pane + package manager built for R          | Writing/editing R scripts, everything R           |
| Jupyter notebook | A document that mixes code, its output, and prose                      | Exploratory analysis, sharing analysis narratives |
| Copilot          | An AI that autocompletes code                                          | While you are typing, in either editor            |
| ChatGPT / Claude | An AI conversation partner                                             | Asking "how do I do X" or "why is this broken"    |

Live demo (everyone types along):

```python
# in a new file hello.py
print("hello, research")
```

```r
# in a new .R script
print("hello, research")
```

Point out: **the code is essentially the same.** Both languages are giving one command — "run the `print` function on the string `hello, research`." The differences between Python and R are 90% cosmetic. The concepts we teach in this course transfer.

---

## Segment 3 (12–22 min): Decomposition — the actual skill

This is the load-bearing segment. Say it out loud: *the hard part of programming is not the code. The hard part is turning a research question into a sequence of unambiguous steps.*

Live example. Take this research question:

> *"Is average blood pressure different between patients on drug A versus drug B?"*

Ask the room: what are the steps? Write them on the board as students call them out. Aim for something like:

1. Get the data (from a file, a database, wherever).
2. Look at the data — how many patients, what columns, any missing values?
3. Split the patients into a Drug A group and a Drug B group.
4. Compute the mean blood pressure of each group.
5. Ask whether the difference is bigger than we'd expect from chance (a statistical test).
6. Report the result — a number and a plot.

Now the reveal: **each of those steps is a chunk of code we will write this semester.** Step 1 is Session 6–7 (reading files, dataframes). Step 2 is Session 9 (EDA). Step 3 is Session 8 (filtering). Step 4 is Session 7 (summaries). Step 5 is Session 11 (stats). Step 6 is Session 10 (viz). The syllabus *is* the decomposition of a research analysis.

Emphasize the meta-point: **when a student asks an AI "analyze my data," the AI has to guess all six of those steps.** When a student who has taken this course asks the AI, they specify step 3 or step 5 with the right vocabulary and get the right answer. That is the entire value proposition of learning to code in the AI era.

---

## Segment 4 (22–28 min): What AI is and is not good at

Two-column list on the board:

**AI is reliably good at:**
- Boilerplate (imports, plot styling, argument parsing)
- Syntax you forgot ("how do I open a CSV in pandas")
- Explaining unfamiliar code line by line
- Suggesting library names
- Refactoring code you already understand

**AI is unreliable at:**
- Anything requiring knowledge of *your* data
- Choosing the right statistical test
- Catching that a column is stored as a string when it should be a number
- Knowing whether a p-value is meaningful for your design
- Small numerical errors (off-by-one, log vs log10, degrees vs radians)
- Package hallucinations (inventing functions that don't exist)

Corollary: **you must always verify.** Run the code. Look at the output. Compare it to what you *expected* the output to be. If you have no expectation, you are not doing science, you are doing typing.

---

## Segment 5 (28–30 min): Preview activity

Introduce the tutor GPT (link on Brightspace). Explain the rules:

- The tutor will *not* give you code. It will ask you questions.
- Full participation credit comes from engaging with the tutor's questions, not from getting the "right" answer.
- Paste your transcript to Brightspace at the end of the session.

Send them to `assistants_per_lecture/01_intro_setup_thinking_gpt.md`.

---

## Key vocabulary introduced this session

- **Program / script** — a text file the interpreter reads and executes top to bottom.
- **Interpreter** — the software that reads code and does what it says (`python`, `R`).
- **Editor** — the software you type code in (VS Code, RStudio).
- **REPL** — Read-Eval-Print Loop. The interactive prompt.
- **Notebook** — a document mixing code cells and prose (Jupyter, Quarto).
- **Decomposition** — breaking a question into steps small enough to code.

---

## Common student mistakes to preempt

- Confusing "Python the language" with "VS Code the editor." (You can edit Python in any text editor.)
- Thinking Copilot is the same as ChatGPT. (Copilot autocompletes as you type; ChatGPT is a chat.)
- Assuming a program that runs is a program that is correct. It is not.
- Copy-pasting AI code without ever reading it.

---

## Pre-work for next session

- Confirm your Python and R installs are working.
- Take the pre-test assessment on Brightspace.
- Complete the tutor activity for Session 1 and paste your transcript.
