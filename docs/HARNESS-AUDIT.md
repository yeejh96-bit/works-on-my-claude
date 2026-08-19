# 하네스 감사 기록부 (HARNESS-AUDIT)

> `harness-audit` 스킬이 매번 읽고 이어 쓰는 기록부다. 골격에서 **걷어낸** 이력(이제 Claude Code 기본이거나
> 지금 모델이 알아서 하는 것)과 **새로 들인** 이력(그 사이 생긴 기능 중 골격이 쓸 만한 것)을 함께 남긴다.
> 다음 감사는 **맨 위 기록의 「마지막 감사 기준 버전」·「마지막 감사 기준 모델」부터** 시작하고, 같은 조사를 반복하지 않는다.
> **감사 본체는 둘 중 하나만 달라도 돈다 — Claude Code 앞 두 자리(`major.minor`) 또는 모델.** (v2.6.0 에서 모델 트리거를 더했다.)
> 맨 위 기록의 **마지막 감사 기준 버전**: Claude Code `2.1.234` (2026-08-18).
> 맨 위 기록의 **마지막 감사 기준 모델**: `Opus 5`.
> 맨 위 기록의 **실측 필요(미확인) 목록**은 아래 v2.7.0 기록의 6번을 본다.
> **③에서 파생됐던 열린 확인(`open:allow-cleanup`)도 2026-08-11 에 통과·닫혔다** — 남은 열린 확인은 아래 목록을 본다.
> ③의 결론(골격에서 `allow` 4줄을 뺄 수 있다)은 **v2.2.0 으로 실행됐다 (2026-08-10).**

<!-- womc:open-checks:begin -->
> **다음 감사가 먼저 볼 것 — 열린 확인 3건**
> (정본은 `TASKS.md` 「할 일」. 조건·확인 방법을 여기 베껴 적지 않는다.)
> - `open:env-deny-redirect` — 입력 리다이렉션(`cat < .env` 류)이 골격의 `.env` deny 를 우회하는지 (파생 자리: v2.7.0 기록 6번①)
> - `open:delegation-vs-preset` — 하네스가 Opus 5 에 심는 「Agent tool 을 시키지 마라」와 womc 「적극 위임」 중 어느 쪽이 이기는지 (파생 자리: v2.7.0 기록 6번②)
> - `open:eject-outputstyle` — `/womc eject womc-plain` 으로 꺼낸 출력 스타일이 접두 없는 이름(`womc-plain`)으로 등록되는지 (파생 자리: v2.8.0 `/code-review` 지적 ⑦)
> **다음 감사는 이 항목들을 새 「실측 필요」로 다시 만들지 말고 `TASKS.md` 의 해당 항목을 갱신한다.**
> (2026-08-18 v2.7.0 감사에서 그 앞의 열린 확인 4건이 **전부 닫혔다** — 결론은 아래 v2.7.0 기록 5번.
> **닫힌 ID 를 이 구획에 백틱으로 남기지 말 것** — 대조 스크립트가 열린 것으로 센다.)
<!-- womc:open-checks:end -->

## v2.7.0 — 2026-08-18 / Claude Code `2.1.234` · 모델 `Opus 5` 기준

### 1. 무엇을 확인했나
- **`/womc update` 7번 단계가 자동으로 부른 감사다** — 사람이 따로 부르지 않았다.
- **모델 축으로 처음 훑은 감사다.** Claude Code 앞 두 자리는 같았고(`2.1.228` → `2.1.234`),
  지난 기록에 기준 모델이 없어(모름 → 다름) 트리거가 성립했다. v2.6.0 이 만든 모델 트리거의 첫 실행이다.
- 조사 분담: 웹 2갈래는 `general-purpose`(ⓐ Opus 5 프롬프팅 문서와 골격 대조 / ⓑ CHANGELOG 훑기 + 열린 확인 4건),
  로컬 1갈래는 `explore`.
- 골격 파일 4개(`CLAUDE.md`·`HARNESS.md`·`.claude/statusline.js`·`.claude/settings.json`)가
  갱신 전 최신 `2.6.0` 판과 **글자 그대로 일치**했다.
- 열린 확인 4건의 답을 전부 얻었다 — **4건 모두 닫혔다**(아래 5번).

### 2. 뒤집힌 전제 — **있음. 이번 감사의 가장 큰 수확이다.**

**① 「구현이 끝나면 검증 단계를 돈다」가 지금 모델에서 역효과다.**
- 근거 원문: "Claude Opus 5 verifies its own work without being told to. If your prompt contains explicit
  verification instructions ... remove them: instructions like these cause over-verification on Claude Opus 5,
  and removing them reduces wasted tokens with no loss in quality.
  **The same applies to legacy harness scaffolding that adds separate verification steps.**"
  및 "do not use subagents to verify or double-check your own work"
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- womc 의 「구현 → 검증」 고정 흐름이 바로 그 legacy harness scaffolding 에 해당한다. 아래 3번에서 걷어냈다.

**② 하네스가 Opus 5 에 「Agent tool 을 시키지 않으면 부르지 마라」를 심는다 — 전제가 뒤집힌 게 아니라 남길 이유가 강해졌다.**
- 근거 원문: "**`claude_code` preset**: when the model is Opus 5, Claude Code adds a line to its system prompt
  telling Claude not to call the Agent tool unless it's asked to." https://code.claude.com/docs/en/agent-sdk/subagents
- 즉 womc 의 「적극 위임」은 **모델 기본과 겹치는 잉여가 아니라 하네스 기본을 상쇄하는 규칙**이다.
  지금까지 「그냥 좋은 습관」으로 보이던 것이 사실은 **없으면 위임 자체가 안 도는 규칙**이었다.
  다만 어느 쪽이 실제로 이기는지는 못 봤다 → 아래 6번②.

