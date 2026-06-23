from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path


path = Path(sys.argv[1])
rows = list(csv.DictReader(path.open("r", encoding="utf-8-sig")))

errors = []
types = Counter(row.get("草图类型", "") for row in rows)
for i, row in enumerate(rows, start=2):
    en = row.get("English Sketch Prompt", "")
    if re.search(r"[\u4e00-\u9fff]", en):
        errors.append((i, "english_contains_chinese"))
    for forbidden in ["Figma", "Claude", "Douyin", "GitHub", "Slack", "Jira", "Remotion"]:
        if forbidden in en:
            errors.append((i, f"english_contains_forbidden_brand:{forbidden}"))
    if any(x not in {"PASS", "FAIL"} for x in [row.get("剪辑审核"), row.get("编导审核"), row.get("风险审核")]):
        errors.append((i, "review_not_pass_fail"))
    if row.get("风险审核") == "FAIL":
        errors.append((i, "risk_fail"))
    if "real webpage content" not in en:
        errors.append((i, "missing_no_real_webpage_guard"))

print("rows=", len(rows))
print("sketch_type_counts=", dict(types))
if len(types) < 2 and len(rows) > 5:
    errors.append((0, "sketch_type_not_discriminating"))
print("errors=", errors[:50])
if errors:
    raise SystemExit(1)
