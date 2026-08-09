# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남

## 지금 하는 일
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

- [~] **v2.0.0·v2.1.0 실사용 검증 4건** — 파일 작업은 전부 끝났고 버전도 `2.1.0` 으로 올라갔다.
  남은 건 **이 저장소 안에서는 할 수 없는 검증**이다. 다른 폴더·새 세션에서 사람이 직접 돌려야 한다.
  - ⚠ **2026-08-10 — 사용자 결정으로 v2.0.0 검증을 미루고 v2.1.0 을 먼저 만들었고, v2.1.0 도 파일 작업이 끝났다.**
  - ✅ **2026-08-10 (같은 날, `/womc update` 의 자동 하네스 감사) — 미확인 2건이 둘 다 닫혔다.**
    `docs/HARNESS-AUDIT.md` v2.0.0 기록 5번 절이 「확인됨」으로 고쳐졌고, 새 v2.1.0 감사 기록이 맨 위에 쌓였다.
    **그중 ②는 실제 버그로 판명됐다** — 아래 「할 일」의 첫 항목이 그것이다. 통과 조건 ④(말투)는 그 버그를 고치기 전에는 반드시 실패한다.
  - **먼저 할 것**: 커밋·push → `/plugin marketplace update works-on-my-claude` → `/plugin install womc@works-on-my-claude` → **Claude Code 재시작.**
    로컬 플러그인 캐시가 아직 v1.20.0 판이라, 이걸 안 하면 옛 골격을 깔면서 "검증 실패"로 보인다.
  - 손댈 파일: 없다(검증만). 문제가 나오면 `commands/womc.md` 나 `.claude/settings.json` 을 고친다.
  - 끝난 것으로 보는 조건 4가지(①은 이미 통과):
    - ② **빈 폴더에서 `/womc`** → 생성 파일이 정확히 6개
      (`CLAUDE.md`·`SPEC.md`·`HARNESS.md`·`.gitignore`·`.claude/settings.json`·`.claude/statusline.js`).
      `.claude/agents/`·`.claude/skills/`·`answer-style.js` 가 생기면 옛 캐시를 쓰고 있는 것이다.
    - ③ **v1.20.0 골격 폴더 사본에서 `/womc update`** → 레거시(`.claude/agents/`·`.claude/skills/`·`answer-style.js`)가 지워지고,
      `SPEC.md`·`PLAN.md`·`TASKS.md`·`.claude/rules/`·`settings.json` 에 사용자가 추가한 allow 는 전부 남아 있어야 한다.
    - ④ **새 세션에서 말투** — 메인 답변은 케이브맨, **서브에이전트 보고는 평문 한국어**.
    - ⑤ **`harness-audit` 스킬이 실제로 도는지** (v2.1.0 몫) — 골격을 깐 폴더에서 "하네스 점검해줘"라고 말했을 때
      이 스킬이 잡히고, 현재 Claude Code 버전을 스스로 알아내 「뺄 수 있는 것 / 남길 것 / 실측 필요」를 근거 URL 과 함께 보고하며,
      그 결과가 `docs/HARNESS-AUDIT.md` 맨 위에 새 기록으로 쌓이는지 육안 확인.
      스킬 이름이 안 잡히면 `skills/harness-audit/SKILL.md` 의 frontmatter(`name`·`description` 2키)를 먼저 의심한다 —
      `description` 값이 큰따옴표로 시작하면 YAML 파싱이 깨진다(만들 때 한 번 걸렸던 자리다).
  - ~~**위 ②~⑤ 를 돌리면 미확인 2건도 함께 판명된다.**~~ → **2026-08-10 감사에서 먼저 판명됐다.**
    **진실은 여전히 `docs/HARNESS-AUDIT.md` 한 곳에만 둔다** — 새 「실측 필요」 4건은 그 파일 v2.1.0 기록 5번 절에 있고,
    아래 「할 일」에는 **무엇을 어떻게 확인하는지만** 적는다(내용을 두 곳에 베끼지 않는다).
  - 확인 방법: ①은 이미 통과 — `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.1.0`.

> 아래는 v2.0.0 작업 중 기록이다. **검증 4건이 끝나면 이 절(「이번 작업의 근거」~「남은 일」)을 지우고
> 「끝난 일」의 v2.0.0·v2.1.0 항목만 남긴다.** 지금은 검증에서 문제가 났을 때 어디를 봐야 하는지 알려 주므로 남겨 둔다.
> 전체 계획 원본은 `C:\Users\s2\.claude\plans\glistening-squishing-nest.md`.

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

### 4단계에서 남긴 것 (5단계가 이어 쓴다)
**문서 3종이 모두 새 구조에 맞춰졌다. 남은 것은 5단계뿐이다.**

