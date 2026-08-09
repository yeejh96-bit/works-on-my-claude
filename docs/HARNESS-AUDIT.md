# 하네스 감사 기록부 (HARNESS-AUDIT)

> `harness-audit` 스킬이 매번 읽고 이어 쓰는 기록부다. "Claude Code 가 새 버전에서
> 기본 제공하게 된 기능"을 골격에서 걷어낸 이력을 남긴다. 다음 감사는 **맨 위 기록의
> 「마지막 감사 기준 버전」부터** 시작하고, 같은 조사를 반복하지 않는다.
> 맨 위 기록의 **마지막 감사 기준 버전**: Claude Code `2.1.226` (2026-08-10).
> 맨 위 기록의 **실측 필요(미확인) 목록**은 아래 v2.1.0 기록의 5번을 본다 — 4건이 열려 있다.

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

### 5. 실측 필요 — **4건**
① **`.claude/settings.json` 의 `outputStyle` 을 어떻게 고칠 것인가** (위 2번 버그). 길이 셋이고 각각 대가가 다르다:
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
