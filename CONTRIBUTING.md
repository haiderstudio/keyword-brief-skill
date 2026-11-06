# Contributing

Small, focused improvements are welcome.

- Open an issue first for anything larger than a typo or a clearer example, so the scope can be agreed before work starts.
- Never weaken the safety rules: the skill must write a one-page brief only, from data the user gave it, with one main keyword per page, and must never quote a number it was not given.
- Every claim in a proposed change must be verifiable: a command must be runnable, a brief keyword must trace to the input list it came from, a brief number must trace to the input that gave it.
- Run `python3 tests/test_skill.py` before opening a pull request. It must pass.
- Do not add placeholder text, invented features, or copied content without attribution.
- Python standard library only — no new dependency without a reason in the issue.
