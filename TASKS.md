# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남 · `[-]` 보류(지금 안 집는다 — 끝난 것이 아니다)

## 지금 하는 일
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

- **2026-08-12 — v2.2.3 의 실사용 검증(`pay` 폴더에서 「설명 방식」 절 교체 확인)은 사용자 결정으로 없앴다.**
  구현은 v2.2.3 으로 끝나 있으나, **그 절이 실제로 교체되는지는 사람이 확인한 적 없는 상태로 남는다.**
  나중에 확인하고 싶어지면 「끝난 일」의 v2.2.3 항목에 지문 3종과 조건이 그대로 있으니 새 항목으로 다시 연다.

- [ ] **v2.4.0 확인 — 다음 기능 작업 한 번으로 겸사 본다 (2026-08-12 남김)**
  - **전용 시험대를 만들지 않는다.** 다음에 `plan-feature` 로 큰 작업을 할 때 자연히 확인된다.
  - 손댈 파일: 없음(관찰만 한다). 이어 쓸 것: `agents/plan.md` 「출력 형식」 4)·5) · `skills/plan-feature/SKILL.md` 3절 두 하위절.
  - 끝난 것으로 보는 조건 — 셋 다 봐야 한다:
    ① `plan` 이 「안 고른 길」과 「확실하지 않은 가정」을 **실제로 채워서** 돌려준다(빈 채로 오거나 "없음"만 반복하면 실패).
    ② 메인이 그것을 쉬운 말로 **사용자에게 보여주고 고르게 한다**(안 보여주고 넘어가면 실패 — 이게 이번 설계의 핵심이다).
    ③ 고른 뒤 「안 고른 길」이 `PLAN.md` 「나중에 / 안 할 것」에, 가정이 「설계 결정」에 옮겨 적힌다.
  - **함께 볼 것 — 되묻기가 너무 잦은지.** 작은 변경에까지 대안을 묻고 있으면 3절의 「건너뛴다」 조항이 안 먹는 것이다.
    그러면 `PLAN.md` 「설계 결정」의 가정 2개 중 두 번째를 근거로 조항을 손본다.
  - 확인 방법: 다음 기능 작업 때 화면을 본다. **`scripts/check-sync.py` 는 이걸 못 잡는다.**
    v2.5.0 이 붙인 6번 검사는 두 파일에 항목 이름(「안 고른 길」·「확실하지 않은 가정」)이 **글자 그대로 남아 있는지만** 본다 —
    실제로 채워 오는지·보여주는지·사용자가 고르는지는 사람이 화면을 봐야 안다.

- [ ] **v2.3.0 확인 — 패치만 올랐을 때 감사 본체가 안 도는지 본다 (2026-08-12 남김)**
  - 원래 위 v2.2.3 검증에 얹혀 있던 항목이다. 그쪽이 없어져 독립 항목으로 옮겼다.
  - **⚠ 먼저 `claude plugin update womc@works-on-my-claude` + Claude Code 재시작.** 안 하면 옛 캐시로 돌아 증거가 안 된다.
  - 손댈 파일: 없음(관찰만 한다). 이어 쓸 것: `skills/harness-audit/SKILL.md` 1단계 · `commands/womc.md` 갱신 모드 7번.
  - 끝난 것으로 보는 조건: 아무 womc 프로젝트에서 `/womc update` 를 돌렸을 때, Claude Code 버전의 **앞 두 자리가 지난 감사와 같으면**
    감사 본체(신기능 조사)가 **안 돌고**, 그러면서도 열린 확인 목록 알림과 "그래도 지금 조사할까요?" 한 줄은 **뜬다.**
  - 확인 방법: `/womc update` 를 실행하고 화면을 본다. **`scripts/check-sync.py` 는 이걸 못 잡는다.**

- ✅ **2026-08-11 — v2.2.2 의 실사용 검증 통과. 거기서 드러난 빈틈은 v2.2.3 으로 곧바로 메웠다.**
  - **시험대**: `C:\Users\s2\Documents\project\pay` (옛 골격 — 버전 표식 없음, 절 7개, 레거시 7개 보유. **git 저장소다.**)
    백업은 `<scratchpad>/pay-backup/`. 갱신 전에 「절차 지키기」와 「프로젝트 상세」 사이에 `## 시험용 내 규칙` 절을 하나 끼워 두고 돌렸다.
  - **① 버그 ① 수정 확인 — 통과.** `/womc update` 뒤에도 그 절이 **같은 자리(「절차 지키기」와 「프로젝트 상세」 사이)에 그대로** 있었다.
    골격에 없던 「서브에이전트 보고 규약」 절은 골격 순서대로 새로 들어갔고, 표식은 `2.2.2` 로 올랐다. 화면에도 남긴 절 목록이 떴다.
  - **② 버그 ② 수정은 이 시험대에서 확인되지 않았다 — 오히려 빈틈이 드러났다.** 그 폴더의 「설명 방식」 절은
    `- 모든 설명은 한국어로 한다.` 한 줄뿐인 **아주 옛 골격 원문**인데, `womc:brevity=` 도 `answer-style.js` 도 없어
    v2.2.2 규칙이 「사용자가 고친 것」으로 보고 **보존해 버렸다.** → 아래 「할 일」 → 「그 밖의 할 일」 ④ 로 새로 적었다.
  - **함께 확인된 것**: 옛 `allow` 4줄 청소(다시 통과) · 레거시 7개(`agents/` 5 · `skills/` 2) 삭제 · `outputStyle`·`statusLine` 추가 ·
    `SPEC.md`·`.gitignore`·`.claude/rules/`·프로그램 코드는 손대지 않음.
  - **`easy-welfare` 는 시험대가 못 됐다** — 12:36 에 먼저 갱신됐는데 사용자 절이 원래 없었고, 화면도 보지 못했다.
    남은 옛 골격 폴더는 `easy-welfare\reference\pay` 하나다.

- ✅ **2026-08-11 — 재시작 뒤 확인을 실행했다. `open:allow-cleanup` 통과·닫음. 갱신 모드 버그 2건을 새로 찾았다.**
  - **1) 전제 확보** — `claude plugin update` 는 이미 최신(`2.2.1`)이었고 사용자가 Claude Code 를 껐다 켠 것을 확인했다.
    설치 캐시는 `~/.claude/plugins/installed_plugins.json` 에서 본다(`version` · `lastUpdated`). GitHub 최신 `commands/womc.md` 도 `2.2.1` 로 같았다.
  - **2) `open:allow-cleanup` — 통과. 닫았다.** 시험대는 `C:\Users\s2\Documents\project\ax`(골격 `1.20.0`, 옛 4줄 보유, **git 저장소가 아니다**).
    갱신 전에 사용자 항목 `Bash(npm test:*)` 를 한 줄 넣어 두고 돌렸다 → **옛 4줄은 전부 사라지고 그 한 줄은 남았다**(확인 뒤 도로 뺐다).
    레거시 8개(`agents/` 5 · `skills/` 2 · `answer-style.js`)도 지워졌고 `outputStyle` 이 `womc:womc-caveman` 으로 새로 들어갔다.
    백업은 `<scratchpad>/ax-backup/` 에 뒀다 — `ax` 는 git 이 아니라 이게 유일한 되돌리기 수단이다.
  - **3) `open:audit-open-notice` — 못 닫았다.** 이 저장소에서 `/womc update` 를 돌렸을 때 열린 확인 3건이 화면에 뜨긴 했으나,
    항목의 조건은 「Claude Code 버전이 지난 감사와 **같아도** 뜨는지」인데 그때 버전이 달랐다(감사 기준 `2.1.226` vs 현재 `2.1.227`).
    **다음에 버전이 같은 상태에서 한 번 더 본다.**
  - **4) 하네스 감사는 건너뛰었다** — 기준 `2.1.226` → 현재 `2.1.227` 로 패치 하나 차이라 소득이 적다고 보고 사용자가 ⓑ(건너뛰기)를 골랐다.
  - **→ 이번에 찾은 갱신 모드 버그 2건은 아래 「할 일」 → 「그 밖의 할 일」에 있다.** 그게 이번 확인의 진짜 소득이다.

