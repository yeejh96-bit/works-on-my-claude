# 하네스 감사 기록부 (HARNESS-AUDIT)

> `harness-audit` 스킬이 매번 읽고 이어 쓰는 기록부다. 골격에서 **걷어낸** 이력(이제 Claude Code 기본이거나
> 지금 모델이 알아서 하는 것)과 **새로 들인** 이력(그 사이 생긴 기능 중 골격이 쓸 만한 것)을 함께 남긴다.
> 다음 감사는 **맨 위 기록의 「마지막 감사 기준 버전」부터** 시작하고, 같은 조사를 반복하지 않는다.
> **감사 본체는 Claude Code 앞 두 자리(`major.minor`)가 달라지면 돈다.** (v3.0.0 에서 모델 트리거를 뺐다.)
> 맨 위 기록의 **마지막 감사 기준 버전**: Claude Code `2.1.251` (2026-08-31).
> 맨 위 기록의 **실측 필요(미확인) 목록**은 아래 v3.2.0 기록의 6번을 본다.
> **③에서 파생됐던 열린 확인(`open:allow-cleanup`)도 2026-08-11 에 통과·닫혔다** — 남은 열린 확인은 아래 목록을 본다.
> ③의 결론(골격에서 `allow` 4줄을 뺄 수 있다)은 **v2.2.0 으로 실행됐다 (2026-08-10).**

<!-- womc:open-checks:begin -->
> **다음 감사가 먼저 볼 것 — 열린 확인 4건**
> (정본은 `TASKS.md` 「할 일」. 조건·확인 방법을 여기 베껴 적지 않는다.)
> - `open:env-deny-redirect` — 입력 리다이렉션(`cat < .env` 류)이 골격의 `.env` deny 를 우회하는지 (파생 자리: v2.7.0 기록 6번① · **v3.2.0 감사에서 절반이 문서로 답이 나왔다**)
> - `open:delegation-vs-preset` — 하네스가 Opus 5 에 심는 「Agent tool 을 시키지 마라」와 womc 「적극 위임」 중 어느 쪽이 이기는지 (파생 자리: v2.7.0 기록 6번② · **v3.2.0 감사가 공식 Opus 5 권고를 얹었다 — 무게가 또 커졌다**)
> - `open:import-command` — `/import` 가 womc 온보딩 병합과 겹치는지 (파생 자리: v2.8.0 기록 6번 · **v3.2.0 감사에서 조사는 끝났고 안내 한 줄만 남았다**)
> - `open:subagent-cache-ttl` — 서브에이전트 캐시 수명을 1시간으로 늘리는 것의 순이득 (파생 자리: v3.2.0 기록 4번①·6번)
> (출력 스타일 eject 확인은 v3.0.0 에서 대상 폐지로 닫혔다 — `docs/CHANGELOG.md` v3.0.0 항목.)
> **다음 감사는 이 항목들을 새 「실측 필요」로 다시 만들지 말고 `TASKS.md` 의 해당 항목을 갱신한다.**
> (2026-08-18 v2.7.0 감사에서 그 앞의 열린 확인 4건이 **전부 닫혔다** — 결론은 아래 v2.7.0 기록 5번.
> **닫힌 ID 를 이 구획에 백틱으로 남기지 말 것** — 대조 스크립트가 열린 것으로 센다.)
<!-- womc:open-checks:end -->

## v3.2.0 — 2026-08-31 / Claude Code `2.1.251` · 모델 `Opus 5` 기준

### 1. 무엇을 확인했나
- **트리거는 성립하지 않았다.** Claude Code 앞 두 자리가 같다(`2.1.235` → `2.1.251`, 패치만).
  `/womc update` 7번이 「그래도 조사할까요?」로 멈췄고, **사용자가 「감사 돌려」라고 해서 돈 감사다.**
