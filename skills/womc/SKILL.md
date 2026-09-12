---
name: womc
description: 프로젝트 폴더에 womc 기본 하네스(CLAUDE.md · .claude/settings.json · 상태줄)를 깔거나 v4 철학에 맞게 다시 짠다. 세션 시작 훅이 「세팅 없음」「구버전」을 알리면 사용자에게 묻지 않고 이 스킬을 부른다. 사용자가 /womc 를 직접 쳐도 같은 절차다.
---

<!-- womc:skeleton-version=4.9.0 -->

# womc 세팅

목적: **사람은 무엇을 원하는지와 되돌릴 수 없는 결정만 맡는다. 되묻기·계획·구현·검증은 모델이 맡는다.**
그래서 하네스는 얇다. 사용자가 승인하거나 결정하는 일을 최소로 줄이고, 모델이 좋아질수록 더 얇아진다. 만든 것에 애착을 갖지 않는다.

## 0. 먼저 확인
- 현재 폴더에 `CLAUDE.md` 가 있고 그 안에 `womc:skeleton-version=` 표식이 있으면 → 표식의 첫 자리가 이 스킬과 같으면 「C. 골격만 갱신」, 다르면 「B. 다시 짜기」. 표식 버전이 이 스킬 맨 위 표식과 같으면 브리핑만 본다 — 칸이 넷 밖이거나 칸 밖에 적힌 줄이 있거나 40줄이 넘으면 브리핑 기준대로 훑어 정리하고, 아니면 할 일이 없다고 한 줄 알리고 끝낸다.
- `CLAUDE.md` 가 있는데 표식이 없으면(womc 를 안 쓰던 프로젝트) → 「B. 다시 짜기」.
- `CLAUDE.md` 가 없으면 → 「A. 새로 깔기」.
- git 저장소가 아니면 묻지 않고 `git init` 부터 한다.

## A. 새로 깔기
1. 아래 「정본」 네 파일을 만든다. 셋은 `${CLAUDE_PLUGIN_ROOT}/templates/` 에서 복사하고 `.gitignore` 만 새로 쓴다. 이미 있는 파일은 덮어쓰지 않는다.
2. 폴더를 읽는다(파일 목록·README·설정 파일). 코드로 알 수 있는 것은 묻지 않는다.
3. 브리핑을 채운다(브리핑 절의 기준대로). 빈 폴더면 「무엇을 만들 건가」 한 가지만 AskUserQuestion 으로 선택지를 곁들여 묻는다. 코드가 있으면 보통 아무것도 묻지 않고 추정해 적는다.
4. 체크포인트 커밋을 남기고 「만든 파일 · 브리핑에 적은 것」을 한 줄씩 보고한다.

## B. 다시 짜기 (기존 프로젝트 · 구버전 womc)
기존 하네스 구조에 얽매이지 않는다. 절 제목·파일 배치·옛 절차는 지키지 않고 v4 모양으로 새로 쓴다.
1. 체크포인트 커밋을 남긴다(이 커밋이 있어 아래 지우기를 묻지 않는다).
2. 기존 하네스 전부를 읽는다: `CLAUDE.md`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, `.claude/settings.json`, `PLAN.md`, `TASKS.md`, `docs/CHANGELOG.md`, `AGENTS.md` 등.
3. 남길 것은 **코드로 알 수 없는 사실**뿐이다.
   - 사용자가 적은 프로젝트 사실·지킬 것·끝난 조건·확인 명령 → 새 `CLAUDE.md` 「브리핑」으로. 이때도 브리핑 기준(「이 줄이 없으면 다음 작업이 달라지나」)을 적용해, 의향·계획·사정·진행 기록은 옮기지 않고 지운다.
   - 특정 경로에만 걸리는 제약 → `.claude/rules/<이름>.md` 에 `paths` 를 붙여서. 기준은 브리핑과 같다.
   - 배경·근거·숫자·결정 경위·긴 목록 → `docs/<주제>.md` 로 옮기고 브리핑에는 「…할 때는 이 문서를 읽는다」 한 줄만 남긴다.
   - 브리핑은 칸 넷이다. 40줄이 넘으면 한 줄씩 기준으로 따져 걸리는 것만 주제별로 `docs/` 로 가른다.
   - 사용자가 직접 만든 스킬·훅·MCP 설정 → 그대로 둔다.
   - `AGENTS.md` 가 있으면 새 `CLAUDE.md` 첫 줄에 `@AGENTS.md` 로 불러온다.
