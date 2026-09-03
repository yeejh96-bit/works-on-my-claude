---
name: womc
description: 프로젝트 폴더에 womc 기본 하네스(CLAUDE.md · .claude/settings.json · 상태줄)를 깔거나 v4 철학에 맞게 다시 짠다. 세션 시작 훅이 「세팅 없음」「구버전」을 알리면 사용자에게 묻지 않고 이 스킬을 부른다. 사용자가 /womc 를 직접 쳐도 같은 절차다.
---

<!-- womc:skeleton-version=4.0.0 -->

# womc 세팅

철학: **하네스는 얇게, 나머지는 모델을 믿고 맡긴다.** 사용자가 승인하거나 결정하는 일을 최소로 줄인다.
하네스 기능은 그때 모델의 약점을 덮는 임시 장치다. 모델이 좋아지면 뺀다. 만든 것에 애착을 갖지 않는다.

## 0. 먼저 확인
- 현재 폴더에 `CLAUDE.md` 가 있고 그 안에 `womc:skeleton-version=` 표식이 있으면 → 「B. 다시 짜기」. 표식 버전이 이 스킬 맨 위 표식과 같으면 할 일이 없다고 한 줄 알리고 끝낸다.
- `CLAUDE.md` 가 있는데 표식이 없으면(womc 를 안 쓰던 프로젝트) → 「B. 다시 짜기」.
- `CLAUDE.md` 가 없으면 → 「A. 새로 깔기」.
- git 저장소가 아니면 묻지 않고 `git init` 부터 한다.

## A. 새로 깔기
1. 아래 「정본」 네 파일을 그대로 만든다. 이미 있는 파일은 덮어쓰지 않는다.
2. 폴더를 읽는다(파일 목록·README·설정 파일). 코드로 알 수 있는 것은 묻지 않는다.
3. 브리핑을 채운다. 빈 폴더면 「무엇을 만들 건가」 한 가지만 AskUserQuestion 으로 선택지를 곁들여 묻는다. 코드가 있으면 보통 아무것도 묻지 않고 추정해 적는다.
4. 체크포인트 커밋을 남기고 「만든 파일 · 브리핑에 적은 것」을 한 줄씩 보고한다.

## B. 다시 짜기 (기존 프로젝트 · 구버전 womc)
기존 하네스 구조에 얽매이지 않는다. 절 제목·파일 배치·옛 절차는 지키지 않고 v4 모양으로 새로 쓴다.
1. 체크포인트 커밋을 남긴다(이 커밋이 있어 아래 지우기를 묻지 않는다).
2. 기존 하네스 전부를 읽는다: `CLAUDE.md`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`, `.claude/settings.json`, `PLAN.md`, `TASKS.md`, `docs/CHANGELOG.md`, `AGENTS.md` 등.
3. 남길 것은 **코드로 알 수 없는 사실**뿐이다.
   - 사용자가 적은 프로젝트 사실·지킬 것·끝난 조건·확인 명령 → 새 `CLAUDE.md` 「브리핑」으로.
   - 특정 경로에만 걸리는 제약 → `.claude/rules/<이름>.md` 에 `paths` 를 붙여서.
   - 사용자가 직접 만든 스킬·훅·MCP 설정 → 그대로 둔다.
   - `AGENTS.md` 가 있으면 새 `CLAUDE.md` 첫 줄에 `@AGENTS.md` 로 불러온다.
4. 옛 하네스는 지운다: womc 가 만들었던 `agents/`·`skills/`(plan-feature·make-rule·harness-audit)·`PLAN.md`·`TASKS.md`(끝난 항목)·`docs/CHANGELOG.md`·`docs/HARNESS-AUDIT.md`·`.claude/rules/제약-*.md`(paths 없는 것) 등. git 이 추적하는 파일은 `git rm` 으로 지운다(커밋으로 되돌릴 수 있다).
5. 새 `CLAUDE.md` 를 「정본」대로 쓰고 브리핑을 채운다. `.claude/settings.json` 은 정본을 기준으로 하되 사용자가 더한 allow·deny 항목은 남긴다. 상태줄 파일은 정본으로 바꾼다.
6. 커밋하고 「남긴 것 · 옮긴 것 · 지운 것」을 한 줄씩 보고한다. 묻지 않는다.

## 정본

### 1) `CLAUDE.md`
```markdown
# 작업 규칙
<!-- womc:skeleton-version=4.0.0 -->

이 파일은 매 세션 자동으로 읽힌다. 「작업 규칙」은 womc 가 관리하고 「브리핑」은 모델이 채운다. 전체 200줄을 넘기지 않는다.

## 나에 대해
- 나는 코딩을 모른다. 전문 용어는 풀어서 설명한다.
- 모든 설명·보고는 한국어로 한다.
- 답은 결론부터, 대개 다섯 줄 안. 인사말·완충어·도구 중계·꾸밈용 표·이모지는 없앤다.
- 뜻이 상하면 안 줄인다. 부정어·숫자·코드·명령·에러 문구는 그대로.
- 채팅 밖으로 나가는 글(커밋·문서)은 평문이다.

## 일하는 방식
- 하네스는 얇게, 나머지는 네가 판단한다. 여기 없는 것은 네가 정하고 한 줄로 알린다.
- 되돌릴 수 있는 일은 묻지 않는다. 손대기 전에 체크포인트 커밋(git add · git commit)을 남기고 진행한다. push 는 하지 않는다.
- 커밋으로도 못 되돌리는 것만 하기 전에 한 줄로 묻는다: git push / 배포·외부로 보내기 / 데이터베이스 내용 지우기 / git reset --hard / 파일·폴더 지우기(체크포인트 커밋이 있고 git 이 추적하는 파일은 예외) / 폴더 밖으로 옮기기. 무엇이 사라지는지 쉬운 말로 함께 알린다.
- git 저장소가 아니면 묻지 않고 git init 부터 한다.
- 물어야 할 때는 선택지로 묻는다(AskUserQuestion). 답이 달라도 결과가 크게 안 달라지면 묻지 않고 정한다.
- 한 번에 한 기능만 한다. 대화가 무거워지면 /compact 나 새 세션을 제안한다.

