# Shot Sketch Board

中文视频分镜脚本与横屏草图生产 Skill。

它用于把文案、brief、口播稿或已有脚本表，整理成可交给编导、剪辑、后期和 AI 素材老师协作的生产表。核心产出包括分镜表、画面描述、AI 图片/视频提示词、草图索引、飞书协作交付文件。

## 适用场景

- 真人口播、数字人口播、商单视频、AI 科技解说、产品教程、模型测评、Agent / Prompt / Workflow 类内容。
- 需要把中文文案拆成镜头、段落、时长和画面方案。
- 需要给每个镜头设计画面、录屏、动效、AI 生成素材或草图。
- 需要多人协作：编导写方案，剪辑执行，AI 素材老师抽卡，审核检查风险。
- 需要把 Excel 脚本迁移到飞书表格，并避免草图图片丢失。

## 仓库结构

```text
shot-sketch-board/
  SKILL.md
  agents/
    openai.yaml
  references/
    script-table-schema.md
    sketch-style.md
    v15-sketch-baseline.md
    feishu-handoff.md
    style-memory-database.md
    agent-review-rubric.md
    ip-profile-rules.md
    finished-frame-training-library.md
  data/
    global/
    ips/_template/
    directors/_template/
    editors/_template/
    cases/_template/
    mistakes/
  scripts/
    export_feishu_handoff.py
    qa_sketch_prompt_csv.py
```

`shot-sketch-board/` 是真正的 Codex skill 文件夹。仓库根目录的 `README.md` 是给人看的说明书，不属于 skill 本体。

## 固定输出字段

默认输出表格使用这 13 列：

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

如果要交付到飞书，还会额外生成：

- `草图文件`
- `飞书复制说明`

## 下拉值限制

`景别/运镜` 只能使用：

- `远景`
- `全景`
- `中景`
- `近景`
- `特写`

`画面类型` 只能使用：

- `数字/真人口播`
- `AI生成素材`
- `动效制作素材`
- `录屏素材`

`情绪类型` 只能使用：

- `兴奋`
- `平静`
- `轻松`
- `开心`
- `紧张`

不要写 `强调`、`认真`、`提醒`、`口播`、`素材` 这类自由值。

## 核心工作流

1. 读取文案、brief、已有表格和参考素材。
2. 按句子或信息节奏拆镜头。
3. 为每个镜头设计画面：主体位置、素材来源、录屏范围、动效、转场、前后衔接。
4. 判断画面类型：口播、录屏、动效制作、AI 生成。
5. 需要 AI 生成素材时，写中英双语首帧图提示词和图生视频提示词。
6. 需要草图时，生成 16:9 横屏低保真草图。
7. 用剪辑 Agent、编导 Agent、审核 Agent 做三轮检查。
8. 如需飞书协作，生成图包、索引列和 HTML 粘贴版。

## 草图标准

- 草图是给剪辑老师看的结构图，不是最终视觉成片。
- 默认横屏 16:9。
- 背景使用空白草稿纸或白底，不做复杂科技背景。
- 只突出镜头需要表达的元素。
- 不生成可读 UI、代码、网页文字、logo、乱码。
- `录屏素材` 不生成草图，直接使用真实电脑录屏或截图。
- 一个镜头有明显转场时，要做多状态草图：`转场前 / 转场后` 或 `转场前 / 变化中 / 转场后`。

## 飞书协作说明

Excel 里的图片通常是“浮动图片对象”，看起来在单元格里，但不是真正的单元格内容。复制到飞书表格时，图片经常会丢。

所以飞书协作必须使用多件套：

- Excel 预览版
- 草图 PNG 图包
- 草图 zip
- `草图文件` 列
- `飞书复制说明` 列
- HTML 粘贴版
- 草图列 HTML 粘贴版

通用脚本：

```bash
python shot-sketch-board/scripts/export_feishu_handoff.py path/to/storyboard.xlsx --output-dir path/to/output
```

脚本会生成：

- `*_飞书迁移版.xlsx`
- `*_草图图包_飞书迁移版/`
- `*_草图图包_飞书迁移版.zip`
- `*_草图索引_飞书复制.tsv`
- `*_飞书粘贴版_图片在单元格.html`
- `*_飞书草图列粘贴版.html`

## 风格数据库

这个 skill 支持多人、多 IP 的风格沉淀。

- `data/ips/_template/profile.md`：IP 风格模板
- `data/directors/_template/profile.md`：编导偏好模板
- `data/editors/_template/profile.md`：剪辑偏好模板
- `data/cases/_template/case-record.md`：项目案例模板
- `data/mistakes/failure-patterns.md`：常见错误库

原则：不要让一个 IP 的视觉风格污染另一个 IP。每次新增成品图、参考视频或老师反馈时，只提炼可复用规则，不要把一次性的内容当成通用标准。

## 安装方式

把 `shot-sketch-board/` 文件夹复制到你的 Codex skills 目录，例如：

```text
C:\Users\<你的用户名>\.codex\skills\shot-sketch-board
```

或使用你自己的 skill installer 从 GitHub 子目录安装：

```text
jkaxuwg-design/shot-sketch-board/shot-sketch-board
```

## 使用示例

可以这样向 Codex 提需求：

```text
使用 shot-sketch-board，把这份文案拆成横屏视频分镜表，输出画面描述、画面类型、情绪类型、AI 提示词和草图方案。
```

```text
这份 Excel 是终版脚本，帮我生成飞书迁移版，草图不要丢。
```

```text
这是某个 IP 的成品图和原文案，帮我把它沉淀进风格数据库。
```

## 公开发布注意

这个公开版本只保留通用模板和规则，不包含具体账号的私有训练数据。真实 IP、编导、剪辑老师的偏好建议在自己的私有仓库或本地数据库里维护。