### 3. 무엇을 뺐나 (근거)
- **매번 도는 검증 단계** — 근거는 위 2번①. 네 자리를 고쳤다:
  - `CLAUDE.md` 「절차 지키기」의 "검증을 건너뛰고 다음으로 가자고 하면 ... 한 번 권한다" 줄 **삭제**.
  - `CLAUDE.md` 「적극 위임」의 "동작 검증은 `verify` 에" 를 **「고정 단계 아님」으로 교체**.
  - `skills/plan-feature/SKILL.md` 5절을 **「동작 확인 (고정 단계 아님 — 필요할 때만)」으로 교체**.
  - `agents/verify.md` 의 `description` 을 **조건부로 좁힘**(부를 조건이 맞을 때만 걸리게).
- **`verify` 에이전트 자체는 남겼다.** 테스트·실행 로그를 메인 대화에서 떼어내는 값은 모델과 무관하게 유효하다.
  **뺀 것은 「매번 돈다」는 강제이지 도구가 아니다.**

### 4. 무엇을 새로 들였나 (근거)
- **골격 파일을 바꿔야 하는 신기능은 `2.1.228`~`2.1.234` 구간에 없었다.**
- 대신 `HARNESS.md` 에 **사실 2줄**을 더했다(골격 동작이 아니라 「무엇이 안 막히는가」를 적는 자리다):
  - ⓐ `Read` deny 가 Claude Code **`2.1.228` 부터 파일 쓰기까지 함께 막는다** — 원문 "v2.1.228 or later on writes".
    골격이 손댈 것 없이 구멍이 메워진 건이다. https://code.claude.com/docs/en/permissions
  - ⓑ PowerShell 규칙은 **별칭까지 정규화해 잡지만**("A rule written for the cmdlet name also matches its aliases"),
    **Python·Node 스크립트처럼 프로그램이 대신 읽고 쓰는 것은 못 막는다**
    ("arbitrary subprocesses that read or write files indirectly"). 같은 URL

### 5. 무엇을 왜 남겼나
- **「적극 위임」** — 위 2번②. 하네스가 심는 「부르지 마라」 줄을 상쇄한다.
  문턱값(파일 3개·긴 로그·독립 갈래 2개)도 공식 권장과 같은 방향이다:
  "Do not delegate work you can finish yourself in a handful of tool calls."
- **「한 번에 한 기능만」·「범위를 넓히지 마라」류** — 공식이 권하는 대응책 그 자체다:
  "Claude Opus 5 can also expand the scope of a task ... For narrow tasks, constrain scope explicitly."
- **「필요한 만큼만 보여준다」** — 잉여이기는커녕 **강화 대상**이다:
  "Claude Opus 5's default user-facing responses run longer than prior Opus models'. ...
  To control response length, prompt for it explicitly."
- **「확실하지 않으면 되묻지 말고 먼저 조사」** — 공식이 덧붙이라고 권하는 지시다:
  "Make routine judgment calls yourself, and check in only when different readings of the request
  would lead to materially different work."
- **서브에이전트 보고 규약** — 도구 출력 격리는 하네스가 보장하지만 **최종 메시지의 길이·형식은 지시로만 잡힌다.**
- **`PLAN.md`·`TASKS.md` 파일 방식** — Claude Code `2.1.233` 에서 "Todo/task-tracking tools no longer available on newer models".
  **세션 간 작업 이어가기의 유일한 수단이 됐다**(v2.1.1 기록 5번⑤ 의 판정이 이걸로 더 굳었다).
- **`.claude/statusline.js`** — 모델명·컨텍스트·5시간/주간 한도를 스크립트 없이 보여주는 내장 수단이 문서에 없다.
- **서브에이전트 fork 기본값 켜짐(`2.1.232`)은 채택하지 않았다** — fork 는 부모 컨텍스트를 통째로 물려받아,
  토큰 절약이 목적인 4종과 방향이 반대다.

**열린 확인 4건 — 전부 닫혔다.**
- `open:statusline-v2` → **닫음(기각).** `/statusline`·`subagentStatusLine` 둘 다 실재하나 골격을 대체하지 않는다.
  `subagentStatusLine` 은 서브에이전트 패널의 **행 모양**이고 기본 행이 이미 이름·설명·토큰수를 보여준다.
  `/statusline` 은 `~/.claude/` **전역**에 스크립트를 생성해 주는 명령이라 프로젝트별 고정 산출물인 골격과 역할이 다르다
  (오히려 골격 설정을 덮어쓸 위험). https://code.claude.com/docs/en/statusline
- `open:outputstyle-force-plugin` → **닫음(문서 확인 후 기각).** `force-for-plugin: true` 는 실재한다.
  그러나 문서가 "**Overrides the user's `outputStyle` setting**" 이라고 못박아, womc 플러그인이 켜진 **모든** 프로젝트에
  원시인 말투가 강제된다. womc 는 "이 프로젝트에서만" 이 설계이므로 **`settings.json` 한 줄 유지가 맞다.**
  https://code.claude.com/docs/en/output-styles
- `open:ask-gate` → **닫음(통과).** "Rules are evaluated in order: **deny, then ask, then allow.**" +
  "a matching ask rule prompts even when a more specific allow rule also matches the same call."
  「항상 허용」은 `settings.local.json` 에 allow 로 저장되므로 **`ask` 목록은 눌러도 다시 묻는다.**
  `PowerShell(...)` 표기도 문서에 정식 기재다(`:*` 접미사 = 뒤 ` *`). https://code.claude.com/docs/en/permissions
- `open:audit-open-notice` → **닫음(통과).** 이번 실행에서 **버전이 안 올라간 상태로도** `/womc update` 가
  열린 확인 4건을 사용자에게 한 줄씩 알렸다(2026-08-18 실측).

