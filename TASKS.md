# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[x]` 끝남 · `[-]` 보류(지금 안 집는다 — 끝난 것이 아니다)

## 지금 하는 일
(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 「끝난 일」의 결정 이유를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

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
  - → **v2.2.1 로 마무리했다.** 손댄 파일 전부와 남긴 이름은 아래 「끝난 일」의 v2.2.1 항목에 있다.

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
  결정 이유는 「끝난 일」의 v2.0.0 항목과 `docs/HARNESS-AUDIT.md` 에 남아 있다.

## 끝난 일

- [x] 열린 확인을 「정본 규약」으로 다시 짬 + 서브에이전트 모델 조정 (v2.2.1) — **2026-08-11**
  - 근거: `/code-review` 가 기록 파일에서 확정한 결함 10건. 전문을 두 파일에 복제하던 옛 방식이 곧 어긋났다(위 「지금 하는 일」 맨 위 항목).
  - 손댄 파일: `TASKS.md`(이 파일) · `docs/HARNESS-AUDIT.md` · `skills/plan-feature/SKILL.md` ·
    `skills/harness-audit/SKILL.md` · `commands/womc.md`(갱신 모드 3번·7번) · `scripts/check-sync.py` ·
    `agents/implement.md` · `agents/verify.md` · `SPEC.md` · `PLAN.md` · `.claude-plugin/plugin.json`
  - 남긴 것:
    - **정본은 이 파일 「할 일」 한 곳이다.** 배경·조건·경고·확인 방법 전문은 여기에만 쓰고,
      `docs/HARNESS-AUDIT.md` 머리의 앵커 구획 **`<!-- womc:open-checks:begin -->` ~ `<!-- womc:open-checks:end -->`** 에는
      ID 한 줄 + 링크만 둔다. **두 파일은 항상 같이 고친다** — 한쪽만 고치면 아래 대조 검사가 DRIFT 로 잡는다.
    - **열린 확인 ID 3개**: `open:allow-cleanup` · `open:statusline-v2` · `open:audit-open-notice`(이번 장치의 동작 확인용 신설).
      ID 는 항목 제목 줄 끝에 HTML 주석으로 붙이고 **`- [ ]` 항목에만** 붙인다. 닫거나 보류로 내릴 때 주석도 함께 지운다.
    - **보류 표기 `[-]` 신설** — `[x]` 에 각주를 달아 뜻을 뒤집던 방식을 폐기했다(`skills/plan-feature/SKILL.md` 표기 어휘 + 뜻 뒤집기 금지 문장).
    - **`scripts/check-sync.py` 에 5번째 검사 「열린 확인 ID 대조」 추가** — 상수 `OPEN_BEGIN`/`OPEN_END` 로 AUDIT 앵커 구획을 잘라
      백틱 ID 집합을 뽑고, `TASKS.md` 의 ID 주석 집합과 대조한다. 어긋나면 DRIFT + 양쪽 차집합 출력.
      ID 주석이 `- [ ]` 아닌 줄에 있어도 DRIFT.
    - **알림 장치**: `skills/harness-audit/SKILL.md` 1단계와 `commands/womc.md` 갱신 모드 7번은
      Claude Code 버전이 지난 감사와 **같아도** 앵커 구획을 읽어 열린 확인 목록을 화면에 알린다(멈추기 전에 알린다).
      감사 5단계에 중복 생성 금지·ID 주석·전문은 TASKS 에만, 6단계에 구획 갱신 의무를 못 박았다.
    - 갱신 모드 3번은 옛 `allow` 4줄 청소 결과를 **완료 보고에 적어야** 하고, 7번은 그 결과를 `open:allow-cleanup` 의 근거로 사용자에게 확인받는다.
    - **서브에이전트 모델**: `agents/implement.md` · `agents/verify.md` 를 `sonnet` → **`opus`**.
      현재 4종 = explore `haiku` · plan `opus` · implement `opus` · verify `opus` (`SPEC.md` 3항 3번도 같이 갱신).
    - 버전은 `py scripts/bump-version.py 2.2.1` 한 줄로 6곳을 올렸다(손으로 세지 말 것).
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 9항목 전부 OK, 버전 `2.2.1`.
    **알림이 실제로 화면에 뜨는지는 스크립트로 못 잡는다** — 아래 「할 일」의 `open:audit-open-notice` 에서 사람이 확인한다.

- [x] 골격에서 `permissions.allow` 의 PowerShell 4줄을 뺌 (v2.2.0) — **2026-08-10**
  - 근거: 같은 날 실측(위 「지금 하는 일」의 2) · `docs/HARNESS-AUDIT.md` v2.1.1 기록 5번③). **다시 실측하지 말 것.**
  - 손댄 파일: `.claude/settings.json` · `commands/womc.md`(3자리) · `HARNESS.md` · `README.md`(2자리) · `SPEC.md` · `PLAN.md` · 이 파일 · `.claude-plugin/plugin.json`
  - 남긴 것:
    - `allow` 는 이제 **빈 배열**이다(키는 남겼다 — 사용자가 나중에 채울 자리). `.claude/settings.json` 과
      `commands/womc.md` 5번 절 임베드 **두 곳을 같은 값으로** 고쳤다. 한쪽만 고치면 `check-sync.py` 가 DRIFT 로 잡는다.
    - **갱신 모드 3번에 옛 4줄 청소를 넣은 것이 절반의 핵심이다** (`commands/womc.md` 갱신 모드 3번) —
      `allow` 에 옛 기본값 4줄이 **그대로** 있으면 그 4개만 지운다. **다른 항목은 사용자가 넣은 것이라 안 건드린다.**
      이 예외가 없으면 이미 깔린 프로젝트가 영영 옛 4줄을 안고 간다(v2.1.1 의 `outputStyle` 자동 교정과 같은 패턴이다).
    - 문구를 고친 자리는 **`HARNESS.md` ↔ `commands/womc.md` HARNESS 임베드 사본이 글자 그대로 같아야 한다** — 둘 다 같이 고쳤다.
    - 버전은 `py scripts/bump-version.py 2.2.0` 한 줄로 6곳을 올렸다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.2.0`.
    **갱신 모드의 옛 4줄 청소가 실제로 도는지는 스크립트로 못 잡는다** — 위 「할 일」의 남은 항목에서 사람이 확인한다.

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
      B안은 「할 일」의 「닫힌 것 · 보류」 소절에 `[-]` 보류로 있다(집지 않는다).
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

> 최근 작업만 여기 남긴다. **v1.19.0 이하의 지난 기록은 `docs/CHANGELOG.md` 로 옮겼다** — 옛 결정 이유를 찾을 때는 그 파일을 본다.
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

## 할 일

> **이 절이 열린 확인의 정본이다.** 배경·조건·경고·확인 방법 **전문은 여기에만** 쓴다.
> `docs/HARNESS-AUDIT.md` 에는 ID 한 줄과 링크만 둔다. **전문은 여기 한 곳뿐 — 지우지 말 것**(다른 곳에 사본이 없다).
>
> 2026-08-10 하네스 감사 2회(`/womc update` 가 자동 실행)가 넘긴 4건은 **③④⑤ 가 닫혔고, ②는 보류다** —
> 전부 아래 「닫힌 것 · 보류」 소절에 있다. **지금 열려 있는 일은 3건**이다:
> v2.2.0 갱신 모드 확인(`open:allow-cleanup`) · `subagentStatusLine` 판단(`open:statusline-v2`) ·
> 열린 확인 알림이 실제로 뜨는지(`open:audit-open-notice`, 2026-08-11 재설계가 새로 만든 것).
> **감사 기록의 파생 자리는 항목마다 다르다**: `open:statusline-v2` 는 `docs/HARNESS-AUDIT.md` v2.1.1 기록
> **4번 절 「새로 챙길 만한 것 2가지」**, `open:allow-cleanup` 은 같은 기록 **5번③ 의 「이후 이력 ②」**
> (①은 v2.2.0 완료 기록이고, **②가 열린 확인**이다).
>
> **2026-08-11 — 열린 3건은 전부 「급하지 않음」이다.** 셋 다 확인일 뿐이고 실패해도 세팅이 깨지지 않는다.
> 전용 시험 폴더를 만들어 붙잡지 않고, 다음에 `/womc update` 나 상태줄을 손볼 일이 생겼을 때 겸사 확인한다.
> 그래서 지금은 **새 기능을 시작해도 되는 상태다** — 하던 것부터 끝내라고 말릴 항목이 없다.
>
> **읽는 순서 주의 (2026-08-11)**: 골격 안내는 「할 일」 **맨 위** 항목을 집으라고 하지만, 이 파일에서는 그렇게 하면
> 안 된다. 그래서 **열린 항목을 위로, 닫힌 것·보류를 아래로** 재배치했다. 위쪽 `[ ]` 세 건은 전부 「급하지 않음」이라
> 지금 집을 일이 아니고, 새 기능을 시작하는 것이 맞다. 아래 `[-]` 보류 항목은 **집지 않는다.**
>
> **잊히지 않게 하는 장치 (2026-08-11 재설계)**: 열린 확인은 `docs/HARNESS-AUDIT.md` 머리의
> `womc:open-checks` 구획에 **ID 한 줄씩만** 올라간다(전문 정본은 여기 `TASKS.md`).
> `harness-audit`(`skills/harness-audit/SKILL.md` 1단계)과 `/womc update`(갱신 모드 7번)는 **버전이 안 올라가도**
> 그 구획을 읽어 열린 확인 목록을 화면에 알린다. 두 파일의 ID 집합이 어긋나면 `scripts/check-sync.py` 가 DRIFT 로 잡는다.
> **한쪽만 고치면 이 장치가 끊긴다** — 두 파일을 항상 같이 고친다.

### 열려 있는 것 (셋 다 급하지 않음)

- [ ] **v2.2.0 갱신 모드가 옛 `allow` 4줄을 실제로 지우는지 확인 — 급하지 않음 · 다음 `/womc update` 때 겸사 확인 (2026-08-11 결정)** <!-- open:allow-cleanup -->
  - **일부러 전용 시험 폴더를 만들지 않는다.** 다음에 `/womc update` 를 쓸 일이 생겼을 때 겸사 확인한다.
  - **⚠ 항목 공통 전제 — 플러그인 재설치 + Claude Code 재시작 뒤라야 의미가 있다.** 겸사 확인이든 전용 시험 폴더든 똑같이 걸린다.
    옛 플러그인 캐시로 돌린 `/womc update` 는 v2.2.0 의 청소 분기를 아예 안 갖고 있어 **무엇을 봐도 증거가 안 된다.**
    (이 저장소 안에서는 못 한다.)
  - **⚠ 겸사 확인이 성립하는 조건**: 그 폴더의 `.claude/settings.json` 이 **갱신 전에 옛 4줄을 갖고 있었을 때만** 이 항목의
    확인이 된다. 정리 분기는 옛 4줄이 있을 때만 도는 코드이기 때문이다(`commands/womc.md` 갱신 모드 3번).
    이미 v2.2.0 이 반영된 폴더는 갱신 전에도 `allow: []`, 후에도 `[]` 이므로 **`[]` 를 봤다는 것만으로는 아무 증거가 안 된다.**
    → 그런 폴더에서 확인했다면 이 항목을 **닫지 말고 `[ ]` 로 그대로 둔다.**
  - **그러니 갱신을 돌리기 전에 `allow` 를 먼저 본다.** 옛 4줄이 있으면 그 폴더가 이 항목의 시험대이고, 없으면 그냥 지나간다.
    (이 저장소 자신의 `.claude/settings.json` 은 이미 `allow: []` 이라 **시험대가 못 된다** — 여기서 돌려도 확인은 안 된다.)
  - **급하지 않은 이유**: 이 확인이 실패해도 세팅이 깨지지 않는다. 옛 4줄이 남을 뿐이고, 그 4줄은 읽기 전용 명령 허용이라 해롭지 않다.
  - 확인 방법: 옛 골격(4줄이 든 `.claude/settings.json`)이 깔린 폴더에서 `/womc update` 를 돌린 뒤,
    그 파일의 `allow` 가 `[]` 가 됐는지 본다. **사용자가 직접 넣은 다른 allow 항목은 남아 있어야 한다** — 같이 확인한다.
  - 굳이 전용 시험 폴더를 만들 거라면 `.claude/settings.json` 에 4줄 + 사용자 항목 1줄(예: `Bash(npm test:*)`)을 넣어 두고 돌린다
    (위 공통 전제는 그대로 걸린다).

- [ ] **`subagentStatusLine`·`/statusline` 을 골격에 들일지 판단 — 급하지 않음 · 생각날 때 (감사 v2.1.1 기록 4번 절 「새로 챙길 만한 것 2가지」)** <!-- open:statusline-v2 -->
  - 2026-08-11 결정: 지금 `statusline.js` 가 잘 돌고 있어 급할 이유가 없다. 상태줄을 손볼 일이 생기면 그때 함께 본다.
  - `subagentStatusLine`(v2.1.205+)은 서브에이전트 패널 행을 따로 꾸민다. `/statusline` 은 상태줄 스크립트를 자동 생성해 준다.
    후자가 쓸 만하면 골격이 `.claude/statusline.js` 를 직접 들고 갈 필요가 줄어든다.
  - 확인 방법: 시험 폴더에서 `/statusline` 을 한 번 돌려 무엇이 생기는지 보고, 지금 `statusline.js` 가 보여 주는
    5시간·주간 한도까지 나오는지 비교한다. 안 나오면 지금 것을 유지한다.

- [ ] **버전이 안 올라가도 `/womc update`·감사가 열린 확인 목록을 화면에 알리는지 확인 — 급하지 않음 · 다음 `/womc update` 때 겸사 확인** <!-- open:audit-open-notice -->
  - 2026-08-11 「정본 규약」 재설계가 만든 장치 자체의 동작 확인이다. **관찰만 하는 항목이라 손댈 파일이 없다.**
  - 무엇을 보는가: `/womc update` 갱신 모드 **7번**과 `harness-audit` **1단계**는 Claude Code 버전이 지난 감사와 **같아도**
    `docs/HARNESS-AUDIT.md` 머리의 `womc:open-checks` 구획을 읽어 열린 확인 목록을 알려야 한다.
    (버전이 벌어졌을 때만 감사가 돌던 옛 흐름에서는, 버전이 그대로면 열린 확인이 영영 눈에 안 걸렸다.)
  - 이어 쓸 것: `docs/HARNESS-AUDIT.md` 머리의 `womc:open-checks` 구획(`<!-- womc:open-checks:begin -->` ~ `:end`).
  - **⚠ 여기도 플러그인 재설치 + Claude Code 재시작 뒤라야 의미가 있다** — 옛 캐시의 `commands/womc.md`·스킬에는 이 지시가 없다.
  - 끝난 것으로 보는 조건: 재설치+재시작 뒤 `/womc update` 를 돌렸을 때, Claude Code 버전이 지난 감사와 같아도
    **열린 확인 3건이 화면에 표시된다.**
  - 확인 방법: 아무 womc 프로젝트에서 `/womc update` 를 실행하고 화면을 본다.

### 닫힌 것 · 보류 (집지 않는다)

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

<!-- 끝난 항목은 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
