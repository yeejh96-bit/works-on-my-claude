# 변경 이력 (CHANGELOG)

> `TASKS.md` 「끝난 일」에서 넘어온 과거 작업 기록이다.
> `TASKS.md` 는 최근 작업만 남기고, 오래된 항목은 여기로 옮겨 보관한다.
> 각 항목의 형식은 `TASKS.md` 와 같다 — 손댈 파일 · 남긴 것 · 확인 방법.
> 한 줄 요약만 필요하면 `PLAN.md` 의 「만든 것(버전 이력)」을 본다.

## v2.1.0 — 하네스 감사 절차를 골격에 심음 (검증까지 완료, 2026-08-10)

- ✅ **검증 통과** — 시험 폴더에서 `/womc update` 를 돌리자 7번 단계가 **사람이 부르지 않았는데** 감사를 실행했고,
    그 폴더에 `docs/HARNESS-AUDIT.md` 가 규정 형식(제목줄 + 5개 절, 근거 URL 포함)으로 새로 생겼다.
    **배운 것**: 감사는 자기 폴더의 기록만 본다 — 지난 기록이 없는 폴더에서 돌리면 이미 끝난 일을 다시 「뺄 수 있음」으로 올린다.
    결과를 옮겨 올 때 지난 기록과 대조해야 한다(`docs/HARNESS-AUDIT.md` v2.1.1 기록 3번에서 그렇게 2건을 기각했다).
  - 손댈 파일: `skills/harness-audit/SKILL.md`(신설) · `docs/HARNESS-AUDIT.md`(신설) ·
    `HARNESS.md` · `commands/womc.md` · `README.md` · `SPEC.md` · `.claude-plugin/plugin.json` · `PLAN.md` · `TASKS.md`
  - 남긴 것:
    - **신설 `skills/harness-audit/SKILL.md` (세 번째 스킬)** — 7단계 절차: ① `claude --version` + `docs/HARNESS-AUDIT.md` 로 지난 감사 버전 확인
      ② `explore` 병렬 위임으로 그 사이 변경 조사(결론마다 근거 URL 필수) ③ 골격 항목을 「뺄 수 있음 / 남길 것 / 실측 필요」 셋으로만 판정
      ④ 사용자에게 쉬운 말로 보고(파일은 안 고친다) ⑤ 「실측 필요」를 `TASKS.md` 「할 일」로 넘김 ⑥ `docs/HARNESS-AUDIT.md` 에 기록 ⑦ 실제 정리는 `plan-feature` 로 인계.
      **`.claude/skills/` 가 아니라 플러그인 루트 `skills/` 에 있다** — 이제 스킬은 플러그인이 직접 제공한다.
    - **신설 `docs/HARNESS-AUDIT.md` (감사 기록부)** — 첫 기록이 v2.0.0 이다. 형식 고정:
      제목줄 「어느 womc 버전 — 언제 / 어느 Claude Code 버전 기준」 + 절 5개(1.무엇을 확인했나 · 2.뒤집힌 전제 · 3.무엇을 뺐나 · 4.무엇을 왜 남겼나 · 5.실측 필요).
      맨 위 인용문에 「마지막 감사 기준 버전」(지금 Claude Code `2.1.224`)과 「실측 필요 목록이 몇 번 절인지」를 적어 둔다. **최신 기록이 맨 위다.**
      → **v2.0.0 의 미확인 2건(`subagent_type` 이름 · 플러그인 출력 스타일을 `outputStyle` 이 해석하는지)이 이 파일 5번 절에 "열려 있음"으로 옮겨졌다.**
        확인되면 그 자리를 「확인됨」으로 고치고 인용문의 기준 버전도 올린다.
    - **`commands/womc.md` 갱신 모드에 7번 단계 「하네스 감사 (자동)」 신설** — `/womc update` 가 끝나면 곧바로
      `docs/HARNESS-AUDIT.md` 의 마지막 감사 버전과 `claude --version` 을 대조해, 벌어져 있으면 `harness-audit` 를 **그 자리에서 실행**한다.
      사용자가 스킬을 따로 부르지 않아도 "플러그인 업데이트 → `/womc update` → 하네스 점검"이 한 흐름으로 이어진다.
      **「뺄 수 있음」이 나와도 파일을 바로 지우지 않고 한 번 묻는다**(골격 삭제는 되돌리기 번거롭고 근거가 틀리면 세팅이 깨진다).
      스킬이 없거나 실행이 안 되면 **조용히 건너뛰고 갱신 자체는 성공**으로 끝낸다 — 감사 때문에 갱신이 실패하면 안 된다.
    - **`SessionStart` 훅(원래 계획의 C안)은 안 만들었다** — `/womc update` 가 감사를 자동으로 부르게 되어 알림 훅의 이득이 더 줄었다.
      이유는 `PLAN.md` 「나중에 / 안 할 것」에 적어 뒀다.
    - **`harness-audit` 2단계의 조사 위임이 도구와 안 맞던 것을 고쳤다** — 웹 조사(공식 문서·CHANGELOG)는 `general-purpose` 에 위임한다.
      `explore` 는 `tools: Read, Grep, Glob` 뿐이라 웹을 못 본다(`agents/explore.md`). 로컬 파일 조사만 `explore` 몫이다.
      로컬 경로도 womc 저장소 기준에서 **사용자 프로젝트 기준**으로 고쳤다 — 이 스킬은 남의 프로젝트에서 돌기 때문이다.
    - 문서 6자리에 스킬 2종 → **3종** 반영: `HARNESS.md`(플러그인이 주는 것 절) · `commands/womc.md`(같은 절의 임베드 사본, **글자 그대로 같아야 한다**) ·
      `commands/womc.md` 꺼내기 모드 목록 · `README.md` 2곳 · `SPEC.md` 3항 4번.
    - `scripts/check-sync.py` 는 **안 고쳤다** — 스킬은 `commands/womc.md` 에 임베드되지 않아(플러그인이 직접 제공) 대조 대상이 아니다. 다음에도 스킬을 늘릴 때 이 스크립트는 안 건드려도 된다.
    - 버전은 `py scripts/bump-version.py 2.1.0` 한 줄로 6곳을 올렸다(수동으로 세지 말 것).
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.1.0`.
    스킬이 실제로 도는지는 사람이 새 세션에서 확인한다(위 「지금 하는 일」의 ⑤).

## v2.0.0 — Claude Code 2.1.x 기본기능에 맞춘 하네스 간소화 (검증까지 완료, 2026-08-10)

- ✅ **검증 3건 통과** — ① 빈 폴더에서 `/womc` → 생성 파일 정확히 6개(레거시 0개).
    ② v1.20.0 골격 사본에서 `/womc update` → 레거시 8개 삭제, 사용자 파일(`SPEC.md`·`PLAN.md`·`TASKS.md`·`.claude/rules/`·추가 allow) 전부 보존,
    **본문만 고친 `.claude/agents/verify.md` 는 「사용자가 고친 것」으로 판정해 남겼다**(판정 기준을 넓힐 필요 없음). ③ 말투는 `TASKS.md` 「끝난 일」의 v2.1.1 항목 참조.
  - 손댈 파일: `agents/`(신설 4) · `skills/`(신설 2) · `output-styles/womc-caveman.md`(신설) · `commands/womc.md` ·
    `CLAUDE.md` · `HARNESS.md` · `SPEC.md` · `README.md` · `.claude/settings.json` · `scripts/check-sync.py` ·
    `scripts/bump-version.py`(신설) · `.claude-plugin/plugin.json`. **삭제**: `.claude/agents/`(5) · `.claude/skills/`(2) · `.claude/answer-style.js`.
  - **뒤집힌 전제 (이 작업 전체의 근거 — 다시 의심하지 말 것)**: v1.19.0 에 "커스텀 서브에이전트는 CLAUDE.md 를 **안** 물려받는다"고
    기록해 뒀으나 Claude Code 2.1.224 에서 **거짓**이다. 공식 문서: "Explore and Plan are the only subagents that omit
    CLAUDE.md and git status. Every other built-in and custom subagent loads both." 이 저장소에서 `explore` 를 띄워 **실측 확인**했다.
    이 한 문장이 에이전트 보일러플레이트 ~100줄과 케이브맨 말투 5판본을 지탱하고 있었다.
  - **0단계 실측 5건 (다시 조사하지 말 것)**:
    ① 플러그인 루트 `agents/` 지원 확실(공식 플러그인 8개가 사용 중) — 단 `subagent_type` 값이 `explore` 인지 `womc:explore` 인지는 **미확인**.
    ② 프로젝트 `.claude/agents/` 가 플러그인 것을 override — 문서 명시.
    ③ 플러그인이 준 output style 이름을 `settings.json` 의 `outputStyle` 이 해석하는지 — **미확인**(참고할 사례가 0건이었다).
    ④ 커스텀 서브에이전트의 CLAUDE.md 상속 — **확정**(위 참조).
    ⑤ 소문자 `plan` 은 내장 `Plan` 을 오버라이드하지 않는다 — **확정**(대소문자 구분, 둘이 동시에 떠 있었다).
  - **계획에서 취소한 것 2가지**: `plan`→`design` 개명(이름 충돌이 없어 이득 없음, 고칠 곳 12군데 절약) ·
    `statusLine` 의 `refreshInterval`(단위가 초·최소 1이라 몇 초마다 node 를 새로 띄우게 됨 — 비용이 이득보다 크다).
  - 남긴 것:
    - **서브에이전트·스킬·말투를 플러그인 루트로 옮겼다.** 이제 `/womc` 가 복사하지 않는다 → 골격 생성물 11개 → **6개**.
      에이전트 4종은 공통 규칙을 지우고 "`CLAUDE.md` 「서브에이전트 보고 규약」을 따른다" 한 줄로 대체(상속되므로).
      「너는 메인의 대화 이력을 못 본다」만 남겼다 — 이건 상속되지 않는 사실이다.
    - **`review` 에이전트 폐지** → Claude Code 기본 `/code-review` 권유. `plan-feature` §6 도 그렇게 재작성.
    - **말투는 출력 스타일 `output-styles/womc-caveman.md` 한 곳**. `keep-coding-instructions: true` **필수**
      (기본값 false 면 Claude Code 내장 코딩 지침이 통째로 빠진다). `settings.json` 의 `hooks` 삭제 + `outputStyle` 추가.
    - `commands/womc.md` **800줄 → 495줄**. 임베드 6개(`CLAUDE.md`·`SPEC.md`·`HARNESS.md`·`.gitignore`·`settings.json`·`statusline.js`)만 남았다.
    - **신설 `/womc eject <이름>`** — 플러그인이 주는 정의를 프로젝트로 꺼낸다. 스킬만 비대칭(플러그인 스킬은 `womc:` 이름표라 꺼내도 둘 다 살아남는다).
    - **신설 `scripts/bump-version.py`** — 표식 6곳 일괄 변경. `--dry-run` 지원. `VERSION_MARKER_FILES` 는 `check-sync.py` 와 같은 값을 유지한다.
    - `check-sync.py`: `EMBEDDED_FILES` 12→4개, 버전 표식을 `re.findall` **전수 검사**로(예전엔 첫 표식만 봐서 뒤쪽이 옛 버전이어도 통과했다), README 검사 5종→4종.
    - **HARNESS.md 를 고칠 때는 `commands/womc.md` 임베드 사본도 같이 고쳐야 한다** — 글자 그대로 같지 않으면 `check-sync.py` 가 DRIFT 로 잡는다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.0.0`.
    나머지 3건(빈 폴더 생성 · `update` 보존 · 말투)은 사람이 새 세션에서 확인한다.

