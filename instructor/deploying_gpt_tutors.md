# Deploying a tutor `.md` file as a custom GPT in ChatGPT Edu

Every file in `assistants_per_lecture/` and `assistants_by_unit/` is a plain
Markdown document with three parts: a **name**, a **description**, and an
**instructions block** in a fenced code block. This page is the mechanical
steps for turning one of those files into an actual GPT students can click a
link to and talk to. Budget about 10 minutes per tutor the first time; under 3
minutes for a re-deploy once you've done it once.

Do this for **Session 1 now** — it's the one that goes live tomorrow. The rest
of Unit 1 can follow over the next few weeks.

---

## Before you start

- Sign in to **chatgpt.com** with your **Vanderbilt ChatGPT Edu account**, not
  a personal account. If the top-left shows your personal workspace instead of
  a Vanderbilt one, switch workspaces first (click the workspace name, top
  left) — anything you build in the wrong workspace won't be shareable with
  students the way you need it to be.
- Have the tutor's `.md` file open in a second window so you can copy from it.

---

## Step 1 — Open the GPT Builder

1. In the left sidebar, click **Explore GPTs**.
2. Click **+ Create** (top right).
3. You'll land on a screen with two tabs: **Create** (a chat interface that
   builds the GPT for you conversationally) and **Configure** (a plain form).

**Use Configure, not Create.** The chat-based builder is meant for people
improvising a GPT from scratch; we already have a finished, reviewed prompt,
and pasting it directly into Configure avoids the builder chat rephrasing or
"improving" anything on the way in.

---

## Step 2 — Fill in the Configure tab

Working from the top of the `.md` file:

| Configure field | Comes from the `.md` file | Notes |
|---|---|---|
| **Name** | The line after `**Assistant title (paste as the assistant's name):**` | Copy it exactly, including the em dash and session number — students match this against the name on Brightspace. |
| **Description** | The line after `**Short description (paste as the assistant's description):**` | This is what shows in the GPT's header and in Explore GPTs. |
| **Instructions** | Everything **between** the two ` ``` ` fences under "System prompt / instructions" | Copy from just after the opening fence to just before the closing fence — do not include the fences themselves. This is the whole system prompt; nothing needs to be added or removed. **Hard cap: 8,000 characters** — see below. |
| **Conversation starters** | Leave blank, or optionally add the six problem names (e.g. "Problem 1 — Verify the tools") | Not load-bearing. The tutor's own opening move handles the warm-up. |
| **Knowledge** | Leave empty for Session 1 | See the note on file attachments below for later sessions. |

Copy the instructions block **exactly as written**, including the section
headers inside it (Ironclad rules, Voice, Time budget, etc.) — those aren't
formatting for the `.md` file, they're part of the prompt itself.

---

### The 8,000-character cap

ChatGPT's Instructions field takes at most **8,000 characters**, and a longer
paste is **truncated silently** — no error, no warning. The failure mode is
nasty: the tutor works fine early on and then ignores rules that lived near the
end of the prompt, which is exactly where the escalation and "never teach ahead"
rules sit.

Before deploying or re-deploying, run:

```bash
python instructor/check_prompt_length.py
```

It reports every tutor's prompt length and exits non-zero if any is over. All
thirteen currently fit; Session 1 is the tightest at 7,787.

---

## Step 3 — Capabilities (this is the part people get wrong)

Scroll down to **Capabilities**. Every tutor in this course is built assuming
these are off:

- [ ] **Web Browsing** — OFF. Nothing in any tutor needs live web access, and
  leaving it on risks the tutor fetching something off-syllabus mid-session.
- [ ] **Code Interpreter / Data Analysis** — OFF. This is the important one.
  If it's left on, the tutor *can run Python for the student*, which directly
  undermines every "I will not write code for you" rule in the prompt — a
  student can ask it to just execute the answer instead of reasoning it out.
  Some tutors (e.g. Session 5, Problem 6) deliberately reference the student
  using ChatGPT *separately* to generate code to critique — that's a different
  conversation from the tutor itself, not a reason to enable this here.
- [ ] **Image generation (DALL·E)** — OFF. Not used anywhere in this course.

If a later unit's tutor genuinely needs one of these on (check that session's
`.md` file — it would say so explicitly), that will be called out in the file.
None of Unit 1's do.

---

## Step 4 — Knowledge files (optional, and mostly for later sessions)

Some tutor files suggest attaching a companion deck so the tutor can point
students at a specific slide by content, not just by number. For Session 1,
this isn't necessary — the tutor already references the vocabulary slide by
number and the deck is separately posted on Brightspace.

If you do attach a deck later: use the **`.pptx` file directly** under
**Knowledge**, not a screenshot or PDF export. Keep in mind that anything
uploaded as Knowledge becomes something the GPT *can* quote from in an
answer — for the Socratic tutors here, that's fine, since they're built to
redirect rather than lecture, but don't attach anything (real student data,
answer keys) you wouldn't want a student able to ask the GPT to summarize.

---

## Step 5 — Publish and set sharing

1. Click **Create** (top right).
2. You'll be asked **who can access this GPT**. Choose:
   **"Anyone at [Vanderbilt's workspace name] with the link."**
   Do **not** choose "Only me" (students can't reach it) or "Everyone" /
   public GPT Store (it would be discoverable by anyone with a ChatGPT
   account, not just this class — and the instructions block is plainly
   visible to anyone who opens it, which is fine internally but not something
   to publish openly).
3. Click through to finish. You'll land on the GPT's own page with a URL like
   `https://chatgpt.com/g/g-XXXXXXXXX-cpbp-8306-tutor-session-1`.