- ✅ **2026-08-11 — 열린 확인을 「정본 규약」으로 다시 짰다 (기록 파일 재설계).**
  바로 아래 항목이 남긴 장치가 **전문을 두 파일에 복제**하는 방식이라 곧 어긋났다. 그래서 규약을 바꿨다.
  - **정본은 이 파일 「할 일」 한 곳뿐이다** — 배경·조건·경고·확인 방법 전문은 여기에만 쓴다. **지우지 말 것**(다른 곳에 사본이 없다).
  - `docs/HARNESS-AUDIT.md` 는 머리의 `womc:open-checks` 구획에 **ID 한 줄 + 링크**만 둔다.
  - 열린 항목마다 고정 ID 를 붙였다: `open:allow-cleanup` · `open:statusline-v2` · `open:audit-open-notice`.
    ID 는 항목 제목 줄 끝에 HTML 주석으로 붙인다(주석 안에 `open:` + 이름). **`- [ ]` 항목에만** 붙이고,
    닫거나 보류로 내릴 때 주석도 함께 지운다. (여기 설명 줄에는 **주석 형태를 그대로 쓰지 않는다** — 대조 스크립트가 ID 로 셀 수 있다.)
  - 보류 표기를 `[x]` 에서 **`[-]`** 로 바꿨다 — 표기 자체가 뜻을 담게 되어 각주로 뒤집을 필요가 없어졌다.
  - 손댄 파일: 이 파일 · `docs/HARNESS-AUDIT.md`. (같은 작업의 다른 단계에서 `skills/harness-audit/SKILL.md` ·
    `commands/womc.md` 갱신 모드 7번 · `scripts/check-sync.py` 가 이 구획을 읽고 대조하도록 함께 고쳐진다.)
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK(두 파일의 ID 집합이 어긋나면 DRIFT).
    **알림이 실제로 화면에 뜨는지는 스크립트로 못 잡는다** — 아래 「할 일」의 `open:audit-open-notice` 에서 사람이 확인한다.
  - → **v2.2.1 로 마무리했다.** 손댄 파일 전부와 남긴 이름은 `docs/CHANGELOG.md` 의 v2.2.1 항목에 있다(「끝난 일」에서 옮겨 갔다).

- ✅ **2026-08-11 — `/code-review` 가 이 파일에서 잡은 5건을 고쳤다 (버전 변경 없음, 기록 파일만).**
  손댄 파일: 이 파일 · `docs/HARNESS-AUDIT.md`. 확인: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 OK.
  - ① 「겸사 확인」이 아무것도 못 걸러내던 문제 — **옛 4줄이 있던 폴더에서만 확인이 성립**한다는 조건과,
    이미 `[]` 인 폴더는 시험대가 못 된다는 경고를 「할 일」 항목에 넣었다.
  - ② 「다음 `/womc update` 때 겸사」를 실제로 알려 줄 장치가 없던 문제 — 두 건을 `docs/HARNESS-AUDIT.md` 에도
    「열려 있음」으로 적었다. 자동 감사가 그 파일부터 읽으므로 다음 갱신 때 눈에 걸린다.
    **다만 그때는 조건·확인 방법 전문을 통째로 베껴 적었고, 그래서 두 파일이 곧 어긋났다** — 위 「정본 규약」 항목으로 다시 짰다.
  - ③ 2026-08-11 결정이 `TASKS.md` 에만 있던 문제 — 같은 결정을 `docs/HARNESS-AUDIT.md` 에도 남겼다.
    **다음 감사가 같은 항목을 새로 만들지 말고 기존 항목을 갱신하라고 그 파일에 못 박았다**(중복 방지).
  - ④ 「할 일」 머리말이 v2.1.1 기록 5번 절을 가리키던 오류 — 두 건이 서로 다른 절에 있어 항목마다 따로 가리키게 고쳤다.
  - ⑤ 「할 일」 맨 위가 보류 항목이던 문제 — **열린 것 / 닫힌 것·보류** 두 소절로 재배치했다.
    (그때는 보류 항목(`force-for-plugin`)에 `[x]` 를 붙이고 각주로 뜻을 뒤집었다 — 위 항목에서 `[-]` 보류 표기로 고쳤다.)
  - **다음에 이 두 파일 중 하나를 고칠 때는 다른 하나도 같이 본다** — ②의 장치가 두 파일이 맞물려 있어야 작동한다.