## v1.20.0 — 「끝난 일」 회전 규칙을 womc 골격에 심음

- 손댈 파일: `.claude/skills/plan-feature/SKILL.md`, `commands/womc.md`, `CLAUDE.md`,
  `.claude-plugin/plugin.json`, `README.md`
- 남긴 것:
  - 골격의 `TASKS.md` 템플릿 「끝난 일」 절에 인용문 2줄 추가 — 항목 5개 초과 시 오래된 것부터
    `docs/CHANGELOG.md` 로 옮기고(없으면 그때 생성), 형식은 그대로 두고 위치만 옮긴다.
  - `plan-feature` 스킬 「4. 구현」 절 끝에 같은 취지 한 줄 추가(구현 후 TASKS 를 갱신하는 그 자리에서 회전을 판단하게).
  - 두 문구는 `.claude/skills/plan-feature/SKILL.md` 와 `commands/womc.md` 임베드 사본에 **글자 그대로 같이** 들어간다.
    한쪽만 고치면 `check-sync.py` 가 DRIFT 로 잡는다.
  - **버전 표식이 4곳이 아니라 5곳이었다** — `commands/womc.md` 맨 위 주석·CLAUDE.md 템플릿 안·온보딩 구획 안·
    `plugin.json` 에 더해 **저장소 자신의 `CLAUDE.md` 첫 줄 표식**도 올려야 `check-sync.py` 가 통과한다.
    (`README.md` 제목 버전까지 세면 6곳.) `commands/womc.md` 맨 위 주석의 "4곳" 안내는 이 점에서 부정확하다 — 다음에 손볼 때 고칠 것.
  - `commands/womc.md` 의 갱신 모드 설명문에 나오는 `womc:skeleton-version` 언급 3곳은 값을 비교하라는 지시문이라 숫자를 박지 않는다 — 건드리지 않았다.
  - `docs/` 폴더는 골격이 만들지 않는다. 회전이 처음 일어날 때 만든다.
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `1.20.0` 통과.

