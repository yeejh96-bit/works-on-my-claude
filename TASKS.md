# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남

## 지금 하는 일
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

- [~] **하네스 감사가 남긴 실측 3건 — 재시작 한 번으로 순서대로 처리한다 (2026-08-10 시작)**
  사용자가 재시작하고 돌아와 "다음 뭐 하지?"라고 물으면 **이 항목을 그대로 읽어 안내한다.**
  각 건의 배경·근거 URL 은 `docs/HARNESS-AUDIT.md` v2.1.1 기록 5번 절에 있다.
  - **1) 내장 Task 도구가 `TASKS.md` 체크박스를 대체하는지 (감사 5번⑤)** — 재시작 직후 바로.
    - 재시작 전에 이 세션에서 `TaskCreate` 로 `#1 [실측용] 재시작 뒤에도 이 항목이 남아 있는지 확인` 을 만들어 두었다.
    - 사용자에게 `/tasks` 를 실행해 그 항목이 보이는지 물어본다(도구로는 `TaskList`).
    - **보이면 「유지됨」** → 체크박스 대체 가능성이 있으므로 `plan-feature` 로 넘겨 검토한다.
      **안 보이면 「세션용」** → `TASKS.md` 체크박스는 대체 불가. 그대로 두고 「할 일」의 그 항목을 닫는다.
    - 판정을 `docs/HARNESS-AUDIT.md` v2.1.1 기록 5번⑤ 와 「할 일」 양쪽에 적는다.
  - **2) `permissions.allow` 의 PowerShell 4줄이 필요한지 (감사 5번③)**
    - 먼저 사용자에게 `/permissions` 로 **권한 모드가 기본인지** 확인시킨다. bypass·acceptEdits 면 프롬프트가 안 떠서 결과를 믿을 수 없다.
    - `.claude/settings.json` 의 `allow` 4줄(`PowerShell(git status:*)`·`(git diff:*)`·`(git log:*)`·`(Get-ChildItem:*)`)을 지운다 → 재시작 →
      PowerShell 로 `git status` 를 실행해 본다.
    - **프롬프트가 뜨는지는 사용자만 볼 수 있다** — 반드시 사용자에게 물어본다.
      안 뜨면 4줄을 뺄 수 있다(그러면 `commands/womc.md` 5번 절의 임베드도 같이 고친다). 뜨면 그대로 둔다.
    - 확인이 끝나면 `git checkout .claude/settings.json` 으로 되돌린다.
  - **3) `/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지 (감사 5번④)** — 2)가 "필요하다"로 나올 때만.
    - 사용자가 `/fewer-permission-prompts` 를 실행한다(슬래시 명령이라 Claude 가 직접 못 돌린다).
    - `git diff .claude/settings.json` 으로 무엇이 추가됐는지 확인한다. PowerShell 읽기 전용 명령이 들어가면 골격에 4줄을 박는 대신 이 스킬에 맡길 수 있다.
    - 확인이 끝나면 되돌린다.
  - 손댈 파일: `.claude/settings.json`(임시로만, 되돌린다) · 결과 기록은 `docs/HARNESS-AUDIT.md` · `TASKS.md`.
  - 끝난 것으로 보는 조건: 3건 각각이 「확인됨」 또는 「필요 없음」으로 판정되고 그 판정이 두 파일에 적혔을 때.
    골격을 실제로 줄이는 일은 이 항목이 하지 않는다 — 「뺄 수 있음」이 나오면 `plan-feature` 로 넘긴다.
- ✅ **2026-08-10 — v2.0.0·v2.1.0·v2.1.1 의 실사용 검증 5건이 전부 통과했다.** 결과는 아래 「끝난 일」의 각 항목에 적어 두었다.
  검증에 쓴 시험 폴더(`womc-old-test`, v1.20.0 커밋 `481bd76` 의 골격 사본)는 그 안에서 나온 감사 기록을
  `docs/HARNESS-AUDIT.md` v2.1.1 기록으로 옮긴 뒤 지웠다.
  v2.0.0 작업 중의 단계별 기록(「이번 작업의 근거」~「5단계에서 남긴 것」)은 검증이 끝나 역할이 사라졌으므로 이 자리에서 지웠다 —
  결정 이유는 「끝난 일」의 v2.0.0 항목과 `docs/HARNESS-AUDIT.md` 에 남아 있다.

## 끝난 일

- [x] 말투가 한 번도 안 켜지던 버그 수정 — A안 (v2.1.1) — **검증까지 완료 (2026-08-10)**
  - ✅ **육안 검증 통과** — 재시작 뒤 메인 답변이 실제로 원시인 말투로 나왔다. `womc:explore` 서브에이전트 보고는 평문 한국어였다.
    시험 폴더에 `/womc update` 를 돌렸을 때도 `outputStyle` 이 `"womc:womc-caveman"` 으로 들어갔다(갱신 모드 3번의 자동 교정이 동작).
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

- [x] 하네스 감사 절차를 골격에 심음 (v2.1.0) — **검증까지 완료 (2026-08-10)**
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

> 최근 작업만 여기 남긴다. **v1.18.0 이하의 지난 기록은 `docs/CHANGELOG.md` 로 옮겼다** — 옛 결정 이유를 찾을 때는 그 파일을 본다.
> 이 절이 다시 길어지면(대략 항목 5개 이상) 오래된 것부터 같은 형식 그대로 `docs/CHANGELOG.md` 맨 위로 옮긴다.

- [x] Claude Code 2.1.x 기본기능에 맞춘 하네스 간소화 (v2.0.0) — **검증까지 완료 (2026-08-10)**
  - ✅ **검증 3건 통과** — ① 빈 폴더에서 `/womc` → 생성 파일 정확히 6개(레거시 0개).
    ② v1.20.0 골격 사본에서 `/womc update` → 레거시 8개 삭제, 사용자 파일(`SPEC.md`·`PLAN.md`·`TASKS.md`·`.claude/rules/`·추가 allow) 전부 보존,
    **본문만 고친 `.claude/agents/verify.md` 는 「사용자가 고친 것」으로 판정해 남겼다**(판정 기준을 넓힐 필요 없음). ③ 말투는 위 v2.1.1 항목 참조.
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

> 아래 4건은 2026-08-10 하네스 감사 2회(`/womc update` 가 자동 실행)가 남긴 것이다.
> **각 항목의 배경·근거 URL·선택지는 `docs/HARNESS-AUDIT.md` 의 v2.1.1 기록 5번 절에 있다** — 여기엔 확인 방법만 적는다.
> (감사 5번①「`outputStyle` 을 어떻게 고칠 것인가」는 확인됨으로 닫혔다 — v2.1.1 의 A안이 실제로 동작한다.)

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

- [ ] **내장 Task 도구(`TaskCreate`·`/tasks`)가 `TASKS.md` 체크박스를 대체하는지 확인 (감사 5번⑤ — 신규)**
  - `TodoWrite` 는 v2.1.142 부터 기본 비활성이고 구조화된 Task 도구로 대체됐다. 그 목록은 **세션을 껐다 켜도 유지된다.**
    맞다면 골격의 `[ ]`/`[~]`/`[x]` 추적이 중복이다. **단 「손댈 파일·이어 쓸 것·끝난 것으로 보는 조건·확인 방법」 서술은 대체물이 없다** — 그건 남긴다.
  - 확인 방법: 이 저장소에서 `/tasks` 로 항목을 두어 개 만들고 Claude Code 를 껐다 켠 뒤 그대로 남아 있는지 본다.
    남아 있어도 위 네 가지 서술을 담을 자리가 있는지까지 봐야 판단할 수 있다.

- [ ] **`subagentStatusLine`·`/statusline` 을 골격에 들일지 판단 (감사 4번 「새로 챙길 것」 — 신규, 급하지 않음)**
  - `subagentStatusLine`(v2.1.205+)은 서브에이전트 패널 행을 따로 꾸민다. `/statusline` 은 상태줄 스크립트를 자동 생성해 준다.
    후자가 쓸 만하면 골격이 `.claude/statusline.js` 를 직접 들고 갈 필요가 줄어든다.
  - 확인 방법: 시험 폴더에서 `/statusline` 을 한 번 돌려 무엇이 생기는지 보고, 지금 `statusline.js` 가 보여 주는
    5시간·주간 한도까지 나오는지 비교한다. 안 나오면 지금 것을 유지한다.

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
