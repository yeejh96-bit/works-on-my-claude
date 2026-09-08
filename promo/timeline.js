// 장면·효과음이 같이 쓰는 시간표 (초 단위). scene.html 과 audio.js 둘 다 읽는다.
const T = {
  fps: 30,
  duration: 32.5,
  scenes: {
    hook:    [0,    3.0],
    problem: [3.0,  8.0],
    reveal:  [8.0,  11.5],
    install: [11.5, 17.5],
    flow:    [17.5, 26.5],
    why:     [26.5, 29.5],
    cta:     [29.5, 32.5],
  },
  typing: [
    { id: 'p_user', at: 3.3,  text: '로그인 기능 만들어줘', cps: 16 },
    { id: 'i1',     at: 12.1, text: '/plugin marketplace add yeejh96-bit/works-on-my-claude', cps: 46 },
    { id: 'i2',     at: 14.3, text: '/plugin install womc@works-on-my-claude', cps: 46 },
    { id: 'f_user', at: 17.9, text: '가계부 웹앱 만들어 줘', cps: 15 },
  ],
  prompts: [4.4, 4.8, 5.15, 5.45, 5.75],
  changedAt: 6.2,
  errorAt: 6.7,
  shakeAt: 7.3,
  boomAt: 8.0,
  whooshes: [3.0, 11.5, 17.5, 26.5, 29.5],
  oks: [13.7, 15.6],
  files: [16.25, 16.4, 16.55, 16.7],
  replyAt: 19.2,
  steps: [20.4, 21.2, 22.0, 23.0, 23.8],
  askAt: 24.8,
  cards: [26.9, 27.6, 28.3],
  ctaAt: 30.2,
};
if (typeof module !== 'undefined') module.exports = T;
