# 프로젝트 명세 (SPEC)

> 이 파일을 채운 뒤 작업을 시작한다. 비어 있으면 먼저 채운다.
> 이 파일은 CLAUDE.md 에 딸려 매 세션 로드된다. 너무 길어지지 않게 유지하고,
> 특정 영역에만 해당하는 세부 내용은 `.claude/rules/` 규칙으로 옮긴다(make-rule 스킬 참고).

## 1. 기술 스택
- Claude Code 플러그인. 코드가 아니라 **마크다운 지시문 파일**로 이루어진다.
- 슬래시 명령: `commands/womc.md`
- 플러그인/마켓플레이스 메타데이터: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- 배포: GitHub 저장소 `yeejh96-bit/works-on-my-claude` → `/plugin` 으로 설치.

## 2. 뭘 푸는가
새 프로젝트를 시작할 때마다 `CLAUDE.md`·명세·`.claude/` 구조를 손으로 만드는 번거로움을 없앤다.
빈 폴더에서 `/womc` 한 번이면 매번 똑같은 최소 운영체계(컨텍스트 엔지니어링 + 하네스 + 운영 절차)가 깔린다.
코딩을 모르는 사용자도 Claude Code가 꾸준히 잘 일하게 만드는 것이 목표.

## 3. 핵심 기능 (3~5개)
1. `/womc` — 빈 폴더에 고정 골격 생성(이미 있는 파일은 덮어쓰지 않고 건너뜀). `/womc update` 는 불변 골격만 최신으로 교체(사용자가 채운 파일은 보존).
2. 항상 로드되는 규칙(CLAUDE.md) + 프로젝트 명세(SPEC.md, `@import`)만 always-on으로 유지.
3. 위임용 서브에이전트 2종: `explore`(조사) · `verify`(검증) — 무거운 작업을 별도 컨텍스트로 빼 토큰 절약.
4. 운영 스킬 2종: `plan-feature`(쪼개기·PLAN/TASKS 관리·검증) · `make-rule`(규칙 자동 생성).
5. 안전 기본값(settings.json): 비밀 `.env` 읽기 차단(견본 `.env.example` 은 읽힘) + 자주 쓰는 읽기 전용 명령 허용.

## 4. 화면 흐름
GUI 없음(CLI 플러그인). 사용자 흐름:
`/womc` 실행 → 골격 생성 → `SPEC.md` 채움 → "○○ 기능 만들자" → `plan-feature` 가 PLAN/TASKS 생성·구현·검증.

## 5. 저장할 데이터
사용자 데이터 저장 없음. 이 저장소가 관리하는 산출물은 골격 정의 그 자체:
`commands/womc.md`(생성될 파일 내용의 원본), 플러그인 메타데이터, `README.md`, `LICENSE`.
버전은 `.claude-plugin/plugin.json` 의 `version` 으로 관리한다.

## 6. 안 만들 것
- `.mcp.json` 자동 생성 안 함(프로젝트마다 다름 → 필요할 때 직접 추가).
- 기술 스택·기능을 골격에 미리 박지 않음(SPEC 빈 템플릿으로만 둠).
- `/womc` 가 SPEC 를 대신 채우거나 코드를 구현하지 않음(구조 생성까지만).
- GUI/웹 UI 없음.