- ✅ **하네스 감사가 남긴 실측 3건 — 전부 끝났다 (2026-08-10).**
  다음에 할 일은 **새 기능**이다 — 「할 일」에 열려 있는 3건은 전부 「급하지 않음」이라 붙잡을 필요가 없다.
  (「할 일」 맨 위 항목을 집으라는 골격 안내는 여기서는 적용하지 않는다. 이유는 「할 일」 머리말에 적어 두었다.)
  - **1) 내장 Task 도구가 `TASKS.md` 체크박스를 대체하는지 (감사 5번⑤)** — **대체 못 한다.** 내장 Task 목록은 세션용이다.
    골격 그대로 유지. 실측 내용은 「할 일」의 닫힌 항목과 `docs/HARNESS-AUDIT.md` v2.1.1 기록 3번·5번⑤ 에 있다.
  - **2) `permissions.allow` 의 PowerShell 4줄이 필요한지 (감사 5번③)** — **필요 없다. 뺄 수 있다.**
    - **실측**: `.claude/settings.json` 의 `allow` 4줄과 `.claude/settings.local.json` 의 같은 3줄을 모두 지우고,
      `~/.claude/settings.json` 의 `"defaultMode": "auto"` 를 프로젝트 설정의 `"defaultMode": "default"` 로 덮은 상태에서
      (상태바 `⏸ manual mode on` 확인) `git status` · `Get-ChildItem` 을 실행 → **둘 다 권한 프롬프트가 뜨지 않았다.**
    - **1차 측정은 무효였다** — 도중에 사용자가 auto 로 바꿔 분류기가 대신 승인하는 상태였다. manual 로 되돌려 다시 측정했다.
      **다음에 권한 실측을 할 때는 측정 직전·직후에 상태바 모드를 반드시 확인한다.**
    - **판정의 범위**: 확인된 것은 "실사용에서 프롬프트가 안 뜬다"까지다. 내장 자동 허용 때문인지 샌드박스 실행 때문인지는
      갈라내지 못했다 — 어느 쪽이든 골격에 4줄을 박을 이유가 없다는 결론은 같다.
    - **측정에 쓴 파일 2개는 백업으로 원상 복구했다** (`.claude/settings.json` · `.claude/settings.local.json`).
      `"defaultMode": "default"` 임시 줄도 함께 사라졌다. `git diff` 에 두 파일이 안 뜨는 것으로 확인했다.
    - **골격에서 실제로 4줄을 빼는 일은 이 항목이 하지 않는다** — 「할 일」로 넘겼고, **v2.2.0 으로 끝났다**
      (아래 「끝난 일」의 v2.2.0 항목 · 「할 일」의 「닫힌 것 · 보류」 소절에 `[x]` 로 있다).
  - **3) `/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지 (감사 5번④)** — **불필요해졌다.**
    2)가 "필요 없음"으로 나와 대체할 대상 자체가 사라졌다. allow 목록을 다시 늘리고 싶어질 때만 꺼낸다.
  - 손댄 파일: `.claude/settings.json`·`.claude/settings.local.json`(둘 다 원상 복구) · 기록은 `docs/HARNESS-AUDIT.md` v2.1.1 기록 5번 · 이 파일.
- ✅ **2026-08-10 — v2.0.0·v2.1.0·v2.1.1 의 실사용 검증 5건이 전부 통과했다.** 결과는 아래 「끝난 일」의 각 항목에 적어 두었다.
  검증에 쓴 시험 폴더(`womc-old-test`, v1.20.0 커밋 `481bd76` 의 골격 사본)는 그 안에서 나온 감사 기록을
  `docs/HARNESS-AUDIT.md` v2.1.1 기록으로 옮긴 뒤 지웠다.
  v2.0.0 작업 중의 단계별 기록(「이번 작업의 근거」~「5단계에서 남긴 것」)은 검증이 끝나 역할이 사라졌으므로 이 자리에서 지웠다 —
  결정 이유는 `docs/CHANGELOG.md` 의 v2.0.0 항목(2026-08-11 에 「끝난 일」에서 그리로 옮겼다)과 `docs/HARNESS-AUDIT.md` 에 남아 있다.

## 끝난 일

- [x] **v2.10.1 — 대화 도중 상태줄이 사라져 돌아오지 않던 버그 수정 (2026-08-20)**
  - 근거: 사용자가 「계속 대화하다 보면 상태창이 없어진다」고 신고했다. 원인을 Claude Code 2.1.237 본체 번들을
    직접 뜯어 확인했다(추정 아님). **상태줄에는 「마지막 값 유지」가 없다** — 상태줄 명령이 0 이 아닌 코드로 끝나거나
    빈 출력을 내면 `onResult(undefined)` 가 그대로 반영돼 상태줄이 **통째로 안 그려진다**(`children: y ? <text> : null`).
    게다가 재실행 조건이 「새 답변 도착 또는 추적 값 8종 변화」뿐이라, 한 번 실패하면 **다음 사건이 올 때까지 빈칸으로 남는다.**
    (`refreshInterval` 이 설정에 없으면 주기 재실행도 없다.) 그래서 「대화하다 보니 없어졌다」로 보인다.
  - 실패를 부르던 자리 2곳: ① `settings.json` 의 명령이 **상대 경로** `node .claude/statusline.js` 라
    실행 위치가 프로젝트 루트가 아니면 종료코드 1 로 죽는다(다른 폴더에서 직접 실행해 재현 확인).
    ② 스크립트에 예외 방어가 없어 어떤 예외든 곧바로 0 이 아닌 종료 → 상태줄 삭제.
  - 손댄 파일: `.claude/settings.json`(라이브) · `.claude/statusline.js`(라이브) ·
    `commands/womc.md`(임베드 사본 2개 + 5번·6번 절 설명 + 갱신 모드 3번 예외) · `PLAN.md` · 이 파일 ·
    버전 표식 6곳(`py scripts/bump-version.py 2.10.1`).
  - 남긴 것 — 다음에 이 파일들을 고칠 사람이 반드시 알아야 하는 것:
    - `settings.json` 의 `statusLine.command` = **`node "${CLAUDE_PROJECT_DIR}/.claude/statusline.js"`**.
      이 변수는 Claude Code 가 자식 프로세스 env 에 넣어 주고, PowerShell 셸일 때는 본체가 `${env:CLAUDE_PROJECT_DIR}` 로
      자동 치환하므로 bash·PowerShell 양쪽에서 동작한다(본체 함수 `lIw` 가 그 치환을 한다 — 2026-08-20 번들 확인).
      **상대 경로로 되돌리지 말 것.**
    - `settings.json` 의 **`statusLine.refreshInterval: 10`**(초). 스키마에 있는 정식 키다(`min(1)`).
      이게 두 번째 안전장치다 — 어떤 이유로 한 번 실패해도 10초 뒤 저절로 되살아난다.
    - `statusline.js` 의 **`emit()` · `FALLBACK` · `process.on("uncaughtException"/"unhandledRejection")` ·
      3초 `guard` 타이머 · `JSON.parse` 실패 시 `d = {}` 로 계속 진행** — 이 다섯이 「무슨 일이 있어도 0 으로 끝나고
      최소 한 줄은 찍는다」를 지키는 부분이다. 걷어내면 버그가 그대로 돌아온다.
      (옛 코드는 파싱 실패 시 `"statusline: invalid input"` 을 찍고 끝냈는데, 이제는 기본값으로 채워 정상 줄을 낸다.)
    - `commands/womc.md` 갱신 모드 3번의 **예외 조항** — 기존 `command` 가 옛 기본값 `node .claude/statusline.js`
      **글자 그대로**면 새 기본값으로 교체한다. 이게 없으면 이미 깔린 프로젝트에 이 고침이 영영 안 닿는다.
  - **확인 방법**: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 종료코드 0. (2026-08-20 통과.)
    스크립트 단독 확인: `echo {} | node .claude/statusline.js; echo $?` → 종료코드 0 이고 빈 출력이 아니어야 한다.
  - **아직 사람이 봐야 하는 것**: 「대화를 오래 해도 상태줄이 안 사라지는지」는 실사용으로만 확인된다.
    이 세션은 **옛 설정으로 시작했으므로 새 설정이 적용되지 않는다** — Claude Code 를 껐다 켠 뒤부터 본다.
    다시 사라지면 원인이 하나 더 있다는 뜻이므로, 그때는 `refreshInterval` 이 되살리는지(10초 안에 돌아오는지)를 먼저 본다.

- [x] **v2.10.0 — 상태줄에 세션 ID 표시 추가 (2026-08-19)**
  - 근거: 사용자가 「모델명·컨텍스트·5시간/주간 한도·폴더명 옆에 세션 ID 도 나오게 해달라」고 요청했다.
    표시 형태는 물어서 **전체 UUID** 로 골랐다(앞 8글자만 자르는 안은 안 골랐다 — `claude --resume <id>` 에 그대로 못 쓴다).
  - 손댄 파일: `commands/womc.md`(임베드 statusline.js 사본 + 설명 3곳: 파일 목록·6번 절 머리말·마무리 안내) ·
    `.claude/statusline.js`(라이브 사본) · `HARNESS.md` · `README.md` · `SPEC.md` · `PLAN.md` · 이 파일 ·
    버전 표식 6곳(`py scripts/bump-version.py 2.10.0` 한 줄 — 손으로 세지 말 것).
  - 남긴 것:
    - `statusline.js` 의 **`const sid = d.session_id || "";`** — stdin JSON 의 `session_id` 를 읽는다.
      출력은 `if (sid) line += ...` 한 줄인데 **앞에 줄바꿈(`
`)이 붙어 상태줄이 2줄이 된다** — 1줄째는 기존 그대로,
      2줄째는 세션 ID 만 **회색(ANSI 90)** 으로 찍는다(폴더명은 1줄째 청록 36). 여러 줄 상태줄은 Claude Code 가 공식 지원한다
      (`https://code.claude.com/docs/en/statusline` 의 「Display multiple lines」 — 2026-08-19 확인).
      값이 없으면(옛 Claude Code 등) 그 칸만 조용히 빠지고 나머지는 그대로 나온다.
    - **정본은 `commands/womc.md` 의 임베드 사본, 라이브 사본은 `.claude/statusline.js`.**
      `scripts/check-sync.py` 1번이 글자 단위로 대조하므로 한쪽만 고치면 DRIFT 다.
    - 최종 형식: 1줄째 `<model> │ <used>k/<ctx>k │ S:<5h>% W:<week>% │ <folder>`, 2줄째 `<session-id>` (파일 3행 주석과 같다).
  - 확인 방법: 샘플 JSON 을 `node .claude/statusline.js` 에 흘려 넣어 세션 ID 가 맨 끝에 붙는지 봤고,
    `{}` 만 넣었을 때 다른 칸이 안 깨지고 2줄째도 안 나오는지 봤다 — 둘 다 통과. `py scripts/check-sync.py` 전 항목 OK.
    **실제 터미널 상태줄에 뜨는 것은 사용자가 Claude Code 를 다시 켜 봐야 확인된다.**