- 조사 구간: `2.1.235` → `2.1.251` (그 사이 릴리스 전부).
- 조사 분담: 웹 2갈래는 `general-purpose`(ⓐ 뺄 거리 + 열린 확인 3건의 문서상 답 / ⓑ 새로 들일 것), 로컬 1갈래는 `explore`.
- 같은 세션의 `/womc update` 가 골격 3개(`CLAUDE.md`·`.claude/settings.json`·`.claude/statusline.js`)와 플러그인(3.2.0)이
  최신판과 **글자 그대로 일치**함을 확인했다 — 갱신에서 고친 파일 0개.
- always-on 로드량 실측: `CLAUDE.md` 61줄 + `.claude/rules/제약-공통.md` 41줄 = **102줄.** (`SPEC.md` 폐지 후 첫 실측이다.)
- ⓐ 갈래는 CHANGELOG 를 WebFetch 요약이 아니라 **raw 파일을 받아 직접 대조**했다 — 요약 모델이 없는 항목을 엉뚱한 버전에 붙이는 것을 그 자리에서 잡아냈다. **다음 감사도 CHANGELOG 는 raw 로 받아 직접 grep 한다.**

### 2. 뒤집힌 전제 — **없음. 대신 미확인 가정 2건이 문서로 확정됐다.**
- **「`ask` 가 `allow` 를 이기는가」 → 이긴다.** "a matching ask rule prompts even when a more specific allow rule also matches the same call"
  https://code.claude.com/docs/en/permissions
  게다가 **auto 모드에서도 자동 승인되지 않는다** — 「Actions no mode auto-approves」의 첫 항목이 "Tools matched by an explicit ask rule" 이다.
  https://code.claude.com/docs/en/permission-modes
  **Pro·Max 는 이제 세션이 auto 모드로 시작하는데도** 골격의 승인 관문(v2.5.0)이 그대로 산다는 뜻이다.
- **「프리픽스 `:*` 표기」 → 정식 문법이다.** "The `:*` suffix is an equivalent way to write a trailing wildcard, so `Bash(ls:*)` matches the same commands as `Bash(ls *)`."
  단 **꼬리에서만** 유효하다 — `Bash(git:* push)` 처럼 가운데 두면 콜론이 글자 그대로 취급돼 아무것도 안 맞는다(`2.1.246` 이 이 경우 시작 시 경고를 넣었다).
  골격의 `ask` 8줄은 `:*` 가 전부 맨 끝이라 정상 동작한다. **앞으로 `ask` 를 늘릴 때도 `:*` 는 맨 끝에만 쓴다.**
- 남은 가정 「Windows git 표기」는 이번에도 확인 못 했다.
- **이 두 확정을 `.claude/rules/제약-공통.md` 「아직 확인 못 한 가정」에 반영하는 것은 이 스킬이 하지 않는다**(골격 파일은 안 고친다). → `plan-feature` 몫이다.

### 3. 무엇을 뺐나 — **없음. 「뺄 수 있음」이 하나도 안 나왔다.**
- `permissions.ask` 8줄 → **남길 것.** 내장 안전장치가 이걸 대신하지 못한다(아래 5번).
- `permissions.deny` 7줄 → **남길 것.** 비밀 파일 보호는 여전히 손으로 적는 것이 공식 방법이고, 새 문법도 프리셋도 안 생겼다.
- `.claude/statusline.js` → **남길 것.** 내장 상태줄 요소나 템플릿 변수는 없다. `refreshInterval` 동작도 그대로다.
- `CLAUDE.md` 산문 규칙 4종 → **남길 것.** 기본이 된 것은 없다. 다만 「적극 위임」은 아래 6번의 재검토 대상이다.
- PowerShell `ask` 줄을 줄일 여지도 **없었다** — 별칭은 자동 정규화되지만("A rule written for the cmdlet name also matches its aliases"), 골격은 이미 cmdlet 이름으로 한 줄씩만 적어 뒀다.

