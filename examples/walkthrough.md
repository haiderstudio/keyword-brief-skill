# Walkthrough — running the skill on the sample input

This is the real run of the skill on `examples/sample-input.md`,
done on Nov 6, 2026, following `skills/keyword-brief-skill/SKILL.md`.

## Input given

`examples/sample-input.md` — Mara's Bike Repair, Leeds:

- Keyword list (5 keywords, the user's own words): bike
  puncture repair leeds, bicycle brake repair, bike chain
  replacement cost, fix flat tyre bike, bike service near me.
- Notes: Home is puncture repair in Leeds, same-day, while
  you wait; Services is brake repair and chain replacement,
  with prices; Blog is how to fix a flat tyre at home.
- Numbers: 40 clicks for "bike puncture repair leeds" and
  12 clicks for "bicycle brake repair" in October 2026,
  from the user's Search Console export. No search volume,
  no keyword difficulty, no rankings given.

## What the skill did

1. Read the input. Five keywords, three pages, two numbers
   with their source.
2. Picked one main keyword per page: Home takes "bike
   puncture repair leeds" (the shop's main job), Services
   takes "bicycle brake repair", Blog takes "fix flat tyre
   bike". No two pages share a main keyword.
3. The other two keywords became supporting keywords:
   "bike service near me" under Home, "bike chain
   replacement cost" under Services.
4. Wrote the brief, `examples/sample-brief.md`. The two
   click counts are in the Numbers section, each with
   "from your Search Console export" beside it. Search
   volume and keyword difficulty are listed under Missing,
   not filled in.

## Checks run

```bash
python3 tests/test_skill.py
```

Output (last lines):

```text
PASS test_sample_number_traced_40
PASS test_sample_number_traced_2026
PASS test_sample_number_traced_12
PASS test_sample_number_traced_2026
PASS test_sample_number_has_source
PASS test_sample_number_has_source
PASS test_thin-brief.md_no_digits
PASS test_more-keywords-brief.md_no_digits
All tests passed.
```

65 checks, all PASS, exit 0. Run twice; same result both
times.

The thin brief (`examples/thin-brief.md`) was checked the
same way: no digit anywhere in the file, and its Numbers
section says "No numbers given — none quoted." The
more-keywords brief (`examples/more-keywords-brief.md`)
was checked the same way: eight keywords in, three main
keywords, three supporting, two on the "Not used this
round" list, no digit anywhere in the file.

## Install check (fresh folder)

```bash
rm -rf /tmp/kb20-fresh
cp -r . /tmp/kb20-fresh
cd /tmp/kb20-fresh
mkdir -p .agents/skills
cp -r skills/keyword-brief-skill .agents/skills/keyword-brief-skill
python3 tests/test_skill.py
```

Result: the install commands ran clean, the installed
copy is identical to the source folder, and all 65 tests
pass from the fresh copy, exit 0.
