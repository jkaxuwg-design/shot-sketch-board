# Sketch Style Reference

Use this style for reusable horizontal storyboard sketches across different IPs and topics.

## Visual Identity

- Canvas: 16:9 horizontal.
- Fidelity: low-fidelity production storyboard, not final artwork.
- Palette: white, black, warm gray, cool gray, muted blue for subjects, soft yellow for highlights.
- Lines: clean vector-like lines, simple blocking, clear object boundaries.
- Background: default to blank white or very light draft paper. No dark grid, cyberpunk clutter, decorative glows, code rain, tech wallpaper, or mood background unless the user explicitly asks. The sketch should feel like an editor-facing production draft, not a finished visual.
- Text: no generated readable text. Use blank bars, cards, placeholder blocks, icons, arrows, and highlight frames.
- People: simplified presenter or human silhouette. Do not generate real faces unless a source reference is explicitly provided.
- Web/UI: use generic desktop window frames and gray rectangles. Real screenshots are replaced later in editing.

## Four Shot Templates

## Blank Draft Standard

Use this as the default for all future sketch images:

- Keep the background empty: white/light gray paper only.
- Draw only the shot's required elements: subject, material box, crop frame, highlight, arrow, motion path, before/after relationship, or key prop.
- Remove atmosphere, decoration, texture, cinematic lighting, synthetic UI scenery, and unrelated background graphics.
- For real footage, website screenshots, and screen recordings, draw generic placeholders only. Real assets are inserted by the editor.
- If the row's `画面类型` is `录屏素材`, do not generate or embed a sketch. The editor should use the actual desktop screen recording/screenshot material.
- If one shot contains multiple movement states, generate multiple frames for that same shot:
  - `转场前 / 变化中 / 转场后` for three-state movement.
  - `前 / 后` for simple before-after movement.
  - `主画面` for static presenter, simple metaphor, or simple diagram shots.
- Every frame inside a multi-frame card must also be horizontal 16:9. Never use portrait sub-frames in a horizontal video project.
- The multi-frame card must make the transition legible without asking the editor to infer the movement.

### 真人/数字口播

Use a medium or close-medium horizontal frame. Put the presenter left, center, or right according to the row's visual need. Add only simple placeholder keyword cards if useful. Keep the presenter readable and avoid complex backgrounds.

### 录屏素材

Do not generate a sketch image when a row is marked `录屏素材`. Use the actual screen recording or screenshot provided by production.

If the user explicitly asks for a planning diagram for a screen recording row, use a large desktop-window placeholder inside the 16:9 frame. Add:

- crop rectangle
- zoom target
- highlight box
- arrow for movement
- optional blurred surrounding blocks

Do not fake webpage text or UI copy.

### 动效制作素材

Use diagram layout:

- cards
- nodes
- arrows
- split-screen
- timeline
- ladder
- triangle
- loop ring
- before/after comparison

Every diagram must have a single visual thesis.

For layer-evolution shots such as `Prompt -> Context -> Tooling -> Agent System -> Loop`, use a two-frame transition by default. Frame 1 is one clean full-width S-shaped evolution timeline: earliest layer at the lower-left part of the S path, most advanced layer near the upper-right/top, five large nodes with simple icons, no node text labels, current layer highlighted with a soft yellow halo and blue progressed path. Frame 2 is the transition landing frame: the current layer icon zooms up to occupy the center of the whole frame, with simple motion rays or scale rings. Do not repeat the full S timeline in Frame 2. The table text explains the layer names; the sketch must prioritize clean composition and the zoom transition.

For context-inflow shots such as "documents, codebase, chat history, requirements, and specs are fed into AI", do not draw only a few generic cards. Build a rich context-cloud around the central AI/agent subject. Represent each source as an icon card, for example: documents, code repository, historical conversations, product requirements, project specs, API docs, data tables, test reports, user feedback, design assets, competitor references, and brand/style rules. Use arrows flowing into the agent, and show the agent becoming larger when the amount of context increases.

For old prompt-to-agent comparison shots such as "person -> prompt -> Agent" or "old mode: human gives one prompt", draw one complete horizontal screen composition by default. Place a simplified person on the left, a GPT/Gemini/Codex-like generic AI input box in the center, and a generic Agent robot on the right. Use arrows from person to input box and from input box to Agent. Do not write real product names, UI copy, prompt text, or readable labels inside the sketch; use gray placeholder lines and a send-button icon.

For Loop-system overview shots such as "goal enters a loop" or "Loop handles trigger, execution, verification, memory, and judgment", draw one complete horizontal system map by default, not separated before/middle/after cards. Put the person or goal input on the left, a central Agent inside a loop ring in the middle, five icon nodes around the ring for trigger, execute, verify, memory, and judge, and an output/result card on the right. Use arrows to show the goal entering the loop and the result leaving it. Avoid readable node labels in the sketch; use icons and color accents.

### AI生成素材

Use abstract concept blocking:

- control ring
- workflow track
- task card
- verification gate
- memory archive
- tool bench
- maze
- workplace map

Still keep sketch fidelity low. Do not make cinematic final frames in the sketch pass.

## Prompt Formula

Chinese prompt:

> 生成一张 16:9 横屏低保真分镜草图。风格是专业制作说明图、通用线框图、广告分镜板、干净线稿。画面不包含任何可读文字、网页内容、代码、logo、字幕。主体：{subject}. 构图：{composition}. 高亮：{highlight}. 运镜/动作：{motion}. 使用黑白灰线稿，少量蓝色标主体，少量黄色标高亮区域。

English prompt:

> Create a 16:9 horizontal low-fidelity storyboard sketch, professional production planning style, generic wireframe plus advertising storyboard, clean line art. Do not include readable text, UI copy, code, logos, subtitles, or real webpage content. Subject: {subject}. Composition: {composition}. Highlight: {highlight}. Motion indication: {motion}. Use black, white and gray linework, muted blue for main subjects, soft yellow for highlighted areas.

## Anti-AI-Look Rules

- Do not use “cinematic futuristic interface” for sketches.
- Do not ask for “detailed UI text”.
- Do not use dense sci-fi panels, code strings, random glyphs, tiny labels, fake dashboards, or decorative holograms.
- Do not combine too many story beats in one sketch.
- Prefer one strong shape per idea: ring, ladder, triangle, gate, workstation, desktop window, split screen.