### 4. 무엇을 새로 들였나 — **아직 없다. 후보 2건을 사용자에게 넘겼다.**
(고치는 일은 이 스킬이 하지 않는다 — `plan-feature` 몫이다.)
- **① 서브에이전트 캐시 수명** — `subagentPromptCacheTtl`(`2.1.242`, 설정 한 줄로 전부) 또는 `experimental.cacheTtl`(`2.1.248`, 에이전트별 머리말). **둘 중 하나만 고른다** — 설정이 머리말을 이겨서 둘 다 넣으면 뒤가 죽는다.
  https://code.claude.com/docs/en/prompt-caching#cache-lifetime · https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
  **서브에이전트 요청은 구독 플랜에서도 기본 5분 캐시만 받는다**(메인 대화만 1시간). 위임을 많이 쓰는 골격일수록 이득이 크다.
  골격의 어디: `commands/womc.md` 의 `.claude/settings.json` 템플릿 + 라이브 사본 — **둘을 같이 고쳐야 check-sync 1번을 통과한다.**
  → 순이득(1시간 캐시는 쓰기 요금이 더 비싸다)은 실측 전엔 단정 못 함. 열린 확인 `open:subagent-cache-ttl`.
- **② 상태줄 `prompt_cache`** — `warm`·`hit_ratio` 같은 캐시 통계가 상태줄 JSON 에 새로 들어왔다(`2.1.251`).
  https://code.claude.com/docs/en/statusline#prompt-cache-fields
  골격의 첫 번째 목표(컨텍스트를 얇게)를 **처음으로 눈에 보이게** 만든다 — `/compact` 나 새 세션을 시작할 시점의 근거가 된다. 서브에이전트 요청은 이 통계에서 빠져 정확히 「메인이 얇은가」만 보여 준다.
  골격의 어디: `.claude/statusline.js` + `commands/womc.md` 안의 같은 코드 사본. 넣는다면 `warm`+`hit_ratio` 한 조각만 — 상태줄은 얇게 두는 것이 방침이다.
- **안 들일 것으로 가른 것**: `PreModelSwitch`·`PostModelSwitch` 훅(`2.1.251` 신규 — 「훅으로 만드는 것은 안 한다」로 이미 닫혔다) · `rate_limits.spend_limit`(Claude apps gateway 뒤에서만 오는 값이라 개인 Pro·Max 에는 영영 안 온다 → 죽은 코드만 는다) · `modelPicker`·`modelPricing`·`ANTHROPIC_DEFAULT_MODEL`·`spellcheck`·`--restricted`·`keybindingFlavor`(개인 취향·조직 정책이지 골격이 하는 일과 무관).

### 5. 무엇을 왜 남겼나
- **`permissions.ask` 8줄** — 내장 회로차단기는 작업폴더 *바깥*(홈·드라이브 루트·상위 폴더)을 겨냥한 `rm` 만 무조건 막고, **폴더 안쪽의 `rm -rf src/` 는 안 걸린다.** `git reset --hard` 류는 **auto 모드 분류기만** 막아 manual 모드엔 관문이 없고, `git push` 는 분류기 기본 차단 목록에 아예 없다(막는 건 force push 와 비밀정보를 실어 보내는 push 뿐이다). `mv` 는 어떤 내장 장치에도 안 걸린다. → **ask 8줄이 전부 내장 장치보다 넓다.**
  https://code.claude.com/docs/en/permission-modes
- **`permissions.deny` 7줄** — 형태까지 정답이다. 문서는 `Write(...)`·`Glob(...)` 로 쓴 경로 규칙은 "받아들이되 절대 참조하지 않고 시작 시 경고한다"고 못 박는데, 골격은 전부 `Read(...)` 라 그 함정을 피했다. `2.1.251` 이 「Grep·Glob 이 심링크 너머 `Read` deny 를 안 지키던 것」을 고쳐 **가만히 있었는데 더 강해졌다.**
  https://code.claude.com/docs/en/permissions
