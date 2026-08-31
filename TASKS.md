# 작업 목록 (TASKS)

> PLAN의 한 단계를 실제 작업으로 쪼갠 체크리스트다.
> **다른 세션에서 이어 작업해도 되도록**, 각 항목은 그것만 읽고 바로 시작할 수 있게 적는다.
> 표기: `[ ]` 안 함 · `[~]` 하는 중 · `[-]` 보류(지금 안 집는다 — 끝난 것이 아니다)
> **끝남을 나타내는 표기는 없다** — 끝나면 이 파일에서 사라지고 `docs/CHANGELOG.md` 에만 남는다.

## 지금 하는 일

(아직 없음.)

(v3.1.0(코드가 스펙이다: SPEC.md 폐지)은 2026-08-31 에 끝나 `docs/CHANGELOG.md` 의 v3.1.0 항목으로 옮겼다.
v3.0.0 대개편은 2026-08-31 에 끝나 `docs/CHANGELOG.md` 의 v3.0.0 항목으로 옮겼다. 그 실사용 관찰 항목도
같은 날 트리거가 없어 `docs/CHANGELOG.md` 「저장소 정리 — 트리거 없는 열린 확인 4건 이관」으로 옮겼다.)

(이 파일과 `PLAN.md` 는 기록용으로 남겨 두며 지우지 않는다. **git 에 올린다** — 다른 PC 에서 이어 작업할 때
진행 상태와 지난 결정 이유(`docs/CHANGELOG.md`)를 그대로 볼 수 있어야 하기 때문이다. 커밋할 때 이 두 파일도 함께 넣는다.)

## 할 일

> **이 절이 열린 확인의 정본이다.** 배경·조건·경고·확인 방법 **전문은 여기에만** 쓴다.
> `docs/HARNESS-AUDIT.md` 에는 ID 한 줄과 링크만 둔다. **전문은 여기 한 곳뿐 — 지우지 말 것**(다른 곳에 사본이 없다).
> 열린 확인은 그 파일 머리의 `womc:open-checks` 구획에 **ID 한 줄씩만** 올라간다
> (`harness-audit` 과 `/womc update` 가 버전이 안 올라가도 그 구획을 읽어 화면에 알린다).
> **두 파일의 ID 집합이 어긋나면 `scripts/check-sync.py` 가 DRIFT 로 잡는다 — 한쪽만 고치면 장치가 끊기니 항상 같이 고친다.**
>
> **2026-08-31 현재 열려 있는 것은 2건이다** — 아래 둘뿐이고, 둘 다 지금 확인할 수 있다.
> 같은 날 **트리거가 없던 확인 4건을 지웠다**(경위와 원문은 `docs/CHANGELOG.md` 「저장소 정리 — 트리거 없는 열린 확인 4건 이관」).
> **미리 예측해서 남기지 않는다 — 지우고, 써 보고, 같은 데서 두 번 이상 걸릴 때만 되살린다.**
>
> 닫힌 확인들의 결론은 `docs/CHANGELOG.md` 에 있다 — 「열린 확인 4건 닫음」(2026-08-18 v2.7.0 감사) ·
> 「저장소 정리 — TASKS.md 「지금 하는 일」의 완료 기록 이관」(2026-08-31: `open:delegation-vs-preset` · v2.12.0 확인 · v2.13.0 확인).

### 열려 있는 것 (둘 다 급하지 않음)

