# worksonmyclaude

Claude Code 커스텀 슬래시 명령 백업 저장소.

## 들어있는 것
- `.claude/commands/womc.md` — `/womc` 명령. 새 프로젝트 폴더에서 실행하면
  항상 동일한 기본 골격(CLAUDE.md, SPEC.md, README.md, .gitignore, `.claude/` 하위 폴더)을
  현재 폴더에 생성한다. (스택·MCP처럼 프로젝트마다 다른 것은 넣지 않는다.)

## 복구 방법
PC를 새로 세팅하거나 Claude Code를 다시 깐 경우, 이 저장소의 `womc.md` 를
아래 위치에 복사하면 `/womc` 명령이 그대로 살아난다.

- 모든 프로젝트에서 쓰려면: `~/.claude/commands/womc.md`
  (Windows: `C:\Users\<사용자>\.claude\commands\womc.md`)
- 특정 프로젝트에서만 쓰려면: `<프로젝트>/.claude/commands/womc.md`

## 사용법
1. 빈 프로젝트 폴더에서 Claude Code 실행
2. `/womc` 입력 → 기본 골격 생성
3. `SPEC.md` 채우기 → 계획(PLAN) 짜기 → 한 기능씩 구현
