---
name: rejected-ideas-dont-go-in-rules
description: "안 하기로 한 구현방향을 제약-공통.md 에 매번 적지 말 것, 파일만 길어진다"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a6393a0a-62bd-4acb-97b2-b0f8ef97ae66
  modified: 2026-09-03T10:33:53.177Z
---

내가 제안했다가 사용자가 "안 넣을래"로 접은 구현방향은 `.claude/rules/제약-공통.md` 「사용자가 닫은 것」에 적지 않는다. 접었으면 그냥 접고 끝낸다.

**Why:** 그 파일은 골격을 설계할 때 켜지는 always-on 자리다. 한 번 접은 아이디어까지 다 쌓으면 매번 길어지고, 정작 중요한 닫힌 결정이 묻힌다. 사용자가 2026-09-03 에 직접 지우라고 했다 — "매번 이렇게 안하기로 한 구현방향을 제약에 넣으면 제약공통 파일이 길어지잖아."

**How to apply:** 거기 적는 것은 **사용자가 방향을 못 박은 것**(다시 열지 말라고 한 것)과 **진지하게 검토 후 기각한 설계 대안**뿐이다. 내가 던졌다가 바로 접힌 제안은 대상이 아니다. 애매하면 안 적는다. [[user-decided-means-stop-checking]]
