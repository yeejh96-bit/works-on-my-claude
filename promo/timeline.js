// 장면·효과음이 같이 쓰는 시간표 (초 단위). scene.html 과 audio.js 둘 다 읽는다.
// 자막은 최소 2.5초, 터미널 응답은 3초 이상 머문다.
const T = {
  fps: 30,
  duration: 50.0,
  scenes: {
    hook:    [0,    4.5],
    problem: [4.5,  12.5],
    reveal:  [12.5, 18.0],
    install: [18.0, 27.0],
    flow:    [27.0, 39.5],
    why:     [39.5, 45.5],
    cta:     [45.5, 50.0],
  },
  typing: [
    { id: 'p_user', at: 4.8,  text: '로그인 기능 만들어줘', cps: 16 },
    { id: 'i1',     at: 18.8, text: '/plugin marketplace add yeejh96-bit/works-on-my-claude', cps: 46 },
    { id: 'i2',     at: 22.0, text: '/plugin install womc@works-on-my-claude', cps: 46 },
    { id: 'f_user', at: 27.5, text: '가계부 웹앱 만들어 줘', cps: 15 },
  ],
  prompts: [6.0, 6.4, 6.75, 7.05, 7.35],
  changedAt: 8.0,
  errorAt: 9.0,
  shakeAt: 11.4,
  boomAt: 12.5,
  whooshes: [4.5, 18.0, 27.0, 39.5, 45.5],
  oks: [20.5, 23.4],
  files: [24.3, 24.45, 24.6, 24.75],
  replyAt: 29.0,
  steps: [31.0, 32.0, 33.0, 34.0, 35.0],
  askAt: 36.3,
  cards: [40.0, 41.2, 42.4],
  ctaAt: 46.9,
};
if (typeof module !== 'undefined') module.exports = T;