- **한글 파일 이름 방침**(`.claude/rules/제약-공통.md` 같은 이름) — `2.1.248` 이 「`@` 멘션이 비라틴 문자를 못 맞추던 것」을, `2.1.239` 가 「BOM 붙은 `agents/*.md`·`SKILL.md` 가 **소리 없이 무시**되던 것」을 고쳤다. Windows + 한글 이름 조합이 이제 안전하다 — 방침을 그대로 쓴다.
- **`skills/*/SKILL.md` 배치와 frontmatter** — `2.1.246` 이 이 배치의 스킬 수를 0 으로 세던 버그와 `name` 에 `plugin:` 접두어가 겹쳐 보이던 버그를 고쳤다. 실측해 보니 골격의 스킬 3종은 접두어 없이 `name: harness-audit` 식이라 애초에 안 걸렸다.
- **`verify` 서브에이전트** — Opus 5 프롬프팅 가이드가 "'use a subagent to verify' 류 지시는 빼라 … 별도 검증 단계를 더하는 레거시 하네스 뼈대도 마찬가지"라고 명시한다. 골격은 이미 「구현이 끝날 때마다 자동으로 부르는 고정 단계가 아니다」로 좁혀 놨다 — **그 좁힘이 공식 권고와 정확히 맞아 그대로 남긴다.**
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **`commands/womc.md` 배치** — 문서가 새 플러그인에는 `skills/` 를 권하지만("Use `skills/` for new plugins") 기존 `commands/` 는 계속 동작한다고 명시한다("Your existing `.claude/commands/` files keep working"). 이번 구간의 변화가 아니라 「뺄 거리」로 올리지 않았다.
  https://code.claude.com/docs/en/plugins

### 6. 실측 필요
- **`CLAUDE.md` 「적극 위임」이 공식 Opus 5 권고와 어긋난다 — 이번 감사의 가장 큰 발견이다.**
  Anthropic 은 "Claude Opus 5 delegates to subagents more readily than prior models. Delegation pays off on genuinely independent, sizeable tracks of work, but **it multiplies cost and time when applied to small tasks**" 라며 「작은 일은 위임하지 마라 / 하나로 되면 하나만 써라 / spawn 수를 낮게 유지하라」를 권한다.
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
  womc 는 v3.0.0 에서 **「위임 문턱값을 골격에 박지 않는다」를 사용자가 닫았는데, 모델 쪽 권고가 정반대로 왔다.**
  → 기존 열린 확인 `open:delegation-vs-preset` 에 이 근거를 얹었다 (정본: `TASKS.md` 「할 일」).
- → 열린 확인 `open:subagent-cache-ttl` (정본: `TASKS.md` 「할 일」) — 캐시 수명을 1시간으로 늘렸을 때의 순이득과, 플러그인이 제공하는 에이전트에서 `experimental.cacheTtl` 이 먹히는지.
- → 열린 확인 `open:env-deny-redirect` (정본: `TASKS.md` 「할 일」) — **절반은 문서로 답이 나왔다.** `Read` deny 는 Claude Code 가 알아보는 Bash 파일 명령(`cat`·`head`·`tail`·`sed`)에도 걸리고 Grep·Glob 검색 결과에서도 빠지지만, **임의 서브프로세스(파이썬·노드 스크립트가 스스로 파일을 여는 것)는 안 막는다**(문서 명시). 입력 리다이렉션은 `2.1.232` 에 권한 검사 대상이 됐다가 `2.1.233` 에서 되돌려졌고 **이 구간에 안 돌아왔다**(전 구간 grep 확인). 공식 해법인 샌드박스는 macOS·Linux·WSL2 전용이라 **Windows 네이티브인 이 환경엔 대안이 없다.**
  https://code.claude.com/docs/en/permissions
- → 열린 확인 `open:import-command` (정본: `TASKS.md` 「할 일」) — **조사 부분은 끝났다.** `/import [codex|gemini]`(`2.1.213+`)는 **Codex·Gemini CLI 설정만** 대상이고, `AGENTS.md` 같은 지시 파일을 `CLAUDE.md` 에 **한 번 복사해 붙인다.** womc 는 `@AGENTS.md` **연결**을 넣어 사본을 안 만드는데, **공식 문서가 바로 그 방식을 권한다** — "create a `CLAUDE.md` that imports it so both tools read the same instructions without duplicating them", Windows 에서는 symlink 대신 import 를 쓰라고까지 명시한다. → **womc 의 선택이 공식 권고와 일치한다.** 남은 것은 **겹침 안내 한 줄**뿐이다: 온보딩으로 `@AGENTS.md` 를 넣은 뒤 `/import` 를 돌리면 같은 내용이 **연결 + 사본으로 두 번** 들어간다(`womc:begin/end` 구획이 그 사본까지 감싸주지 않는다).
  https://code.claude.com/docs/en/commands · https://code.claude.com/docs/en/memory
