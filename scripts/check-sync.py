#!/usr/bin/env python3
"""
womc 저장소 정합성 검사 (커밋 전에 한 번 돌리면 좋다).

실행:  py scripts/check-sync.py     (Windows)
       python3 scripts/check-sync.py (Mac/Linux)

검사 네 가지:
1) commands/womc.md 안에 박힌 "원본" 텍스트와, 이 저장소가 실제로 dogfood 하는
   라이브 파일(CLAUDE.md, HARNESS.md, settings.json, statusline.js)이 글자 그대로 일치하는지.
   (한쪽만 고쳐 조용히 어긋나는 걸 막는다.)
   에이전트·스킬·출력 스타일은 v2.0.0 부터 플러그인이 직접 제공하므로 womc.md 에 임베드하지 않는다 → 대조 대상이 아니다.
2) README.md 제목 끝의 버전과 .claude-plugin/plugin.json 의 version 이 같은지.
3) womc:skeleton-version 표식이 plugin.json 의 version 과 같은지 — commands/womc.md 와 CLAUDE.md 에 있는
   **모든** 표식을 전수 검사한다. (이 표식은 /womc update 의 "옛 캐시" 판정 기준이라 어긋나면 캐시 감지가 조용히 오작동한다.
   예전에는 첫 표식 하나만 봐서, 뒤쪽 표식이 옛 버전으로 남아도 통과하는 구멍이 있었다.)
4) README.md 본문에 서브에이전트 4종 이름이 모두 등장하는지. (문서가 옛 구성에 멈춰 있는 걸 잡는다.)

하나라도 어긋나면 종료코드 1 로 끝난다.
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent


def norm(s: str) -> str:
    return s.replace("\r\n", "\n").strip()


# womc.md 원본에 박혀 있어야 할 라이브 파일들
# (플러그인이 직접 제공하는 agents/·skills/·output-styles/ 는 임베드하지 않으므로 여기 없다)
EMBEDDED_FILES = [
    "CLAUDE.md",
    "HARNESS.md",
    ".claude/settings.json",
    ".claude/statusline.js",
]

# 버전 표식(womc:skeleton-version=x.y.z)이 들어 있는 파일들 — 전수 검사한다
VERSION_MARKER_FILES = [
    "commands/womc.md",
    "CLAUDE.md",
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

# 3) 골격 버전 표식 ↔ plugin.json 버전 (모든 표식을 전수 검사)
total_markers = 0
for rel in VERSION_MARKER_FILES:
    text = (ROOT / rel).read_text(encoding="utf-8")
    found = re.findall(r"womc:skeleton-version=(\d+\.\d+\.\d+)", text)
    if not found:
        print(f"DRIFT  {rel} 에 womc:skeleton-version 표식이 없음")
        problems.append(f"skeleton-version:{rel}")
        continue
    total_markers += len(found)
    stale = sorted({v for v in found if v != plugin_version})
    if stale:
        print(
            f"DRIFT  {rel} 의 골격 버전 표식 {', '.join(stale)} != plugin.json({plugin_version})"
            f"  [표식 {len(found)}개 중 어긋남]"
        )
        problems.append(f"skeleton-version:{rel}")
    else:
        print(f"OK     {rel} 의 골격 버전 표식 {len(found)}개 모두 == plugin.json ({plugin_version})")

# 4) README 본문에 서브에이전트 4종이 모두 언급되는지
readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
missing = [a for a in ("explore", "plan", "implement", "verify") if a not in readme_text]
if not missing:
    print("OK     README 에 서브에이전트 4종 모두 등장")
else:
    print(f"DRIFT  README 에 빠진 서브에이전트: {', '.join(missing)}")
    problems.append("README agents")

if problems:
    print(f"\n[!] 어긋난 항목 {len(problems)}개 — 커밋 전에 맞춰 주세요.")
    sys.exit(1)
print("\n[OK] 모두 일치.")
