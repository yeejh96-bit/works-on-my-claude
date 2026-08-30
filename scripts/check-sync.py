#!/usr/bin/env python3
"""
womc 저장소 정합성 검사 (커밋 전에 한 번 돌리면 좋다).

실행:  py scripts/check-sync.py     (Windows)
       python3 scripts/check-sync.py (Mac/Linux)

검사 일곱 가지:
1) commands/womc.md 안에 박힌 "원본" 텍스트와, 이 저장소가 실제로 dogfood 하는
   라이브 파일(CLAUDE.md, settings.json, statusline.js)이 글자 그대로 일치하는지.
   (한쪽만 고쳐 조용히 어긋나는 걸 막는다.)
   에이전트·스킬·출력 스타일은 v2.0.0 부터 플러그인이 직접 제공하므로 womc.md 에 임베드하지 않는다 → 대조 대상이 아니다.
   CLAUDE.md 는 「## 프로젝트 상세」 절 앞까지만 본다(SECTION_SPLIT) — v3.1.0 부터 그 절 본문은 프로젝트마다 다른
   사용자 내용이라 글자 대조가 성립하지 않는다. 절 안쪽 소절 이름이 사라지는 건 6번(LINKED_LITERALS)이 지킨다.
2) README.md 제목 끝의 버전과 .claude-plugin/plugin.json 의 version 이 같은지.
3) womc:skeleton-version 표식이 plugin.json 의 version 과 같은지 — commands/womc.md 와 CLAUDE.md 에 있는
   **모든** 표식을 전수 검사한다. (이 표식은 /womc update 의 "옛 캐시" 판정 기준이라 어긋나면 캐시 감지가 조용히 오작동한다.
   예전에는 첫 표식 하나만 봐서, 뒤쪽 표식이 옛 버전으로 남아도 통과하는 구멍이 있었다.)
4) README.md 본문에 서브에이전트 4종 이름이 모두 등장하는지. (문서가 옛 구성에 멈춰 있는 걸 잡는다.)
5) 열린 확인(open-checks) 대조 — TASKS.md 의 열린 항목에 붙은 ID 주석과 docs/HARNESS-AUDIT.md 의
   앵커 구획 안 목록이 같은지. (한쪽만 고쳐 두 목록이 조용히 어긋나는 걸 막는다.
   ID 주석이 닫힌 항목에 남아 있는 것도 함께 잡는다.)
6) 파일 사이 문자열 결합 대조 — 「안 고른 길」·「확실하지 않은 가정」·`제약-공통.md` 파일명·그 안의 절 제목처럼
   여러 파일에 글자 그대로 같이 있어야 성립하는 이름이, 각 파일에 최소 횟수만큼 남아 있는지(LINKED_LITERALS).
   임베드 대상이 아니라 1번이 못 보는 agents/·skills/·commands/ 사이의 결합을 잡는다.
   한계: 글자만 보지 뜻은 못 보므로, 양쪽을 동시에 같은 이름으로 다듬으면 그대로 통과한다.
7) 옛 기록 배너 잔류 검사 — PLAN.md·TASKS.md 에 「⚠ … 옛 기록 …」 배너가 붙은 절이 남아 있는지.
   어떤 절이 옛 기록이 됐으면 배너를 붙여 그 자리에 두지 말고 docs/CHANGELOG.md 로 옮겨야 한다.
   (docs/CHANGELOG.md 는 옛 기록을 모으는 곳이라 대상이 아니다.)

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


# 라이브 파일 중 "여기까지만 대조한다"는 경계 (그 절부터는 프로젝트마다 내용이 달라진다)
# 값은 줄 첫머리에서 시작하는 제목 문자열이다 — 본문 안의 백틱 언급에 걸리지 않게 앞에 개행을 붙인다.
SECTION_SPLIT = {"CLAUDE.md": "\n## 프로젝트 상세"}

# womc.md 원본에 박혀 있어야 할 라이브 파일들
# (플러그인이 직접 제공하는 agents/·skills/·output-styles/ 는 임베드하지 않으므로 여기 없다)
EMBEDDED_FILES = [
    "CLAUDE.md",
    ".claude/settings.json",
    ".claude/statusline.js",
]

# 여러 파일에 "글자 그대로" 같이 있어야 성립하는 결합들
# (한쪽 이름만 다듬으면 조용히 어긋나는 자리 — 각 파일에 최소 몇 번 나와야 하는지로 적는다)
LINKED_LITERALS = [
    # 「안 고른 길」·「확실하지 않은 가정」: plan 의 출력 계약 ↔ plan-feature 3절이 그 이름으로 받는다
    # (v3.0.0. 최소치를 실측 개수로 조였다 — 아래 「끝난 것으로 보는 조건」과 같은 이유로 여유를 두지 않는다)
    ("안 고른 길", {"agents/plan.md": 3, "skills/plan-feature/SKILL.md": 4}),
    ("확실하지 않은 가정", {"agents/plan.md": 3, "skills/plan-feature/SKILL.md": 3}),
    # 제약이 사는 곳: make-rule 이 이름을 정하고 ↔ plan-feature 3절·이관 절차가 그 이름으로 찾아 적는다
    # ↔ 골격 CLAUDE.md(=commands/womc.md 임베드 사본)의 규칙도 같은 파일명을 가리킨다 (v2.13.0)
    # plan-feature 쪽은 5→3 으로 내렸다 — v3.0.0 이 그 스킬을 줄이면서 같은 파일명을 가리키던 두 자리가 사라졌다.
    (
        "제약-공통.md",
        {
            "skills/plan-feature/SKILL.md": 3,
            "skills/make-rule/SKILL.md": 1,
            "CLAUDE.md": 1,
            "commands/womc.md": 1,
        },
    ),
    # 「사용자가 닫은 것」: 안 고른 길·확정된 가정이 들어가는 절 이름 — make-rule 이 만들고 plan-feature 가 그 이름으로 적는다
    # ⚠ 실제로 그 절을 가진 파일(.claude/rules/제약-공통.md)도 함께 센다 — 안 세면 절 이름을 바꿔도 검사가 통과해
    #   다음 plan-feature 실행이 "없으면 그때 만든다"에 따라 같은 뜻의 절을 하나 더 만든다(한 사실이 두 곳으로 갈라진다).
    (
        "사용자가 닫은 것",
        {
            "skills/plan-feature/SKILL.md": 1,
            "skills/make-rule/SKILL.md": 1,
            ".claude/rules/제약-공통.md": 1,
        },
    ),
    # 짝인 「나중에 · 안 할 것」도 같은 이유로 센다 (v2.13.1)
    # plan-feature 쪽은 3→2 로 내렸다 — v3.0.0 축소로 그 이름을 부르던 한 자리가 사라졌다.
    (
        "나중에 · 안 할 것",
        {
            "skills/plan-feature/SKILL.md": 2,
            "skills/make-rule/SKILL.md": 1,
            ".claude/rules/제약-공통.md": 3,
        },
    ),
    # 「끝난 것으로 보는 조건」: plan 의 출력 → plan-feature 4절이 그 이름으로 넘김 → implement 의 입력 계약
    # (v2.6.0. 한 곳만 이름을 다듬으면 종료 조건이 조용히 안 넘어간다)
    # ⚠ 최소치는 "지금 실제 개수"로 잡는다 — 여유를 두면 v2.6.0 이 더한 자리를 통째로 지워도 옛 자리 몫으로 통과한다.
    #   (plan-feature 3회 = TASKS 템플릿 1 + 3절 1 + 4절 1. 4절은 v3.0.0 축소로 2회에서 1회가 됐다 → 최소치도 4→3.)
    (
        "끝난 것으로 보는 조건",
        {
            "agents/plan.md": 1,
            "agents/implement.md": 2,
            "skills/plan-feature/SKILL.md": 3,
        },
    ),
    # 「프로젝트 상세」 절 안쪽 소절 3종: 1번 검사가 v3.1.0 부터 그 절을 안 보게 됐으니(SECTION_SPLIT) 소절 이름은 여기서 지킨다
    # — 골격 템플릿(commands/womc.md)과 이 저장소의 라이브 CLAUDE.md 가 같은 소절 이름을 쓰는지만 센다.
    ("### 뭘 푸는가", {"CLAUDE.md": 1, "commands/womc.md": 1}),
    ("### 안 만들 것", {"CLAUDE.md": 1, "commands/womc.md": 1}),
    ("### 어디서 돌아가나 (배포)", {"CLAUDE.md": 1, "commands/womc.md": 1}),
    # 「새로 들일 것」: 감사 판정 축 ↔ /womc update 7번이 그 이름으로 사용자에게 묻는다 (v2.6.0)
    # womc.md 쪽은 1로 내렸다 — 나머지 한 자리가 HARNESS.md 템플릿 안이었는데 v3.0.0 에서 그 절을 통째로 지웠다.
    (
        "새로 들일 것",
        {"skills/harness-audit/SKILL.md": 7, "commands/womc.md": 1},
    ),
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
    split = SECTION_SPLIT.get(rel)
    if split is None:
        target, note = live, ""
    else:
        head, found, _ = live.partition(split)
        if not found:
            print(f"DRIFT  {rel} 에 「{split.strip()}」 절이 없음")
            problems.append(rel)
            continue
        # 앞부분 + 제목 줄까지만 본다 — 이렇게 붙여서 찾으면 원본 쪽도 같은 자리에서 그 절이 시작함이 함께 확인된다
        target, note = head + split, f"  (「{split.strip()}」 절 앞까지)"
    if target in src:
        print(f"OK     {rel}{note}")
    else:
        print(f"DRIFT  {rel}  (womc.md 원본과 라이브 불일치){note}")
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

# 5) 열린 확인(open-checks) 대조 — TASKS.md 의 ID 주석 ↔ docs/HARNESS-AUDIT.md 앵커 구획
#    앵커는 "정확히 그 줄"이 아니라 "그 문자열이 들어 있는 줄"로 찾는다(앵커 줄에 다른 글자가 붙어도 잡히게).
OPEN_BEGIN = "womc:open-checks:begin"
OPEN_END = "womc:open-checks:end"
open_comment_re = re.compile(r"<!--\s*open:([a-z0-9-]+)\s*-->")
open_tick_re = re.compile(r"`open:([a-z0-9-]+)`")

# 5-1) TASKS.md — HTML 주석 형태만 센다(본문의 백틱 언급은 ID 가 아니다)
tasks_ids = set()
for lineno, line in enumerate((ROOT / "TASKS.md").read_text(encoding="utf-8").splitlines(), 1):
    ids = open_comment_re.findall(line)
    if not ids:
        continue
    tasks_ids.update(ids)
    if not line.lstrip().startswith("- [ ]"):
        shown = ", ".join(f"open:{i}" for i in ids)
        print(f"DRIFT  TASKS.md:{lineno} 닫힌/보류 항목에 ID 주석이 남아 있음 ({shown})  [ID 주석은 열린 '- [ ]' 항목에만]")
        problems.append(f"open-checks:TASKS.md:{lineno}")

# 5-2) docs/HARNESS-AUDIT.md — 앵커 구획 안쪽만 센다
audit_lines = (ROOT / "docs/HARNESS-AUDIT.md").read_text(encoding="utf-8").splitlines()
begins = [i for i, line in enumerate(audit_lines) if OPEN_BEGIN in line]
ends = [i for i, line in enumerate(audit_lines) if OPEN_END in line]
audit_ids = None
if len(begins) != 1 or len(ends) != 1:
    print(
        f"DRIFT  docs/HARNESS-AUDIT.md 의 열린 확인 앵커가 짝이 안 맞음"
        f"  [begin {len(begins)}개 / end {len(ends)}개, 각각 1개여야 함]"
    )
    problems.append("open-checks anchor")
elif begins[0] > ends[0]:
    print("DRIFT  docs/HARNESS-AUDIT.md 의 열린 확인 앵커 순서가 뒤집힘 (begin 이 end 보다 뒤)")
    problems.append("open-checks anchor")
else:
    audit_ids = set(open_tick_re.findall("\n".join(audit_lines[begins[0] + 1 : ends[0]])))

# 5-3) 두 목록 대조
if audit_ids is not None:
    if tasks_ids == audit_ids:
        print(f"OK     열린 확인 ID {len(tasks_ids)}개 일치 (TASKS.md == docs/HARNESS-AUDIT.md)")
    else:
        only_tasks = sorted(tasks_ids - audit_ids)
        only_audit = sorted(audit_ids - tasks_ids)
        print("DRIFT  열린 확인 목록 불일치 (TASKS.md != docs/HARNESS-AUDIT.md)")
        print(f"       TASKS 에만: {', '.join('open:' + i for i in only_tasks) if only_tasks else '(없음)'}")
        print(f"       AUDIT 에만: {', '.join('open:' + i for i in only_audit) if only_audit else '(없음)'}")
        problems.append("open-checks")

# 6) 파일 사이 문자열 결합 대조 — 같은 이름이 양쪽에 그대로 남아 있는지
for literal, expected in LINKED_LITERALS:
    ok = True
    for rel, minimum in expected.items():
        path = ROOT / rel
        if not path.exists():
            print(f"DRIFT  {rel} 파일이 없음  [「{literal}」이 최소 {minimum}번 있어야 함]")
            problems.append(f"linked-literal:{literal}:{rel}")
            ok = False
            continue
        count = path.read_text(encoding="utf-8").count(literal)
        if count < minimum:
            print(f"DRIFT  {rel} 에 「{literal}」이 최소 {minimum}번 필요한데 {count}번")
            problems.append(f"linked-literal:{literal}:{rel}")
            ok = False
    if ok:
        where = ", ".join(f"{rel}×{n}" for rel, n in expected.items())
        print(f"OK     「{literal}」 결합 유지 ({where} 이상)")

# 7) 옛 기록 배너 잔류 검사 — 배너를 붙여 남기지 말고 docs/CHANGELOG.md 로 옮기는 게 규칙이다
#    한 줄 안에 ⚠ 와 '옛 기록' 이 함께 있을 때만 잡는다(둘 중 하나만 있는 평범한 문장은 통과).
STALE_BANNER_FILES = ["PLAN.md", "TASKS.md"]
stale_banner_hits = []
for rel in STALE_BANNER_FILES:
    path = ROOT / rel
    if not path.exists():
        continue
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "⚠" in line and "옛 기록" in line:
            print(f"DRIFT  {rel}:{lineno} 옛 기록 배너가 남아 있음  [배너로 남기지 말고 그 절을 docs/CHANGELOG.md 로 옮기세요]")
            problems.append(f"stale-banner:{rel}:{lineno}")
            stale_banner_hits.append(rel)
if not stale_banner_hits:
    print(f"OK     옛 기록 배너 없음 ({', '.join(STALE_BANNER_FILES)})")

if problems:
    print(f"\n[!] 어긋난 항목 {len(problems)}개 — 커밋 전에 맞춰 주세요.")
    sys.exit(1)
print("\n[OK] 모두 일치.")
