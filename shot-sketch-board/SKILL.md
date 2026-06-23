---
name: shot-sketch-board
description: Generate horizontal video storyboard script tables, shot design, AI image/video prompts, and low-fidelity sketch boards from Chinese video copy, briefs, or script spreadsheets. Use when the user asks to turn 文案, brief, 口播稿, 商单脚本, 分镜, 镜头设计, 草图, storyboard, AI画面提示词, or Excel storyboard templates into a production-ready table for editors, directors, reviewers, and AI image/video generation.
---

# Shot Sketch Board

Use this skill to turn a user-provided video copy or brief into a 16:9 production storyboard table. The output must be useful for a real editor: clear shot intent, clean material placement, allowed dropdown values, AI keyframe prompts, image-to-video prompts, and optional sketch images.

## Required Output Columns

Always generate or preserve this table schema unless the user provides a stricter template:

1. `镜头/段落/时长`
2. `景别/运镜`
3. `画面描述`
4. `台词/旁白`
5. `画面类型`
6. `情绪类型`
7. `动效/后期花字`
8. `备注`
9. `首帧图提示词（中文）`
10. `首帧图提示词（英文）`
11. `图生视频提示词（中文）`
12. `图生视频提示词（英文）`
13. `草图/画面`

Read `references/script-table-schema.md` before creating or editing a full script table.

## Allowed Dropdown Values

- `景别/运镜`: `远景`, `全景`, `中景`, `近景`, `特写`
- `画面类型`: `数字/真人口播`, `AI生成素材`, `动效制作素材`, `录屏素材`
- `情绪类型`: `兴奋`, `平静`, `轻松`, `开心`, `紧张`

Do not invent other dropdown values. If the user template has different options, follow the template.

## Core Workflow

1. **Read inputs**
   - Read the user copy, brief, reference script, and any supplied spreadsheet.
   - Preserve the user’s final wording unless the user explicitly asks to rewrite or compress.
   - If a spreadsheet already exists, study its columns, styles, dropdowns, and existing conventions before editing.
   - If the user identifies an IP, director, editor, or training case, read `references/style-memory-database.md` and only the relevant profile under `data/`.

2. **Split script into rows**
   - Default rule: one sentence or one clear speaking beat equals one shot row.
   - Keep section timing from the user when provided. If no timing exists, estimate timing from natural Chinese speaking speed and mark it clearly.
   - Do not compress copy merely to fit visuals. Only adjust copy when requested.

3. **Design each shot**
   - Decide the shot’s information role: hook, evidence, explanation, operation, comparison, transition, summary, CTA.
   - Choose material source: presenter, screen recording, provided asset, motion graphic, AI-generated keyframe, or sketch-only planning frame.
   - Write `画面描述` so an editor can build the shot without guessing: subject placement, screen area, crop/highlight target, motion start/end, and next-shot connection.

4. **Write prompts**
   - Fill prompt columns only when the row needs AI-generated image/video material.
   - Leave prompt columns empty for `录屏素材` rows and rows that use provided footage/assets only.
   - Prompts must not request readable Chinese/English text, real webpage UI, code, logos, exact brand assets, or fake screenshots.

5. **Generate sketches when useful**
   - Generate sketches only for rows with non-empty `画面描述` and non-`录屏素材` visual needs.
   - Skip `录屏素材`; real desktop recording/screenshot is the source material.
   - Use `references/v15-sketch-baseline.md` and `references/sketch-style.md` for sketch layout rules.
   - Sketches are editor-facing low-fidelity boards, not final art.
   - If the user will copy the workbook into Feishu Sheets, read `references/feishu-handoff.md`; do not rely on Excel floating images as true cell contents.

6. **Run three-role review**
   - Use `references/agent-review-rubric.md`.
   - 剪辑 agent: can an editor execute it without guessing?
   - 编导 agent: is the visual idea tied to the line and strong enough?
   - 审核 agent: does it avoid wrong aspect ratio, fake UI/text/code/logo, clutter, and polluted IP style?
   - If any role fails, revise before delivery.

7. **Update style memory when requested**
   - If the user provides finished frames, aligned script-video examples, or repeated feedback, record reusable rules in `data/`.
   - Store IP style under `data/ips/`, director preferences under `data/directors/`, editor preferences under `data/editors/`, and project learnings under `data/cases/`.
   - Store recurring mistakes under `data/mistakes/failure-patterns.md`.

## V15 Baseline

The current accepted baseline is recorded as rules in `references/v15-sketch-baseline.md`.

Use it as a quality reference for:

- 16:9 horizontal layout.
- Blank draft-paper sketch background.
- No sketching for screen-recording rows.
- Two-frame layer-evolution transition: S timeline highlight, then current icon zooms full-frame.
- Person -> generic AI input box -> Agent flow.
- Loop system map: goal input -> Agent in loop -> output.
- Low-text sketch language using icons, lines, frames, arrows, and placeholders.

Known areas for future improvement:

- Context-inflow shots should become cleaner icon-cloud compositions.
- Workbench/worksite shots should gain stronger spatial hierarchy.
- Empty-agent shots should show clearer contrast between subject and missing resources.

## References

- `references/script-table-schema.md`: required columns and per-column writing rules.
- `references/v15-sketch-baseline.md`: accepted v15 visual baseline and QA checklist.
- `references/sketch-style.md`: sketch visual style, prompt formula, and anti-AI-look rules.
- `references/feishu-handoff.md`: Feishu copy/paste handoff rules for sketch images, image packages, and HTML paste files.
- `references/style-memory-database.md`: how to read and write IP/director/editor/case memory without style pollution.
- `references/ip-profile-rules.md`: prevent one IP’s style from polluting another IP.
- `references/finished-frame-training-library.md`: optional finished-frame pattern memory.
- `references/agent-review-rubric.md`: required 剪辑/编导/审核 review standards.

## Style Memory Data

- `data/global/universal-production-rules.md`: universal production rules shared by every IP.
- `data/ips/`: IP-specific visual profiles and reusable patterns.
- `data/directors/`: director-specific storyboard preferences.
- `data/editors/`: editor-specific execution preferences.
- `data/cases/`: project case records.
- `data/mistakes/failure-patterns.md`: repeated failure patterns and fixes.

## Scripts

- `scripts/qa_sketch_prompt_csv.py`: QA sketch prompt CSV exports.
- `scripts/export_feishu_handoff.py`: export embedded sketch images, add Feishu-safe index columns, and create HTML paste files.
