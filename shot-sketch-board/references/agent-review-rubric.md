# Three-Agent Review Rubric

Use these roles after drafting sketch plans. Each role must output pass/fail and concrete fixes. Do not accept neutral comments such as “mostly okay”, “depends”, or “can consider”.

## 剪辑 Agent

Judges whether the editor can execute the sketch.

Pass only if:

- The shot has a clear 16:9 layout.
- The main subject position is obvious.
- Material source is clear: real footage, screen recording, motion-graphics tool, or AI visual.
- Motion has start, movement, and end.
- Highlight/crop/zoom targets are explicit for screen-recording shots.
- Three-panel sketches are used when a shot has meaningful transition or camera movement.
- Multi-state shots use separate blank-draft frames such as `转场前 / 变化中 / 转场后`, so the editor can see the movement path.

Fail if:

- Editor must guess where to place screenshots or presenter.
- Motion is just “高级动效” or “转场” without specifics.
- There are too many simultaneous visual elements.
- A decorative background hides the actual shot elements.

## 编导 Agent

Judges whether the image is conceptually strong and tied to the line.

Pass only if:

- The image answers the spoken line, not just decorates it.
- Abstract concepts are turned into concrete metaphors.
- The shot connects to the previous or next shot when part of a sequence.
- The visual thesis is strong enough to understand with subtitles off.
- The design is not generic AI-tech wallpaper.
- The background is blank draft paper unless the script specifically requires a real background or provided material.

Fail if:

- The sketch prompt is a literal but shallow object list.
- The metaphor is weak, generic, or unrelated.
- The shot lacks hierarchy or emotional direction.

## 审核 Agent

Judges production risk, consistency, and hallucination risk.

Pass only if:

- No generated readable text is requested.
- No fake real webpage, code, logo, UI copy, or brand asset is requested.
- No wrong aspect ratio appears.
- No outdated circular presenter-window assumption appears unless explicitly requested.
- The style is low-fidelity storyboard, not final poster or cinematic concept art.
- Empty visual-description rows are skipped.

Fail if:

- Any prompt risks乱码, fake UI, fake website, fake code, or fake person.
- A prompt asks AI to create content that should come from provided materials.
- The sketch could mislead the editor about final assets.
