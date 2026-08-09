# 하네스 감사 기록부 (HARNESS-AUDIT)

> `harness-audit` 스킬이 매번 읽고 이어 쓰는 기록부다. "Claude Code 가 새 버전에서
> 기본 제공하게 된 기능"을 골격에서 걷어낸 이력을 남긴다. 다음 감사는 **맨 위 기록의
> 「마지막 감사 기준 버전」부터** 시작하고, 같은 조사를 반복하지 않는다.
> 맨 위 기록의 **마지막 감사 기준 버전**: Claude Code `2.1.224` (2026-08).
> 맨 위 기록의 **실측 필요(미확인) 목록**은 아래 v2.0.0 기록의 5번을 본다 — 2건이 아직 열려 있다.

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

### 5. 실측 필요 (미확인) — **2건, 아직 열려 있음**
① 플러그인 서브에이전트를 부를 때 `subagent_type` 값이 `explore` 인지 `womc:explore` 인지.
② 프로젝트 `.claude/settings.json` 의 `outputStyle` 이 **플러그인이 제공한** 출력 스타일 이름을 해석하는지.
   안 되면 폴백 둘: `output-styles/womc-caveman.md` 에 `force-for-plugin: true` 추가(단 "항상 켜짐"이
   되어 사용자 결정과 어긋나므로 다시 물어야 한다) / `/config` 에서 직접 고르게 안내.

**두 건 모두 아직 "실측 필요" 상태로 열려 있다** — 2026-08-10 사용자 결정으로 검증을 미루고 v2.1.0 을
먼저 시작했기 때문이다. 확인되는 대로 이 자리를 「확인됨」으로 고칠 것.
