# 변경 이력 (CHANGELOG)

> `TASKS.md` 「끝난 일」에서 넘어온 과거 작업 기록이다.
> `TASKS.md` 는 최근 작업만 남기고, 오래된 항목은 여기로 옮겨 보관한다.
> 각 항목의 형식은 `TASKS.md` 와 같다 — 손댈 파일 · 남긴 것 · 확인 방법.
> 한 줄 요약만 필요하면 `PLAN.md` 의 「만든 것(버전 이력)」을 본다.

## v2.3.0 — 하네스 감사 트리거를 `major.minor` 로 바꿈 (2026-08-12)
  - 근거: Claude Code 는 패치(세 번째 자리)가 자주 오른다. 지금까지는 버전이 **조금이라도** 다르면 `/womc update` 뒤
    감사 본체(신기능 조사)가 돌아, 버그 수정뿐인 패치 갱신에도 매번 오래 걸렸다.
    **전례가 이 파일에 남아 있다** — 2026-08-11 에 기준 `2.1.226` → 현재 `2.1.227` 패치 하나 차이로 감사가 뜨자
    사용자가 ⓑ(건너뛰기)를 골랐다(위 「지금 하는 일」의 2026-08-11 항목 4번).
  - 손댄 파일: `skills/harness-audit/SKILL.md`(1단계) · `commands/womc.md`(갱신 모드 7번) · `PLAN.md` · 이 파일 ·
    `.claude-plugin/plugin.json`(버전 표식은 `py scripts/bump-version.py 2.3.0` 한 줄로 6곳 — 손으로 세지 말 것).
  - 남긴 것:
    - **버전 대조는 앞 두 자리(`major.minor`)로만 한다.** 앞 두 자리가 같으면(= 패치만 올랐거나 아예 같으면)
      감사 본체를 건너뛰고, `a` 나 `b` 가 올랐을 때만 신기능을 조사한다. 같은 규칙이 **두 파일에 다 들어갔다** —
      `skills/harness-audit/SKILL.md` 1단계와 `commands/womc.md` 갱신 모드 7번. **한쪽만 고치면 흐름이 어긋난다.**
    - **건너뛸 때도 열린 확인 목록 알림은 그대로 뜬다**(`docs/HARNESS-AUDIT.md` 머리의 `womc:open-checks` 구획).
      이건 v2.2.1 이 만든 장치라 이번 변경이 끊지 않도록 두 파일 모두에 명시했다.
    - **"그래도 지금 조사할까요?" 한 줄을 덧붙인다** — 건너뛰기가 강제가 아니라 기본값일 뿐이다.
      사용자가 좋다고 하면 그 자리에서 감사를 돌린다.
    - **감사를 돌릴 때 조사 구간은 패치까지 포함한 「마지막 감사 기준 버전 ~ 현재 버전」 전체다** —
      건너뛴 패치들의 변경도 그때 함께 훑으므로 빠뜨리는 구간이 없다(이 조항이 건너뛰기의 안전장치다).
    - 버전은 2.2.4 → **2.3.0**(`.claude-plugin/plugin.json`).
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `2.3.0`.
    **문구 자체는 스크립트가 못 잡는다** — 스킬 파일은 `commands/womc.md` 에 임베드되지 않아 대조 대상이 아니다.
    두 파일에 「앞 두 자리」 문구가 있는지 읽어 확인한다.
    **실제 동작(패치만 오른 상태에서 감사가 안 도는지)은 다음 `/womc update` 때 사람이 본다** — 위 「지금 하는 일」.