## v1.19.0 — 하네스 감사 지적 13건 일괄 수정

- 손댈 파일: `commands/womc.md`, `CLAUDE.md`, `HARNESS.md`, `README.md`, `.claude/answer-style.js`,
  `.claude/statusline.js`, `.claude/settings.local.json`, `scripts/check-sync.py`, `.claude-plugin/plugin.json`
- 먼저 확인한 것 (`claude-code-guide` 위임): `.claude/rules/` 의 `paths` 필터 **공식 지원 맞음**,
  커스텀 서브에이전트는 CLAUDE.md **안 물려받는 게 맞음**, UserPromptSubmit 훅의 **평문 stdout 주입 유효**.
  → 감사에서 "고쳐야 한다"고 지적됐던 이 3건은 기존 서술이 옳아 **고치지 않았다**. 다시 의심되면 이 결론부터 볼 것.
  **단, 가운데 항목은 v2.0.0 에서 거짓으로 판명됐다** — 커스텀 서브에이전트는 CLAUDE.md 를 **물려받는다**(이 파일 위쪽 v2.0.0 항목 참고).
- 남긴 것 (갱신 모드 = `commands/womc.md` 「갱신 모드」 절):
  - 1번에 「덮기 전 공통 확인」 블록 신설 — agents/skills 를 덮기 전 골격인지 판정, 사용자 파일이면 건너뛰고 보고.
  - `CLAUDE.md` 덮을 때 기존 `## 설명 방식` 절을 읽어 두었다가 되돌려 놓도록 지시(말투 설정 보존). `answer-style.js` 도 같은 방식으로 문구 보존.
  - `womc:begin`/`womc:end` 를 **정확 일치가 아니라 "그 문자열이 들어 있는 줄"** 로 찾도록 명시 — 구획 중복 누적 방지.
  - 0-b 임시파일 경로를 `${TMPDIR:-${TEMP:-/tmp}}` 로 통일(`%TEMP%` 는 Git Bash 에서 안 풀림).
  - 다운그레이드 방지 단계 추가 — 프로젝트 `CLAUDE.md` 의 `womc:skeleton-version` 이 적용하려는 것보다 높으면 멈춤.
