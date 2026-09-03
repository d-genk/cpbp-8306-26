# Brightspace — Session 2 (09/03/2026)

Everything to post before Session 2, and the copy to paste into each item.

Unlike Session 1, the tutor activity runs **in class** (minutes 36–55), so the
tutor link has to be live and reachable before you walk in.

---

## 1. Files to upload

| File | From | Why it has to be there |
|---|---|---|
| `CPBP8306_Session2_Variables_and_Types.pptx` | `slides/` | Students refer back to the vocabulary slide (16); the tutor sends them to it by name |
| **`data/patients.csv`** | `data/` | **New this week.** The lecture demo loads it, and the tutor's Problem 3 references its `age` column |
| `unit1_cheatsheet.md` | `handouts/` | Already posted for Session 1 — confirm it is still visible |

`data/patients.csv` is the one genuinely new upload. It is synthetic — no real
patients, safe to distribute.

---

## 2. The tutor link

Deploy from `assistants_per_lecture/02_variables_types_tutor.md` following
`instructor/deploying_gpt_tutors.md`, then record the URL in
`instructor/gpt_links.md` and post it here.

**Capabilities: Web Browsing OFF, Code Interpreter OFF.** Code Interpreter
matters more this week than last — the entire session is *predict, then run*, and
a tutor that can execute code for them removes the point of the exercise.

Suggested copy:

> **Session 2 participation — due before you leave today.**
>
> Work through the Session 2 tutor. Six problems, about twenty minutes. You will
> be handed broken code and asked to **predict what it does before running it**.
>
> **Predicting wrong is fine and expected. Refusing to predict is not.** Credit
> is for engaging with the questions, not for being right.
>
> Paste the whole conversation here as-is, including anywhere you went in
> circles.
>
> Install still not working? Do the activity anyway — every problem works as a
> thought experiment, and the tutor knows that. Flag an instructor or the TA.

---

## 3. Homework list for the page

> **Before Session 3:**
>
> 1. If your install is still incomplete, finish it — the guide from Session 1 is still posted.
> 2. **Choose your project dataset.** Due Session 4, which is two weeks away. Start looking now.
> 3. Nothing else. This week is light on purpose.

---

## 4. Carried over from Session 1 — check these are still live

- [ ] Install guide and both `check_setup` scripts still posted
- [ ] Session 1 tutor link still reachable (students had until today to submit)
- [ ] Pre-test link still open for anyone who missed it in class

---

## Night-before checklist

- [ ] Deck uploaded
- [ ] `data/patients.csv` uploaded
- [ ] Session 2 tutor deployed, tested signed-out, link posted
- [ ] Participation assignment accepts pasted text, due end of class today
- [ ] Homework list on the page
- [ ] Run `python demos/02_types_demo.py` once from the repo root so you know it works on the machine you are teaching from