- [x] **v2.9.0 — 하네스 감사가 올린 「새로 들일 것」 후보 3건 반영 (2026-08-19)**
  - 근거: 2026-08-19 하네스 감사(`docs/HARNESS-AUDIT.md` **v2.8.0 기록 4번**)가 후보 3건을 올렸고 사용자가 「반영하자」라고 했다.
    감사 스킬은 반영을 직접 하지 않고 `plan-feature` 로 넘기게 되어 있다 — 그 넘어온 일이 이 항목이다.
  - 손댄 파일: `commands/womc.md`(프론트매터 · 온보딩 2-b 소절 · 온보딩 마무리 안내 · 갱신 ⓐⓑ 이월 · 역방향 제안 ·
    완료 보고 · 온보딩 설명 한 줄) · `agents/implement.md` · `agents/verify.md` · `HARNESS.md` · `SPEC.md` ·
    `PLAN.md` · 이 파일 · `docs/HARNESS-AUDIT.md` · 버전 표식은 `py scripts/bump-version.py 2.9.0` 한 줄로 6곳
    (`.claude-plugin/plugin.json` · `README.md` 제목 · `commands/womc.md` 3 · `CLAUDE.md` 1 — 손으로 세지 말 것).
  - 남긴 것:
    - **① `disable-model-invocation: true`** — `commands/womc.md:5` 프론트매터. `/womc` 는 파일을 새로 쓰는
      **부작용 워크플로**라 모델이 스스로 부르면 안 된다. 근거로 **커스텀 슬래시 명령이 스킬로 통합됐다는 문서**를 확인했다:
      "Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at
      `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."
      → 스킬용 프론트매터 필드가 `commands/womc.md` 에도 유효하다. https://code.claude.com/docs/en/skills
    - **② `effort: high`** — `agents/implement.md:6` · `agents/verify.md:6`. `agents/plan.md:6` 이 이미 쓰던 패턴이다.
      이제 **opus 3종이 모두 `high`** 고, haiku 인 `explore` 만 없다. 근거로 **`effort` 가 서브에이전트 공식
      프론트매터 필드**임을 확인했다: "Effort level when this subagent is active. Overrides the session effort level.
      … Options: `low`, `medium`, `high`, `xhigh`, `max`" https://code.claude.com/docs/en/sub-agents
    - **③ `AGENTS.md` 감지·연결 — 감사 원안(무조건 import)과 다르게 「제안 후 승낙」으로 넣었다**(사용자가 고른 길).
      **자리가 여섯이라 한 자리만 고치면 어긋난다**:
      `commands/womc.md:384` 새 소절 「2-b) 기존 `AGENTS.md` 감지 (있을 때만)」 — 루트 `AGENTS.md` 만 보고,
      줄 수를 세어 사용자에게 묻고, 좋다고 할 때만 `CLAUDE.md` 의 `@SPEC.md` **다음 줄**에 `@AGENTS.md` 를 넣는다(멱등) ·
      `:404` 온보딩 마무리 안내 열거에 「AGENTS 연결」 · `:484`(갱신 ⓑ 구획 교체 경로)와 `:493`(갱신 ⓐ 절 병합 6단계)의
      **`@AGENTS.md` 이월 규칙 — 이게 없으면 `/womc update` 한 번에 연결이 조용히 사라진다** ·
      `:495` 역방향 제안(연결이 없으면 자동으로 넣지 않고 제안만) · `:496` 무엇을 했는지 완료 보고에 한 줄.
    - **`HARNESS.md:21` ↔ `commands/womc.md:153` 은 온보딩 설명 한 줄을 글자 단위로 공유한다**(정본–사본).
      이번에 양쪽을 같이 갱신했다 — 한쪽만 고치면 `scripts/check-sync.py` 1번이 DRIFT 로 잡는다.
    - `SPEC.md:20` 3절 1번 열거에 「루트에 `AGENTS.md` 가 있으면 **물어본 뒤에만** `@AGENTS.md` 로 연결」 한 구절.
    - **안 고른 길 6개와 새 설계 결정 3개**는 `PLAN.md` 의 「나중에 / 안 할 것」·「설계 결정」에 옮겨 적었다.
    - 옛 `v2.5.0` 항목은 「끝난 일」 5개 초과 회전 규칙에 따라 `docs/CHANGELOG.md` 맨 위로 옮겼다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → **전 항목 OK, 버전 `2.9.0`**(열린 확인 ID 4개 일치 포함).
  - **⚠ 아직 실측 안 된 것 — 셋 다 화면으로 확인한 적이 없다. 「동작한다」고 적지 말 것:**
    - **①②는 문서 근거만으로 채택했다.** 확인 방법: Claude Code 를 껐다 켠 뒤 `/womc` 가 명령 목록에 뜨는지,
      손으로 실행되는지 본다. **안 뜨면 `disable-model-invocation` 그 한 줄만 되돌리면 된다.**
      `effort: high` 는 화면 표시가 없어, 프론트매터가 거부되지 않는지(두 에이전트가 정상 기동하는지)로만 본다.
    - **③의 온보딩·갱신 이월도 실제 기존 프로젝트에서 돌려본 적이 없다.** 다음에 기존 코드가 있는 폴더에
      `/womc` 를 깔 때, 이어서 같은 폴더에 `/womc update` 를 한 번 더 돌릴 때 겸사 본다
      (**루트에 `AGENTS.md` 가 있는 폴더라야 시험대가 된다**).
    - **`check-sync.py` 는 셋 다 못 잡는다** — 글자가 파일에 있는지만 보지 실행 중 동작은 못 본다.
  - **열린 확인은 이번에 하나도 닫히지 않았다 — 4건 그대로다.** 다만 `open:import-command` 의 「이어 쓸 것」은
    후보 ③ 이 처리됐다는 사실에 맞춰 고쳤다.

- [x] **v2.8.0 — 답변 말투를 「원시인(케이브맨)」에서 「쉬운 말 + 짧게」로 교체 (2026-08-19)**
  - 근거: 사용자 요청. "케이브맨 규칙 없애자. 이용자가 쉽게 알아들을 수 있게, 최대한 간결하고 짧은 문장으로."
    옛 말투는 짧기는 했지만(2~5단어 명사형 단문) **쉽지는 않았다** — 코딩을 모르는 사용자가 읽는다는
    전제와 어긋났다. 새 말투는 「쉽게」를 첫째, 「짧게」를 둘째로 둔다.
  - 손댄 파일: `output-styles/womc-caveman.md` → **`output-styles/womc-plain.md`**(git mv + 내용 전면 재작성) ·
    `commands/womc.md`(골격 원본 6자리 + 갱신 모드 이주 규칙) · `.claude/settings.json` · `CLAUDE.md` ·
    `SPEC.md` · `HARNESS.md` · `README.md` · `skills/make-rule/SKILL.md` · `PLAN.md` · 이 파일 ·
    버전 표식은 `py scripts/bump-version.py 2.8.0` 한 줄로 6곳.
  - 남긴 것:
    - **새 등록 키는 `womc:womc-plain`**(`settings.json` 의 `outputStyle` 값). 파일명·frontmatter `name` 은
      접두 없이 `womc-plain` 이다 — 접두는 **등록 키에만** 붙는다(v2.1.1 이 겪은 헷갈리기 쉬운 자리).
    - **말투 규칙의 정본은 `output-styles/womc-plain.md` 한 곳**이다. 다른 파일에 규칙을 베껴 적지 않는다.
      요지: 존댓말 평서형 · 한 문장 한 뜻(40자 넘으면 끊기) · 답변 기본 5줄 안 · 전문 용어는 괄호로 풀이 ·
      다음 할 일·되묻는 질문·위험 경고·명령어/숫자는 줄이지 않음 · 정확함이 짧음보다 우선.
    - **`/womc update` 이주 규칙**(`commands/womc.md` 갱신 모드 3번): `outputStyle` 값이
      `"womc:womc-caveman"` 또는 `"womc-caveman"` 이면 `"womc:womc-plain"` 으로 고치고 완료 보고에 알린다.
      그 셋 말고 다른 값이면 사용자가 고른 말투이므로 그대로 둔다. **옛 이름 문자열 2개는 이 규칙 안에만
      일부러 남아 있다** — 지우면 이미 깔린 프로젝트가 새 말투로 못 넘어온다.
    - 옛 `v2.4.0` 항목은 「끝난 일」 5개 초과 회전 규칙에 따라 `docs/CHANGELOG.md` 맨 위로 옮겼다.
  - **`/code-review` 지적 7건을 같은 버전 안에서 전부 반영했다**(아직 커밋 전이라 v2.8.1 을 따로 내지 않았다):
    ① `/womc update` 의 「설명 방식」 절 판정에 **네 번째 지문 `womc-caveman`** 추가 — 없으면 v2.0.0~v2.7.0 프로젝트의
    CLAUDE.md 가 「사용자가 고친 것」으로 오판돼, 없는 스타일을 가리키는 죽은 문장으로 영영 굳는다(가장 컸다).
    ② 그 옆 「판정 근거」 불변식을 판본 6개·세 지문 → **7개·네 지문**으로 갱신 + "말투 이름을 또 바꾸면 지문을 늘려라" 경고.
    ③ 레거시 정리 대상에 `.claude/output-styles/womc-caveman.md` 추가(+ 보존했을 때 안내 한 줄).
    ④ 갱신 모드가 접두 빠진 **새** 이름 `"womc-plain"` 도 교정하되, **꺼낸 파일이 있을 때는 손대지 않는다**(⑤와 짝).
    ⑤ eject 절차에 **4-b 단계** 신설 — 말투를 꺼내면 `outputStyle` 을 접두 없는 `"womc-plain"` 으로 바꿔야 꺼낸 것이 쓰인다.
    ⑥ `PLAN.md` 「설계 결정」이 사라진 `womc-caveman.md` 를 가리키던 두 줄 수정.
    ⑦ 같은 절의 「베껴 적지 않는다」 규칙을 **「한 줄 요지까지만 둔다」**로 고쳐, HARNESS/SPEC/README 의 한 줄 요지와 모순되지 않게 했다.
  - **열린 확인 1건을 새로 열었다 — `open:eject-outputstyle`.** ⑤가 기대는 "꺼낸 출력 스타일은 접두 없는 이름으로
    등록된다"는 **실측하지 않은 가정**이다. 전문은 이 파일 「할 일」에, ID 한 줄은 `docs/HARNESS-AUDIT.md` 머리 구획에 있다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → **전 항목 OK, 버전 `2.8.0`**.
    (1차에 `HARNESS.md` DRIFT 1건이 잡혔다 — 골격 원본과 라이브 문구를 두 사람이 다르게 적어서다. 라이브 문구로 통일해 해소.)
    **말투가 실제로 바뀌는지는 사람이 봐야 한다** — Claude Code 를 껐다 켠 뒤 답변이 쉬운 말·짧은 문장으로 나오는지 육안 확인.

- [x] **v2.7.0 — 하네스 감사(모델 축 첫 실행): 검증을 고정 단계에서 조건부로 내림 (2026-08-18)**
  - 계기: `/womc update` 7번이 자동으로 부른 감사. Claude Code 앞 두 자리는 같았고(`2.1.228` → `2.1.234`),
    **지난 기록에 기준 모델이 없어(모름 → 다름) 모델 축으로 처음 훑었다** — v2.6.0 이 만든 모델 트리거의 첫 실행이다.
    조사 분담: 웹 2갈래는 `general-purpose`, 로컬 1갈래는 `explore`.
  - **가장 큰 것 — 전제가 뒤집혔다.** 공식 프롬프팅 문서가 못박았다: "Claude Opus 5 verifies its own work without being
    told to ... **The same applies to legacy harness scaffolding that adds separate verification steps.**"
    (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
    womc 의 「구현 → 검증」 고정 흐름이 정확히 그 legacy scaffolding 이었다.
  - 손댄 파일: `commands/womc.md` · `CLAUDE.md` · `HARNESS.md` · `skills/plan-feature/SKILL.md` · `agents/verify.md` ·
    `SPEC.md` · `PLAN.md` · `README.md` · `.claude-plugin/plugin.json` · `docs/HARNESS-AUDIT.md` · 이 파일.
  - 남긴 것:
    - **검증이 고정 단계에서 조건부로 내려갔다** — 네 자리를 함께 고쳤다: `CLAUDE.md` 「절차 지키기」의
      "검증을 건너뛰고 다음으로 가자고 하면 ... 한 번 권한다" 줄 삭제 · `CLAUDE.md` 「적극 위임」의 "동작 검증은 `verify` 에" 를
      「고정 단계 아님」으로 교체 · `skills/plan-feature/SKILL.md` **5절**을 「동작 확인 (고정 단계 아님 — 필요할 때만)」으로 교체 ·
      `agents/verify.md` 의 `description` 을 조건부로 좁힘. **`CLAUDE.md` 는 `commands/womc.md` 의 임베드 사본과 쌍이다 —
      한쪽만 고치면 check-sync 1번이 DRIFT 로 잡는다.**
    - **`verify` 에이전트 자체는 남아 있다** — 테스트·실행 로그를 메인 대화에서 떼어내는 값은 모델과 무관하다.
      **뺀 것은 「매번 돈다」는 강제이지 도구가 아니다.** 다시 「매번」으로 되돌리지 말 것(근거는 위 문서).
    - **`HARNESS.md` 에 권한 한계 사실 2줄** — ⓐ `Read` deny 가 Claude Code `2.1.228` 부터 **쓰기까지 함께 막는다** ·
      ⓑ PowerShell 규칙은 별칭까지 잡지만 **Python·Node 스크립트가 대신 읽고 쓰는 건 못 막는다**.
      근거 https://code.claude.com/docs/en/permissions
    - **열린 확인은 4건 닫히고 2건이 새로 열렸다** — 닫힌 넷은 바로 아래 항목, 새 둘은 「할 일」의 「열려 있는 것」 소절.
      `docs/HARNESS-AUDIT.md` 머리의 `womc:open-checks` 구획도 그 2건으로 다시 썼다(**두 파일을 항상 같이 고친다**).
    - 감사 기록 본체는 `docs/HARNESS-AUDIT.md` 의 **v2.7.0 기록**(절 6개). 머리 인용문의 기준 버전·기준 모델도 이번 값으로 올렸다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK(열린 확인 ID **2개** 일치 포함).
  - **아직 사람이 봐야 하는 것**: 검증을 안 돌려도 품질이 안 떨어지는지 · 위임이 실제로 도는지는 스크립트가 못 본다 —
    뒤쪽은 열린 확인 `open:delegation-vs-preset` 으로 넘겼다.

- [x] **열린 확인 4건 닫음 — 2026-08-18 v2.7.0 감사에서 전부 결론이 났다**
  - 넷 다 **골격을 그대로 둔다**는 결론이다. 다시 열지 말 것 — 다시 열려면 아래 근거를 먼저 뒤집어야 한다.
  - [x] ~~`subagentStatusLine`·`/statusline` 을 골격에 들일지~~ → **기각.** 둘 다 실재하나 골격을 대체하지 않는다.
    `subagentStatusLine` 은 서브에이전트 패널의 **행 모양**이고 기본 행이 이미 이름·설명·토큰수를 보여준다.
    `/statusline` 은 `~/.claude/` **전역**에 스크립트를 생성해 주는 명령이라 프로젝트별 고정 산출물인 골격과 역할이 다르다
    (오히려 골격 설정을 덮어쓸 위험). 근거 https://code.claude.com/docs/en/statusline
  - [x] ~~출력 스타일 `force-for-plugin` 으로 `outputStyle` 한 줄을 뺄 수 있는지~~ → **기각(문서 확인).**
    기능은 실재하지만 문서가 "Overrides the user's `outputStyle` setting" 이라고 못박아 **womc 가 켜진 모든 프로젝트에**
    원시인 말투가 강제된다. womc 는 "이 프로젝트에서만" 이 설계이므로 `settings.json` 한 줄을 유지한다.
    근거 https://code.claude.com/docs/en/output-styles
  - [x] ~~골격 `permissions.ask` 가 실제로 「항상 허용」을 이기는지~~ → **통과.**
    "Rules are evaluated in order: **deny, then ask, then allow.**" + "a matching ask rule prompts even when a more
    specific allow rule also matches the same call." 「항상 허용」은 `settings.local.json` 에 allow 로 저장되므로
    `ask` 목록은 눌러도 **다시 묻는다.** `PowerShell(...)` 표기도 문서에 정식 기재다(`:*` 접미사 = 뒤 ` *`).
    근거 https://code.claude.com/docs/en/permissions  → **v2.5.0 의 전제가 확인됐다. 되돌릴 것 없음.**
  - [x] ~~버전이 안 올라가도 `/womc update`·감사가 열린 확인 목록을 알리는지~~ → **통과.**
    이번 실행에서 **버전이 안 올라간 상태로도** `/womc update` 가 열린 확인 4건을 한 줄씩 알렸다(2026-08-18 실측).
    v2.2.1 「정본 규약」 재설계가 만든 장치가 실제로 돈다.
  - 남긴 것: 넷 다 `docs/HARNESS-AUDIT.md` **v2.7.0 기록 5번**에 근거 원문과 함께 있다.
    v2.2.4 기록 5번의 `force-for-plugin` 「실측 필요」 자리도 「확인됨(v2.7.0 에서 기각)」으로 고쳐 뒀다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 열린 확인 ID 가 **2개**로 줄고 두 파일이 일치.

> 최근 작업만 여기 남긴다. **v2.6.0 이하의 지난 기록은 `docs/CHANGELOG.md` 로 옮겼다** — 옛 결정 이유를 찾을 때는 그 파일을 본다.
> 이 절이 다시 길어지면(대략 항목 5개 이상) 오래된 것부터 같은 형식 그대로 `docs/CHANGELOG.md` 맨 위로 옮긴다.

## 할 일

> **이 절이 열린 확인의 정본이다.** 배경·조건·경고·확인 방법 **전문은 여기에만** 쓴다.
> `docs/HARNESS-AUDIT.md` 에는 ID 한 줄과 링크만 둔다. **전문은 여기 한 곳뿐 — 지우지 말 것**(다른 곳에 사본이 없다).
>
> **2026-08-18 v2.7.0 감사에서 그때까지 열려 있던 확인 4건이 전부 닫혔다** — 넷의 결론(통과인지 기각인지)과
> 근거 URL 은 「끝난 일」의 「열린 확인 4건 닫음」 항목에 있다. **지금 열려 있는 확인은 4건이다.**
> 그중 둘은 그 v2.7.0 감사가 새로 연 것이고 — 입력 리다이렉션(`cat < .env` 류)이 `.env` deny 를 우회하는지(`open:env-deny-redirect`) ·
> 「적극 위임」이 하네스의 「Agent tool 을 부르지 마라」를 이기는지(`open:delegation-vs-preset`) —
> 하나는 v2.8.0 `/code-review` 가(`open:eject-outputstyle`), 하나는 2026-08-19 감사가 열었다(`open:import-command`).
> (`open:allow-cleanup` 은 2026-08-11 에 통과·닫았다 — 「닫힌 것 · 보류」 소절 참고.)
> **「열린 확인」 2건과 별개로, 아래 「그 밖의 할 일」 소절에 보통 할 일이 따로 있다** — 그건 확인이 아니라 고칠 것이라 ID 주석이 없다.
> **2026-08-11 — 갱신 모드 버그 ①②④는 v2.2.2·v2.2.3 으로 다 고쳤다. 여기 남은 것은 ③ 하나다.**
> **지금 집을 것은 이 소절이 아니라 「지금 하는 일」의 맨 위 열린 항목이다** — 2026-08-14 현재 v2.4.0 확인, 그다음이 v2.3.0 확인이다.
> (버전 이름 대신 **맨 위 열린 항목**으로 가리킨다 — 이름을 박아 두면 새 항목이 생길 때마다 이 줄이 낡는다. 실제로 그렇게 낡아 리뷰에 걸렸다.)
> **감사 기록의 파생 자리**: 열린 4건 중 2건은 `docs/HARNESS-AUDIT.md` v2.7.0 기록의 6번 절이고
> (`open:env-deny-redirect` = 6번①, `open:delegation-vs-preset` = 6번②),
> `open:eject-outputstyle` 은 v2.8.0 의 `/code-review` 지적에서, `open:import-command` 는
> 2026-08-19 감사(`docs/HARNESS-AUDIT.md` v2.8.0 기록 6번)에서 나왔다.
>
> **열린 확인은 전부 「급하지 않음」이다** (2026-08-19 현재 4건). 전부 확인일 뿐이고 실패해도 세팅이 깨지지 않는다.
> 전용 시험 폴더를 만들어 붙잡지 않고, 다음에 `/womc update` 나 상태줄을 손볼 일이 생겼을 때 겸사 확인한다.
> 그래서 지금은 **새 기능을 시작해도 되는 상태다** — 하던 것부터 끝내라고 말릴 항목이 없다.
>
> **읽는 순서 주의 (2026-08-11)**: 골격 안내는 「할 일」 **맨 위** 항목을 집으라고 하지만, 이 파일에서는 그렇게 하면
> 안 된다. 그래서 **열린 항목을 위로, 닫힌 것·보류를 아래로** 재배치했다. 위쪽 「열려 있는 것」 `[ ]` 항목은 전부 「급하지 않음」이라
> 지금 집을 일이 아니다. **집을 것은 그 아래 「그 밖의 할 일」이다.** 아래 `[-]` 보류 항목은 **집지 않는다.**
>
> **잊히지 않게 하는 장치 (2026-08-11 재설계)**: 열린 확인은 `docs/HARNESS-AUDIT.md` 머리의
> `womc:open-checks` 구획에 **ID 한 줄씩만** 올라간다(전문 정본은 여기 `TASKS.md`).
> `harness-audit`(`skills/harness-audit/SKILL.md` 1단계)과 `/womc update`(갱신 모드 7번)는 **버전이 안 올라가도**
> 그 구획을 읽어 열린 확인 목록을 화면에 알린다. 두 파일의 ID 집합이 어긋나면 `scripts/check-sync.py` 가 DRIFT 로 잡는다.
> **한쪽만 고치면 이 장치가 끊긴다** — 두 파일을 항상 같이 고친다.

### 열려 있는 것 (넷 다 급하지 않음)

- [ ] **입력 리다이렉션(`cat < .env` 류)이 골격의 `.env` deny 를 우회하는지 실측 — 급하지 않음 · 다음에 `.env` 를 쓰는 폴더에서 겸사** <!-- open:env-deny-redirect -->
  - 2026-08-18 v2.7.0 감사가 연 항목이다. Claude Code `2.1.232` 가 Bash **입력 리다이렉션**을 권한 검사 대상에 넣었다가
    `2.1.233` 에서 되돌렸다("Reverted 2.1.232 Bash permission changes for Cygwin symlinks and input redirections").
    **되돌린 지금 `cat < .env` 가 골격의 `.env` deny 를 우회하는지 확인 못 했다.**
  - 손댈 파일: 없음(관찰만 한다). 우회로 판명되면 `HARNESS.md` 의 **권한 한계 설명**을 고친다 —
    골격 `deny` 목록 자체는 그대로다(리다이렉션은 경로 규칙으로 막을 수 있는 것이 아니다).
  - 이어 쓸 것: `HARNESS.md` 에 v2.7.0 이 더한 한계 2줄(ⓐ `Read` deny 가 `2.1.228` 부터 쓰기까지 막는다 ·
    ⓑ 프로그램이 대신 읽고 쓰는 건 못 막는다)이 고칠 자리다. deny 목록의 정본은 `commands/womc.md` 의
    `.claude/settings.json` 템플릿, 라이브 사본은 `.claude/settings.json`(한쪽만 고치면 check-sync 1번이 DRIFT 로 잡는다).
    근거 문서 https://code.claude.com/docs/en/permissions
  - 끝난 것으로 보는 조건: 막히는지 안 막히는지 사람이 화면으로 확인하고, **안 막히면 `HARNESS.md` 문구까지 고친** 상태.
  - 확인 방법: 아무 프로젝트에 더미 `.env`(가짜 값만 넣는다)를 두고 Bash 로 `cat < .env` 를 시켜 차단되는지 본다.
    `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 로는 못 잡는다(설정이 파일에 있는지만 본다).

