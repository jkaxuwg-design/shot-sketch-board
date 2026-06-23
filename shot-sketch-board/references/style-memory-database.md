# Style Memory Database

Use this reference when the user wants the skill to learn from different IPs, directors, editors, finished videos, or feedback.

The database is a memory system, not a model-training system. It stores reusable production rules, style preferences, examples, and failure cases so future storyboard work can adapt without mixing styles.

## Directory Map

```text
data/
  global/
    universal-production-rules.md
  ips/
    _template/profile.md
  directors/
    _template/profile.md
  editors/
    _template/profile.md
  cases/
    _template/case-record.md
  mistakes/
    failure-patterns.md
```

## Reading Workflow

Before drafting a storyboard:

1. Identify whether the user specified an IP, director, editor, case, or reference video.
2. Always apply the universal rules in `references/script-table-schema.md`, `references/sketch-style.md`, and `data/global/universal-production-rules.md`.
3. If the IP is known, read only that IP profile from `data/ips/`.
4. If the director or editor is known, read only that person's profile.
5. If the task resembles a saved case, read the case record and only reuse transferable patterns.
6. If there is a conflict, follow this priority:
   - current user instruction;
   - final copy or final spreadsheet supplied in the current turn;
   - locked template dropdown values;
   - IP profile;
   - director/editor preference;
   - global rules;
   - older cases.

## Writing Workflow

When the user provides new training material:

1. Extract reusable production grammar, not one-off content.
2. Record the source line, finished-frame description, what worked, and when to reuse the pattern.
3. Store the pattern under the correct IP or case.
4. Store personal preferences under the director/editor profile, not the IP profile.
5. Store repeated mistakes in `data/mistakes/failure-patterns.md`.
6. Mark uncertain observations as `needs confirmation` instead of turning them into hard rules.

## Contamination Controls

- Do not apply one IP's background, typography, presenter layout, or frame treatment to another IP unless the user asks.
- Do not treat a single finished frame as a universal style.
- Do not copy brand names, real UI text, real logos, or readable code into AI prompts.
- Do not let editor convenience override script meaning; simplify execution while preserving the line's visual idea.
- Do not let director preference override locked dropdown values.

## Record Quality Standard

A good memory record includes:

- when to use the pattern;
- when not to use it;
- composition ratio and subject placement;
- motion rhythm;
- material source;
- sketch rule;
- prompt risk;
- one or more linked examples if available.

A bad memory record is vague, such as `make it high-end`, `more visual`, `AI tech feeling`, or `use this style everywhere`.
