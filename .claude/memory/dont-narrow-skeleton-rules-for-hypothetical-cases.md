---
name: dont-narrow-skeleton-rules-for-hypothetical-cases
description: 골격 규칙의 범위를 가상의 문제 때문에 좁히지 말 것. 넓은 표현을 두고 모델 기본 동작을 믿는다.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d63101f9-9e63-4d01-922d-b93c517b2a23
  modified: 2026-09-04T12:06:38.979Z
---

골격 1단계 「요청이 모호하면 되묻는다」를 「새 기능 요청이 모호하면」으로 좁혔다가 사용자가 되돌리게 했다(2026-09-04, v4.1.1 → revert).

**Why:** 고장 신고에 되물을까 봐 좁힌 건데, 실제로 안 생긴 문제였다. 좁히면 설정·문서·구조 정리 요청은 되묻지 않게 되어 더 손해다. 사용자는 넓은 표현을 선호한다.

**How to apply:** 골격 문장은 넓게 두고, 예외는 모델 기본 동작에 맡긴다. 줄을 더하거나 범위를 좁히기 전에 「지금 실제로 생긴 문제인가」를 먼저 묻는다. [[rejected-ideas-dont-go-in-rules]] 와 같은 결이다.