- 남긴 것 (생성 모드·골격):
  - 생성된 `CLAUDE.md` 맨 위(H1 바로 아래)에 `<!-- womc:skeleton-version=x.y.z -->` 를 찍는다. 온보딩 병합 구획 안에도 같은 표식.
    **버전을 올릴 때 고칠 자리가 4곳이 됐다** — `commands/womc.md` 맨 위 표식, CLAUDE.md 골격 안 표식, 온보딩 구획 안 표식, `plugin.json`. (`commands/womc.md` 맨 위 주석에 적어 뒀다.)
    **v2.0.0 부터는 `scripts/bump-version.py` 가 6곳을 한 번에 올린다 — 손으로 세지 말 것.**
  - 생성 끝에 `git rev-parse --git-dir` 로 저장소 여부 확인 → 아니면 `git init` 을 **묻는다**(자동 실행 안 함).
  - 온보딩 CLAUDE.md 병합 템플릿에서 "지시문이 본문에 섞여 들어가던" 형태를 《여기》 자리표시자 + 별도 설명으로 정리.
- 남긴 것 (저장소 자체):
  - `settings.local.json` 의 `PowerShell(git *)` 를 동사별로 분리(파괴적 git 명령 무프롬프트 통과 차단) + `py scripts/check-sync.py` 허용 추가.
  - `scripts/check-sync.py` 에 검사 3개 추가: `.claude/answer-style.js` 를 `EMBEDDED_FILES` 에 포함,
    `womc.md` 골격 버전 표식 ↔ `plugin.json` 대조, README 에 서브에이전트 5종이 모두 등장하는지.
  - `CLAUDE.md` 「세션을 이어서 하기」의 "세션 시작 시 PLAN/TASKS 를 먼저 읽는다" → **"필요할 때만 읽는다"** 로 변경.
    (매 세션 무조건 읽으면 import 안 한 의미가 없어 always-on 과 같아진다.)
  - `.claude/answer-style.js` 출력을 6줄 → 1줄 핵심으로 축소. 전체 규칙은 CLAUDE.md 에만 두고 훅은 짧게 유지(파일 주석에 그 이유를 적어 뒀다).
  - `.claude/statusline.js` 의 `statusline-debug.json` 기록 코드 2곳 제거(rate_limits 없는 환경에서 상태줄 갱신마다 홈에 파일을 계속 쓰던 디버그 잔재).
  - `HARNESS.md`·`README.md` 사실관계 정정 — "읽기 전용 4종은 실수로도 못 고침"(verify·review 는 Bash 보유),
    ".env 차단이 서브에이전트에도 적용"(Bash 로는 뚫림), README 의 에이전트 2종 → 5종, "verify 는 haiku"(실제 sonnet), statusline.js 누락.
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 15항목 전부 OK, 버전 `1.19.0` 통과.
  추가로 `node .claude/answer-style.js`·`node .claude/statusline.js` 직접 실행해 정상 출력 확인,
  `~/.claude/statusline-debug.json` 의 mtime 이 실행 시각보다 앞선 것으로 재기록 안 됨을 확인.
  (`.claude/answer-style.js` 는 v2.0.0 에서 삭제됐다 — 말투는 출력 스타일이 맡는다.)