## v2.2.4 — `plan-feature` 검증 절에 「실패했을 때 되돌아가는 경로」를 명시 (2026-08-12)
  - 근거: 「5. 검증(verify 위임)」 절이 verify 의 **"실패" 뒤에 무엇을 할지**를 적어 두지 않았다.
    그래서 실패했을 때의 처리가 매번 즉흥 판단이었고, 몇 번까지 다시 시켜 보는지도 정해져 있지 않았다.
  - 손댄 파일: `skills/plan-feature/SKILL.md`(「5. 검증(verify 위임)」 절) · `PLAN.md` · 이 파일 · `.claude-plugin/plugin.json`
  - 남긴 것:
    - **되돌아가는 경로가 절차문에 박혔다**: verify 실패 → verify 가 짚은 원인을 `implement` 에 넘겨 고치고 **다시 verify**.
    - **재위임 상한은 한 작업 항목당 2회다.** 2회를 쓰고도 실패하면 **멈추고** 사용자에게 무엇이 왜 실패했는지 보고한 뒤
      "계획을 다시 짜 볼까요?"라고 되묻는다. 사용자가 좋다고 하면 **3단계(`plan` 위임)로 되돌아가** 설계부터 다시 하며
      **실패 원인을 `plan` 에 함께 넘긴다**(같은 설계로 또 두들기지 않게 하는 것이 이 조항의 요점이다).
    - **실패한 채로 6·7절로 넘어가지 않고, `TASKS.md` 항목도 `[x]` 로 닫지 않는다.** 실패가 「끝난 일」로 둔갑하는 것을 막는 안전장치다.
    - 버전은 2.2.3 → **2.2.4**(`.claude-plugin/plugin.json`).
  - 확인 방법: `skills/plan-feature/SKILL.md` 5절에 「실패했을 때 — 되돌아가는 경로」 소절이 있고
    **2회 상한**·**`plan` 복귀** 문구가 들어 있는지 읽어 확인. `.claude-plugin/plugin.json` 의 `version` 이 `2.2.4` 인지 확인.
    **스크립트로는 문구를 못 잡는다** — 스킬 파일은 `commands/womc.md` 에 임베드되지 않아 `check-sync.py` 의 대조 대상이 아니다
    (`PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 는 버전 표식 6곳이 `2.2.4` 로 맞는지만 확인해 준다).

## v2.2.3 — 「설명 방식」 절 판정이 아주 옛 골격 판을 못 잡던 빈틈을 메움 (2026-08-11)
  - 근거: 같은 날 `pay` 폴더 실측. v2.2.2 의 지문 두 개(`womc:brevity=` · `answer-style.js`)는 **그 표식이 생기기 전 판본을 못 잡아**,
    `- 모든 설명은 한국어로 한다.` 한 줄뿐인 v1.10 이하 원문을 「사용자 커스텀」으로 오판해 보존했다.
  - 손댄 파일: `commands/womc.md`(갱신 모드 1번의 「설명 방식」 절 판정) · `PLAN.md` · 이 파일 · `.claude-plugin/plugin.json`
    (`py scripts/bump-version.py 2.2.3` 한 줄로 6곳).
  - 남긴 것:
    - **판정 지문이 3종이 됐다**: `womc:brevity=` · `answer-style.js` · **본문이 `- 모든 설명은 한국어로 한다.` 한 줄뿐일 때.**
      셋 중 하나면 옛 골격이므로 최신으로 교체한다. 사용자가 그 한 줄에 자기 줄을 더해 뒀으면 한 줄이 아니라 **보존된다**(원래 목적은 그대로).
    - **역대 판본을 전수 조사했다 — 6개다. 다시 조사하지 말 것.** 이 저장소 git 히스토리에서 `commands/womc.md` 의
      모든 커밋(37개)을 훑어 확인했다: v1.10 이하(한 줄) · v1.11 · v1.12 · v1.13~v1.18 · v1.19~v1.20 · v2.0.0 이후(현행).
      표식이 없는 것은 **첫 번째뿐**이고 **과거는 더 늘지 않으므로** 세 지문이면 완전하다. 이 근거를 절차문 안에도 적어 뒀다
      (`commands/womc.md` 「설명 방식」 판정 바로 아래 줄).
    - 캐시 대조안(로컬 플러그인 캐시와 공백 무시 비교)과 되묻기안(사용자에게 한 번 확인)은 **둘 다 쓰지 않았다** —
      전수 조사로 판본이 유한하다는 게 확인돼 지문 한 줄이면 충분해졌다. 캐시가 없는 컴퓨터에서도 동작한다.
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 9항목 전부 OK, 버전 `2.2.3`.
    **실제로 교체되는지는 스크립트로 못 잡는다** — 사람이 돌려 봐야 한다. 그 검증 항목은 **2026-08-12 에 사용자 결정으로 없앴다**
    (위 「지금 하는 일」 첫 줄). 그래서 이 수정은 **미검증 상태로 남아 있다.** 다시 확인하려면 여기 적힌 지문 3종과 조건으로 새 항목을 연다.

## v2.2.2 — 갱신 모드가 사용자의 `CLAUDE.md` 를 덮어쓰던 버그 2건 수정 (2026-08-11)

- 근거: 같은 날 `ax` 폴더에 `/womc update` 를 돌리다 **실측으로** 드러났다. **다시 조사하지 말 것.**
  ① 첫 줄이 골격이면 통째로 덮는 ⓐ 분기가 파일 중간의 사용자 절(「절영봇 절대 원칙」 7개)을 지울 뻔했다.
  ② 「설명 방식」 절을 무조건 되돌려 놓는 규칙 탓에 그 절만 `1.14.0` 판에 묶여, 이미 지워진 `answer-style.js` 를
  가리키는 죽은 문장이 남아 있었다(파일 머리 표식은 `1.20.0` 이었다).
- 손댄 파일: `commands/womc.md`(갱신 모드 1번의 `CLAUDE.md` 항목) · `PLAN.md` · `TASKS.md` · `.claude-plugin/plugin.json`
  (버전 표식은 `py scripts/bump-version.py 2.2.2` 한 줄로 6곳을 올렸다 — 손으로 세지 말 것).
- 남긴 것:
  - **ⓐ 분기가 「절 단위 병합」이 됐다** (`commands/womc.md` 갱신 모드 1번). 기존 파일을 `## ` 제목으로 쪼개
    **골격 절 제목 8개에 해당하는 절만** 최신 골격으로 교체하고, **그 목록에 없는 제목의 절은 원래 자리에 그대로 남긴다.**
    골격에는 있는데 없는 절은 골격 순서대로 새로 넣는다.
  - **골격 절 제목 8개 목록의 정본 위치는 `commands/womc.md` 의 ⓐ 병합 절차 2번**이다.
    **`CLAUDE.md` 템플릿의 `## ` 제목을 바꾸면 이 목록도 같은 작업에서 함께 고친다** — 안 고치면 그 절이
    「사용자가 쓴 절」로 오인돼 옛 판이 영원히 남는다. (이 경고는 절차문 안에도 적어 뒀다.)
  - **「설명 방식」 절 판정이 조건부가 됐다**(ⓐ·ⓑ 모두 적용): 절 안에 폐기된 `womc:brevity=` 나 `answer-style.js` 가
    보이면 **옛 골격 판이므로 최신으로 교체**, 그 표식 없이 최신 문구와 다르면 **사용자 커스텀이므로 보존**,
    절을 못 찾으면 기본값. 무조건 되돌려 놓던 옛 규칙이 그 절을 옛 판에 영구히 묶던 것을 이걸로 끊었다.
  - 완료 보고 요구 2개 추가: **남긴 사용자 절의 제목 목록** · **「설명 방식」 절을 교체했는지 보존했는지.**
  - ⓑ 의 `womc:begin` 정확일치 금지 경고는 내용 그대로 두되, ⓑ 설명 **바로 뒤로 위치를 옮겼다**(중간에 14줄이 끼어 무엇을 가리키는지 멀어졌었다).
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 9항목 전부 OK, 버전 `2.2.2`.
- ✅ **실사용 검증 통과 (2026-08-11, `pay` 폴더)** — 사용자가 끼워 둔 `## 시험용 내 규칙` 절이 갱신 뒤에도 같은 자리에 그대로 남았다.
  **다만 「설명 방식」 판정에 빈틈이 남았다**(표식 없는 아주 옛 판을 사용자 커스텀으로 오판) — v2.2.3 으로 메웠다.

## v2.2.1 — 열린 확인을 「정본 규약」으로 다시 짬 + 서브에이전트 모델 조정 (2026-08-11)

- 근거: `/code-review` 가 기록 파일에서 확정한 결함 10건. 전문을 두 파일에 복제하던 옛 방식이 곧 어긋났다(`TASKS.md` 「지금 하는 일」의 「정본 규약」 항목).
- 손댄 파일: `TASKS.md` · `docs/HARNESS-AUDIT.md` · `skills/plan-feature/SKILL.md` ·
  `skills/harness-audit/SKILL.md` · `commands/womc.md`(갱신 모드 3번·7번) · `scripts/check-sync.py` ·
  `agents/implement.md` · `agents/verify.md` · `SPEC.md` · `PLAN.md` · `.claude-plugin/plugin.json`
- 남긴 것:
  - **정본은 `TASKS.md` 「할 일」 한 곳이다.** 배경·조건·경고·확인 방법 전문은 여기에만 쓰고,
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
  **알림이 실제로 화면에 뜨는지는 스크립트로 못 잡는다** — `TASKS.md` 「할 일」의 `open:audit-open-notice` 에서 사람이 확인한다.

## v2.2.0 — 골격에서 `permissions.allow` 의 PowerShell 4줄을 뺌 (2026-08-10)

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
- ✅ **실사용 검증 통과 (2026-08-11, `ax` 폴더)** — 사용자 항목 `Bash(npm test:*)` 를 한 줄 넣어 두고 `/womc update` 를 돌렸더니
  **옛 4줄만 사라지고 그 한 줄은 남았다.** 이로써 열린 확인 `open:allow-cleanup` 을 닫았다(`TASKS.md` 「할 일」의 「닫힌 것 · 보류」).

## v2.1.1 — 말투가 한 번도 안 켜지던 버그 수정, A안 (검증까지 완료, 2026-08-10)

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
      B안은 `TASKS.md` 「할 일」의 「닫힌 것 · 보류」 소절에 `[-]` 보류로 있다(집지 않는다).
  - 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 8항목 전부 OK, 버전 `2.1.1`.
    **말투가 실제로 켜지는지는 스크립트로 못 잡는다** — 커밋·push → 플러그인 재설치 → **Claude Code 재시작** 후
    메인 답변이 원시인 말투인지 육안 확인해야 한다(위 ✅ 로 통과 확인).

## v2.1.0 — 하네스 감사 절차를 골격에 심음 (검증까지 완료, 2026-08-10)

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

## v2.0.0 — Claude Code 2.1.x 기본기능에 맞춘 하네스 간소화 (검증까지 완료, 2026-08-10)

- ✅ **검증 3건 통과** — ① 빈 폴더에서 `/womc` → 생성 파일 정확히 6개(레거시 0개).
    ② v1.20.0 골격 사본에서 `/womc update` → 레거시 8개 삭제, 사용자 파일(`SPEC.md`·`PLAN.md`·`TASKS.md`·`.claude/rules/`·추가 allow) 전부 보존,
    **본문만 고친 `.claude/agents/verify.md` 는 「사용자가 고친 것」으로 판정해 남겼다**(판정 기준을 넓힐 필요 없음). ③ 말투는 `TASKS.md` 「끝난 일」의 v2.1.1 항목 참조.
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

## v1.20.0 — 「끝난 일」 회전 규칙을 womc 골격에 심음

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

## v1.19.0 — 하네스 감사 지적 13건 일괄 수정

- 손댈 파일: `commands/womc.md`, `CLAUDE.md`, `HARNESS.md`, `README.md`, `.claude/answer-style.js`,
  `.claude/statusline.js`, `.claude/settings.local.json`, `scripts/check-sync.py`, `.claude-plugin/plugin.json`
- 먼저 확인한 것 (`claude-code-guide` 위임): `.claude/rules/` 의 `paths` 필터 **공식 지원 맞음**,
  커스텀 서브에이전트는 CLAUDE.md **안 물려받는 게 맞음**, UserPromptSubmit 훅의 **평문 stdout 주입 유효**.
  → 감사에서 "고쳐야 한다"고 지적됐던 이 3건은 기존 서술이 옳아 **고치지 않았다**. 다시 의심되면 이 결론부터 볼 것.
  **단, 가운데 항목은 v2.0.0 에서 거짓으로 판명됐다** — 커스텀 서브에이전트는 CLAUDE.md 를 **물려받는다**(이 파일 위쪽 v2.0.0 항목 참고).
- 남긴 것 (갱신 모드 = `commands/womc.md` 「갱신 모드」 절):
  - 1번에 「덮기 전 공통 확인」 블록 신설 — agents/skills 를 덮기 전 골격인지 판정, 사용자 파일이면 건너뛰고 보고.
  - `CLAUDE.md` 덮을 때 기존 `## 설명 방식` 절을 읽어 두었다가 되돌려 놓도록 지시(말투 설정 보존). `answer-style.js` 도 같은 방식으로 문구 보존.
  - `womc:begin`/`womc:end` 를 **정확 일치가 아니라 "그 문자열이 들어 있는 줄"** 로 찾도록 명시 — 구획 중복 누적 방지.
  - 0-b 임시파일 경로를 `${TMPDIR:-${TEMP:-/tmp}}` 로 통일(`%TEMP%` 는 Git Bash 에서 안 풀림).
  - 다운그레이드 방지 단계 추가 — 프로젝트 `CLAUDE.md` 의 `womc:skeleton-version` 이 적용하려는 것보다 높으면 멈춤.
- 남긴 것 (생성 모드·골격):
  - 생성된 `CLAUDE.md` 맨 위(H1 바로 아래)에 `<!-- womc:skeleton-version=x.y.z -->` 를 찍는다. 온보딩 병합 구획 안에도 같은 표식.
    **버전을 올릴 때 고칠 자리가 4곳이 됐다** — `commands/womc.md` 맨 위 표식, CLAUDE.md 골격 안 표식, 온보딩 구획 안 표식, `plugin.json`. (`commands/womc.md` 맨 위 주석에 적어 뒀다.)
    **v2.0.0 부터는 `scripts/bump-version.py` 가 6곳을 한 번에 올린다 — 손으로 세지 말 것.**
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
  (`.claude/answer-style.js` 는 v2.0.0 에서 삭제됐다 — 말투는 출력 스타일이 맡는다.)

## v1.19.0 커밋 + `PLAN.md`·`TASKS.md` 를 git 에 포함

- 남긴 것: 커밋 `82bc25b`(v1.19.0 수정 9개), 커밋 `ac8f105`(`PLAN.md`·`TASKS.md` 추적 시작).
  이전 판에는 "이 두 파일은 git 미포함 유지"라고 적혀 있었으나 **방침이 바뀌어 git 에 포함한다** — 앞으로 커밋에 함께 넣는다.
- 확인 방법: `git status --short` 가 비어 있고, `git ls-files PLAN.md TASKS.md` 에 두 파일이 나온다.

## v1.18.0 — 버전 올릴 때 PLAN/TASKS 동반 갱신 규칙 + 답변에서 줄번호 표기 폐지

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`,
  `.claude/skills/plan-feature/SKILL.md`, `.claude-plugin/plugin.json`, `README.md`
- 남긴 것:
  - `CLAUDE.md` 「세션을 이어서 하기」에 "버전을 올리는 작업이면 PLAN/TASKS 도 함께 갱신" 규칙 추가.
    같은 문구가 `commands/womc.md` 의 CLAUDE.md 템플릿에도 글자 그대로 들어감.
  - `plan-feature` 스킬 「작은 변경」 항목에 **예외** 하위 불릿 추가 — 버전 변경이면 크기 무관하게 PLAN/TASKS 갱신.
    이게 v1.13~1.17 동안 기록이 멈춰 있던 원인을 막는 장치다.
  - `CLAUDE.md` 「설명 방식」에 "파일은 이름만, 줄번호 안 붙임" 규칙 추가 + `.claude/answer-style.js` 의 출력 배열에도 같은 줄 추가
    (훅이 매 입력마다 재주입하도록). 서브에이전트 5종의 `파일경로:줄번호` 보고 프로토콜은 그대로 뒀다 —
    메인이 사용자에게 옮길 때만 줄번호를 뗀다.
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `1.18.0` 통과.

## v1.17.0 — 케이브맨 단일 강제 (4단계 폐지)

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`, `HARNESS.md`, `SPEC.md`, `README.md`,
  `.claude/skills/make-rule/SKILL.md`, `.claude/skills/plan-feature/SKILL.md`, `scripts/check-sync.py`
- 남긴 것: `womc:brevity=` 표식·약하게/보통/최소 정의·강도 전환 안내 전부 삭제.
  `.claude/answer-style.js` 는 `RULES` 객체·`readLevel()` 제거하고 고정 `RULE` 문자열 하나로 단순화(CLAUDE.md 안 읽음).
  `scripts/check-sync.py` 의 `womc:brevity=` 정규화 로직도 같이 제거(더 이상 값이 달라질 일이 없어서).
- 확인 방법: `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` → 전 항목 OK, 버전 `1.17.0` 통과.

## v1.17.0 — 대화 답변 「지우지 않는 것」 목록에서 파일경로:줄번호 삭제

(위 항목과 같은 커밋)

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`
- 남긴 것: 목록에서 "파일 경로와 `경로:줄번호`" 만 뺌. 서브에이전트(`explore`/`plan`/`implement`/`verify`/`review`) 보고 프로토콜의
  `파일경로:줄번호` 관례는 별개 시스템이라 그대로 둠 — 손대지 않았다.
- 확인 방법: `py scripts/check-sync.py` 전부 OK

## v1.16.0 — 케이브맨 문장 종결 명사형 강제

- 손댈 파일: `CLAUDE.md`, `commands/womc.md`, `.claude/answer-style.js`
- 남긴 것: "-다"·"-이다"·"-한다"·"-했다" 서술형 어미 금지, 명사형(-음/-ㅁ) 또는 명사만 남기고 끝내는 규칙 + 견본 3개 추가.
- 확인 방법: 세 파일에 같은 규칙 문구가 글자 그대로 들어갔는지 육안 대조(당시엔 `check-sync.py` 실행 안 함).

## v1.15.0 이전 (상세 기록 없음)

이 세 버전은 `TASKS.md` 가 갱신되지 않던 시기의 작업이라 단계별 기록이 남아 있지 않다.
한 줄 요약만 `PLAN.md` 의 버전 이력에 있으며, 상세는 각 커밋의 diff 를 본다.

- v1.15.0 — `/womc update` 가 플러그인 자체도 갱신. (커밋 `686d1a2`)
- v1.14.0 — `/womc update` 가 옛 캐시를 스스로 우회. (커밋 `07ae551`)
- v1.13.0 — 답변 말투 강제 훅(`.claude/answer-style.js`) + `/womc update` 옛 캐시 차단. (커밋 `822a34d`)
- v1.12.0 — 케이브맨 말투를 womc 의 기본 문체로.