- [ ] **입력 리다이렉션(`cat < .env` 류)이 골격의 `.env` deny 를 우회하는지 실측 — 급하지 않음 · 다음에 `.env` 를 쓰는 폴더에서 겸사** <!-- open:env-deny-redirect -->
  - 2026-08-18 v2.7.0 감사가 연 항목이다. Claude Code `2.1.232` 가 Bash **입력 리다이렉션**을 권한 검사 대상에 넣었다가
    `2.1.233` 에서 되돌렸다("Reverted 2.1.232 Bash permission changes for Cygwin symlinks and input redirections").
    **되돌린 지금 `cat < .env` 가 골격의 `.env` deny 를 우회하는지 확인 못 했다.**
  - 손댈 파일: 없음(관찰만 한다). 우회로 판명되면 `commands/womc.md` 의 `.claude/settings.json` 설명 절(deny 설명)에
    **권한 한계 한 줄**을 더한다 — 골격 `deny` 목록 자체는 그대로다(리다이렉션은 경로 규칙으로 막을 수 있는 것이 아니다).
    (v2.7.0 때는 이 한계 설명이 `HARNESS.md` 에 있었는데, 그 파일은 v3.0.0 에서 없어졌다 — 이제 갈 곳은 womc.md 의 deny 설명이다.)
  - 이어 쓸 것: deny 목록의 정본은 `commands/womc.md` 의 `.claude/settings.json` 템플릿, 라이브 사본은
    `.claude/settings.json`(한쪽만 고치면 check-sync 1번이 DRIFT 로 잡는다). 근거 문서 https://code.claude.com/docs/en/permissions
  - 2026-08-31 v3.2.0 감사가 **절반을 문서로 답했다**: `Read` deny 는 Claude Code 가 알아보는 Bash 파일 명령(`cat`·`head`·`tail`·`sed`)에도 걸리고 Grep·Glob 검색 결과에서도 빠지지만, **임의 서브프로세스(파이썬·노드 스크립트가 스스로 파일을 여는 것)는 안 막는다**(문서 명시). 입력 리다이렉션은 `2.1.233` 의 되돌림 이후 `2.1.251` 까지 **안 돌아왔다**(전 구간 grep 확인) — 남은 절반은 그대로 열려 있다.
  - 공식 해법인 샌드박스(OS 수준 차단)는 macOS·Linux·WSL2 전용이라 **Windows 네이티브인 이 환경엔 대안이 없다** — 우회로 판명돼도 고칠 수 있는 건 위 「손댈 파일」의 한 줄짜리 한계 설명뿐이다.
  - 끝난 것으로 보는 조건: 막히는지 안 막히는지 사람이 화면으로 확인하고, **안 막히면 위 deny 설명 문구까지 고친** 상태.
  - 확인 방법: 아무 프로젝트에 더미 `.env`(가짜 값만 넣는다)를 두고 Bash 로 `cat < .env` 를 시켜 차단되는지 본다.
    `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 로는 못 잡는다(설정이 파일에 있는지만 본다).
  - **닫히는 조건 있음(지금도 가능)**: `.env` 파일이 있는 아무 폴더에서 `cat < .env` 를 한 번 시켜 보고 막히는지 화면으로 보면 끝난다.
    막을 트리거가 없을 뿐 조건은 명확하다.

- [ ] **`/import` 가 womc 온보딩 병합과 겹치거나 충돌하는지 실측 — 급하지 않음 · 다음에 기존 프로젝트에 `/womc` 를 깔 때 겸사** <!-- open:import-command -->
  - 2026-08-19 감사가 연 항목이다. **온보딩 절차가 이미 있는 기능을 손으로 다시 하고 있을 수 있다.**
  - 무엇이 불확실한가: 공식 문서(memory)는 `2.1.213+` 의 `/import` 가 `AGENTS.md`·MCP 서버·서브에이전트·스킬을
    한 번에 끌어온다고만 적는다. womc 온보딩은 그와 별개로 기존 `CLAUDE.md`·`.claude/settings.json` 에
    `womc:begin/end` 구획을 병합한다.
    **겹치는 범위가 어디까지인지, 둘을 같이 돌리면 충돌하는지 못 봤다.** https://code.claude.com/docs/en/memory
  - 손댈 파일: 겹치는 것으로 판명되면 `commands/womc.md` 의 「기존 프로젝트 온보딩」 2절에서 겹치는 단계를 빼고
    `/import` 를 먼저 돌리라고 안내한다. 안 겹치면 아무것도 안 고친다(관찰만).
  - 이어 쓸 것: 온보딩 병합 절차의 정본은 `commands/womc.md` 「기존 프로젝트 온보딩」 2절.
    같은 감사가 올린 후보 ③(`AGENTS.md` 감지 → `@AGENTS.md` import)은 **v2.9.0 에서 이미 처리됐다** —
    무조건 import 가 아니라 **「제안 후 승낙」** 방식이고, 자리는 온보딩 2-b 소절이다(`docs/CHANGELOG.md` 의 v2.9.0 항목 참고).
    **이 항목에 남은 것은 `/import` 와 겹치는지 하나뿐이다.**
  - 2026-08-31 v3.2.0 감사가 **조사 부분을 끝냈다.** `/import [codex|gemini]`(`2.1.213+`)는 **Codex·Gemini CLI 설정만** 대상이고, `AGENTS.md` 같은 지시 파일을 `CLAUDE.md` 에 **한 번 복사해 붙인다.** womc 는 `@AGENTS.md` **연결**을 넣어 사본을 안 만드는데 **공식 문서가 바로 그 방식을 권한다** — "so both tools read the same instructions without duplicating them", Windows 에서는 symlink 대신 import 를 쓰라고까지 명시한다. → **womc 의 선택이 공식 권고와 일치한다.** https://code.claude.com/docs/en/commands · https://code.claude.com/docs/en/memory
  - **남은 것은 겹침 안내 한 줄뿐이다** — 온보딩으로 `@AGENTS.md` 를 넣은 뒤 `/import` 를 돌리면 같은 내용이 **연결 + 사본으로 두 번** 들어간다(`womc:begin/end` 구획이 그 사본까지 감싸주지 않는다). 이 한 줄을 `commands/womc.md` 「기존 프로젝트 온보딩」 1-b 소절에 넣으면 이 항목은 닫힌다 — 온보딩 단계를 빼는 일은 없다.
  - 끝난 것으로 보는 조건: `/import` 가 무엇을 끌어오는지 화면으로 확인하고, 겹치면 `commands/womc.md` 문구까지 고친 상태.
  - 확인 방법: 기존 코드가 있는 아무 폴더에서 `/import` 를 돌려 무엇을 끌어오는지 보고,
    이어서 `/womc` 를 돌려 온보딩이 같은 일을 또 하는지 본다.
    `PYTHONIOENCODING=utf-8 py scripts/check-sync.py` 로는 못 잡는다(문구가 파일에 있는지만 본다).
  - **닫히는 조건 있음, 트리거 없음**: 기존 프로젝트에 `/womc` 를 까는 일이 생겨야 확인된다.
    그 일이 언제 생길지는 정해져 있지 않다.

<!-- 끝난 항목은 이 파일에 남기지 않는다. docs/CHANGELOG.md 에 이렇게 적는다:
- [x] 항목 이름
  - 남긴 것: 만들어진 파일 경로, 다음 단계가 쓸 함수·설정 이름 (다음 항목의 「이어 쓸 것」에 그대로 옮겨 적는다)
  - 확인 방법: 통과를 확인한 명령
-->