## 기능 작업 순서
1. 브리핑을 읽고 일을 단계로 쪼갠다. 한 세션에 안 끝날 크기면 TASKS.md 에 적는다.
2. 체크포인트 커밋.
3. 구현. 무거운 조사·구현·확인은 서브에이전트에 맡기고 결론만 받는다.
4. 끝났다고 말하기 전에 브리핑의 확인 방법을 별도 서브에이전트가 실행한다. 만든 쪽이 스스로 판정하지 않는다.
5. 실행 결과·화면(로그 요지·스크린샷)을 붙여 한 줄로 보고하고 커밋한다.

## TASKS.md (필요할 때만)
- 한 세션에 안 끝날 일에만 만든다. 항목마다 「손댈 파일 · 이어 쓸 것 · 끝난 조건 · 확인 방법」 네 줄.
- 끝난 항목은 지운다. 파일이 비면 파일도 지운다. 끝난 기록은 커밋 메시지가 맡는다.

## 규칙·스킬 남기기
- 앞으로 계속 지킬 제약은 .claude/rules/<이름>.md 에 남기되 반드시 paths 를 붙인다(그 파일을 만질 때만 읽히게). 전체에 걸치는 규칙은 브리핑에 한 줄로.
- 같은 절차를 두 번 이상 하면 .claude/skills/<이름>/SKILL.md 로 남긴다.
- 작업 시작 때 부푼 것(끝난 항목이 남은 TASKS.md · paths 없는 규칙 · 200줄 넘는 이 파일)이 보이면 묻지 않고 정리하고 한 줄 보고한다.

## 브리핑 (모델이 채우고 고친다)
코드로 알 수 없는 것만 적는다. 보통 「할 일 · 지킬 것 · 끝난 조건 · 확인 방법(빌드·테스트·실행 명령)」이 들어가지만 필요한 것만 적고 없는 칸은 만들지 않는다.
사용자가 한 말 중 앞으로도 지킬 것은 여기로 옮긴다. 브리핑이 바뀌면 .claude/rules 와 .claude/settings.json 도 그에 맞춘다.

(아직 비어 있음 — 첫 대화에서 폴더를 읽고 채운다)
```

### 2) `.claude/settings.json`
- allow: 파일 수정·조회·git·실행 명령을 **구체 항목으로** 적는다(`Bash(*)` 같은 넓은 규칙은 auto mode 가 무시한다).
- ask: 되돌릴 수 없는 것만 — `git push` · `git reset --hard` · `rm` · `mv`.
- deny: `.env` 류 읽기·수정(`.env.example` 은 예외).
```json
{
  "statusLine": {
    "type": "command",
    "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/statusline.js\"",
    "refreshInterval": 10
  },
  "permissions": {
    "allow": [
      "Bash(ls:*)", "Bash(cat:*)", "Bash(head:*)", "Bash(tail:*)", "Bash(grep:*)", "Bash(rg:*)",
      "Bash(find:*)", "Bash(wc:*)", "Bash(sort:*)", "Bash(uniq:*)", "Bash(awk:*)", "Bash(cut:*)",
      "Bash(tr:*)", "Bash(diff:*)", "Bash(file:*)", "Bash(stat:*)", "Bash(which:*)", "Bash(echo:*)",
      "Bash(printf:*)", "Bash(du:*)", "Bash(df:*)", "Bash(xargs:*)", "Bash(jq:*)", "Bash(tree:*)",
      "Bash(pwd)", "Bash(cd:*)",
      "Bash(git status:*)", "Bash(git log:*)", "Bash(git diff:*)", "Bash(git show:*)",
      "Bash(git ls-files:*)", "Bash(git rev-parse:*)", "Bash(git check-ignore:*)", "Bash(git branch:*)",
      "Bash(git remote:*)", "Bash(git config:*)", "Bash(git blame:*)", "Bash(git add:*)",
      "Bash(git commit:*)", "Bash(git init:*)", "Bash(git stash:*)", "Bash(git switch:*)",
      "Bash(git fetch:*)", "Bash(git pull:*)", "Bash(git rm:*)",
      "Bash(python3:*)", "Bash(python:*)", "Bash(node:*)", "Bash(pytest:*)",
      "Bash(npm run:*)", "Bash(npm test:*)", "Bash(npm ci:*)", "Bash(npm install:*)", "Bash(npm ls:*)",
      "Bash(npx:*)", "Bash(uv run:*)", "Bash(pip install:*)", "Bash(pip3 install:*)",
      "Bash(mkdir:*)", "Bash(cp:*)", "Bash(touch:*)", "Bash(sed:*)", "Bash(chmod:*)",
      "Edit", "Write", "NotebookEdit"
    ],
    "ask": [
      "Bash(git push:*)", "Bash(git reset --hard:*)", "Bash(rm:*)", "Bash(mv:*)",
      "PowerShell(git push:*)", "PowerShell(git reset --hard:*)", "PowerShell(Remove-Item:*)", "PowerShell(Move-Item:*)"
    ],
    "deny": [
      "Read(**/.env)", "Read(**/.env.local)", "Read(**/.env.*.local)", "Read(**/.env.development)",
      "Read(**/.env.production)", "Read(**/.env.test)", "Read(**/.env.staging)", "Edit(**/.env)"
    ]
  }
}
```
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