- [ ] **「적극 위임」이 하네스의 「Agent tool 을 부르지 마라」를 이기는지 관찰 — 급하지 않음 · 다음 기능 작업 때 겸사** <!-- open:delegation-vs-preset -->
  - 2026-08-18 v2.7.0 감사가 연 항목이다. **womc 의 위임 설계 전체가 이 대결의 결과에 걸려 있다.**
  - 무엇이 맞서는가: Claude Code 의 `claude_code` 프리셋은 모델이 Opus 5 일 때 시스템 프롬프트에
    "시키지 않으면 Agent tool 을 부르지 마라" 한 줄을 **자동으로 넣는다**(https://code.claude.com/docs/en/agent-sdk/subagents).
    `CLAUDE.md` 「적극 위임」은 정반대를 시킨다. **어느 쪽이 이기는지, 실제 위임률이 어떤지 못 봤다.**
  - 손댈 파일: 없음(관찰만 한다). 위임이 안 돌면 `CLAUDE.md` 「적극 위임」 문구를 더 강하게 쓰거나
    `skills/plan-feature/SKILL.md` 에 명시적 위임 지시를 넣는다. **그때 `commands/womc.md` 의 임베드 사본도 함께 고친다**(한쪽만 고치면 DRIFT).
  - 이어 쓸 것: `CLAUDE.md` 「적극 위임」의 문턱값 3가지(파일 3개 이상 · 긴 로그 · 독립 갈래 2개 이상) ·
    근거 원문은 `docs/HARNESS-AUDIT.md` v2.7.0 기록 **2번②**.
  - 끝난 것으로 보는 조건: 파일 3개 이상을 뒤져야 하는 작업에서 `explore` 가 실제로 불리는지 사람이 화면으로 확인하고,
    안 불리면 문구를 어떻게 고칠지 **결정까지 마친** 상태.
  - 확인 방법: 새 세션에서 파일 3개 이상을 뒤져야 하는 일을 시키고 서브에이전트가 실제로 뜨는지 본다.
    **`check-sync.py` 는 못 잡는다** — 문구가 파일에 있는지만 보지 실행 중에 불리는지는 못 본다.

- [ ] **꺼낸 출력 스타일이 접두 없는 이름으로 등록되는지 실측 — 급하지 않음 · 다음에 말투를 손볼 때 겸사** <!-- open:eject-outputstyle -->
  - 2026-08-19 v2.8.0 의 `/code-review` 가 연 항목이다. **`/womc eject womc-plain` 이 지금은 헛일일 수 있다.**
  - 무엇이 불확실한가: 출력 스타일 조회는 **등록 키 정확일치**다. 플러그인이 주는 것은 `womc:womc-plain`,
    프로젝트 `.claude/output-styles/` 에 꺼낸 것은 **접두 없이 `womc-plain`** 으로 등록된다고 **가정**했다.
    이 가정 위에서 `commands/womc.md` 의 eject 절차 4-b 단계가 `settings.json` 값을 `"womc-plain"` 으로 바꾸고,
    갱신 모드 3번은 그 값을 **파일이 있을 때만** 교정하지 않고 놔둔다. **가정이 틀리면 두 자리가 같이 틀린다.**
  - 손댈 파일: 틀린 것으로 판명되면 `commands/womc.md` 의 **eject 절차 4-b 단계**와 **5번 안내의 말투 불릿**,
    그리고 **갱신 모드 3번의 `"womc-plain"` 조건부 교정** 세 자리를 함께 고친다(한 자리만 고치면 어긋난다).
  - 이어 쓸 것: 등록 키 규칙의 근거 설명은 `commands/womc.md` 의 `.claude/settings.json` 설명 절에 있다(접두 함정).
    v2.1.1 이 같은 함정으로 겪은 버그 기록은 `PLAN.md` 버전 이력 v2.1.1 항목.
  - 끝난 것으로 보는 조건: 꺼낸 파일이 실제로 쓰이는지 사람이 화면으로 확인하고,
    **안 쓰이면 위 세 자리 문구까지 고친** 상태.
  - 확인 방법: 아무 프로젝트에서 `/womc eject womc-plain` 을 한 뒤 꺼낸 파일의 문구를 알아보게 고치고,
    `settings.json` 의 `outputStyle` 을 `"womc-plain"` 으로 바꿔 Claude Code 를 껐다 켠다. 고친 문구대로 답하는지 본다.
    안 먹으면 `/config` 의 Output style 목록에 꺼낸 쪽이 뜨는지도 함께 본다.
    `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 로는 못 잡는다(문구가 파일에 있는지만 본다).
  - **2026-08-19 감사 — 가정의 절반이 문서로 확인됐다(항목은 그대로 열어 둔다).**
    출력 스타일 문서 원문: "The file name becomes the style name unless you set `name` in the frontmatter."
    → 프로젝트 `.claude/output-styles/womc-plain.md` 는 **접두 없이 `womc-plain`** 으로 등록된다. womc 가 세운 가정이 맞다.
    https://code.claude.com/docs/en/output-styles
    남은 절반(플러그인이 주는 쪽이 `womc:womc-plain` 으로 등록되는지)은 문서에 없다 — 다만 이 저장소가 그 값으로
    실제 동작 중이라 사실상 확인된 셈이다. **끝난 것으로 보는 조건이 「사람이 화면으로 확인」이라 자동으로 닫지 않았다.**
    닫으려면 위 「확인 방법」을 한 번 돌려 보면 된다.

- [ ] **`/import` 가 womc 온보딩 병합과 겹치거나 충돌하는지 실측 — 급하지 않음 · 다음에 기존 프로젝트에 `/womc` 를 깔 때 겸사** <!-- open:import-command -->
  - 2026-08-19 감사가 연 항목이다. **온보딩 절차가 이미 있는 기능을 손으로 다시 하고 있을 수 있다.**
  - 무엇이 불확실한가: 공식 문서(memory)는 `2.1.213+` 의 `/import` 가 `AGENTS.md`·MCP 서버·서브에이전트·스킬을
    한 번에 끌어온다고만 적는다. womc 온보딩은 그와 별개로 ⓐ 코드를 훑어 `SPEC.md` 초안을 쓰고
    ⓑ 기존 `CLAUDE.md`·`.claude/settings.json` 에 `womc:begin/end` 구획을 병합한다.
    **겹치는 범위가 어디까지인지, 둘을 같이 돌리면 충돌하는지 못 봤다.** https://code.claude.com/docs/en/memory
  - 손댈 파일: 겹치는 것으로 판명되면 `commands/womc.md` 의 「기존 프로젝트 온보딩」 2절에서 겹치는 단계를 빼고
    `/import` 를 먼저 돌리라고 안내한다. 안 겹치면 아무것도 안 고친다(관찰만).
  - 이어 쓸 것: 온보딩 병합 절차의 정본은 `commands/womc.md` 「기존 프로젝트 온보딩」 2절.
    같은 감사가 올린 후보 ③(`AGENTS.md` 감지 → `@AGENTS.md` import)은 **v2.9.0 에서 이미 처리됐다** —
    무조건 import 가 아니라 **「제안 후 승낙」** 방식이고, 자리는 온보딩 2-b 소절이다(「끝난 일」의 v2.9.0 항목 참고).
    **이 항목에 남은 것은 `/import` 와 겹치는지 하나뿐이다.**
  - 끝난 것으로 보는 조건: `/import` 가 무엇을 끌어오는지 화면으로 확인하고, 겹치면 `commands/womc.md` 문구까지 고친 상태.
  - 확인 방법: 기존 코드가 있는 아무 폴더에서 `/import` 를 돌려 무엇을 끌어오는지 보고,
    이어서 `/womc` 를 돌려 온보딩이 같은 일을 또 하는지 본다.
    `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 로는 못 잡는다(문구가 파일에 있는지만 본다).

### 그 밖의 할 일 (열린 확인 아님 — 고칠 것)

- [x] ~~**① 갱신 모드가 사용자가 `CLAUDE.md` 에 덧붙인 절을 통째로 날린다**~~ · [x] ~~**② 「설명 방식」 절 보존 규칙이 그 절을 옛 골격에 영구히 묶는다**~~
  → **둘 다 v2.2.2 로 고쳤다 (2026-08-11).** 무엇을 어떻게 바꿨는지는 `docs/CHANGELOG.md` 의 v2.2.2 항목에 있다(「끝난 일」에서 옮겨 갔다).
  **①은 같은 날 `pay` 폴더에서 실사용으로 통과를 확인했다.** ②는 그 시험대에서 확인되지 않았고 대신 아래 ④ 가 드러났다.

- [x] ~~**④ 「설명 방식」 절 판정이 아주 옛 골격 판을 「사용자 커스텀」으로 오판한다**~~
  → **v2.2.3 으로 고쳤다 (2026-08-11).** 지문에 「본문이 `- 모든 설명은 한국어로 한다.` 한 줄뿐일 때」를 더했다.
  역대 판본이 6개뿐임을 git 전수 조사로 확인했으므로 이 지문 셋이면 완전하다 — 「끝난 일」의 v2.2.3 항목 참고.
  **실제로 교체되는지는 아직 사람이 못 봤고, 앞으로도 예정에 없다** — 그 검증 항목은 2026-08-12 에 사용자 결정으로 없앴다.

- [ ] **③ 감사 스킬이 `womc:open-checks` 구획을 「새로 만들」 줄 모른다**
  - `skills/harness-audit/SKILL.md` **6단계**는 `docs/HARNESS-AUDIT.md` 가 없으면 새로 만들라고 하지만,
    그때 **`<!-- womc:open-checks:begin -->` ~ `<!-- womc:open-checks:end -->` 앵커 구획을 만들라는 지시가 없다.**
    **5단계**는 「구획에 한 줄 더한다」고만 해서, 구획이 없는 프로젝트에서는 **더할 자리가 없다.**
  - 지금은 다른 프로젝트에 열린 항목이 없어 무해하지만, **생기면 걸린다.**
  - 손댈 파일: `skills/harness-audit/SKILL.md`
  - 이어 쓸 것: 앵커 문자열 `womc:open-checks`(begin/end). `scripts/check-sync.py` 5번 검사가 이 구획을 읽는다.
  - 끝난 것으로 보는 조건: 6단계에 **파일이 없을 때 앵커 구획까지 만드는 지시**가 들어가고,
    5단계에 **「구획이 없으면 그때 만든다」** 가 들어감.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 전 항목 OK
    (이 검사가 직접 잡지는 못하므로 **문구 확인으로 대신한다**).

### 닫힌 것 · 보류 (집지 않는다)

- [x] ~~**v2.2.0 갱신 모드가 옛 `allow` 4줄을 실제로 지우는지 확인**(`open:allow-cleanup`)~~
  → **통과. 닫았다 (2026-08-11).** 시험대 `C:\Users\s2\Documents\project\ax`(골격 `1.20.0`, 옛 4줄 보유).
  갱신 전에 사용자 항목 `Bash(npm test:*)` 를 한 줄 넣어 두고 `/womc update` 를 돌렸더니 **옛 4줄만 사라지고 그 한 줄은 남았다.**
  플러그인 캐시 `2.2.1` + Claude Code 재시작 뒤에 돌린 것이라 증거로 성립한다. 자세한 것은 「지금 하는 일」의 2026-08-11 항목.

- [x] ~~**골격에서 `permissions.allow` 의 PowerShell 4줄을 뺀다**~~ → **v2.2.0 으로 끝났다 (2026-08-10).** 「끝난 일」 참고.

- [x] ~~**`/fewer-permission-prompts` 로 allow 목록을 대체할 수 있는지 확인 (감사 5번④)**~~
  → **불필요해졌다 (2026-08-10).** 위 항목이 "필요 없음"으로 나와 대체할 대상 자체가 사라졌다.
  allow 목록을 다시 늘리고 싶어질 때만 꺼낸다.

- [x] ~~**내장 Task 도구(`TaskCreate`·`/tasks`)가 `TASKS.md` 체크박스를 대체하는지 확인 (감사 5번⑤)**~~
  → **확인됨: 대체 못 한다 (2026-08-10). 골격은 그대로 둔다.**
  - 실측: 세션 A 에서 `TaskCreate` 로 항목 1개 생성 → Claude Code 재시작 → 새 세션에서 `TaskList` 가 `No tasks found`,
    사용자가 `/tasks` 로 본 화면도 빈 목록이었다. 내장 Task 목록은 **세션용**이라 세션을 넘는 인수인계에 못 쓴다.
    (그 사이 `/clear` 도 실행됐으므로 소실 원인이 재시작인지 `/clear` 인지는 구분 안 되지만, 어느 쪽이든 결론은 같다.)
  - 그래서 `TASKS.md` 의 `[ ]`/`[~]`/`[x]` 와 「손댈 파일·이어 쓸 것·완료 조건·확인 방법」 서술을 **전부 유지한다.**
    `docs/HARNESS-AUDIT.md` v2.1.1 기록 3번의 「뺄 수 있음」 판정도 이것으로 기각했다.

- [-] **`force-for-plugin: true` 가 이 판에서 실제로 먹는지 확인 (감사 5번②)** — **보류. 집지 않는다.**
  A안으로 고쳤으므로 지금은 필요 없다. 나중에 "프로젝트마다 `outputStyle` 을 박지 않게" 하고 싶어질 때 **새 항목으로 다시 연다.**
  - 다시 열 때의 확인 방법(보관): `output-styles/womc-caveman.md` frontmatter 에 넣고 플러그인 재설치 → 재시작 →
    **settings.json 에 `outputStyle` 이 아예 없는 폴더**에서 메인 답변이 원시인 말투로 나오는지 본다.
  - **2026-08-18 — 다시 열 이유가 없어졌다.** v2.7.0 감사가 문서로 기각했다: 이 옵션은 "Overrides the user's
    `outputStyle` setting" 이라 **womc 가 켜진 모든 프로젝트에** 말투를 강제한다("이 프로젝트에서만"이 womc 설계다).
    결론은 「끝난 일」의 「열린 확인 4건 닫음」 항목. 보류 표기는 기록으로 남겨 둔다.

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