## v1.19.0 커밋 + `PLAN.md`·`TASKS.md` 를 git 에 포함

- 남긴 것: 커밋 `82bc25b`(v1.19.0 수정 9개), 커밋 `ac8f105`(`PLAN.md`·`TASKS.md` 추적 시작).
  이전 판에는 "이 두 파일은 git 미포함 유지"라고 적혀 있었으나 **방침이 바뀌어 git 에 포함한다** — 앞으로 커밋에 함께 넣는다.
- 확인 방법: `git status --short` 가 비어 있고, `git ls-files PLAN.md TASKS.md` 에 두 파일이 나온다.

## v1.18.0 — 버전 올릴 때 PLAN/TASKS 동반 갱신 규칙 + 답변에서 줄번호 표기 폐지

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`,
  `.claude/skills/plan-feature/SKILL.md`, `.claude-plugin/plugin.json`, `README.md`
- 남긴 것:
  - `CLAUDE.md` 「세션을 이어서 하기」에 "버전을 올리는 작업이면 PLAN/TASKS 도 함께 갱신" 규칙 추가.
    같은 문구가 `commands/womc.md` 의 CLAUDE.md 템플릿에도 글자 그대로 들어감.
  - `plan-feature` 스킬 「작은 변경」 항목에 **예외** 하위 불릿 추가 — 버전 변경이면 크기 무관하게 PLAN/TASKS 갱신.
    이게 v1.13~1.17 동안 기록이 멈춰 있던 원인을 막는 장치다.
  - `CLAUDE.md` 「설명 방식」에 "파일은 이름만, 줄번호 안 붙임" 규칙 추가 + `.claude/answer-style.js` 의 출력 배열에도 같은 줄 추가
    (훅이 매 입력마다 재주입하도록). 서브에이전트 5종의 `파일경로:줄번호` 보고 프로토콜은 그대로 뒀다 —
    메인이 사용자에게 옮길 때만 줄번호를 뗀다.
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `1.18.0` 통과.

## v1.17.0 — 케이브맨 단일 강제 (4단계 폐지)

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`, `HARNESS.md`, `SPEC.md`, `README.md`,
  `.claude/skills/make-rule/SKILL.md`, `.claude/skills/plan-feature/SKILL.md`, `scripts/check-sync.py`
