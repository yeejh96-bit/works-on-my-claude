---
name: womc-delegation-conflicts-with-opus5-harness
description: "CLAUDE.md 「적극 위임」과 Opus 5 하네스의 \"시키지 않으면 Agent 부르지 마라\"가 정면 충돌 — 사용자는 기록만 남기기로 함"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3162589b-3033-4e68-bce8-a25e2753b131
  modified: 2026-08-18T00:34:35.776Z
---

2026-08-18 하네스 감사에서 확인. Opus 5 일 때 Claude Code 는 시스템 프롬프트에 **"시키지 않으면 Agent 도구를 부르지 마라"** 를 직접 넣는다(`claude_code` 프리셋, 실측). 반면 womc 골격의 `CLAUDE.md` 「적극 위임」 절은 "무거운 일은 서브에이전트에 맡겨라"라고 민다. 같은 컨텍스트에 반대 지시 둘.

같은 감사에서 `verify` 서브에이전트도 공식 삭제 권고 대상으로 확인됐다 — Opus 5 지침이 "검증하라는 지시는 과잉검증을 유발한다, 고쳐 쓰지 말고 지워라"라고 명시.

**사용자 결정(2026-08-18): 빼지 않고 기록만 남긴다.** 넷 다 womc 골격 절이라 이 프로젝트 `CLAUDE.md` 에서 고쳐도 다음 `/womc update` 가 되돌리기 때문. 진짜로 빼려면 womc 플러그인 저장소(`commands/womc.md` 의 CLAUDE.md 템플릿)를 고쳐야 한다.

**How to apply:** 위임 판단은 CLAUDE.md 문구를 기계적으로 따르지 말고 실제 필요로 정한다 — 파일 여러 개를 뒤지는 조사·긴 로그는 위임이 여전히 맞고, 자기 작업을 다시 확인하려고 `verify` 를 부르는 것은 하지 않는다. 이 결정을 사용자에게 다시 제안하지 말 것(이미 「기록만」으로 닫혔다). 상세는 `docs/HARNESS-AUDIT.md` 맨 위 기록.

관련: [[tool-name-deprecation-verify-by-running]]