### 6. 실측 필요 — **새로 2건**
① **입력 리다이렉션이 `.env` deny 를 우회하는지** — Claude Code `2.1.232` 가 Bash 입력 리다이렉션을 권한 검사 대상에
   넣었다가 `2.1.233` 에서 되돌렸다("Reverted 2.1.232 Bash permission changes for Cygwin symlinks and input redirections").
   **`cat < .env` 류가 골격의 `.env` deny 를 지금 우회하는지 확인 못 함.**
   확인 방법: 아무 프로젝트에 더미 `.env` 를 두고 Bash 로 `cat < .env` 를 시켜 차단되는지 본다.
   우회되면 `HARNESS.md` 의 한계 설명을 고친다.
   → 열린 확인 `open:env-deny-redirect` (정본: `TASKS.md` 「할 일」)
② **「적극 위임」과 하네스 프리셋 중 어느 쪽이 이기는지** — 하네스가 Opus 5 세션에 심는
   「Agent tool 을 시키지 않으면 부르지 마라」 줄과 womc 「적극 위임」이 정면으로 맞선다(위 2번②).
   **어느 쪽이 이기는지, 실제 위임률이 어떤지 확인 못 함.**
   확인 방법: 파일 3개 이상을 뒤져야 하는 작업을 새 세션에서 시켜 `explore` 가 실제로 불리는지 관찰한다.
   안 불리면 「적극 위임」 문구를 더 강하게 쓰거나 `plan-feature` 에 명시적 위임 지시를 넣는다.
   → 열린 확인 `open:delegation-vs-preset` (정본: `TASKS.md` 「할 일」)

## v2.2.4 — 2026-08-12 / Claude Code `2.1.228` 기준

### 1. 무엇을 확인했나
- **`/womc update` 7번 단계가 자동으로 부른 감사다** — 사람이 따로 부르지 않았다.
- 지난 감사 기준(`2.1.226`)부터 현재(`2.1.228`)까지의 CHANGELOG 를 훑고,
  골격이 손으로 떠안고 있는 8항목을 공식 문서와 대조했다 — 상태줄 · `.env` 차단 · `allow` 목록 ·
  서브에이전트 4종 · `CLAUDE.md` 상속 · `outputStyle` · `.claude/rules/` · `PLAN.md`·`TASKS.md`.
- 조사 분담: 웹(공식 문서·CHANGELOG)은 `general-purpose`, 로컬 실태는 메인이 직접 확인했다 —
  골격 파일 5개가 최신 `2.2.4` 판과 **글자 그대로 일치**했다.

### 2. 뒤집힌 전제
- **없음.** 지난 기록의 전제 8개가 이번 문서 대조에서 모두 그대로 유효했다.

### 3. 무엇을 뺐나 (근거)
- **뺀 것 없음.** `2.1.226`~`2.1.228` 구간에 골격 8항목과 맞닿는 변경이 CHANGELOG 에 기재되지 않았다.
  근거: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

### 4. 무엇을 왜 남겼나
- **상태줄 스크립트** — 상태줄은 여전히 「사용자가 설정한 셸 스크립트를 실행하는 바」이고 기본 상태줄이 대체하지 않는다.
  `rate_limits.five_hour`·`seven_day` 는 스크립트에 넘어오는 입력 필드일 뿐 자동 표시가 아니다. https://code.claude.com/docs/en/statusline
- **`.env` 읽기 차단** — 문서의 `Read(./.env)` 는 예시 deny 규칙일 뿐, 기본 차단이라는 기재가 없다. https://code.claude.com/docs/en/settings
- **`allow` 빈 목록** — 읽기 전용 파일 접근은 무승인이고, Bash 의 내장 읽기전용 명령 집합은 모든 모드에서 무프롬프트라
  allow 를 채울 이유가 없다(정책 유지). https://code.claude.com/docs/en/permissions#read-only-commands
- **서브에이전트 4종** — 기본 제공에 `implement`·`verify` 대응이 없다. `explore`·`plan` 은 이름이 겹치지만
  같은 이름의 프로젝트 에이전트가 내장을 덮어쓰며 `model` 을 유지하므로 haiku 지정을 살리려면 남긴다. https://code.claude.com/docs/en/sub-agents
- **`CLAUDE.md` 상속** — 내장 Explore·Plan 만 `CLAUDE.md` 를 건너뛰고 그 밖의 내장·커스텀 서브에이전트는 모두 읽는다
  (SPEC 기술 그대로 유효). https://code.claude.com/docs/en/sub-agents
- **`outputStyle`** — 설정 자체는 현역이고 폐기 예고가 없다(폐기된 것은 `/output-style` **명령** 쪽으로 v2.1.91 에 이미 제거됨). https://code.claude.com/docs/en/output-styles
- **`.claude/rules/`** — 자동 인식 유지. `paths` 없으면 시작 시 로드, 있으면 매칭 파일 접근 시 로드. https://code.claude.com/docs/en/memory
- **`PLAN.md`·`TASKS.md`** — 플랜 모드는 세션 내 승인 흐름일 뿐 계획을 파일로 남겨 세션을 잇는 기능이 아니다.
  auto memory 는 Claude 가 스스로 남기는 학습 노트라 사용자 주도 작업 대장을 대신하지 못한다. https://code.claude.com/docs/en/memory

### 5. 실측 필요
- ~~**새로 하나 나왔다** — 출력 스타일 프론트매터 `force-for-plugin: true` 로 플러그인 스타일을 강제 적용할 수 있다.~~
  → **확인됨 (v2.7.0 에서 기각으로 닫혔다, 2026-08-18).** 기능은 실재하지만 문서가
  "Overrides the user's `outputStyle` setting" 이라고 못박아 **womc 가 켜진 모든 프로젝트에 말투가 강제된다.**
  "이 프로젝트에서만" 이 womc 설계이므로 골격 `settings.json` 의 `outputStyle` 한 줄은 그대로 둔다.
  판정 전문은 위 v2.7.0 기록 5번. https://code.claude.com/docs/en/output-styles
