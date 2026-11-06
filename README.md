# keyword-brief-skill

Write a one-page keyword brief from your own data, no invented numbers.

[![CI](https://github.com/haiderstudio/keyword-brief-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/haiderstudio/keyword-brief-skill/actions/workflows/ci.yml) [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](LICENSE)

## What it does

When an AI coding agent loads this skill, it takes the
keyword list, notes, and numbers you gave it and writes a
one-page keyword brief. One job, in this order:

1. Reads what you gave it: your keyword list, word for
   word; your notes about each page; and any numbers you
   already have, with their source.
2. Picks one main keyword per page. No two pages share a
   main keyword. Extra keywords wait for later pages;
   none is forced onto a page it does not fit.
3. Writes the brief: one keyword per page, what each page
   should cover (from your notes only), and a Numbers
   section with only the numbers you gave, each with its
   source named.
4. Lists what is missing. A number you did not give is
   listed as missing, not filled in. If you gave no
   numbers at all, the Numbers section says "No numbers
   given — none quoted." and has no number in it.

A keyword that is not in your list never appears in the
brief. A number that you did not give never appears in
the brief.

## What it does NOT do

- It does not do keyword research. Finding new keywords,
  checking what people search for, or looking at what
  competitors rank for is research, a different job.
- It does not quote search volume, keyword difficulty,
  competition, or rankings. If you did not give those
  numbers, this skill does not have them.
- It does not invent a keyword, a topic, or a number to
  fill a gap. A gap is listed as missing.
- It does not write the pages. It writes the brief. The
  pages come after, from the brief.
- It does not promise traffic, rankings, or better search
  placement. A brief is a plan for pages. What a search
  engine does with those pages is not this skill's to
  promise.
- It does not call a keyword tool, an API, or a search
  engine. It uses your data only, and needs no API key
  or secret.

## Who it is for

People with a small site who already have a keyword list
— from their own site, their own search box, or their own
notes — and want a plain one-page brief that maps one
keyword to each page, without made-up volumes. If you have
no list yet, this skill asks for one instead of guessing.

## How this differs from similar tools

Checked on GitHub on Nov 6, 2026. The quoted search
`"keyword-brief-skill"` returns 0 results — no repo by
that name exists. The unquoted search `keyword brief
skill` returns several SEO keyword skills, all of which do
live research: a business-aware keyword planner for Codex,
an SEO keyword research skill for Claude, and a ten-field
template that turns keyword research into writer-ready
briefs. No star counts are claimed for them here — the
search page did not show any.

The wide versions of the job live inside bigger suites,
not as one-job skills:

- Claude SEO (AgriciDaniel/claude-seo) is a full SEO
  suite with 26 sub-skills; its keyword work does live
  research. This skill is one file, brief-only, and does
  no research.
- The marketingskills pack (Corey Haines) holds 50
  skills, including SEO keyword work. This skill is one
  file and uses your data only.
- SEOJuice Skills (calm-north/seojuice-skills) has a
  `brief` skill that analyses the live SERP and a
  `find-keywords` skill that scores opportunities. This
  skill analyses no SERP and scores nothing.
- The SEO skill by iannuttall/seo runs 70+ audit tools
  through a local CLI and MCP server, and needs your own
  DataForSEO or Ahrefs key for keyword data. This skill
  needs no key, because it quotes no data it was not
  given.
- The `seo-keyword` skill (rampstackco/claude-skills)
  does keyword research from seed terms. This skill does
  no research — it briefs from a list you already have.
- The `content-brief` skill
  (indranilbanerjee/digital-marketing-pro) writes a
  production-ready brief and researches the keyword
  landscape. This skill writes a one-page brief from
  your list and notes only.

None of those were copied. The one-keyword-per-page rule,
the no-numbers-no-claims rule, the "not used this round"
list, and all three worked examples here are original.

## Install

This skill follows the open Agent Skills format: a folder with a
`SKILL.md` file.

**Claude Code / Codex / Gemini CLI (project level):**

```bash
mkdir -p .agents/skills
cp -r skills/keyword-brief-skill .agents/skills/keyword-brief-skill
```

## Usage

Give the agent your keyword list, your notes about each
page, and any numbers you already have, in your own words,
and tell it to use this skill. The agent follows
`skills/keyword-brief-skill/SKILL.md`: it reads what you
gave, maps one main keyword per page, writes a one-page
brief, checks every keyword and number back against what
you gave, and hands it over with a "not used this round"
list and a "missing" list.

If you have no numbers, say so — the brief will have
none. If you have no keyword list, the skill asks for one
instead of guessing.

## Example 1 — a full brief, with numbers you gave

Input: `examples/sample-input.md` — a bike repair shop in
Leeds, five keywords, notes for three pages, and two
click counts from the user's Search Console export for
October 2026. The skill writes `examples/sample-brief.md`:

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

## Example 2 — a thin brief, no numbers at all

Input: `examples/thin-input.md` — a sourdough bakery,
three keywords, one line of notes per page, no numbers.
The skill writes `examples/thin-brief.md`:

```markdown
# Keyword brief — Tom's Sourdough Bakery

Main keyword: sourdough bread near me

## One keyword per page

| Page | Main keyword | Supporting keywords |
|------|--------------|---------------------|
| Home | sourdough bread near me | — |
| Shop | sourdough starter kit | — |
| About | best sourdough bakery | — |

## What each page should cover

- **Home:** A small sourdough bakery, open every morning.
- **Shop:** Sourdough loaves and starter kits for sale.
- **About:** How Tom started baking sourdough.

## Numbers (from your data only)

No numbers given — none quoted.

## Missing — not quoted

- Search volume: you did not give any, so none is quoted.
- Keyword difficulty: you did not give any, so none is quoted.
```

No numbers given, so no numbers appear — not one digit
in the whole brief. No volume was given, so no volume
appears.

## Example 3 — more keywords than pages

Input: `examples/more-keywords-input.md` — a garden
centre, eight keywords for three pages, no numbers. The
skill writes `examples/more-keywords-brief.md`:

```markdown
# Keyword brief — Green Thumb Garden Centre

Main keyword: garden centre near me

## One keyword per page

| Page | Main keyword | Supporting keywords |
|------|--------------|---------------------|
| Home | garden centre near me | lawn feed |
| Shop | buy compost online | tomato plants for sale, rose bushes for sale |
| Blog | garden tools shop | — |

## What each page should cover

- **Home:** A garden centre, open seven days a week.
- **Shop:** Compost, plants, and tools for sale.
- **Blog:** Growing guides for beginners.

## Numbers (from your data only)

No numbers given — none quoted.

## Missing — not quoted

- Search volume: you did not give any, so none is quoted.
- Keyword difficulty: you did not give any, so none is quoted.

## Not used this round

- herb plants — no page fits it yet, kept for a later page.
- watering cans — no page fits it yet, kept for a later page.
```

Three keywords become main keywords, three become
supporting keywords, and two wait for later pages. None
is forced onto a page it does not fit.

## How it is tested

```bash
python3 tests/test_skill.py
```

The tests check that `SKILL.md` has valid `name` and
`description` frontmatter and the required workflow
sections; that `.gitignore` starts with `.env`; that
every keyword in each example brief appears in its input
file, word for word; that every number in the sample
brief's Numbers section appears in its input with its
source named; that the thin brief and the more-keywords
brief contain no digit at all; that no brief quotes search
volume, difficulty, competition, or a ranking it was not
given; that each brief's mapping table has one main
keyword per page and no two pages share one; that the
more-keywords brief lists exactly two keywords as not
used; and that all three briefs appear verbatim in this
README. No placeholder text anywhere in the repo.
Standard library only — no third-party module is imported.

The walkthrough of the skill run on the sample input is
in `examples/walkthrough.md`, with the exact commands
and their real output.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and pull requests
are welcome; please keep examples real and checkable.

## Licence

MIT — see [LICENSE](LICENSE). This is original work. The
"write a keyword brief" job is widely known; the related
tools named above are listed as related work, not
sources — nothing here was copied from them.