- 「Windows git 표기」 가정(v2.5.0)은 이번에도 확인 못 했다 — `.claude/rules/제약-공통.md` 「아직 확인 못 한 가정」에 그대로 남는다.

## v2.8.0 — 2026-08-19 / Claude Code `2.1.235` · 모델 `Opus 5` 기준

### 1. 무엇을 확인했나
- **트리거는 성립하지 않았다.** Claude Code 앞 두 자리는 같고(`2.1.234` → `2.1.235`, 패치만) 모델도 `Opus 5` 그대로였다.
  `/womc update` 7번이 「그래도 조사할까요?」로 멈췄고, **사용자가 「진행해」라고 해서 돈 감사다.**
- 조사 구간: `2.1.234` → `2.1.235`. 짧아서 `2.1.232`~`2.1.235` 를 함께 훑었다.
- 조사 분담: 웹 2갈래는 `general-purpose`(ⓐ CHANGELOG 훑기 + 열린 확인 3건의 문서상 답 / ⓑ 「새로 들일 것」), 로컬 1갈래는 `explore`.
- 직전 `/womc update` 가 골격 4개(`CLAUDE.md`·`HARNESS.md`·`.claude/statusline.js`·`.claude/settings.json`)가
  최신 `2.8.0` 판과 **글자 그대로 일치**함을 확인했다 — 갱신에서 고친 파일 0개.
- always-on 로드량 실측: `CLAUDE.md` 55줄 + `SPEC.md` 42줄 = **97줄.** 부풀지 않았다.

### 2. 뒤집힌 전제 — **없음. 다만 v2.7.0 결론 하나가 보강됐다.**
- v2.7.0 의 두 결론은 이번에도 유효했다: ⓐ Opus 5 는 시키지 않아도 스스로 검증한다 ⓑ `claude_code` 프리셋이
  Opus 5 에 「시키지 않으면 Agent tool 을 부르지 마라」를 심는다.
- ⓑ 의 원문은 지금도 문서에 그대로 있고, 같은 절에서 **"Either instruction only steers Claude, so set the limits as well"**
  가 새로 확인됐다 — 그 줄이 **강제가 아니라 유도(steer)** 라는 뜻이다.
  https://code.claude.com/docs/en/agent-sdk/subagents
  → `CLAUDE.md` 「적극 위임」이 이길 여지가 문서로 뒷받침됐다. 실제 승부는 여전히 관찰 대상(`open:delegation-vs-preset`).

### 3. 무엇을 뺐나 (근거) — **없음.**
- 조사 구간의 CHANGELOG 변경은 권한 다이얼로그 문구 개선·GitLab MR 배지·Agent tool 인자 검증 등
  **UI 개선과 버그 수정 위주**였다. 골격이 손으로 떠안은 일을 대신하게 된 기능은 없다.
  https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- **기각 ①** — `explore` 가 「뺄 후보」로 올린 `CLAUDE.md:29` 의 위임 지시(조사는 `explore`, 설계는 `plan`…)는
  위 2번ⓑ 의 프리셋을 **상쇄하는 자리**라 빼면 위임 자체가 안 돈다. v2.7.0 기록 2번②와 같은 판단이다.
- **기각 ② (오보 정정)** — `explore` 가 "검증 지시가 `CLAUDE.md` 에 두 번 있다"고 보고했으나 틀렸다.
  실제로는 `CLAUDE.md:31` 한 줄뿐이고, 두 번째로 짚은 자리는 `commands/womc.md` 의 임베드 사본이다
  (정본–사본 관계라 중복이 아니며 `scripts/check-sync.py` 가 일치를 강제한다).

