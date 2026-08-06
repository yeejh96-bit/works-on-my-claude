# 변경 이력 (CHANGELOG)

> `TASKS.md` 「끝난 일」에서 넘어온 과거 작업 기록이다.
> `TASKS.md` 는 최근 작업만 남기고, 오래된 항목은 여기로 옮겨 보관한다.
> 각 항목의 형식은 `TASKS.md` 와 같다 — 손댈 파일 · 남긴 것 · 확인 방법.
> 한 줄 요약만 필요하면 `PLAN.md` 의 「만든 것(버전 이력)」을 본다.

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
