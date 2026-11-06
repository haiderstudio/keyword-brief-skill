---
name: keyword-brief-skill
description: Write a one-page keyword brief from the user's own data, no invented numbers. Use when a user gives you their own keyword list, their own notes about their site, and any numbers they already have, and wants a one-page brief with one main keyword per page. Never quotes search volume, rankings, or competition it was not given. If the user gave no numbers, the brief has no numbers.
---

# keyword-brief-skill

Write a one-page keyword brief from data the user gave you.
One main keyword per page, mapped, with a plain summary.
A number you were not given is a number you do not quote.

## When to use this skill

Use it when:
- The user gives you a keyword list — their own words, from
  their own site, their own search box, or their own notes —
  and wants a brief for their pages.
- The user gives you notes about their site: what each page
  is about, who it is for, what it sells or explains.
- The user gives you numbers they already have, for example
  clicks from their Search Console export, and wants those
  numbers in the brief with their source named.
- The user wants one main keyword per page, so no two pages
  chase the same keyword.

## When NOT to use it

- Do not use it to do keyword research. Finding new
  keywords, checking what people search for, or looking at
  what competitors rank for is research, a different job.
- Do not use it when the user gave you no keywords and no
  notes. There is nothing to brief from, so write nothing.
  Ask for the list and the notes instead.
- Do not use it to quote search volume, keyword difficulty,
  competition, or rankings. If the user did not give you
  those numbers, you do not have them.
- Do not use it to promise traffic, rankings, or better
  search placement. A brief is a plan for pages. What a
  search engine does with those pages is not yours to
  promise.
- Do not use it to write the pages. This skill writes the
  brief. The pages come after, from the brief.

## Workflow

### 1. Read what the user gave you

Read the whole input the user gave you. Write down only
what is actually there:

- The keyword list, exactly as the user wrote it. Copy
  each keyword word for word. Do not tidy it, shorten it,
  or add a keyword of your own.
- The notes about each page: what the page is about, who
  it is for, what it should cover.
- The numbers the user gave, with their source: which
  number came from where, and when. For example, "40
  clicks in October 2026, from your Search Console
  export".
- The list of pages the brief is for.

Do not read anything else into the input. If a fact is not
in what the user gave you, you do not have it.

### 2. Pick one main keyword per page

Give each page exactly one main keyword, by what the page
is about:

- The main keyword is the one keyword from the user's
  list that best matches what the page covers.
- No two pages get the same main keyword. If two pages
  would take the same keyword, pick the page it fits best
  and give the other page its next best keyword from the
  list. Say which page lost out, in one line.
- The rest of the user's keywords become supporting
  keywords for the page they fit best, or go on the
  "not used this round" list (step 4).
- If the user gave more keywords than pages, the extra
  keywords are not forced onto pages. They wait for later
  pages. Forcing a keyword onto a page it does not fit
  makes the brief wrong.
- If the user gave fewer keywords than pages, say so.
  Pages with no keyword are listed under "Missing"
  (step 5). Never invent a keyword to fill the gap.

### 3. Write the brief, one page only

Write the brief in this fixed shape. It fits on one page.
If it runs longer, cut words, not sections.

```markdown
# Keyword brief — <site name, as the user gave it>

Main keyword: <the one keyword for the most important page>

## One keyword per page

| Page | Main keyword | Supporting keywords |
|------|--------------|---------------------|
| <page name> | <one keyword> | <keywords from the user's list, or —> |

## What each page should cover

- **<page name>:** <two or three lines, from the user's notes only>

## Numbers (from your data only)

- <keyword>: <number> <what it is>, <when> — from <source the user named>

## Missing — not quoted

- <what the user did not give, and so is not in this brief>
```

Rules for the brief:

- Every keyword in the brief must be in the user's list,
  copied word for word. A keyword that is not in the list
  is invented — delete it.
- Every number in the brief must be a number the user
  gave, with its source named beside it. A number with no
  source is a guess — delete it.
- The "What each page should cover" lines come from the
  user's notes only. Do not add a topic the notes do not
  mention.
- If the user gave no numbers at all, the Numbers section
  says exactly: "No numbers given — none quoted." It has
  no number in it. Not one.
- Never write "search volume", "monthly searches",
  "keyword difficulty", "competition", or a ranking
  unless the user gave you that exact figure. Those words
  with no figure behind them are still a claim.

### 4. List what was not used

After the brief, list the keywords from the user's list
that got no page this round, under "Not used this round".
One line per keyword, with one line saying why: "no page
fits it yet" or "kept for a later page". A keyword left
out is not a keyword lost — it is a keyword waiting.

### 5. Check the brief, then output it

Before handing the brief over, check it:

1. Read every keyword in the brief back against the
   user's list. Each one must be there, word for word.
   A keyword that is not in the list is invented —
   delete it.
2. Read every number in the brief back against what the
   user gave. Each one must be there, with its source.
   A number with no source is a guess — delete it.
3. Count the main keywords. There is one per page, and
   no two pages share one. Two pages sharing a main
   keyword means the mapping is wrong — fix it.
4. Count the pages. The brief covers every page the user
   named, or lists the ones it could not cover under
   "Missing".

Then output, in this order:

1. The brief, in one code block, ready to paste.
2. A "Not used this round" list: keywords with no page,
   and why.
3. A "Missing" list: numbers and facts the user did not
   give, so the brief does not have them. A missing fact
   is a fact about the input, not a gap to fill.

## Good examples

A full brief from a keyword list, notes, and Search
Console numbers (full worked example in
`examples/sample-input.md` and `examples/sample-brief.md`):

```markdown
# Keyword brief — Mara's Bike Repair, Leeds

Main keyword: bike puncture repair leeds

## One keyword per page

| Page | Main keyword | Supporting keywords |
|------|--------------|---------------------|
| Home | bike puncture repair leeds | bike service near me |
| Services | bicycle brake repair | bike chain replacement cost |
| Blog | fix flat tyre bike | — |

## What each page should cover

- **Home:** Puncture repair in Leeds, same-day, while you wait.
- **Services:** Brake repair and chain replacement, with prices.
- **Blog:** How to fix a flat tyre at home, step by step.

## Numbers (from your data only)

- bike puncture repair leeds: 40 clicks in October 2026 — from your Search Console export
- bicycle brake repair: 12 clicks in October 2026 — from your Search Console export

## Missing — not quoted

- Search volume: you did not give any, so none is quoted.
- Keyword difficulty: you did not give any, so none is quoted.
```

Every keyword is in the user's list. Every number is in
the user's input, with its source. The two numbers the
user did not give are listed as missing, not filled in.

A thin brief from three keywords, one line of notes, and
no numbers at all (full worked example in
`examples/thin-input.md` and `examples/thin-brief.md`):
the brief maps one keyword per page, the Numbers section
says "No numbers given — none quoted.", and it contains
no number anywhere. No volume was given, so no volume
appears.

More keywords than pages (full worked example in
`examples/more-keywords-input.md` and
`examples/more-keywords-brief.md`): eight keywords for
three pages. Three keywords become main keywords, three
become supporting keywords, and two go on the "Not used
this round" list. None is forced onto a page it does not
fit.

## Bad examples (do not write like this)

> The user gave five keywords and no numbers. The brief
> has "bike puncture repair leeds: 1,200 monthly searches".

The number came from nowhere. No numbers given means no
numbers quoted. A made-up volume is worse than no volume.

> The user gave the keyword "bicycle brake repair". The
> brief has "bike brake fix" as a main keyword.

That is not the user's keyword. Copy the list word for
word. A tidied keyword is an invented keyword.

> Two pages both get "bike puncture repair leeds" as their
> main keyword.

One main keyword per page, and no two pages share one.
Two pages chasing the same keyword fight each other.

> The user gave eight keywords for three pages. The brief
> squeezes all eight onto the three pages as main
> keywords.

A page has one main keyword. Extra keywords wait for
later pages. Forcing them in makes the brief wrong.

> The user gave no notes about the blog page. The brief
> says the blog should cover "winter cycling tips".

The notes did not mention winter cycling. A topic from
nowhere is an invented topic. List the page as missing
notes instead.

## Output rules

- Output one brief per site, in one code block, fitting
  on one page.
- Every keyword in the brief must trace to the user's
  list. If it cannot be traced, leave it out.
- Every number in the brief must trace to what the user
  gave, with its source named. If it cannot be traced,
  leave it out.
- Never invent a keyword, a number, a volume, a
  difficulty, a ranking, or a topic.
- Never claim the brief used search volume data, a
  keyword tool, or a competitor check unless you
  actually used one — and this skill uses none of those.
  It uses the user's data only.
- Never promise traffic, rankings, or better search
  placement. The brief is a plan for pages. What a
  search engine does with those pages is outside this
  skill.

## Limits and safety rules

- This skill reads what the user gave and writes one
  brief. It sends nothing anywhere, calls no tool, needs
  no API key or secret, and does no research.
- It writes one main keyword per page. No page gets two
  main keywords, and no two pages share one.
- It never invents a keyword, a number, or a topic. A
  missing fact is listed as missing, never filled in.
- It never copies a brief from another site. Each brief
  is written from the user's own list and notes.
- The brief is not a promise. A mapped keyword is not a
  ranking, and this skill does not check what any search
  engine does — it only checks that every keyword and
  every number comes from the user.