**That URL is the link you post to Brightspace.** Copy it now, before you
navigate away — it's also visible later from **My GPTs** if you need it again.

---

## Step 6 — Test it before posting it

Do not post the link untested. Open it in an incognito/private window (or ask
a colleague to click it) and run through a couple of minutes of Problem 3 or 6 — the two
protected problems — checking:

- It refuses to hand over code when asked directly.
- It asks a follow-up question rather than answering flatly.
- The name and description match what's on Brightspace.
- Capabilities are actually off — try "run this for me" with a short snippet
  and confirm it doesn't execute anything.

If something's off, go back to **My GPTs → (the tutor) → Edit** and fix it
there — you don't need to recreate it from scratch.

---

## Step 7 — Post the link

Put the GPT's URL in that session's Brightspace assignment, alongside the
participation instructions (see `instructor/brightspace_session1.md` for
Session 1 specifically — the same pattern applies to every later session).

---

## Updating a tutor after you've already deployed it

If you edit the `.md` file later (a fix, a rule change), you do **not** need a
new GPT or a new link:

1. Go to **My GPTs** (under Explore GPTs, or your profile menu).
2. Click the tutor, then **Edit GPT**.
3. Replace the Instructions field with the updated block and **Update**.
4. The existing link keeps working — students who already have it get the new
   version on their next message.

This is also why it's worth keeping the `.md` files as the source of truth:
edit the file, then push the same change into the deployed GPT. If the two
drift apart, the file stops being trustworthy documentation of what students
actually experienced.

**Version tracking:** `instructor/review_notes.md` (§5) suggested adding a
version marker (e.g. `<!-- v2026.1 -->`) at the top of each `.md` file and
echoing the same string in the GPT's description, so that if a student reports
odd tutor behavior, you can tell which deployed version they hit. Worth doing
once you're deploying more than one or two of these.

---

## Doing this for all thirteen sessions

Once Session 1 is live, the fastest path for the rest of Unit 1 (and later
units) is:

1. Repeat Steps 1–7 once per file in `assistants_per_lecture/`.
2. Name each GPT to match its file exactly, so the Brightspace link and the
   in-chat name never disagree (students will screenshot mismatches).
3. Keep a running list of the deployed URLs somewhere you control — a private
   note, a spreadsheet, or a new file like `instructor/gpt_links.md` — since
   ChatGPT's **My GPTs** list is the only other place they live, and it's not
   something a TA can see without being made an editor on each one
   individually.

**Adding a co-editor (e.g. the TA):** open the GPT, **Edit GPT → Configure →
sharing settings**, and add them by email if ChatGPT Edu's workspace supports
GPT collaborators — availability of this varies by how Vanderbilt's workspace
is configured. If it's not available, the practical workaround is that only
the person who created a GPT can edit it, so deploy from one shared
instructor account if multiple people need edit access, rather than from an
individual's.

---

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Students report the tutor writes code when asked | Code Interpreter capability was left on — go to Edit GPT, turn it off. |
| Link works for you but not for a student | Sharing was set to "Only me." Edit GPT → sharing → workspace link. |
| GPT gives generic answers, ignores the Socratic rules | The instructions field is empty or truncated — check nothing was cut off when pasting (ChatGPT Edu's field has a character limit; these prompts are all comfortably under it, but a partial paste will silently truncate). |
| Can't find "Explore GPTs" or "+ Create" | You may be signed into a personal account rather than the Vanderbilt workspace — check the workspace switcher, top left. |