- **`README.md` 132줄 → 87줄.**
  - 「수동 설치」 절 **삭제**(`commands/womc.md` 만 복사하면 반쪽 골격이라 잘못된 안내였다).
  - 구조도에서 `.claude/agents/`·`.claude/skills/`·`answer-style.js` 를 뺐다 — 생성물은 6개뿐이다.
  - **「플러그인이 주는 것」 절 신설** — 에이전트 4종·스킬 2종·`womc-caveman`·`/womc eject <이름>`.
  - 표·토큰 절약 절의 "5종"·`review` 언급을 전부 4종으로. 말투 설명을 CLAUDE.md 「설명 방식」 → **출력 스타일**로 정정.
  - 갱신 안내를 3단계 나열에서 "`/womc update` 한 줄 + 안 될 때만 수동" 으로 압축.
  - **제목 버전은 아직 `1.20.0` 이다** — 5단계 `bump-version.py` 가 올릴 자리다.
- **`SPEC.md` 2·3·4·5항 정정** (1항에도 플러그인 루트 `agents/`·`skills/`·`output-styles/` 한 줄 추가).
  - 3항 1번에 `/womc eject` 한 줄, 2번의 `answer-style.js` → `outputStyle`+출력 스타일 파일,
    3번은 **4종 + "서브에이전트도 CLAUDE.md 를 물려받는다"** 로 사실 정정, 4번은 검토를 `/code-review` 권유로.
  - 5항 산출물 목록에 `agents/`·`skills/`·`output-styles/` 추가.
  - **SPEC.md 는 CLAUDE.md 에 `@import` 되므로 매 세션 로드된다** — 늘리지 말 것(32줄 유지).
- 확인: 두 문서에서 `answer-style` 0건, `review` 는 `/code-review` 2건만 남음.
  `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK.

### 5단계에서 남긴 것 (검증만 남았다)
- **신설 `scripts/bump-version.py`** — `py scripts/bump-version.py <새버전>` 한 줄로 표식 6곳을 한꺼번에 올린다
  (`plugin.json` version · `README.md` 제목 · `womc:skeleton-version` 표식 4개 = `commands/womc.md`×3 + `CLAUDE.md`).
  - `--dry-run` 을 주면 어디를 몇 곳 고칠지 보여주기만 한다. **버전을 내리는 건 막아 뒀다**(손으로 해야 한다).
  - 표식 파일 목록 `VERSION_MARKER_FILES` 는 `check-sync.py` 와 **같은 값이어야 한다** — 한쪽에 파일을 추가하면 다른 쪽도 추가한다.
  - 줄바꿈을 보존해 읽고 쓴다(`newline=""`). 이 저장소는 LF 인데 **`plugin.json` 만 CRLF** 라, 안 그러면 그 파일 전체가 diff 로 뜬다.
- **`marketplace.json` 은 안 고쳤다** — 계획에 적혀 있던 "설명문의 5종"이 실제로는 없었다.
  `plugin.json`·`marketplace.json` 의 description 은 "서브에이전트 오케스트레이션"이라고만 적혀 있어 숫자가 안 박혀 있다. 고칠 것이 없다.
- 구조 확인(육안): 플러그인이 주는 파일 7개가 다 있다 —
  `agents/{explore,plan,implement,verify}.md` · `skills/{plan-feature,make-rule}/SKILL.md` · `output-styles/womc-caveman.md`.
  `commands/womc.md` 의 생성 절도 1)~6) 여섯 개뿐이라 통과 조건 ②의 6개와 맞는다.
- 확인: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.0.0`.

## 끝난 일

