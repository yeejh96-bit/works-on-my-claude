# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남

## 지금 하는 일
**없음 — v1.19.0 까지 작업이 끝났고 커밋도 마쳤다.**
새 세션은 이 파일을 이어갈 것이 아니라 아래 「끝난 일」을 기록으로만 읽으면 된다. 새 작업 요청이 오면 「할 일」을 새로 적는다.
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

## 끝난 일

> 최근 작업만 여기 남긴다. **v1.18.0 이하의 지난 기록은 `docs/CHANGELOG.md` 로 옮겼다** — 옛 결정 이유를 찾을 때는 그 파일을 본다.
> 이 절이 다시 길어지면(대략 항목 5개 이상) 오래된 것부터 같은 형식 그대로 `docs/CHANGELOG.md` 맨 위로 옮긴다.

- [x] 「끝난 일」 회전 규칙을 womc 골격에 심음 (v1.20.0)
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

- [x] 하네스 감사 지적 13건 일괄 수정 (v1.19.0)
  - 손댈 파일: `commands/womc.md`, `CLAUDE.md`, `HARNESS.md`, `README.md`, `.claude/answer-style.js`,
    `.claude/statusline.js`, `.claude/settings.local.json`, `scripts/check-sync.py`, `.claude-plugin/plugin.json`
  - 먼저 확인한 것 (`claude-code-guide` 위임): `.claude/rules/` 의 `paths` 필터 **공식 지원 맞음**,
    커스텀 서브에이전트는 CLAUDE.md **안 물려받는 게 맞음**, UserPromptSubmit 훅의 **평문 stdout 주입 유효**.
    → 감사에서 "고쳐야 한다"고 지적됐던 이 3건은 기존 서술이 옳아 **고치지 않았다**. 다시 의심되면 이 결론부터 볼 것.
  - 남긴 것 (갱신 모드 = `commands/womc.md` 「갱신 모드」 절):
    - 1번에 「덮기 전 공통 확인」 블록 신설 — agents/skills 를 덮기 전 골격인지 판정, 사용자 파일이면 건너뛰고 보고.
    - `CLAUDE.md` 덮을 때 기존 `## 설명 방식` 절을 읽어 두었다가 되돌려 놓도록 지시(말투 설정 보존). `answer-style.js` 도 같은 방식으로 문구 보존.
    - `womc:begin`/`womc:end` 를 **정확 일치가 아니라 "그 문자열이 들어 있는 줄"** 로 찾도록 명시 — 구획 중복 누적 방지.
    - 0-b 임시파일 경로를 `${TMPDIR:-${TEMP:-/tmp}}` 로 통일(`%TEMP%` 는 Git Bash 에서 안 풀림).
    - 다운그레이드 방지 단계 추가 — 프로젝트 `CLAUDE.md` 의 `womc:skeleton-version` 이 적용하려는 것보다 높으면 멈춤.
  - 남긴 것 (생성 모드·골격):
    - 생성된 `CLAUDE.md` 맨 위(H1 바로 아래)에 `<!-- womc:skeleton-version=x.y.z -->` 를 찍는다. 온보딩 병합 구획 안에도 같은 표식.
      **버전을 올릴 때 고칠 자리가 4곳이 됐다** — `commands/womc.md` 맨 위 표식, CLAUDE.md 골격 안 표식, 온보딩 구획 안 표식, `plugin.json`. (`commands/womc.md` 맨 위 주석에 적어 뒀다.)
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

- [x] v1.19.0 커밋 + `PLAN.md`·`TASKS.md` 를 git 에 포함
  - 남긴 것: 커밋 `82bc25b`(v1.19.0 수정 9개), 커밋 `ac8f105`(`PLAN.md`·`TASKS.md` 추적 시작).
    이전 판에는 "이 두 파일은 git 미포함 유지"라고 적혀 있었으나 **방침이 바뀌어 git 에 포함한다** — 앞으로 커밋에 함께 넣는다.
  - 확인 방법: `git status --short` 가 비어 있고, `git ls-files PLAN.md TASKS.md` 에 두 파일이 나온다.

## 할 일

- (없음)

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
