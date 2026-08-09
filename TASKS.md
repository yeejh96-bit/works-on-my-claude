# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남

## 지금 하는 일
**v2.0.0 — Claude Code 2.1.x 기본기능에 맞춘 하네스 간소화. 0·1·2·3단계 끝, 4단계 일부(HARNESS.md) 끝. 남은 것은 4단계(README·SPEC)와 5단계.**
전체 계획은 `C:\Users\s2\.claude\plans\glistening-squishing-nest.md` 에 있다. **내일 이어서 할 때 그 파일부터 읽는다.**
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

### 이번 작업의 근거 — 뒤집힌 전제 (가장 중요)
v1.19.0 감사에서 "커스텀 서브에이전트는 CLAUDE.md 를 **안** 물려받는 게 맞음"으로 확인해 기록했었다(아래 v1.19.0 항목).
**Claude Code 2.1.224 에서 이 명제는 거짓이다.** 공식 문서 원문:
> "Explore and Plan are the only subagents that omit CLAUDE.md and git status. Every other built-in and custom subagent loads both."

이 저장소에서 **실측으로 확인했다** — `explore` 서브에이전트를 띄워 물어보니 CLAUDE.md·SPEC.md(@import)·git status 를 전부 받고 있었다.
이 한 문장이 에이전트 보일러플레이트 ~100줄과 케이브맨 말투 5판본을 지탱하고 있었다.

### 0단계 실측 결과 (5건 — 다시 조사하지 말 것)
1. 플러그인 루트 `agents/` — 공식 플러그인 8개가 이미 사용 중(`~/.claude/plugins/marketplaces/claude-plugins-official/plugins/*/agents/`). 지원 확실.
   **`subagent_type` 값이 `explore` 인지 `womc:explore` 인지는 아직 미확인** — `/reload-plugins` 후 실사용에서 확인할 것.
2. 프로젝트 `.claude/agents/` 가 플러그인 것을 override — 문서 명시. 실측은 5단계로 미룸.
3. **플러그인이 제공한 output style 이름을 프로젝트 `settings.json` 의 `outputStyle` 이 해석하는지 — 미확인.**
   로컬에 `output-styles/` 를 쓰는 플러그인 사례가 0건이라 참고할 것이 없었다.
   → 안 되면 폴백 2가지: ① `output-styles/womc-caveman.md` 에 `force-for-plugin: true` 추가(단 "항상 켜짐"이라 사용자 결정과 어긋남 → 다시 물어야 함)
   ② 사용자가 `/config` 에서 직접 고르게 안내.
4. **커스텀 서브에이전트의 CLAUDE.md 상속 — 확정(실측).** 위 참조.
5. **소문자 `plan` 은 내장 `Plan` 을 오버라이드하지 않는다 — 확정.** 이 세션의 에이전트 목록에 소문자 `explore`/`plan` 과
   내장 `Explore`/`Plan` 이 **동시에** 떠 있었다(대소문자 구분).
   → **계획에 있던 `plan` → `design` 개명은 취소했다.** 이름 충돌이 없어 이득이 사라졌고, 고칠 곳 12군데를 아꼈다.

### 계획에서 바뀐 점 2가지 (계획 파일보다 이 기록이 최신이다)
- **`plan` → `design` 개명 취소** (위 5번).
- **`statusLine` 의 `refreshInterval` 추가 취소.** 공식 문서 확인 결과 단위가 **밀리초가 아니라 초**이고 최소값이 `1` 이다
  (계획서의 `3000` 은 50분이 된다). 몇 초마다 node 프로세스를 새로 띄우는 비용이 Windows 에서 이득보다 커서 아예 넣지 않기로 했다.
  womc 상태줄은 이벤트 기반 갱신으로 충분하다.