- **지난 열린 확인 2건은 그대로 열려 있다.**
  → `open:statusline-v2` · `open:audit-open-notice` (정본: `TASKS.md` 「할 일」)
- **확인 못 한 것 2건**:
  `2.1.226` 의 세부 수정 내역(CHANGELOG 가 "Bug fixes and reliability improvements" 한 줄뿐) ·
  기본 permissions deny 목록의 존재 여부(문서에 서술 자체가 없어 없다고 단정할 근거도 못 찾음).

## v2.1.1 — 2026-08-10 / Claude Code `2.1.226` 기준

> **이 기록은 다른 폴더에서 돌아간 감사를 옮겨 온 것이다.** `TASKS.md` 조건 ③ 을 검증하려고 만든
> 시험 폴더(`womc-old-test`, v1.20.0 골격 사본)에서 `/womc update` 를 돌렸고, 그 7번 단계가
> **사람이 부르지 않았는데 스스로** 감사를 실행했다. 조건 ⑤ 가 이걸로 통과했다.
> 그 폴더에는 지난 기록이 없어 감사가 **「첫 감사」로 처리**됐다 — 그래서 이미 끝난 일을 다시
> 「뺄 수 있음」으로 올린 항목이 섞여 있다. 아래 3번에서 그걸 가려냈다.
> **여기서 배운 것**: 감사는 자기 폴더의 `docs/HARNESS-AUDIT.md` 만 본다. 남의 폴더에서 돌리면
> 기억이 없는 상태로 판단하므로, 결과를 옮겨 올 때 반드시 지난 기록과 대조해야 한다.

### 1. 무엇을 확인했나
- 골격이 손으로 떠안고 있는 9가지를 공식 문서와 대조했다 — 상태줄 · `.env` 차단 · `allow` 목록 ·
  서브에이전트 4종 · `CLAUDE.md` 상속 · `outputStyle` · `.claude/rules/` · `PLAN.md`·`TASKS.md` · `/code-review` 대체.
- 조사 분담은 스킬 규정대로였다 — 웹(공식 문서·CHANGELOG)은 `general-purpose`, 로컬 실태는 `explore`.
- 지난 v2.1.0 기록의 「실측 필요」 4건 중 ①이 이번에 닫혔다(아래 2번).

### 2. 뒤집힌 전제
**① 「`outputStyle` 값 문제는 아직 미확인」 → 닫혔다. v2.1.1 의 A안이 실제로 먹는다.**
- 근거(실측): 이 저장소 세션의 메인 답변이 **원시인 말투로 나왔다.** `.claude/settings.json:2` 의 값은 `"womc:womc-caveman"`.
- 근거(실측): 시험 폴더 갱신 결과에도 `"womc:womc-caveman"` 이 들어갔다 — 갱신 모드 3번의 자동 교정이 동작한다.
- 근거(실측): `womc:explore` 서브에이전트를 띄웠더니 보고가 **평문 한국어**였다 — 출력 스타일은 서브에이전트에
  상속되지 않고, 보고 형식은 `CLAUDE.md` 「서브에이전트 보고 규약」이 담당한다는 설계가 그대로 확인됐다.
→ v2.1.0 기록 5번①은 **「확인됨」으로 닫는다.** (B·C안은 채택하지 않았다. B안은 5번②에 보류로 남아 있다.)

**② 「`/output-style` 명령으로 말투를 바꾼다」 → 그 명령은 사라졌다.**
- 근거: https://code.claude.com/docs/en/output-styles — v2.1.73 deprecated, v2.1.91 제거.
  이제 `/config` → Output style 이거나 설정 파일 직접 편집이다.
- 영향: 문서에서 `/output-style` 을 안내하는 자리가 있으면 `/config` 로 고쳐야 한다. **현재 골격에는 없다**(확인함).

**③ 「진행상태는 파일로만 관리할 수 있다」 → 내장 대체물이 생겼다.**
- 근거: https://code.claude.com/docs/en/tools-reference · https://code.claude.com/docs/en/agent-sdk/todo-tracking
- `TodoWrite` 는 v2.1.142 부터 기본 비활성이고, `TaskCreate`/`TaskUpdate`/`TaskGet`/`TaskList` 와 `/tasks` 로 대체됐다.
  이 태스크 목록은 **세션을 다시 켜도 유지된다.**

### 3. 무엇을 뺐나 (근거)
**이번에도 골격 파일은 한 줄도 고치지 않았다.** 아래는 판정과, 그중 **기각한 것**이다.

**기각 2건 — 감사가 기억 없이 돌아 생긴 중복이다.**
- ~~「서브에이전트 정의 안의 하네스 보일러플레이트를 뺄 수 있다」~~ → **이미 v2.0.0 에서 뺐다.**
  지금 `agents/` 4종은 공통 규칙 자리에 "`CLAUDE.md` 「서브에이전트 보고 규약」을 따른다" 한 줄만 있다. 뺄 것이 없다.
- ~~「커스텀 `explore`·`plan` 을 내장 `Explore`·`Plan` 으로 대체할 수 있다」~~ → **v2.1.0 감사가 같은 지적을 이미 기각했다.**
  플러그인 스코프의 `womc:explore` 는 내장 `Explore` 를 덮지 않고 **별개 이름으로 공존**하며 자기 `model: haiku` 를 그대로 쓴다
  (v2.0.0 실측). 내장 `Explore` 는 `CLAUDE.md` 를 안 물려받지만 `womc:explore` 는 물려받는다는 차이도 있다 —
  「서브에이전트 보고 규약」이 상속되는 것이 womc 설계의 전제이므로, 바꾸면 보고 형식이 깨진다.

