# Script Table Schema

Use this reference whenever you create, edit, or QA a storyboard table for this skill.

## Required Columns

Keep these columns in this order unless the user provides a stricter spreadsheet template:

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

## Dropdown Values

Only use these values unless the user's spreadsheet has a different locked dropdown.

- `景别/运镜`: `远景`, `全景`, `中景`, `近景`, `特写`
- `画面类型`: `数字/真人口播`, `AI生成素材`, `动效制作素材`, `录屏素材`
- `情绪类型`: `兴奋`, `平静`, `轻松`, `开心`, `紧张`

Do not write values such as `强调`, `认真`, `提醒`, `口播`, `素材`, `截屏`, or `动效+AI` into locked dropdown columns.

## Per-Column Rules

### 镜头/段落/时长

- If the copy has section timings, preserve them and divide rows inside the section.
- If there is no timing, estimate by natural Chinese speech rhythm.
- Default split: one sentence or one clear speaking beat per row.
- For a shot with multiple visual states, keep one row but describe states as `转场前 / 转场中 / 转场后` in `画面描述` or `备注`.

### 景别/运镜

- Pick the closest allowed value, not a custom camera term.
- Use `中景` or `近景` for presenter shots.
- Use `全景` for full interface, concept maps, timelines, and system diagrams.
- Use `特写` for a single UI control, number, icon, detail, or key visual.
- Use `远景` only when the shot needs broad spatial context.

### 画面描述

Write for an editor, not for a viewer. Include:

- main subject and its exact position;
- supporting elements and their positions;
- start and end state if there is motion;
- what gets highlighted, enlarged, masked, or replaced;
- how this shot connects to the previous or next shot.

Avoid vague phrases such as `科技感画面`, `高级一点`, `做一个转场`, or `展示 AI 概念` without concrete composition.

### 台词/旁白

- Preserve the user's final copy.
- Do not rewrite, compress, or add claims unless the user asks.
- If the row is an insert with no spoken line, leave it blank or write the exact subtitle/card text only if the template requires it.

### 画面类型

- `数字/真人口播`: presenter is the main source. If there is no asset, pure presenter is acceptable.
- `录屏素材`: desktop screen recording, website screenshot, product page, or software operation footage.
- `AI生成素材`: image/video material should be generated from prompts.
- `动效制作素材`: editor builds the visual using shapes, icons, masks, frames, type, simple transitions, or provided layers.

If a real website/software operation can be recorded, prefer `录屏素材` over fake AI UI.

### 情绪类型

Use only the five allowed values:

- `兴奋`: hook, surprising claim, strong benefit, launch moment.
- `平静`: explanation, neutral setup, tutorial steps.
- `轻松`: approachable comparison, simple guidance.
- `开心`: positive conclusion, solved problem, creator benefit.
- `紧张`: pain point, risk, failure, cost, countdown, bottleneck.

### 动效/后期花字

Describe what the editor should actually make:

- text entry and exit;
- box highlight, cursor, glow, zoom, mask, split screen, wipe, flash, freeze, line draw, icon enlarge;
- whether the presenter should stay full frame or become a corner inset;
- subtitle or punchline style when needed.

Use text animation sparingly. It should support the line, not cover the composition.

### 备注

Use this for:

- source material notes;
- screenshot/recording requirements;
- AI asset dependencies;
- sketch state labels;
- warnings such as `不要生成可读网页文字` or `录屏素材不用草图`.

### Prompt Columns

Fill prompt columns only when the row needs AI-generated material.

- `AI生成素材`: fill all four prompt columns.
- `动效制作素材`: fill prompt columns only when an AI-generated base frame is needed.
- `数字/真人口播`: usually leave prompts blank unless a generated insert/background is required.
- `录屏素材`: leave prompt columns blank.

Chinese and English prompts must describe the same visual. The English prompt is for image/video models and should be direct, concrete, and free of unneeded brand names.

Prompt safety:

- do not request readable Chinese/English text inside generated images;
- do not request exact software UI, exact webpage screenshots, exact code, exact logos, or copyrighted characters;
- use generic interface blocks, generic robot icons, generic documents, and abstract diagrams instead.

### 草图/画面

- Embed a sketch only when the row's visual needs construction and is not `录屏素材`.
- Do not add sketches to empty visual rows.
- If one shot has multiple states, place multiple horizontal subframes in the same sketch card and label them clearly.
- Every sketch must stay horizontal 16:9, even when placed inside a table cell.
- Treat Excel-embedded sketch images as local preview only. They are usually floating drawing objects, not true cell contents, and may not copy into Feishu Sheets.
- For Feishu delivery, also generate `草图文件` and `飞书复制说明` columns plus an image folder/zip or HTML paste version. Read `references/feishu-handoff.md`.