- 남긴 것: `womc:brevity=` 표식·약하게/보통/최소 정의·강도 전환 안내 전부 삭제.
  `.claude/answer-style.js` 는 `RULES` 객체·`readLevel()` 제거하고 고정 `RULE` 문자열 하나로 단순화(CLAUDE.md 안 읽음).
  `scripts/check-sync.py` 의 `womc:brevity=` 정규화 로직도 같이 제거(더 이상 값이 달라질 일이 없어서).
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `1.17.0` 통과.

## v1.17.0 — 대화 답변 「지우지 않는 것」 목록에서 파일경로:줄번호 삭제

(위 항목과 같은 커밋)

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`
- 남긴 것: 목록에서 "파일 경로와 `경로:줄번호`" 만 뺌. 서브에이전트(`explore`/`plan`/`implement`/`verify`/`review`) 보고 프로토콜의
  `파일경로:줄번호` 관례는 별개 시스템이라 그대로 둠 — 손대지 않았다.
- 확인 방법: `py scripts/check-sync.py` 전부 OK

## v1.16.0 — 케이브맨 문장 종결 명사형 강제

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`
- 남긴 것: "-다"·"-이다"·"-한다"·"-했다" 서술형 어미 금지, 명사형(-음/-ㅁ) 또는 명사만 남기고 끝내는 규칙 + 견본 3개 추가.
- 확인 방법: 세 파일에 같은 규칙 문구가 글자 그대로 들어갔는지 육안 대조(당시엔 `check-sync.py` 실행 안 함).

## v1.15.0 이전 (상세 기록 없음)

이 세 버전은 `TASKS.md` 가 갱신되지 않던 시기의 작업이라 단계별 기록이 남아 있지 않다.
한 줄 요약만 `PLAN.md` 의 버전 이력에 있으며, 상세는 각 커밋의 diff 를 본다.

- v1.15.0 — `/womc update` 가 플러그인 자체도 갱신. (커밋 `686d1a2`)
- v1.14.0 — `/womc update` 가 옛 캐시를 스스로 우회. (커밋 `07ae551`)
- v1.13.0 — 답변 말투 강제 훅(`.claude/answer-style.js`) + `/womc update` 옛 캐시 차단. (커밋 `822a34d`)
- v1.12.0 — 케이브맨 말투를 womc 의 기본 문체로.