### 4. 무엇을 새로 들였나 (근거) — **후보 3건 전부 v2.9.0 으로 반영됐다 (2026-08-19).**
반영은 이 스킬이 하지 않고 `plan-feature` 로 넘긴다. 사용자가 「반영하자」라고 해서 넘어갔고,
넘긴 결과는 각 후보 끝의 **「→ 반영됨」** 줄에 적었다. 후보:
- **① `commands/womc.md` 프론트매터에 `disable-model-invocation: true`** — `/womc` 는 파일을 새로 쓰는
  **부작용 워크플로**인데 지금 프론트매터(`commands/womc.md:1-5`)에 이 필드가 없어 모델이 문맥상 스스로 부를 여지가 남는다.
  공식 문서가 정확히 이런 경우("workflows with side effects")에 이 필드를 쓰라고 명시한다.
  https://code.claude.com/docs/en/skills
  → 바뀌는 자리: `commands/womc.md` 프론트매터 한 줄.
  → **반영됨 (v2.9.0)**: `commands/womc.md:5` 에 그 한 줄이 들어갔다.
  → 이번에 근거가 하나 더 확인됐다 — **커스텀 슬래시 명령은 스킬로 통합됐다**:
  "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at
  `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."
  → 스킬용 프론트매터 필드가 `commands/womc.md` 에도 유효하다. https://code.claude.com/docs/en/skills
  → **실제 동작은 아직 화면으로 확인하지 않았다** (재시작 뒤 `/womc` 가 목록에 뜨고 손으로 실행되는지).
- **② `agents/implement.md`·`agents/verify.md` 에 `effort: high`** — `agents/plan.md:6` 이 이미 채택한 패턴인데
  같은 opus 를 쓰는 둘에는 없다(구현·검증이 설계보다 쉬울 이유가 없다).
  https://code.claude.com/docs/en/sub-agents
  → 바뀌는 자리: 두 파일의 프론트매터 각 한 줄.
  → **반영됨 (v2.9.0)**: `agents/implement.md:6` · `agents/verify.md:6`.
  이제 **opus 3종이 모두 `high`** 고, haiku 인 `explore` 만 없다.
  → 이번에 근거가 보강됐다 — **`effort` 는 서브에이전트 공식 프론트매터 필드다**:
  "Effort level when this subagent is active. Overrides the session effort level. …
  Options: `low`, `medium`, `high`, `xhigh`, `max`" https://code.claude.com/docs/en/sub-agents
  → **실제 동작은 아직 화면으로 확인하지 않았다** (프론트매터가 거부되지 않는지만 보면 된다).
- **③ 온보딩에 기존 `AGENTS.md` 감지 → `CLAUDE.md` 에서 `@AGENTS.md` import** — 지금 온보딩은
  `CLAUDE.md`·`.claude/settings.json` 만 병합하고 `AGENTS.md`(다른 코딩 에이전트가 쓰는 규칙 파일)는 안 본다.
  공식 문서는 그게 있으면 import 하고 Claude 전용 절만 덧붙이라고 권한다(중복 작성 방지).
  https://code.claude.com/docs/en/memory
  → 바뀌는 자리: `commands/womc.md` 「기존 프로젝트 온보딩」 2절.
  → **반영됨 (v2.9.0) — 다만 이 감사의 원안대로가 아니다.** 「감지하면 import」가 아니라
  **「제안 후 승낙」**으로 들어갔다(2026-08-19 사용자가 고른 길): 루트 `AGENTS.md` 의 줄 수를 세어 알려 주고,
  좋다고 할 때만 `CLAUDE.md` 의 `@SPEC.md` 다음 줄에 `@AGENTS.md` 를 넣는다(멱등).
  이유는 **그 파일이 몇 줄인지 모르는 채로 always-on 로드량을 늘릴 수 없어서다**(위 1번의 97줄 실측이 기준선).
  → 실제로 손댄 자리는 `commands/womc.md` 의 온보딩 2-b 소절 · 마무리 안내 ·
  **갱신 ⓐ(절 병합)ⓑ(구획 교체) 두 경로의 `@AGENTS.md` 이월 규칙** · 역방향 제안 · 완료 보고,
  그리고 `HARNESS.md`·`SPEC.md` 의 설명 한 줄씩이다.
  → **실제 기존 프로젝트에서 돌려보지는 않았다.** 안 고른 길(무조건 import · 줄 수 임계값 자동판단 ·
  내용 복사 · 구획 밖 배치)과 그 기각 이유는 `.claude/rules/제약-공통.md` 「나중에 · 안 할 것」에 있다.

### 5. 무엇을 왜 남겼나
- **`CLAUDE.md` 「적극 위임」 전체** — 위 3번 기각①. 프리셋을 상쇄하는 자리다.
- **`verify` 에이전트** — v2.7.0 과 같은 이유. 로그를 메인에서 떼어내는 값은 모델과 무관하다.
- **`.env` deny 목록** — 리다이렉션 우회 여부와 무관하게 경로 규칙으로 막히는 범위는 그대로 유효하다.
- **스킬에 `allowed-tools` 미도입** — 부작용 명령은 스킬 안에서 그때그때 승인받는 것이 설계 의도(승인 관문)라
  턴 단위 사전승인과 충돌한다. SPEC 5절의 "`allow` 는 비워 둔다" 정책과도 어긋난다.
- **`plugin.json` 의 `hooks`·`mcpServers` 번들 미도입** — v2.0.0 이 `hooks` 를 의도적으로 뺐고
  SPEC 6절이 `.mcp.json` 자동 생성을 「안 만들 것」으로 못박았다. 근거 변화 없음.
- **`sandbox.*` 설정 키 미도입** — v2.1.1 기록 ③의 실측 한계(샌드박스 때문인지 갈라내지 못함)가 아직 그대로다.

### 6. 실측 필요
- 열린 확인 3건은 **그대로 열려 있다** → `open:env-deny-redirect` · `open:delegation-vs-preset` · `open:eject-outputstyle`
  (정본: `TASKS.md` 「할 일」)
  - `open:env-deny-redirect` — **문서로는 못 닫았다.** `2.1.232` 가 넣은 입력 리다이렉션 권한 검사를 `2.1.233` 이
    되돌렸고 `2.1.235` 까지 재도입이 없다 → **지금은 우회 가능 쪽에 무게.** permissions 문서는 deny 가
    `cat`·`head`·`tail`·`sed` 에 걸린다고만 하고 리다이렉션 연산자는 언급하지 않는다.
    https://code.claude.com/docs/en/permissions
  - `open:delegation-vs-preset` — 문서상 어느 쪽이 이기는지 언급 없음. 위 2번의 "only steers" 가 전부다.
  - `open:eject-outputstyle` — **가정의 절반이 문서로 확인됐다.** "The file name becomes the style name unless you
    set `name` in the frontmatter." → 프로젝트 `.claude/output-styles/womc-plain.md` 는 **접두 없이 `womc-plain`** 으로
    등록된다. **womc 가 세운 가정이 맞았다.** https://code.claude.com/docs/en/output-styles
    남은 절반(플러그인이 주는 쪽이 `womc:womc-plain` 으로 등록되는지)은 문서에 없다 — 다만 이 저장소에서 그 값으로
    말투가 실제 동작 중이라 사실상 확인된 셈이다. **끝난 것으로 보는 조건이 「사람이 화면으로 확인」이라 자동으로 닫지 않았다.**
- **새로 연 확인 1건** → `open:import-command` (정본: `TASKS.md` 「할 일」)
- **후보에서 내린 것**: `allowed-tools` 의 `${CLAUDE_PLUGIN_ROOT}` 치환이 플러그인 `commands/` 파일에도 적용되는지는
  문서로 확정 못 했으나, 위 5번에서 `allowed-tools` 도입 자체를 기각했으므로 **열린 확인으로 올리지 않았다.**

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