- [x] 말투가 한 번도 안 켜지던 버그 수정 — A안 (v2.1.1) — **파일 작업 완료, 육안 검증 1건 남음**
  - 손댈 파일: `.claude/settings.json` · `commands/womc.md`(3자리) · `HARNESS.md` · `README.md` · `PLAN.md` · `TASKS.md` · `.claude-plugin/plugin.json`
  - **버그의 정체**: 플러그인이 제공하는 출력 스타일은 레지스트리에 **`플러그인이름:스타일이름`**(`womc:womc-caveman`)으로 등록되고,
    조회는 **키 정확일치**다(정규화가 콜론을 제거하지 않는다). 그런데 골격이 넣던 값은 `"womc-caveman"` 이라 **아무것도 못 찾고 조용히 무시**됐다.
    경고도 안 뜬다. **v1.20.0 이후 지금까지 케이브맨 말투는 한 번도 켜진 적이 없다.**
    근거는 `docs/HARNESS-AUDIT.md` v2.1.0 기록 2번(문서 URL + 설치 바이너리 실측 + 이 세션 자체가 원시인 말투가 아니었다는 실측).
  - 남긴 것:
    - **값 3자리를 `"womc:womc-caveman"` 으로**: `.claude/settings.json:2` · `commands/womc.md` 5번 절 JSON 임베드 · 그 설명 불릿.
      **파일명과 frontmatter `name` 은 안 바꿨다** — `output-styles/womc-caveman.md` / `name: womc-caveman` 그대로다. 접두는 **등록 키에만** 붙는다(헷갈리기 쉬운 자리).
    - **갱신 모드 3번에 자동 교정을 넣은 것이 절반의 핵심이다** (`commands/womc.md` 갱신 모드 3번) —
      `outputStyle` 값이 **정확히 `"womc-caveman"`** 이면 옛 골격의 깨진 값으로 보고 `"womc:womc-caveman"` 으로 **고친다.**
      그 둘 말고 다른 값이면 사용자가 고른 말투이므로 **그대로 둔다.** 이 예외가 없으면 이미 깔린 프로젝트가 영영 안 고쳐진다.
    - `HARNESS.md:47` 안내를 "`/config` 에서 이름 확인" → "**`outputStyle` 값이 `womc:womc-caveman` 인지 확인**"으로 바꿨다.
      **이 줄은 `commands/womc.md` HARNESS 임베드 사본과 글자 그대로 같아야 한다**(어긋나면 `check-sync.py` 가 DRIFT 로 잡는다).
    - 버전은 `py scripts/bump-version.py 2.1.1` 한 줄로 6곳을 올렸다.
    - **A안을 고른 이유**: B안(`force-for-plugin: true`)은 womc 가 켜진 **모든** 프로젝트에 말투를 강제하고 사용자의 `outputStyle` 을 덮어써서
      "프로젝트별로 켠다"는 설계 결정과 어긋난다. C안(프로젝트로 복사)은 "말투 규칙은 한 곳에만" 원칙과 어긋난다.
      B안은 「할 일」에 보류 항목으로 남겨 뒀다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.1.1`.
    **말투가 실제로 켜지는지는 스크립트로 못 잡는다** — 커밋·push → 플러그인 재설치 → **Claude Code 재시작** 후
    메인 답변이 원시인 말투인지 육안 확인해야 한다(위 「지금 하는 일」의 통과 조건 ④).

- [x] 하네스 감사 절차를 골격에 심음 (v2.1.0) — **파일 작업 완료, 실사용 검증 1건은 위 「지금 하는 일」에 남아 있다**
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

> 최근 작업만 여기 남긴다. **v1.18.0 이하의 지난 기록은 `docs/CHANGELOG.md` 로 옮겼다** — 옛 결정 이유를 찾을 때는 그 파일을 본다.
> 이 절이 다시 길어지면(대략 항목 5개 이상) 오래된 것부터 같은 형식 그대로 `docs/CHANGELOG.md` 맨 위로 옮긴다.

- [x] Claude Code 2.1.x 기본기능에 맞춘 하네스 간소화 (v2.0.0) — **파일 작업 완료, 실사용 검증 3건은 위 「지금 하는 일」에 남아 있다**
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

## 할 일

> 아래 4건은 2026-08-10 하네스 감사(`/womc update` 자동 실행)가 남긴 것이다.
> **각 항목의 배경·근거 URL·선택지는 `docs/HARNESS-AUDIT.md` 의 v2.1.0 기록 5번 절에 있다** — 여기엔 확인 방법만 적는다.

- [ ] ~~**`force-for-plugin: true` 가 이 판에서 실제로 먹는지 확인 (감사 5번②)**~~ — **보류.**
  A안으로 고쳤으므로 지금은 필요 없다. 나중에 "프로젝트마다 `outputStyle` 을 박지 않게" 하고 싶어질 때만 다시 꺼낸다.
  - 확인 방법: `output-styles/womc-caveman.md` frontmatter 에 넣고 플러그인 재설치 → 재시작 → **settings.json 에 `outputStyle` 이
    아예 없는 폴더**에서 메인 답변이 원시인 말투로 나오는지 본다.

- [ ] **`permissions.allow` 의 PowerShell 4줄이 정말 필요한지 확인 (감사 5번③)**
  - 문서는 내장 read-only 자동 허용을 **Bash 만** 명시하고 PowerShell 은 언급이 없다. 필요 없으면 골격에서 4줄을 뺄 수 있다.
  - 확인 방법: Windows 에서 임시 폴더에 골격을 깔고 `.claude/settings.json` 의 `allow` 4줄을 지운 뒤,
    `git status` 를 시켜 **권한 프롬프트가 뜨는지** 본다. 안 뜨면 뺄 수 있다(그러면 `commands/womc.md` 5번 절도 같이 고친다).

- [ ] **`/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지 확인 (감사 5번④)**
  - 위 항목이 "필요하다"로 나올 때만 의미가 있다. 골격에 4줄을 박는 대신 이 번들 스킬에 맡겨도 되는지 판단한다.
  - 확인 방법: 골격을 깐 폴더에서 `/fewer-permission-prompts` 를 한 번 돌리고, `.claude/settings.json` 의 `allow` 에
    PowerShell 읽기 전용 명령이 실제로 추가되는지 본다.

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