**남은 판정 1건 → 기각됨 (2026-08-10 실측).**
- ~~**`TASKS.md` 의 체크박스 추적(`[ ]`/`[~]`/`[x]`)** — 내장 Task 도구가 세션을 넘어 유지되므로 중복이다.~~
  **전제가 틀렸다.** 내장 Task 목록은 **세션을 넘어 유지되지 않는다** — 실측 결과는 아래 5번⑤ 참조.
  `TASKS.md` 체크박스는 그대로 남긴다.

### 4. 무엇을 왜 남겼나
지난 기록과 판정이 같다. 근거 URL 만 새로 확인했다.
- `.claude/statusline.js` + `statusLine` — 기본 상태줄이 없다. 쓰는 필드(`context_window.*`·`rate_limits.five_hour`·
  `rate_limits.seven_day`)가 전부 실재한다. https://code.claude.com/docs/en/statusline
- `permissions.deny` 의 `.env` 7줄 — `.env` **읽기**는 기본 차단이 아니다. 기본 보호는 **쓰기**에만 걸리고
  그 목록에 `.env` 가 없다. https://code.claude.com/docs/en/permissions
- `.claude/rules/` + `paths` 프론트매터 — 공식 기능이고 글롭 스코프도 지원한다.
  **새로 확인한 주의점**: 경로 스코프 규칙은 `/compact` 뒤 자동 재주입되지 않고, 해당 파일을 다시 읽을 때 재로드된다.
  https://code.claude.com/docs/en/memory
- 서브에이전트 `implement`·`verify` — 구현·검증 역할의 내장 대응물이 없다. https://code.claude.com/docs/en/sub-agents
- `PLAN.md` — plan mode 는 계획을 파일로 남기지 않는다. 세션·PC 를 넘는 인수인계는 대체물이 없다.
- `outputStyle` 설정 — 기능도 키도 유효하다(위 2번①에서 실측).

**새로 챙길 만한 것 2가지** (빼는 게 아니라 **더할 것**. 둘 다 아직 안 넣었다):
- **`subagentStatusLine`** (v2.1.205+) — 서브에이전트 패널 행을 따로 꾸밀 수 있다. https://code.claude.com/docs/en/statusline
- **`/statusline`** 명령이 상태줄 스크립트를 자동 생성해 준다. 골격이 `statusline.js` 를 손으로 들고 갈 필요가 줄 수 있다. 같은 URL

> **이후 이력 — 2026-08-11: 위 2가지를 「급하지 않음」으로 내렸다.** 지금 `.claude/statusline.js` 가 잘 돌고 있어
> 급할 이유가 없다. 상태줄을 손볼 일이 생겼을 때 함께 판단한다.
> → 열린 확인 `open:statusline-v2` (정본: `TASKS.md` 「할 일」 — 조건·확인 방법은 거기 한 곳에만 있다).

### 5. 실측 필요 — **5건 전부 닫혔고, ③에서 파생됐던 열린 확인 1건(`open:allow-cleanup`)도 2026-08-11 에 닫혔다.**
①~④ 는 v2.1.0 기록에서 그대로 이월된 것이고, ⑤ 가 이번에 새로 생겼다.
닫힌 것: ①(확인됨) · ②(2026-08-11 「보류」) · ③(확인됨 — 뺄 수 있음 → v2.2.0 으로 실행) · ④(불필요) · ⑤(확인됨 — 유지).
파생 확인의 결과는 ③의 「이후 이력 ②」에 있다 — 갱신 모드 청소는 **실제로 돈다**(2026-08-11 실측).

① ~~`outputStyle` 을 어떻게 고칠 것인가~~ → **확인됨 (위 2번①).** A안으로 해결됐다.
② ~~**`force-for-plugin: true` 가 이 판(2.1.226)에서 실제로 먹는지**~~ → **「보류」다 (2026-08-11).**
   A안으로 해결됐으므로 실측할 이유가 없다. "프로젝트마다 `outputStyle` 을 박지 않게" 하고 싶어질 때
   **새 항목으로 다시 연다** — `TASKS.md` 에서도 같은 이유로 **`[-]` 보류로 내렸다**(「할 일」의 「닫힌 것 · 보류」 소절).
   다시 열 때의 확인 방법은 그 항목에 보관돼 있다.
