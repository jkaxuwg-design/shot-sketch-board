# Failure Patterns

Use this file to record repeated problems so future scripts avoid them.

## Global Failures

### Wrong Aspect Ratio

- Problem: sketches or subframes appear vertical in a horizontal project.
- Fix: every sketch and every state inside a sketch card must be 16:9.

### Sketching Screen Recordings

- Problem: rows marked `录屏素材` receive unnecessary草图.
- Fix: skip sketches and prompts for real desktop recording/screenshot rows.

### Fake UI / Garbled Text

- Problem: AI-generated images create fake interfaces, fake code, or unreadable text.
- Fix: use generic blocks, icons, and placeholder lines; real UI must come from actual screenshots or recordings.

### Vague Visual Description

- Problem: editor cannot tell what to place, where to place it, or how it moves.
- Fix: describe subject, position, material source, start state, end state, highlight, and transition.

### Cluttered Concept Sketch

- Problem: too many icons/cards compete in one frame.
- Fix: choose one visual thesis; group elements into lanes, arcs, or before/after states.

### IP Style Pollution

- Problem: one account's background, typography, or presenter layout is copied to another account.
- Fix: read only the relevant IP profile and mark uncertain style as `needs confirmation`.
