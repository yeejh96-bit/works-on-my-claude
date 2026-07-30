#!/usr/bin/env node
/**
 * womc — 답변 말투(짧게 말하기) 강제 훅.
 * UserPromptSubmit 에서 실행되어, CLAUDE.md 의 `womc:brevity=` 값을 읽고
 * 지금 지켜야 할 말투 규칙을 매 입력마다 다시 알려준다.
 * Node.js 내장 모듈만 쓴다. Node 가 없으면 이 훅만 빠질 뿐 다른 기능엔 지장 없다.
 */
const fs = require('fs');
const path = require('path');

const RULES = {
  '약하게': '인사말·사과·칭찬, "~하겠습니다" 같은 예고, 방금 한 말 되풀이를 지운다. 문장은 평소처럼.',
  '보통': '위에 더해 서론·맺음말을 지우고, 결론부터 불릿으로 쪼갠 뒤 종결어미를 뗀다(명사형).',
  '최소': '위에 더해 조사·수식어까지 지우고, 핵심 단어·경로·숫자만 나열한다.',
  '케이브맨': '원시인처럼 말한다. 한 줄에 한 뜻, 2~5 단어 단문. 나는 "나", 사용자는 "너". 동사는 "고침"·"됨"·"망가짐"처럼 기본형. 경어·접속사·비유 금지. 한 문장이 6단어를 넘으면 끊는다.',
};
const DEFAULT_LEVEL = '케이브맨';

function readLevel() {
  const dir = process.env.CLAUDE_PROJECT_DIR || process.cwd();
  try {
    const md = fs.readFileSync(path.join(dir, 'CLAUDE.md'), 'utf8');
    const m = md.match(/womc:brevity\s*=\s*([^\s\->]+)/);
    if (m && RULES[m[1]]) return m[1];
  } catch (e) { /* CLAUDE.md 가 없으면 기본값을 쓴다 */ }
  return DEFAULT_LEVEL;
}

const level = readLevel();
process.stdout.write([
  '[womc 답변 형식 — 지금 강도: ' + level + ']',
  RULES[level],
  '이 규칙은 사용자에게 보내는 대화 답변에만 적용한다(파일에 쓰는 문서·주석·커밋 메시지는 제외).',
  '어느 강도에서도 지우지 않는 것: 파일 경로와 경로:줄번호, 다음에 할 일 한 줄, 되묻는 질문, 위험·주의 경고, 사용자가 골라야 하는 선택지. 경로·명령어·숫자는 원문 그대로.',
  '사용자가 "자세히"·"설명해줘"·"왜?"라고 하면 그 답만 평소 길이로 푼다.',
].join('\n') + '\n');