③ ~~**`permissions.allow` 의 PowerShell 4줄이 필요한지**~~ →
   **확인됨: 필요 없다 (2026-08-10 실측). 골격에서 4줄을 뺄 수 있다.**
   문서는 내장 read-only 자동 허용을 **Bash 만** 명시하지만(https://code.claude.com/docs/en/permissions#read-only-commands),
   같은 절의 예외 목록에 「The same check applies to PowerShell tool commands」가 나온다 — 실측이 그 정황과 일치했다.
   **실측 조건**: 프로젝트 `.claude/settings.json` 의 `allow` 4줄을 지워 `"allow": []` 로 만들고,
   같은 것을 갖고 있던 `.claude/settings.local.json` 의 3줄(`git status*`/`diff*`/`log*`)도 함께 지웠다.
   사용자 설정 `~/.claude/settings.json` 의 `"defaultMode": "auto"` 는 분류기가 대신 승인해 결과를 오염시키므로,
   프로젝트 설정에 `"defaultMode": "default"` 를 임시로 넣어 덮었다(프로젝트가 사용자 설정을 이긴다).
   **실측**: 상태바가 `⏸ manual mode on` 인 상태에서 `git status` · `Get-ChildItem` 을 실행 → **둘 다 권한 프롬프트가 뜨지 않았다.**
   (1차 시도는 도중에 사용자가 auto 로 바꿔 무효였고, manual 로 되돌려 다시 측정한 값이다.)
   **판정의 범위**: "실사용에서 프롬프트가 안 뜬다"까지가 확인된 것이다. 그것이 내장 자동 허용 때문인지
   샌드박스 실행 때문인지는 갈라내지 못했다 — 어느 쪽이든 골격에 4줄을 박을 이유가 없다는 결론은 같다.
   → 실제로 빼는 일은 이 감사가 하지 않는다. `TASKS.md` 「할 일」로 넘겼다(`.claude/settings.json` 과
   `commands/womc.md` 5번 절 임베드를 **함께** 고쳐야 한다 — 한쪽만 고치면 `check-sync.py` 가 DRIFT 로 잡는다).
   측정에 쓴 두 설정 파일은 백업으로 **원상 복구했다.**

   > **이후 이력 ①  — 2026-08-10: v2.2.0 으로 실제로 뺐다.** 골격 `allow` 는 빈 배열이 됐고,
   > 갱신 모드 3번에 **옛 4줄만 골라 지우는 청소 분기**를 넣었다(사용자가 넣은 다른 항목은 안 건드린다).
   > 자세한 내용은 `TASKS.md` 「끝난 일」의 v2.2.0 항목.
   >
   > **이후 이력 ② — 여기서 파생됐던 열린 확인 `open:allow-cleanup` 은 2026-08-11 에 통과·닫혔다.**
   > 옛 골격(`1.20.0`)이 깔린 `ax` 폴더에서 플러그인 `2.2.1` + 재시작 뒤 `/womc update` 를 돌렸더니
   > **옛 4줄만 사라지고, 미리 넣어 둔 사용자 항목 `Bash(npm test:*)` 는 남았다.** 청소 분기가 실제로 돈다.
   > 자세한 것은 `TASKS.md` 「지금 하는 일」의 2026-08-11 항목.
   >
   > **다만 같은 갱신에서 `CLAUDE.md` 쪽 버그 2건이 새로 드러났다** — 사용자가 덧붙인 절이 통째로 지워지는 것과,
   > 「설명 방식」 절이 옛 골격에 영구히 묶이는 것. 둘 다 `TASKS.md` 「할 일」 → 「그 밖의 할 일」에 있다.
④ ~~**`/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지**~~ →
   **불필요해졌다 (2026-08-10).** ③이 "필요 없음"으로 나왔으므로 대체할 대상 자체가 사라졌다.
   allow 목록을 다시 늘리고 싶어질 때만 꺼낸다.
   **확인 방법(보관)**: 골격을 깐 폴더에서 한 번 돌리고 `allow` 에 PowerShell 읽기 전용 명령이 실제로 추가되는지 본다.
⑤ ~~**내장 Task 도구(`TaskCreate`/`/tasks`)가 `TASKS.md` 체크박스를 실제로 대체하는지**~~ →
   **확인됨: 대체 못 한다 (2026-08-10 실측).** 내장 Task 목록은 **세션용**이다.
   **실측**: 세션 A 에서 `TaskCreate` 로 항목 1개를 만들고 Claude Code 를 껐다 켠 뒤, 새 세션에서
   `TaskList` → `No tasks found`, 사용자가 `/tasks` 로 본 화면도 빈 목록이었다.
   (그 사이 `/clear` 도 한 번 실행됐으므로 소실 원인이 재시작인지 `/clear` 인지는 구분되지 않는다 —
   둘 중 무엇이든 **세션을 넘겨 인수인계할 수 없다**는 결론은 같다.)
   → `TASKS.md` 체크박스와 「손댈 파일·이어 쓸 것·완료 조건·확인 방법」 서술을 **전부 그대로 유지한다.**
   위 3번의 「뺄 수 있음」 판정은 이것으로 기각됐다.

## v2.1.0 — 2026-08-10 / Claude Code `2.1.226` 기준

> `/womc update` 의 7번 단계(하네스 감사 자동 실행)가 처음으로 스스로 돌아간 기록이다.
> 다만 이 세션의 스킬 목록은 옛 캐시(2.0.0) 판이라 `womc:harness-audit` 이름이 안 잡혔고,
> `skills/harness-audit/SKILL.md` 절차를 직접 읽어 수행했다. 다음 세션(재시작 후)부터는 이름으로 잡힌다.

### 1. 무엇을 확인했나
- Claude Code `2.1.224` → `2.1.226` 사이의 공식 CHANGELOG 전수(3판).
- 공식 문서 `code.claude.com/docs/en/` 의 sub-agents · output-styles · plugins-reference · settings · permissions · statusline.
- 지난 기록에 **「실측 필요」로 열려 있던 2건**의 답 (아래 2번 — 둘 다 판명됐다).
- 골격 파일 4종(`CLAUDE.md`·`HARNESS.md`·`.claude/settings.json`·`.claude/statusline.js`)이
  2.1.0 골격 원문과 글자 그대로 같은지 — **전부 동일**(로컬 재스캔은 이 대조로 갈음했다).

### 2. 뒤집힌 전제 — **골격에 실제 버그가 있었다**
`.claude/settings.json` 의 `"outputStyle": "womc-caveman"` 은 **아무 스타일과도 매칭되지 않는다.**
플러그인이 제공하는 출력 스타일은 레지스트리에 `플러그인명:이름` 형태(`womc:womc-caveman`)로 등록되고,
조회는 **키 정확일치**로만 이뤄진다(정규화 단계가 콜론을 제거하지 않는다).
- 근거(문서): 플러그인 컴포넌트는 플러그인 이름으로 네임스페이스된다 — https://code.claude.com/docs/en/plugins-reference
- 근거(실측): 설치 바이너리 `~/.local/share/claude/versions/2.1.226` 에서 플러그인 스타일 등록명이
  `` `${플러그인명}:${name}` `` (`source:"plugin"`), 조회는 `e[o]??null` 로 정확일치.
- 근거(실측): **이 세션 자체** — settings.json 에 값이 들어 있는데도 메인 답변에 원시인 말투가 적용되지 않았다.
  경고도 뜨지 않아 조용히 실패한다.
→ v1.20.0 이후 지금까지 **케이브맨 말투는 한 번도 켜진 적이 없다.** 아래 5번의 고치는 길 3가지를 본다.

### 3. 무엇을 뺐나 (근거)
**이번 감사에서 뺀 것은 없다.** 파일은 한 줄도 고치지 않았다(감사는 기록까지만 한다).
뺄 수 있다고 판정된 것 1건은 아래이며, 실제 정리는 `plan-feature` 로 넘긴다.
- **골격 `.claude/settings.json` 의 `outputStyle` 줄** — 출력 스타일 frontmatter 에
  `force-for-plugin: true` 를 넣으면 프로젝트마다 이름을 박을 필요가 없어진다.
  문서 원문: "Plugin output styles only: apply this style automatically whenever the plugin is enabled,
  without requiring users to select it. Overrides the user's `outputStyle` setting."
  근거: https://code.claude.com/docs/en/output-styles
  **다만 "womc 가 켜진 모든 프로젝트에 강제 적용"이 되어 사용자 선택권이 사라진다** — 그래서 자동으로 넣지 않았다.

**2.1.224→2.1.226 구간에서 골격을 줄일 수 있는 변경은 없었다.** 세 판의 항목은 self-hosted runner ·
SendMessage · Remote Control · 인증/샌드박스 버그수정뿐이고, 서브에이전트·출력스타일·스킬·permissions·statusLine
관련 항목은 0건이다. 근거: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### 4. 무엇을 왜 남겼나
- **`permissions.deny` 의 `.env` 차단 7줄** — 기본 제공이 아니다. 문서의 `Read(./.env)` 류는 전부
  사용자가 직접 쓰는 **예시**이고 기본 deny 세트는 없다. 근거: https://code.claude.com/docs/en/permissions
- **`.claude/statusline.js`** — 기본 상태줄이 없다. 문서: "The status line is a customizable bar ...
  that runs any shell script you configure". 5시간·주간 한도는 stdin JSON(`rate_limits.five_hour`/`seven_day`)으로
  **데이터만** 오고 표시는 스크립트 몫이다. 근거: https://code.claude.com/docs/en/statusline
- **서브에이전트 `implement`·`verify`** — 내장 목록(Explore·Plan·general-purpose·claude·statusline-setup·claude-code-guide)에
  구현 전담·검증 전담이 없다. 근거: https://code.claude.com/docs/en/sub-agents
- **스킬 3종** — 번들 스킬은 `/code-review`·`/security-review`·`/fewer-permission-prompts`·`/init`·`/simplify` 계열이고,
  기능 기획→PLAN/TASKS 관리 · 규칙 생성 · 하네스 감사에 해당하는 내장이 없다. 근거: https://code.claude.com/docs/en/skills
- **"출력 스타일은 서브에이전트에 적용되지 않는다"·"서브에이전트도 CLAUDE.md 를 물려받는다(내장 Explore·Plan 만 예외)"**
  — 문서와 여전히 일치. 두 문장 다 그대로 둔다.

**기각한 지적 1건**: 조사원이 "`womc:explore` 의 `model: haiku` 는 이미 무효"라고 보고했으나 **틀렸다.**
근거로 든 문서 문장은 *user/project 스코프에서 `Explore` 라는 이름을 쓴 경우* 이야기다. 플러그인 스코프의
`womc:explore` 는 내장 `Explore` 를 덮지 않고 **별개 이름으로 공존**하며(v2.0.0 감사에서 실측 확인), 자기 `model` 을 그대로 쓴다.

### 5. 실측 필요 — **4건 중 ①은 「확인됨」으로 닫혔다 (2026-08-10, 위 v2.1.1 기록 2번①). ②~④는 v2.1.1 기록 5번으로 이월했다.**
① ~~**`.claude/settings.json` 의 `outputStyle` 을 어떻게 고칠 것인가**~~ → **확인됨: A안을 적용했고 실제로 말투가 켜졌다.**
   (아래 세 갈래는 판단 근거로 남긴다.) 길이 셋이고 각각 대가가 다르다:
   (A) 골격 값을 `"womc:womc-caveman"` 으로 — 가장 작은 수정. 단 플러그인 이름이 바뀌면 깨진다.
   (B) `output-styles/womc-caveman.md` 에 `force-for-plugin: true` — settings.json 의 `outputStyle` 줄 자체가 불필요해진다.
       단 womc 가 켜진 **모든** 프로젝트에 강제 적용되고 사용자의 `outputStyle` 을 덮어쓴다.
   (C) `/womc` 가 스타일 파일을 프로젝트 `.claude/output-styles/` 로 복사 — 현재 값 그대로 해석된다.
       단 SPEC 의 "말투 규칙은 한 곳에만" 원칙과 어긋난다.
   **확인 방법**: 셋 중 하나를 적용하고 Claude Code 를 껐다 켠 뒤, 메인 답변이 원시인 말투로 나오는지 육안 확인.
② **`force-for-plugin: true` 가 이 판(2.1.226)에서 실제로 먹는지** — 문서에는 있으나 CHANGELOG 에 도입 항목을 못 찾았다.
   ①의 (B) 를 고르기 전에 반드시 실제로 켜 보고 확인한다.
③ **`permissions.allow` 의 PowerShell 4줄(`git status`/`diff`/`log`, `Get-ChildItem`)이 필요한지** —
   문서는 내장 read-only 자동 허용을 **Bash 만** 명시하고 PowerShell 절에는 언급이 없다.
   **확인 방법**: Windows 에서 그 4줄을 지운 뒤 `git status` 를 시켜 권한 프롬프트가 뜨는지 본다. 안 뜨면 4줄을 뺄 수 있다.
   근거: https://code.claude.com/docs/en/permissions#read-only-commands
④ **`/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지** — 이 번들 스킬이 프로젝트 settings.json 에
   allowlist 를 자동 추가한다. ③이 "필요하다"로 나올 때, 골격에 박는 대신 이 스킬로 넘겨도 되는지 판단하려면 한 번 돌려 봐야 한다.

## v2.0.0 — 2026-08 / Claude Code `2.1.224` 기준

### 1. 무엇을 확인했나
- 커스텀 서브에이전트의 `CLAUDE.md`·SPEC(`@import`)·git status 상속 여부.
- 플러그인 루트 `agents/` 지원 여부와 프로젝트 `.claude/agents/` 의 override 관계.
- `statusLine` 설정의 `refreshInterval` 단위.
- 소문자 서브에이전트 이름이 내장 에이전트를 오버라이드하는지.
- **확정된 실측 3건**: 플러그인 루트 `agents/` 지원 확실(공식 플러그인 8개가 이미 사용 중,
  `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/*/agents/`) · 프로젝트 `.claude/agents/`
  가 플러그인 것을 override(문서 명시) · 소문자 `plan` 은 내장 `Plan` 을 오버라이드하지 않는다(대소문자
  구분 — 이 세션의 에이전트 목록에 소문자 `explore`/`plan` 과 내장 `Explore`/`Plan` 이 동시에 떠 있었다, 실측).

### 2. 뒤집힌 전제 (가장 중요)
v1.19.0 감사에서 "커스텀 서브에이전트는 `CLAUDE.md` 를 **안** 물려받는 게 맞음"으로 확인해 기록해 뒀었다.
**Claude Code 2.1.224 에서 이 명제는 거짓이다.** 공식 문서 원문:
> "Explore and Plan are the only subagents that omit CLAUDE.md and git status. Every other built-in and custom subagent loads both."

이 저장소에서 **실측으로 확인했다** — `explore` 서브에이전트를 띄워 물어보니 `CLAUDE.md`·`SPEC.md`(`@import`)·
git status 를 전부 받고 있었다. 이 한 문장이 에이전트 보일러플레이트 약 100줄과 케이브맨 말투 5판본을 지탱하고 있었다.

### 3. 무엇을 뺐나
- 에이전트 보일러플레이트 약 100줄 — 위 뒤집힌 전제가 근거. `CLAUDE.md` 를 물려받으므로 4종
  (`agents/explore.md`·`plan.md`·`implement.md`·`verify.md`) 모두 공통 규칙을 지우고
  "`CLAUDE.md` 「서브에이전트 보고 규약」을 따른다" 한 줄로 대체했다.
- 케이브맨 말투 5판본 → 출력 스타일 `output-styles/womc-caveman.md` 한 곳.
- `review` 에이전트 → Claude Code 기본 `/code-review` 로 대체(전용 에이전트를 두지 않기로 함).
- `.claude/agents/`·`.claude/skills/`·`.claude/answer-style.js` 골격 복사 → 플러그인 루트
  `agents/`·`skills/`·`output-styles/` 가 직접 제공(프로젝트로 복사하지 않음).
- `settings.json` 의 `hooks` 블록.
- 결과 수치: `commands/womc.md` 800→495줄, 골격 생성물 11→6개, 에이전트 5→4종.

### 4. 무엇을 왜 남겼나
- `keep-coding-instructions: true` — 출력 스타일 파일에 필수. 기본값 `false` 면 Claude Code 내장
  코딩 지침이 통째로 빠진다.
- 에이전트 파일의 "너는 메인의 대화 이력을 못 본다" 한 줄 — `CLAUDE.md` 상속과 무관한, 서브에이전트
  실행 구조 자체의 사실이라 상속되지 않는다. 4종 전부에 남겼다.
- `.claude/statusline.js` — Claude Code 기본 제공이 아니라 자체 구현이 필요하다.

안 하기로 한 것 2가지:
- `plan` → `design` 개명 취소 — 소문자 `plan` 은 내장 `Plan` 을 오버라이드하지 않는다(대소문자 구분,
  위 1번에서 실측). 이름 충돌이 없어 개명 이득이 사라졌고 고칠 곳 12군데를 아꼈다.
- `statusLine` 의 `refreshInterval` 추가 취소 — 공식 문서 확인 결과 단위가 밀리초가 아니라 **초**이고
  최소값이 `1` 이다. 몇 초마다 node 프로세스를 새로 띄우는 비용이 Windows 에서 이득보다 커서 아예
  넣지 않기로 했다. womc 상태줄은 이벤트 기반 갱신으로 충분하다.

### 5. 실측 필요 (미확인) — **2건 모두 「확인됨」으로 닫혔다 (2026-08-10, 위 v2.1.0 감사)**
① ~~플러그인 서브에이전트를 부를 때 `subagent_type` 값이 `explore` 인지 `womc:explore` 인지.~~
   → **확인됨: `womc:explore` 처럼 플러그인 이름이 붙는다.** 근거(문서): https://code.claude.com/docs/en/plugins-reference ·
   https://code.claude.com/docs/en/hooks ("the agent type is the plugin-scoped identifier ... **not the bare frontmatter name**").
   근거(실측): 이 저장소 세션의 에이전트 목록에 `womc:explore`·`womc:plan`·`womc:implement`·`womc:verify` 로 노출됐다.
   **주의**: `subagent_type: "explore"` 는 오류가 아니라 **내장 `Explore` 에 조용히 붙고**, `"plan"` 은 내장 `Plan` 에 붙는다.
   `"implement"`·`"verify"` 만 "Agent type not found" 로 실패한다.
② ~~프로젝트 `.claude/settings.json` 의 `outputStyle` 이 플러그인이 제공한 출력 스타일 이름을 해석하는지.~~
   → **확인됨: 해석하지 못한다.** 플러그인 스타일은 `womc:womc-caveman` 으로 등록되고 조회는 정확일치라,
   현재 값 `"womc-caveman"` 은 조용히 무시된다(경고 없음). **케이브맨 말투가 지금까지 한 번도 켜진 적이 없다.**
   자세한 근거와 고치는 길 3가지는 **위 v2.1.0 기록의 2번·5번①** 에 있다.
