---
name: korean-skill-names-work
description: 스킬 폴더·name 을 한글로 지어도 Claude Code 가 정상 인식한다(2026-09-12 실측)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 25f9d924-518d-436e-9591-af9b20c82615
  modified: 2026-09-12T06:42:40.472Z
---

`.claude/skills/테스트-한글이름/SKILL.md` 처럼 폴더 이름과 frontmatter `name:` 을 한글로 지어도 세션 스킬 목록에 정상으로 뜬다. ASCII 대조군과 나란히 확인했다.

**Why:** 한글 이름이 안 될까 봐 영어 이름으로 우회할 이유가 없다.
**How to apply:** 이 프로젝트에서 스킬을 만들 때 이름을 한글로 지어도 된다. 다만 슬래시로 부를 때 한글 입력이 필요하니, 자주 직접 치는 스킬은 영어가 편할 수 있다.
