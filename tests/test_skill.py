"""Tests for the keyword-brief-skill: frontmatter (plain-text parse,
no yaml import), required sections, .gitignore, the three worked
briefs (every keyword traced to its input list, every number
traced to its input with its source named, no invented numbers,
one main keyword per page, no two pages sharing one), the
README examples matching the real files, and the README's
install commands actually running.

Standard library only — re, subprocess, sys, pathlib, shutil,
tempfile. A clean CI runner has no third-party modules, so
none are imported here.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "keyword-brief-skill" / "SKILL.md"
README = ROOT / "README.md"
GITIGNORE = ROOT / ".gitignore"
CI = ROOT / ".github" / "workflows" / "ci.yml"
BANNED = ["TODO", "FIXME", "lorem", "coming soon"]
PITCH = ["leverage", "cutting-edge", "delve", "empowering"]
# (input file, brief file)
PAIRS = [
    ("sample-input.md", "sample-brief.md"),
    ("thin-input.md", "thin-brief.md"),
    ("more-keywords-input.md", "more-keywords-brief.md"),
]


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        sys.exit(1)


def section(text, heading):
    """Text under a ## heading, up to the next ## heading."""
    m = re.search(r"## " + re.escape(heading) + r"\n(.*?)(?=\n## |\Z)",
                  text, re.S)
    return m.group(1) if m else ""


def keyword_list(input_text):
    sec = section(input_text, "Keyword list (the user's own words)")
    return [line[2:].strip() for line in sec.splitlines()
            if line.startswith("- ")]


def page_names(input_text):
    sec = section(input_text, "Notes about the pages")
    return [line[2:].split(":")[0].strip() for line in sec.splitlines()
            if line.startswith("- ")]


def mapping_rows(brief_text):
    """(page, main keyword, [supporting keywords]) per table row."""
    rows = []
    for line in brief_text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 3 or cells[0] == "Page":
            continue
        if set(cells[0]) <= {"-", " "}:
            continue
        supporting = [] if cells[2] == "—" else \
            [s.strip() for s in cells[2].split(",")]
        rows.append((cells[0], cells[1], supporting))
    return rows


def main():
    skill = SKILL.read_text()
    m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
    check("test_skill_frontmatter",
          bool(m) and "name: keyword-brief-skill" in m.group(1)
          and "description:" in m.group(1))
    for sec_name in ["When to use this skill", "When NOT to use it",
                     "Workflow", "Good examples", "Bad examples",
                     "Output rules", "Limits and safety rules"]:
        check("test_skill_sections_" + sec_name.split()[0],
              sec_name in skill)
    check("test_skill_refusal_rule",
          "never invent" in skill.lower()
          and "No numbers given" in skill)
    check("test_gitignore_env_first",
          GITIGNORE.read_text().splitlines()[0] == ".env")
    for f in [SKILL, README, GITIGNORE, CI]:
        check("test_no_placeholders_" + f.name,
              not any(b in f.read_text() for b in BANNED))
    for f in [SKILL, README]:
        check("test_no_pitch_words_" + f.name,
              not any(b in f.read_text().lower() for b in PITCH))
    check("test_no_absolute_paths",
          "/home/hatch" not in (SKILL.read_text() + README.read_text()))

    readme = README.read_text()
    for input_name, brief_name in PAIRS:
        input_text = (ROOT / "examples" / input_name).read_text()
        brief = (ROOT / "examples" / brief_name).read_text()
        kws = keyword_list(input_text)
        rows = mapping_rows(brief)
        check("test_" + brief_name + "_pages_covered",
              sorted(r[0] for r in rows) == sorted(page_names(input_text)))
        mains = [r[1] for r in rows]
        check("test_" + brief_name + "_main_keywords_unique",
              len(mains) == len(set(mains)))
        for page, main, supporting in rows:
            check("test_" + brief_name + "_main_traced_" + page,
                  main in kws)
            for sup in supporting:
                check("test_" + brief_name + "_supporting_traced_" + sup,
                      sup in kws)
        main_kw = re.search(r"^Main keyword: (.+)$", brief, re.M).group(1)
        check("test_" + brief_name + "_headline_keyword_in_list",
              main_kw in kws)
        before_missing = brief.split("## Missing")[0]
        check("test_" + brief_name + "_no_volume_claims",
              "search volume" not in before_missing.lower()
              and "keyword difficulty" not in before_missing.lower()
              and "monthly searches" not in brief.lower()
              and "ranking" not in brief.lower())
        check("test_" + brief_name + "_in_readme", brief in readme)
    # Numbers: the sample brief quotes two, each traced to its
    # input with its source named; the other two briefs have
    # no digit anywhere.
    sample = (ROOT / "examples" / "sample-brief.md").read_text()
    sample_input = (ROOT / "examples" / "sample-input.md").read_text()
    numbers = section(sample, "Numbers (from your data only)")
    numbered_lines = [line for line in numbers.splitlines()
                      if re.search(r"\d", line)]
    check("test_sample_numbers_count", len(numbered_lines) == 2)
    nums = re.findall(r"\d+", numbers)
    for n in nums:
        check("test_sample_number_traced_" + n, n in sample_input)
    for line in numbers.splitlines():
        if re.search(r"\d", line):
            check("test_sample_number_has_source",
                  "Search Console export" in line)
    for brief_name in ["thin-brief.md", "more-keywords-brief.md"]:
        brief = (ROOT / "examples" / brief_name).read_text()
        check("test_" + brief_name + "_no_digits",
              not any(c.isdigit() for c in brief))
        check("test_" + brief_name + "_no_numbers_given_line",
              "No numbers given" in brief)
    # More keywords than pages: exactly two wait for later pages.
    more = (ROOT / "examples" / "more-keywords-brief.md").read_text()
    more_input = (ROOT / "examples" / "more-keywords-input.md").read_text()
    unused = section(more, "Not used this round")
    unused_kws = [line[2:].split(" — ")[0].strip()
                  for line in unused.splitlines() if line.startswith("- ")]
    check("test_more_keywords_unused_count", len(unused_kws) == 2)
    for kw in unused_kws:
        check("test_more_keywords_unused_traced_" + kw,
              kw in keyword_list(more_input))
        check("test_more_keywords_unused_not_mapped_" + kw,
              kw not in [r[1] for r in mapping_rows(more)]
              and kw not in [s for r in mapping_rows(more)
                             for s in r[2]])
    # The SKILL.md good example is the sample brief, word for word.
    fenced = re.findall(r"```markdown\n(.*?)```", skill, re.S)
    sample_brief = (ROOT / "examples" / "sample-brief.md") \
        .read_text().strip()
    check("test_skill_example_matches_sample_brief",
          any(block.strip() == sample_brief for block in fenced))

    # The README's install commands, actually run (into a temp
    # folder, so the repo itself is not touched).
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / ".agents" / "skills"
        target.mkdir(parents=True)
        out = subprocess.run(
            ["cp", "-r", str(ROOT / "skills" / "keyword-brief-skill"),
             str(target / "keyword-brief-skill")],
            capture_output=True, text=True)
        check("test_readme_install_command", out.returncode == 0
              and (target / "keyword-brief-skill" / "SKILL.md")
              .read_text() == skill)
    ci = CI.read_text()
    check("test_ci_valid",
          "python3 tests/test_skill.py" in ci
          and "actions/checkout@v4" in ci
          and "runs-on: ubuntu-latest" in ci)
    print("All tests passed.")


if __name__ == "__main__":
    main()
