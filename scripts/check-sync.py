#!/usr/bin/env python3
"""
womc 저장소 정합성 검사 (커밋 전에 한 번 돌리면 좋다).

실행:  py scripts/check-sync.py     (Windows)
       python3 scripts/check-sync.py (Mac/Linux)

검사 두 가지:
1) commands/womc.md 안에 박힌 "원본" 텍스트와, 이 저장소가 실제로 dogfood 하는
   라이브 파일(.claude/agents/*, .claude/skills/*, CLAUDE.md, HARNESS.md, settings.json,
   statusline.js)이 글자 그대로 일치하는지. (한쪽만 고쳐 조용히 어긋나는 걸 막는다.)
2) README.md 제목 끝의 버전과 .claude-plugin/plugin.json 의 version 이 같은지.

하나라도 어긋나면 종료코드 1 로 끝난다.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s: str) -> str:
    return s.replace("\r\n", "\n").strip()


# womc.md 원본에 박혀 있어야 할 라이브 파일들
EMBEDDED_FILES = [
    "CLAUDE.md",
    "HARNESS.md",
    ".claude/agents/explore.md",
    ".claude/agents/plan.md",
    ".claude/agents/implement.md",
    ".claude/agents/verify.md",
    ".claude/agents/review.md",
    ".claude/skills/plan-feature/SKILL.md",
    ".claude/skills/make-rule/SKILL.md",
    ".claude/settings.json",
    ".claude/statusline.js",
]

problems = []

# 1) 원본 ↔ 라이브 대조
src = norm((ROOT / "commands/womc.md").read_text(encoding="utf-8"))
for rel in EMBEDDED_FILES:
    live = norm((ROOT / rel).read_text(encoding="utf-8"))
    if live in src:
        print(f"OK     {rel}")
    else:
        print(f"DRIFT  {rel}  (womc.md 원본과 라이브 불일치)")
        problems.append(rel)

# 2) README 제목 버전 ↔ plugin.json 버전
plugin_version = json.loads(
    (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
)["version"]
readme_first = (ROOT / "README.md").read_text(encoding="utf-8").splitlines()[0]
m = re.search(r"v(\d+\.\d+\.\d+)", readme_first)
readme_version = m.group(1) if m else None
if readme_version == plugin_version:
    print(f"OK     README 제목 버전 == plugin.json ({plugin_version})")
else:
    print(f"DRIFT  README 제목 버전({readme_version}) != plugin.json({plugin_version})")
    problems.append("README version")

if problems:
    print(f"\n[!] 어긋난 항목 {len(problems)}개 — 커밋 전에 맞춰 주세요.")
    sys.exit(1)
print("\n[OK] 모두 일치.")
