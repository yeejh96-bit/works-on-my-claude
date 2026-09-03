---
name: womc-namespace-display-left-as-is
description: "/womc 명령어가 자동완성에 /womc:womc로 겹쳐 보이는 건 정상이며, 사용자가 그대로 두기로 결정함"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ffaa8567-4ecb-469b-87e8-34658f6e78f5
---

`/womc` 슬래시 명령을 입력하면 자동완성에 `/womc:womc`로 표시된다. 이는 플러그인 이름("womc")과 명령어 파일 이름("womc.md")이 같아서 생기는 정상적인 네임스페이스 표시이며, 버그가 아니다. `/womc`만 입력해도 항상 정상 실행된다.

**Why:** 고칠 수는 있으나(플러그인 이름 변경 또는 명령어 파일명 변경) 둘 다 전역 플러그인 설정 파일을 건드려야 하는 화면 표시 문제일 뿐, 기능에는 영향이 없다. 사용자가 "그냥 지금 이대로 둘게"라고 명시적으로 결정함.

**How to apply:** 앞으로 이 주제가 다시 나와도 먼저 나서서 이름 변경을 제안하지 말 것. 사용자가 먼저 다시 요청하면 그때 [[womc 플러그인 관련]] 내용을 참고해 진행한다.