4. 옛 하네스는 지운다: womc 가 만들었던 `agents/`·`skills/`(plan-feature·make-rule·harness-audit)·`PLAN.md`·`TASKS.md`(끝난 항목)·`docs/CHANGELOG.md`·`docs/HARNESS-AUDIT.md`·`.claude/rules/제약-*.md`(paths 없는 것) 등. git 이 추적하는 파일은 `git rm` 으로 지운다(커밋으로 되돌릴 수 있다).
5. 새 `CLAUDE.md` 를 「정본」대로 쓰고 브리핑을 채운다(브리핑 절의 기준대로). `.claude/settings.json` 은 정본을 기준으로 하되 사용자가 더한 allow·deny 항목은 남긴다. 상태줄 파일은 정본으로 바꾼다.
6. 옮긴 뒤 옛 브리핑과 줄 단위로 대조해 사라진 지시가 없는지 본다. 없앤 절 이름을 가리키던 `.claude/rules`·스킬·`docs/` 의 참조도 함께 고친다.
7. 커밋하고 「남긴 것 · 옮긴 것 · 지운 것」을 한 줄씩 보고한다. 묻지 않는다 — 다만 프로젝트 규칙이 하네스 파일을 덮기 전에 묻기를 요구하면 그쪽을 따른다.

## C. 골격만 갱신 (표식의 첫 자리가 같을 때)
브리핑은 건드리지 않는다. 옛 하네스도 지우지 않는다.
1. 체크포인트 커밋. womc 가 만들었던 옛 파일 — 루트 `PLAN.md` · `docs/CHANGELOG.md` · `docs/HARNESS-AUDIT.md` · `.claude/agents/` · `.claude/skills/` 의 plan-feature·make-rule·harness-audit — 이 남아 있으면 「B. 다시 짜기」로 간다. 이름이 비슷해도 사용자가 만든 것이면 옛 파일이 아니다.
2. `CLAUDE.md` 의 첫 줄부터 첫 `### ` 줄 앞까지를 `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md` 로 통째 바꾼다 — 손으로 옮겨 적지 않는다. 첫 `### ` 아래는 한 글자도 건드리지 않는다.
3. `.claude/settings.json` 은 `${CLAUDE_PLUGIN_ROOT}/templates/settings.json` 에 있는 키만 견준다. 정본에 없는 키(`hooks`·`autoMemoryDirectory`·`enabledPlugins` 등)와 사용자가 더한 allow·deny 는 그대로 둔다. 값이 정본과 다르면 커밋 기록을 보고 일부러 바꾼 것이면 남긴다.
4. 상태줄 파일은 정본으로 맞춘다.
5. 브리핑이 규격(칸 넷 · 칸 밖 줄 · 굵게·이모지·꾸밈용 표 · 지시문 40줄)에 어긋나면 고치지 말고 한 줄로 알리기만 한다.
6. 두 가지를 기계로 본다. 브리핑이 그대로인가 — `diff <(git show HEAD:CLAUDE.md | sed -n '/^### /,$p') <(sed -n '/^### /,$p' CLAUDE.md)`. 규칙 부분이 정본과 같은가 — `diff "$CLAUDE_PLUGIN_ROOT/templates/CLAUDE.md" <(sed -n '1,/^### /p' CLAUDE.md | sed '$d')`. 둘 다 빈 결과여야 한다.
7. 커밋하고 「바꾼 것」을 한 줄 보고한다. 묻지 않는다 — 다만 프로젝트 규칙이 하네스 파일을 고치기 전에 묻기를 요구하면 그쪽을 따른다.

## 정본

### 1) `CLAUDE.md`
규칙 부분에는 `### ` 를 쓰지 않는다 — C 2 의 교체 범위가 파일의 첫 `### ` 로 잘린다.
플러그인 폴더의 `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md` 를 그대로 복사한다 — 손으로 옮겨 적지 않는다. 이 파일이 「작업 규칙」 전부이고, 그 뒤에 「### 할 일」부터 브리핑을 붙여 채운다.


### 2) `.claude/settings.json`
플러그인 폴더의 `${CLAUDE_PLUGIN_ROOT}/templates/settings.json` 을 그대로 복사한다 — 손으로 옮겨 적지 않는다.
- allow: 파일 수정·조회·git·실행 명령을 구체 항목으로 적는다(`Bash(*)` 같은 넓은 규칙은 auto mode 가 무시한다). 프로젝트에 필요한 것을 더한다.
- ask: 되돌릴 수 없는 것만 — `git push` · `git reset --hard` · `rm` · `mv`.
- deny: `.env` 류 읽기·수정(`.env.example` 은 예외).

권한 규칙에 `Write(경로)` 를 쓰지 않는다. 경로를 붙일 때는 `Edit(경로)` 로 적는다(`Write(경로)` 는 아무 데도 안 걸리는 죽은 규칙이라 경고만 띄운다).

### 3) `.claude/statusline.js`
플러그인 폴더의 `templates/statusline.js` 를 그대로 복사한다(`${CLAUDE_PLUGIN_ROOT}/templates/statusline.js`). 터미널 아래 한 줄에 모델·토큰·폴더명을 보여 준다. 어떤 경우에도 오류를 내지 않고 조용히 빈 줄을 그린다.

### 4) `.gitignore`
없을 때만 만든다. 있으면 아래 항목 중 빠진 것만 덧붙인다.
```
.claude/settings.local.json
node_modules/
__pycache__/
*.py[cod]
.venv/
venv/
.env
.env.*
!.env.example
dist/
build/
*.log
.DS_Store
Thumbs.db
.vscode/
.idea/
```
