# V15 Sketch Baseline

This file records the accepted v15 sketch-board rules. Use this as a production baseline, not as a fixed visual style for every IP.

## Fixed Rules

- Output is horizontal 16:9.
- Sketches use a clean blank draft-paper background.
- Sketches are low-fidelity planning boards for editors, not final images.
- Do not sketch `录屏素材` rows. Website/software shots should be recorded or screenshotted from the real desktop source.
- Avoid fake readable UI, fake code, fake brand pages, exact logos, and long generated text.
- Use simple shapes, icons, lines, arrows, masks, placeholder panels, and layout blocks.
- A sketch must make the intended composition obvious in three seconds.

## Frame Count Rules

- Static/simple shot: one horizontal frame.
- Clear transition: two frames, usually `转场前 / 转场后`.
- Process or state change: three frames, usually `起点 / 变化中 / 结果`.
- Layer evolution shot: two frames are preferred:
  - first frame shows the full system/timeline and the current node highlighted;
  - second frame zooms the highlighted icon or layer to become the main full-frame visual.

## Accepted Composition Patterns

### S Timeline Evolution

Use for multi-stage model/product evolution.

- Draw a clean S-shaped path across the frame.
- Put each stage on a node with a simple icon.
- The current stage is brighter and slightly larger.
- When explaining one stage, transition to a second frame where that stage icon expands to fill most of the screen.
- Keep labels minimal. Prefer icons over text.

### Person -> Input Box -> Agent

Use for prompt/user-to-agent explanation.

- Left: simple human/presenter silhouette or avatar.
- Center: large generic AI input box, not a real app UI.
- Right: simple agent robot or workflow icon.
- Arrows show the flow from person to input box to agent.
- The input box should be visually important, not a tiny label.

### Context Inflow To Agent

Use when the copy says the AI needs context.

- Center: abstract agent robot/workspace.
- Around it: multiple recognizable input icons flying inward.
- Use icons for files, code repo, chat history, product requirement, project rules, API docs, design spec, test report, meeting note, bug ticket, data table, and calendar/task board.
- The agent can grow or glow as more context enters.
- Avoid a messy icon pile. Group inputs in arcs or lanes.

### Loop System Map

Use when explaining loop/agent execution.

- Start with a goal/input at one side.
- Place the agent inside a circular loop at center.
- The loop contains trigger, execute, verify, remember, and decide phases as icon-only nodes.
- End with output/result on the opposite side.
- Keep the loop readable and spatially balanced.

### Missing Resource / Empty Agent

Use when showing why an agent fails without tools/context/memory.

- Place the agent in the center or left.
- Surround it with empty sockets, broken links, blank file placeholders, or missing tool slots.
- Contrast it with a later state where resources plug in cleanly.

## Known Improvement Targets

Keep improving these areas in future versions:

- Context inflow shots should look like controlled icon-cloud compositions, not scattered labels.
- Workbench/worksite metaphors need stronger foreground, middle ground, and background separation.
- Empty-agent shots should show the missing resource problem more clearly.
- Multi-state cards must not become crowded; if needed, split a row into more storyboard states.

## Self-Review Checklist

Reject and revise a sketch when:

- it is vertical or contains vertical subframes;
- the editor cannot tell what is foreground, middle ground, and background;
- it uses too much text;
- it looks like a fake screenshot instead of a planning sketch;
- it includes cluttered UI/code blocks that may generate unreadable artifacts;
- the shot meaning does not match the line;
- the transition is described in text but not visible in the sketch;
- one IP's finished style has been copied into a different IP without reason.
