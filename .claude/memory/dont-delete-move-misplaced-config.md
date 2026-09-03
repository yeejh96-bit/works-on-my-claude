---
name: dont-delete-move-misplaced-config
description: 엉뚱한 자리의 설정은 지우자고 하지 말고 제 주인 프로젝트로 옮길 수 있는지 먼저 볼 것
metadata:
  type: feedback
---

설정이 엉뚱한 자리에 있으면(예: 홈 `~/.claude/settings.json` 의 `autoMode.environment` 가
`works-on-my-claude` 전용 설명이었던 일) **「지울까요?」로 묻지 말고 「제 주인 프로젝트 설정으로 옮길까요?」를 먼저 본다.**

**Why:** 그 내용은 누가 공들여 만든 것이고, 자리가 틀렸을 뿐 값은 멀쩡하다. 지우면 다시 만들어야 한다.

**How to apply:** 옮길 때 순서 — ① 원문 전문 복사(요약 금지) ② 대상에 붙여 넣고 두 파일 대조해 빠진 줄 0개 확인
③ 확인된 뒤에만 원본에서 지움 ④ 양쪽 `jq empty` 로 문법 확인.
`autoMode.environment` 는 지금 `/home/lee/바탕화면/project/worksonmyclaude/.claude/settings.json` 에 산다.
my-system 용은 따로 두지 않는다 — 없으면 기본값으로 돈다. [[home-settings-not-editable-by-agent]]
