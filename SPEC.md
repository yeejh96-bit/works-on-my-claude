# 프로젝트 명세 (SPEC)

> 이 파일을 채운 뒤 작업을 시작한다. 비어 있으면 먼저 채운다.
> 이 파일은 CLAUDE.md 에 딸려 매 세션 로드된다. 너무 길어지지 않게 유지하고,
> 특정 영역에만 해당하는 세부 내용은 `.claude/rules/` 규칙으로 옮긴다(make-rule 스킬 참고).

## 1. 기술 스택
- Claude Code 플러그인. 코드가 아니라 **마크다운 지시문 파일**로 이루어진다.
- 슬래시 명령: `commands/womc.md`
- 플러그인이 직접 제공하는 것(프로젝트로 복사되지 않음): `agents/`(4종) · `skills/`(2종) · `output-styles/womc-caveman.md`
- 플러그인/마켓플레이스 메타데이터: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
- 배포: GitHub 저장소 `yeejh96-bit/works-on-my-claude` → `/plugin` 으로 설치.

## 2. 뭘 푸는가
새 프로젝트를 시작할 때마다 `CLAUDE.md`·명세·`.claude/` 구조를 손으로 만드는 번거로움을 없앤다.
빈 폴더에서 `/womc` 한 번이면 매번 똑같은 최소 운영체계(컨텍스트 엔지니어링 + 하네스 + 운영 절차)가 깔린다.
코딩을 모르는 사용자도 Claude Code가 꾸준히 잘 일하게 만드는 것이 목표.

## 3. 핵심 기능 (3~5개)
1. `/womc` — 고정 골격 생성(이미 있는 파일은 덮어쓰지 않고 건너뜀). 신규 빈 폴더면 빈 SPEC 템플릿, **기존 코드가 있는 폴더면 온보딩**: `explore` 로 훑어 SPEC 초안을 채우고, 이미 있는 `CLAUDE.md`·`.claude/settings.json` 은 건너뛰지 않고 womc 규칙을 **덧붙여 병합**(사용자 내용 보존, `<!-- womc:begin/end -->` 구획), 코드 관례를 `.claude/rules/` 로 **캡처**(제안 후), 구조 정리가 필요해 보이면 `plan-feature` 리팩터를 **제안**한다(womc 자체는 코드를 옮기지 않음). 골격에는 `.claude/statusline.js`(터미널 하단 상태줄 — 모델명·토큰·5시간/주간 한도·폴더명, Node.js 필요)도 포함되며 `settings.json` 의 `statusLine` 이 실행한다. `/womc update` 는 불변 골격만 최신으로 교체(사용자가 채운 파일은 보존)하며, 그 전에 먼저 `claude plugin update` 로 플러그인 자체도 함께 갱신한다. 갱신 전에 `womc:skeleton-version` 을 최신 버전과 대조해, **옛 캐시면 GitHub 에서 최신 골격을 직접 받아 적용하고, 받지 못할 때만 멈추고 플러그인 업데이트+재시작을 안내**한다. `/womc eject <이름>` 은 플러그인이 제공하는 서브에이전트·스킬·출력 스타일을 그 프로젝트 안으로 복사해 고쳐 쓰게 한다.
2. 항상 로드되는 규칙(CLAUDE.md) + 프로젝트 명세(SPEC.md, `@import`)만 always-on으로 유지. 대화 답변은 원시인 말투(케이브맨, 고정 — 단계 없음)로 강제되며, 말투 규칙은 출력 스타일 `output-styles/womc-caveman.md` **한 곳**에만 두고 `.claude/settings.json` 의 `outputStyle` 이 프로젝트별로 켠다. 파일 문서와 서브에이전트 보고는 대상 아니다(출력 스타일은 서브에이전트에 적용되지 않는다).
3. 오케스트레이션 서브에이전트 4종: `explore`(조사·haiku) · `plan`(설계·opus) · `implement`(구현·sonnet, 유일하게 파일 직접 수정) · `verify`(검증·sonnet). 메인은 지휘자로 얇게 유지하고 무거운 일을 병렬 위임. 서브에이전트도 CLAUDE.md 를 물려받으므로(Explore·Plan 내장 2종만 예외) 공통 규칙은 CLAUDE.md 한 곳에 두고, 각 파일에는 상속되지 않는 것(역할·입력계약·출력계약)만 적는다. 코드 검토 전용 에이전트는 두지 않는다 — Claude Code 기본 `/code-review` 를 쓴다.
4. 운영 스킬 3종: `plan-feature`(기능 추가·수정 겸용 — 큰 작업은 쪼개 PLAN/TASKS 관리, 작은 변경·버그수정·리팩터는 가벼운 경로, 조사→설계→구현→검증 위임 후 검토는 `/code-review` 권유. 세션이 바뀌어도 이어지도록 각 작업 항목에 손댈 파일·이어 쓸 것·완료 조건·확인 방법을 남긴다) · `make-rule`(규칙 자동 생성) · `harness-audit`(골격에서 뺄 것 점검·기록).
5. 안전 기본값(settings.json): 비밀 `.env` 읽기 차단(견본 `.env.example` 은 읽힘) + 자주 쓰는 읽기 전용 명령 허용.

## 4. 화면 흐름
GUI 없음(CLI 플러그인). 사용자 흐름:
`/womc` 실행 → 골격 생성(기존 프로젝트면 SPEC 초안까지) → `SPEC.md` 채움·검토 → "○○ 만들자 / ○○ 고쳐줘" → `plan-feature` 가 작업 크기에 맞춰 (큰 작업은 PLAN/TASKS 생성) 구현·검증.

## 5. 저장할 데이터
사용자 데이터 저장 없음. 이 저장소가 관리하는 산출물은 골격 정의 그 자체:
`commands/womc.md`(생성될 파일 내용의 원본), `agents/`·`skills/`·`output-styles/`, 플러그인 메타데이터, `README.md`, `LICENSE`.
버전은 `.claude-plugin/plugin.json` 의 `version` 으로 관리한다.

## 6. 안 만들 것
- `.mcp.json` 자동 생성 안 함(프로젝트마다 다름 → 필요할 때 직접 추가).
- 기술 스택·기능을 골격에 미리 박지 않음(SPEC 빈 템플릿으로만 둠).
- `/womc` 가 코드를 구현하지 않음(구조 생성까지만). SPEC 도 대신 채우지 않음 — 단, **기존 프로젝트 감지 시 코드를 훑어 SPEC 초안 작성은 예외**(사용자 검토 전제). 온보딩의 구조 정리도 womc 가 직접 코드를 옮기지 않고 `plan-feature` 로 넘긴다(감지·제안까지만).
- GUI/웹 UI 없음.

## 7. 어디서 돌아가나 (배포)
GitHub 저장소 `yeejh96-bit/works-on-my-claude` 에 push → 사용자가 Claude Code 에서 `/plugin` 으로 설치.
