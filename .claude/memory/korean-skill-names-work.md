---
name: korean-skill-names-work
description: 한글 스킬 이름은 되지만 womc 골격에 강제 규칙으로 넣지 않기로 했다(2026-09-12)
metadata:
  node_type: memory
  type: feedback
  originSessionId: 25f9d924-518d-436e-9591-af9b20c82615
  modified: 2026-09-12T06:47:39.153Z
---

기술적으로는 된다: `.claude/skills/테스트-한글이름/SKILL.md` 처럼 폴더 이름과 frontmatter `name:` 을 한글로 지으면 스킬 목록에도 뜨고 `Skill` 도구 호출도 성공한다(ASCII 대조군과 나란히 실측).

그런데 이걸 womc 골격 규칙으로 넣었다가 사용자가 곧바로 접었다. 「스킬 이름을 한글로 짓는다」 + 「다시 짜기 때 기존 스킬 이름도 한글로 바꾼다」 두 줄을 넣고 4.4.0 으로 올렸던 것을 전부 되돌렸다.

**Why:** 되는 것과 규칙으로 강제할 것은 다르다. 이름을 한글로 바꾸면 그 이름을 부르던 곳까지 따라 고쳐야 하고, 슬래시로 직접 칠 때 한글 입력이 걸린다.
**How to apply:** womc 골격에 스킬 이름 언어를 강제하는 줄을 다시 넣지 않는다. 이름은 그때그때 모델이 정한다. 사용자가 먼저 다시 꺼내지 않는 한 이 안을 제안하지 않는다. [[rejected-ideas-dont-go-in-rules]]
