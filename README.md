# works-on-my-claude

Claude Code에서 `/womc` 한 번으로 새 프로젝트의 기본 골격을 까는 커스텀 슬래시 명령.

## 무엇을 푸는가
새 프로젝트를 시작할 때마다 `CLAUDE.md`, 명세 파일, `.claude/` 폴더 구조를 **0에서 손으로 만드는 번거로움**을 없앤다. 빈 폴더에서 `/womc` 만 입력하면 매번 똑같은 골격이 깔린다.

## 설치

Claude Code 안에서 두 줄이면 끝이다.

```
/plugin marketplace add yeejh96-bit/works-on-my-claude
/plugin install womc@works-on-my-claude
```

설치 후 `/reload-plugins` 를 실행하면 `/womc` 가 바로 잡힌다.

### 수동 설치 (플러그인을 쓰지 않을 때)
이 레포의 `commands/womc.md` 를 내려받아 아래 위치에 두어도 된다.
- Mac / Linux: `~/.claude/commands/womc.md`
- Windows: `C:\Users\<사용자명>\.claude\commands\womc.md`

특정 프로젝트에서만 쓰려면 `<프로젝트>/.claude/commands/womc.md` 에 둔다.

## 사용법
1. 새(빈) 프로젝트 폴더를 만든다.
2. 그 폴더에서 Claude Code를 실행한다.
3. 프롬프트에 `/womc` 를 입력한다.
4. 현재 폴더에 골격이 생성된다. 이후 `SPEC.md` 를 채우고 → 계획을 짜고 → 한 기능씩 구현한다.

`/womc` 는 **구조 생성까지만** 한다. SPEC를 대신 채우거나 코드를 짜지 않는다.

> ※ `/womc` 실행 중 파일 생성 권한을 물어보면 "허용"을 선택하세요.

## 생성되는 구조
```
현재폴더/
├─ CLAUDE.md          # 항상 적용되는 불변 작업 규칙 (끝에서 @SPEC.md import)
├─ SPEC.md            # 프로젝트 명세 빈 템플릿 (헤더 6개만)
├─ README.md          # 생성된 프로젝트 자체의 구조 설명
├─ .gitignore         # node_modules / .env / dist 등
└─ .claude/
   ├─ settings.json      # 하네스: 안전한 읽기 전용 명령 미리 허용 (허용 프롬프트 줄임)
   ├─ agents/
   │  ├─ README.md
   │  └─ explore.md      # 코드 조사 전용 서브에이전트 — 조사를 별도 컨텍스트로 빼 토큰 절약
   ├─ skills/
   │  ├─ README.md
   │  └─ plan-feature/SKILL.md  # 기능을 작게 쪼개 한 번에 하나씩 구현하는 절차(필요할 때만 로드)
   └─ rules/README.md    # 세부 규칙 자리 (@import 로 켜는 옵션)
```
> `.mcp.json` 은 **만들지 않는다.** MCP는 프로젝트마다 다르므로 필요할 때 직접 추가한다.

## 하네스가 토큰·컨텍스트를 아끼는 방식
골격은 "맥락을 잘 채우는 것"에서 그치지 않고, **작업 중 컨텍스트가 불어나는 걸 막는 장치**를 함께 깐다.

- **`explore` 서브에이전트** — 여러 파일을 뒤지는 무거운 조사를 *별도 컨텍스트*에서 끝내고 **결론만** 메인 대화로 가져온다. 조사 과정의 파일 내용이 본 대화에 쌓이지 않아 토큰이 절약된다.
- **`plan-feature` 스킬** — 큰 작업을 한꺼번에 벌이지 않고 작은 단계로 쪼개 하나씩 진행하게 해, 한 세션에 컨텍스트가 터지는 걸 막는다. 스킬은 **필요할 때만 로드**돼 평소 컨텍스트를 차지하지 않는다.
- **CLAUDE.md의 "컨텍스트·토큰 아끼기" 규칙** — 위 두 습관(무거운 조사는 위임, 한 번에 한 기능, 길어지면 `/compact`)을 매 세션 Claude에게 상기시킨다.
- **settings.json 읽기 전용 허용** — `git status` 같은 안전한 명령을 미리 허용해 프롬프트 왕복을 줄인다.

## 설계 원리
**변하지 않는 것만 내용을 채우고, 프로젝트마다 달라지는 것은 빈 칸으로 두거나 아예 만들지 않는다.**

- 항상 같은 것 (→ 내용을 채움): 코딩 입문자라는 점, "코드는 전체 파일로 제공", "한국어로 설명" 같은 불변 작업 규칙.
- 프로젝트마다 다른 것 (→ 빈 틀 또는 생성 안 함): 기술 스택·기능은 `SPEC.md` 빈 템플릿으로만, MCP 설정은 아예 생성하지 않음.

골격에 스택·MCP를 미리 박아두면 다음 프로젝트에서 오히려 걸리적거리기 때문이다.

## 파일 로드 방식
- **CLAUDE.md** 는 Claude Code가 켜질 때 **매 세션 자동으로 로드**된다.
- **SPEC.md** 는 CLAUDE.md 맨 끝의 `@SPEC.md` 줄을 통해 **import 되어 함께 딸려 로드**된다.

즉 불변 규칙(CLAUDE.md)과 프로젝트 명세(SPEC.md)가 매 세션 한 묶음으로 Claude에게 전달된다.

## 이름 유래
"It works on my machine"(내 컴퓨터에선 되는데…) 밈을 비튼 이름 — 여기선 **내 Claude에선 잘 된다**.

## 라이선스
MIT — 자세한 내용은 [LICENSE](./LICENSE) 참고.
