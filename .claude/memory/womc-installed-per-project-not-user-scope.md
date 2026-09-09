---
name: womc-installed-per-project-not-user-scope
description: womc 는 각 프로젝트 폴더에 project 범위로 깔고, PC 전역(user 범위)에는 깔지 않는다. 「PC 전역 것 지워」는 프로젝트 설치를 건드리지 말라는 뜻
metadata:
  type: feedback
---

womc 플러그인은 bbokji · easy-welfare · my-system · saas · socialproof 각 폴더에 project 범위로 설치돼 있다(2026-09-09). PC 전역(user 범위)에는 깔지 않는다.

**Why:** 2026-09-09 사용자가 「PC 전역 것만 지워」라고 했을 때, 당시 유일한 설치가 user 범위 하나였는데 그걸 지워서 모든 프로젝트에서 womc 가 사라졌다. 사용자는 프로젝트별 설치가 있는 줄 알고 있었고, 그건 남기길 원했다.

**How to apply:** 「전역 것 지워」류 요청이면 먼저 project 범위 설치가 실제로 있는지 확인하고, 없으면 지우기 전에 「지우면 모든 프로젝트에서 사라진다」를 알리거나 project 범위로 옮겨 놓는다. 설치는 각 폴더에서 `claude plugin marketplace add yeejh96-bit/works-on-my-claude --scope project` 후 `claude plugin install womc@works-on-my-claude --scope project`.
