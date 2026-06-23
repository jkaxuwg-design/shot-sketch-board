# Finished Frame Training Library

Use this library as visual memory from completed videos. These are not final prompts to copy directly; they are production patterns to reuse when matching similar script intent.

Important: source lines may contain product names or brand names because they come from real scripts. Do not copy those names into AI sketch prompts. Convert them into generic placeholders such as process panel, code panel, engine panel, assistant icon, or real screenshot inserted during editing.

## Shared Visual Language

- Aspect ratio: 16:9 horizontal.
- Background: dark charcoal or black board with subtle grid lines.
- Main containers: large rounded rectangles with white stroke, soft shadow, and image/video content inside.
- Typography in finished edit: large white Chinese display type with light gray drop shadow. In sketches, do not generate this text; represent it as blank title bars or text blocks.
- Layout rhythm: one large visual anchor plus one secondary panel or question stack.
- Motion implication: panels slide or scale into place; text/questions appear one by one; key panel may push forward.

## Example 001: Mechanism Explanation / Result vs Code

Source line:

> 简单来说，它不是直接画视频，而是让AI先写出一套完整的前端网页代码，再通过Remotion引擎精准渲染输出成视频

Finished-frame pattern:

- Left/front: large rounded rectangle containing the “not directly drawing video” visual result. It sits in front and occupies roughly 55%-60% of width.
- Right/back: darker rounded rectangle behind it, containing the code/editor/process side. It is partially covered by the foreground panel.
- Background: dark grid board.
- Text treatment: large bottom-left phrase for the negated idea, large right-lower phrase for the actual mechanism. Subtitle sits bottom center.

Reusable shot logic:

- Use for lines explaining “not A, but B”, hidden mechanism, pipeline, or underlying process.
- Sketch should show two-layer comparison:
  - foreground panel = surface result / wrong assumption
  - background panel = real process / code / engine / workflow
- Do not ask AI to draw readable code. Use dark editor-like gray lines.
- In a 3-panel sketch:
  - Start: foreground result panel appears alone.
  - Motion: background process panel slides in from right and tucks behind.
  - End: both panels lock into layered layout, highlight shifts from result to process.

Sketch prompt core:

> 16:9 horizontal low-fidelity storyboard sketch, dark grid background, two overlapping rounded rectangles with white outlines, large foreground result panel on the left, darker background process/code panel behind it on the right, no readable text, code shown only as faint gray lines, clean production planning style.

## Example 002: Presenter + Question Wall

Source line:

> Agent是个啥？跟之前的AI助手有什么区别？普通人能用吗？用来干嘛的？这些问题我都被问过无数次了。

Finished-frame pattern:

- Left: large rounded rectangle containing presenter medium shot. The presenter fills most of the left panel.
- Right: dark grid negative space with stacked large question lines.
- Typography: one larger headline question at upper right, secondary questions stacked with generous spacing below.
- Tone: direct, explanatory, approachable.

Reusable shot logic:

- Use for hook questions, FAQ openings, “很多人问过”, “到底是什么”, “普通人能不能用”, “有什么区别”.
- Sketch should show:
  - presenter panel left, 50%-55% width
  - question wall right, 40%-45% width
  - three to four blank text bars stacked vertically, first one largest
- Do not generate readable questions in the sketch. Use blank white/gray bars with different sizes. Real text is added in edit.
- In a 3-panel sketch:
  - Start: presenter panel already on screen.
  - Motion: question bars appear one by one on the right.
  - End: final stacked question wall holds.

Sketch prompt core:

> 16:9 horizontal low-fidelity storyboard sketch, dark grid background, large rounded presenter video panel on the left with simplified presenter silhouette, right side contains a stacked question-wall layout using blank white title bars, first bar largest, clean spacing, no readable text, no logos.

## Pattern Selection Rules

- If the script line contains multiple questions or FAQ framing, prefer `Presenter + Question Wall`.
- If the script line contrasts a misconception with an underlying mechanism, prefer `Mechanism Explanation / Result vs Code`.
- If the script line shows proof from webpage/screenshots, use the general `真实素材占位` pattern but keep the same dark grid and rounded white frame language.
- If the script line explains process, pipeline, rendering, code, model, workflow, or engine, prefer layered panels rather than generic futuristic UI.