### 1단계에서 남긴 것 (2단계가 그대로 이어 쓴다)
**신설 — 플러그인 루트 (이제 `/womc` 가 생성하지 않고 플러그인이 직접 제공한다):**
- `agents/explore.md`(25→17줄) · `agents/plan.md`(28→21, `effort: high` 추가) · `agents/implement.md`(27→22) · `agents/verify.md`(26→20)
  - 4종 모두 언어·말투·"확인 못 함"·원문금지 줄을 지우고 **`CLAUDE.md` 「서브에이전트 보고 규약」을 따른다`** 한 줄로 대체했다.
  - 「너는 메인의 대화 이력을 못 본다」는 **남겼다** — 이건 상속되지 않는 사실이다.
- `skills/plan-feature/SKILL.md` — §6 을 `review` 위임 → **사용자에게 `/code-review` 권유**로 재작성. §5(verify)는 그대로.
- `skills/make-rule/SKILL.md` — §0 의 문체 분기를 `CLAUDE.md`+`answer-style.js` 2곳 → **출력 스타일 파일 1곳**으로.
  §2 끝에 "`paths` 스코프 규칙은 서브에이전트 전달이 보장되지 않는다" 한 줄 추가.
- `output-styles/womc-caveman.md` — 케이브맨 말투 **정본**. `keep-coding-instructions: true` **필수**(기본값 false 면 Claude Code 내장 코딩 지침이 통째로 빠진다).

**삭제:** `.claude/agents/`(5개, `review.md` 포함) · `.claude/skills/`(2개) · `.claude/answer-style.js`
→ `.claude/` 에 남은 것은 `settings.json` · `statusline.js` 둘뿐이다.

**수정:**
- `CLAUDE.md` — 「설명 방식」 15줄→2줄, 「서브에이전트 보고 규약」 6줄 신설, 「적극 위임」 재작성(위임 판단 기준 3가지 명시·5종→4종),
  「절차 지키기」에 "스킬 목록이 안 보여도 `plan-feature` 로 부른다" 보강.
- `.claude/settings.json` — `hooks` 블록 삭제, `"outputStyle": "womc-caveman"` 추가. **`deny` 7줄과 `allow` 4줄은 그대로 두었다.**

### 3단계도 끝냈다 (커밋 `7433ad6`)
1단계를 끝내니 `check-sync.py` 가 지운 파일을 찾다 죽어 커밋이 막혔다. 그래서 3단계를 앞당겨 같이 처리했다.
- `EMBEDDED_FILES` 12개 → **4개**(`CLAUDE.md`·`HARNESS.md`·`.claude/settings.json`·`.claude/statusline.js`).
- 버전 표식 검사를 `re.search` → **`re.findall` 전수 검사**로 바꾸고 대상 파일을 `VERSION_MARKER_FILES`
  (`commands/womc.md`·`CLAUDE.md`)로 뺐다. 예전에는 첫 표식 하나만 봐서 뒤쪽이 옛 버전이어도 통과하는 구멍이 있었다.
  지금 `commands/womc.md` 에 표식이 3개 있고 전부 검사된다.
- README 검사 5종 → 4종.
- **`commands/womc.md` 의 `CLAUDE.md`·`.claude/settings.json` 임베드 사본도 라이브와 똑같이 맞췄다**(안 그러면 DRIFT).
  → `commands/womc.md` 의 「설명 방식」·「서브에이전트 보고 규약」·「적극 위임」·「절차 지키기」·6번 settings 블록은 **이미 최신이다. 다시 안 고쳐도 된다.**
- 확인: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK.

**신설 `scripts/bump-version.py` 는 아직 안 만들었다** — 5단계에서 버전을 올릴 때 만들면 된다(표식 6곳 일괄 변경).

### 2단계에서 남긴 것 (4·5단계가 이어 쓴다)
**`commands/womc.md` 800줄 → 495줄.** 다음이 실제로 바뀐 자리다.

- **임베드 3구획 삭제 완료** — 에이전트 5종·스킬 2종·`answer-style.js`. 남은 임베드는 6개
  (`CLAUDE.md`·`SPEC.md`·`HARNESS.md`·`.gitignore`·`settings.json`·`statusline.js`).
  절 번호가 당겨졌다: **5) `.claude/settings.json` · 6) `.claude/statusline.js`** (예전 6·7번). 8번 절은 사라졌다.
- `allowed-tools` 에서 `WebFetch` 제거. `argument-hint` 는 `[update | eject <이름>]`, `description` 도 eject 를 언급하도록 고쳤다.
- 맨 위 버전 주석 → "버전을 올리면 `py scripts/check-sync.py` 를 돌려라"(개수를 세지 않는다).
- **사실 정정 완료** — "서브에이전트는 CLAUDE.md 를 못 물려받는다"는 문장이 저장소에서 사라졌다.
  HARNESS 임베드에는 반대로 "**서브에이전트도 이 파일을 함께 물려받는다**"가 들어갔다.
- 마무리 안내에 2줄 추가 — `.claude/` 는 보호 경로라 매번 권한을 묻는다 / 말투는 Claude Code 재시작 후 적용.
- **갱신 모드 단계 번호가 바뀌었다** — 새 **2번이 「레거시 정리」**(옛 `.claude/agents/`·`.claude/skills/`·`answer-style.js` 삭제,
  판정은 1번의 「덮기 전 공통 확인」 재사용), 예전 2번(settings 병합)은 **3번**이 됐고 그 안에서 `outputStyle` 추가와 `hooks` 제거를 다룬다.
  이후 3·4·5 → **4·5·6**. 0·0-b 와 다운그레이드 방지는 그대로 두었다.
- **신설 「꺼내기 모드 (`/womc eject <이름>`)」** — 파일 맨 끝. 서브에이전트 4종·스킬 2종·`womc-caveman` 을 프로젝트로 복사한다.
  스킬 비대칭(플러그인 스킬은 `womc:` 네임스페이스라 복사해도 둘 다 살아남음)을 안내에 적어 두었다.
- **`HARNESS.md` 는 4단계 몫이지만 여기서 같이 끝냈다** — womc.md 임베드와 라이브가 글자 그대로 같아야 해서(`check-sync.py` DRIFT) 따로 할 수 없었다.
  54줄 → **64줄**(줄어드는 대신 늘었다: 「먼저 — 이 골격은 womc 플러그인이 있어야 온전히 동작한다」 설치 2줄과
  「플러그인이 주는 것」 절이 새로 들어갔다). `/fewer-permission-prompts`·`/config` 안내 한 줄씩도 들어갔다.
  **HARNESS.md 를 다시 고칠 일이 생기면 `commands/womc.md` 임베드와 같이 고쳐야 한다.**
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK (버전은 아직 `1.20.0`).

### 남은 일 (4단계 나머지·5단계) — 이 순서대로
**커밋은 막혀 있지 않다. 검사기는 통과 상태다.** 버전은 아직 `1.20.0` 이다.

- **4단계 — 문서 (두 파일 서로 병렬 가능. `HARNESS.md` 는 위에서 이미 끝냈다)**
  - `README.md`(132→~100): **「수동 설치」 절 삭제**(이제 `commands/womc.md` 만 복사하면 반쪽 골격이라 잘못된 안내다),
    구조도·에이전트 4종 갱신, 중복 설명 압축.
  - `SPEC.md` 2·3·4항 정정: 에이전트 5종→4종, 미니 하네스 근거 정정, 말투 관리 방식 변경, 스킬 2종은 유지.
    `/womc eject` 도 3항 1번에 한 줄 넣는다(2단계에서 새로 생긴 기능이라 SPEC 에 없다).
  - 확인: 두 문서에서 `answer-style`·`review` 언급 0건.

- **5단계 — 버전 2.0.0 + 실사용 검증**
  - `scripts/bump-version.py` 를 만들어 표식 6곳(`commands/womc.md`×3·`CLAUDE.md`·`plugin.json`·`README.md` 제목)을 한 번에 올린다.
  - `marketplace.json` 설명문의 "5종"도 고친다. `PLAN.md` 버전 이력 + `TASKS.md` 「끝난 일」을 같은 작업에서 갱신한다.
  - 통과 조건 넷: ① `check-sync.py` 전 항목 OK, 버전 `2.0.0`
    ② 빈 폴더에서 `/womc` → 생성 파일이 정확히 6개(`CLAUDE.md`·`SPEC.md`·`HARNESS.md`·`.gitignore`·`.claude/settings.json`·`.claude/statusline.js`)
    ③ v1.20.0 골격 폴더 사본에서 `/womc update` → 레거시 정리되고 `SPEC.md`·`PLAN.md`·`TASKS.md`·`.claude/rules/`·사용자 추가 allow 는 전부 보존
    ④ 새 세션에서 메인 답변은 케이브맨, **서브에이전트 보고는 평문 한국어**
  - **여기서 위 0단계 실측 미확인 2건(플러그인 `subagent_type` 값, `outputStyle` 이 플러그인 스타일 이름을 해석하는지)이 함께 판명된다.**
    `outputStyle` 이 안 먹으면 폴백 2가지가 위 「0단계 실측 결과」 3번에 적혀 있다.

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

- [ ] **v2.1.0 — 하네스 감사 절차를 골격에 심는다** (v2.0.0 을 끝낸 뒤에 시작한다)
  - 왜: 지금 womc 에는 **"Claude Code 가 업데이트되면 골격이 따라 얇아지는 절차"가 없다.**
    v2.0.0 작업(Claude Code 2.1.224 에 맞춘 간소화)은 사용자가 그때그때 말해야만 시작되는 일회성 수정이었다.
    `/womc update` 도 "womc 최신판"을 가져올 뿐, Claude Code 최신 기능을 보고 골격을 줄여 주지는 않는다.
    이 항목은 그 빠진 고리를 절차로 굳히는 것이다. **v2.0.0 자체가 이 절차의 첫 실전 사례이므로, 그것을 끝낸 뒤에 만들어야 절차가 정확해진다.**
  - 손댈 파일: 신설 `skills/harness-audit/SKILL.md` · 신설 `docs/HARNESS-AUDIT.md`(감사 기록) ·
    `commands/womc.md`(골격 안내에 새 스킬 한 줄) · `README.md` · `HARNESS.md` · `SPEC.md` 3항(스킬 2종 → 3종) ·
    `scripts/check-sync.py`(새 임베드가 생기면 대조 대상 추가) · `.claude-plugin/plugin.json`
  - 이어 쓸 것 (v2.0.0 이 남기는 것):
    - 플러그인 루트 `skills/` 구조 — 새 스킬도 여기에 만든다(`.claude/skills/` 아니다).
    - v2.0.0 의 0단계 실측 결과 5건과 「계획에서 바뀐 점 2가지」 — **첫 감사 기록의 내용 그 자체**로 `docs/HARNESS-AUDIT.md` 에 옮겨 적는다.
    - `commands/womc.md` 가 임베드하는 파일이 4개로 줄어든 상태(스킬은 플러그인이 직접 제공하므로 임베드 대상이 아니다).
  - 만들 것 3가지:
    - **A. `harness-audit` 스킬** — ① `claude --version` 으로 현재 버전 확인 ② `docs/HARNESS-AUDIT.md` 에서 지난 감사 버전 읽기
      ③ 그 사이 CHANGELOG·공식 문서(`code.claude.com/docs/en/*`) 조사(`explore` 병렬 위임)
      ④ 골격 항목을 하나씩 대조해 "이제 Claude Code 기본으로 되는가" 판정 ⑤ 뺄 수 있는 것·반드시 남길 것을 **근거 URL과 함께** 보고
      ⑥ 문서에 명시 없는 것은 "실측 필요"로 따로 묶어 `TASKS.md` 에 남긴다(v2.0.0 의 0단계 스파이크가 그 견본).
    - **B. `docs/HARNESS-AUDIT.md`** — 「언제 · 어느 CC 버전 기준 · 무엇을 확인 · 무엇을 뺐나 · 무엇을 왜 남겼나」.
      다음 감사가 이걸 읽고 이어가 같은 조사를 반복하지 않게 한다. **뒤집힌 전제도 여기 적는다**
      (예: v1.19.0 의 "서브에이전트는 CLAUDE.md 를 안 물려받는다"가 2.1.224 에서 거짓이 된 일).
    - **C. `SessionStart` 훅 (선택)** — 현재 CC 버전과 마지막 감사 버전이 많이 벌어졌으면 "감사할 때 됨" 한 줄 띄움.
      Node.js 필요 → 없으면 조용히 넘어가야 한다. **A·B 를 먼저 만들고, C 는 필요하다고 판단될 때만 붙인다.**
  - 끝난 것으로 보는 조건: 빈 폴더에 `/womc` 를 깐 뒤 `harness-audit` 를 불렀을 때,
    현재 CC 버전을 스스로 알아내고 "뺄 수 있는 것 / 남길 것"을 근거 URL과 함께 보고하며, 그 결과가 `docs/HARNESS-AUDIT.md` 에 기록된다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 전 항목 OK + 실제로 스킬을 한 번 돌려 보고서가 나오는지 육안 확인.

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
