// 배경음악(로파이 일렉트로닉)과 효과음을 코드로 합성해 mix.wav 로 쓴다.
const fs = require('fs');
const T = require('./timeline');

const SR = 44100;
const N = Math.ceil(T.duration * SR);
const L = new Float64Array(N), R = new Float64Array(N);

// 결정적 난수(매번 같은 소리)
let seed = 7;
const rnd = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296 * 2 - 1; };

// gen(i, n) → 샘플값. at 초부터 dur 초 동안 더한다. pan: -1(왼)~1(오른)
function add(at, dur, gen, vol = 1, pan = 0) {
  const s = Math.floor(at * SR), n = Math.floor(dur * SR);
  const gl = Math.min(1, 1 - pan) * vol, gr = Math.min(1, 1 + pan) * vol;
  for (let i = 0; i < n && s + i < N; i++) { const v = gen(i, n); L[s + i] += v * gl; R[s + i] += v * gr; }
}
const env = (i, n, a, d) => { const t = i / n; return t < a ? t / a : Math.max(0, 1 - (t - a) / (1 - a)) ** d; }; // 어택·감쇠
const exp = (i, k) => Math.exp(-i / SR * k);

// 단순 원-폴 로우패스(노이즈용)
function lp(cut) { let y = 0; return (x, c = cut) => { const a = 1 - Math.exp(-2 * Math.PI * c / SR); y += a * (x - y); return y; }; }

// ---------- 악기 ----------
function pad(at, dur, freqs, vol) {
  for (const f of freqs) {
    const det = 1 + (rnd() * 0.002);
    add(at, dur, (i, n) => {
      const t = i / SR, e = env(i, n, 0.25, 1.6);
      const vib = 1 + 0.003 * Math.sin(2 * Math.PI * 5 * t);
      let v = 0; for (let h = 1; h <= 5; h++) v += Math.sin(2 * Math.PI * f * det * vib * h * t + h) / Math.pow(h, 1.7);
      return v * e;
    }, vol, rnd() * 0.5);
  }
}
function bass(at, f, dur, vol) {
  add(at, dur, (i, n) => { const t = i / SR; const e = env(i, n, 0.01, 2.5);
    return (Math.sin(2 * Math.PI * f * t) + 0.35 * Math.sin(2 * Math.PI * 2 * f * t) + 0.12 * Math.sin(2 * Math.PI * 3 * f * t)) * e; }, vol);
}
function kick(at, vol) {
  add(at, 0.35, i => { const t = i / SR; const f = 45 + 110 * Math.exp(-t * 28); return Math.sin(2 * Math.PI * f * t) * exp(i, 11) * 1.4; }, vol);
}
function snare(at, vol) {
  const f = lp(3200);
  add(at, 0.22, i => { const t = i / SR; return (f(rnd()) * exp(i, 22) * 0.9 + Math.sin(2 * Math.PI * 190 * t) * exp(i, 40) * 0.6); }, vol);
}
function hat(at, vol, len = 0.05) {
  let p = 0; add(at, len, i => { const x = rnd(); const y = x - p; p = x; return y * exp(i, 90); }, vol, 0.25); // 하이패스 흉내(차분)
}
function pluck(at, f, vol, len = 0.35, pan = 0) {
  add(at, len, i => { const t = i / SR; return (Math.sin(2 * Math.PI * f * t) + 0.5 * Math.sin(2 * Math.PI * 2 * f * t) * exp(i, 18) + 0.2 * Math.sin(2 * Math.PI * 3 * f * t) * exp(i, 30)) * exp(i, 9); }, vol, pan);
}

// ---------- 효과음 ----------
function click(at) { // 키보드 타건
  const f = lp(2500 + rnd() * 1500);
  add(at, 0.03, i => f(rnd()) * exp(i, 220) * 2.2 + Math.sin(2 * Math.PI * (2200 + rnd() * 400) * i / SR) * exp(i, 400) * 0.6, 0.22);
}
function whoosh(at) {
  const f = lp(400);
  add(at - 0.2, 0.55, (i, n) => { const p = i / n; const c = 300 + 5000 * Math.sin(Math.PI * p) ** 2; return f(rnd(), c) * Math.sin(Math.PI * p) ** 1.5 * 2.2; }, 0.35);
}
function blip(at) { add(at, 0.09, i => Math.sin(2 * Math.PI * 920 * i / SR) * exp(i, 40) + 0.3 * Math.sin(2 * Math.PI * 1840 * i / SR) * exp(i, 60), 0.22); }
function buzz(at) { add(at, 0.3, i => (Math.sin(2 * Math.PI * 105 * i / SR) > 0 ? 1 : -1) * 0.5 * exp(i, 8) + Math.sin(2 * Math.PI * 52 * i / SR) * exp(i, 6) * 0.5, 0.25); }
function ding(at, base = 1318.5) { add(at, 0.7, i => (Math.sin(2 * Math.PI * base * i / SR) + 0.5 * Math.sin(2 * Math.PI * base * 1.5 * i / SR) + 0.25 * Math.sin(2 * Math.PI * base * 2 * i / SR)) * exp(i, 6), 0.2); }
function tick(at) { add(at, 0.25, i => (Math.sin(2 * Math.PI * 1760 * i / SR) + 0.4 * Math.sin(2 * Math.PI * 2637 * i / SR)) * exp(i, 16), 0.16); }
function pop(at) { add(at, 0.08, i => { const t = i / SR; return Math.sin(2 * Math.PI * (600 + 900 * Math.exp(-t * 60)) * t) * exp(i, 55); }, 0.18); }
function boom(at) {
  add(at, 1.4, i => { const t = i / SR; const f = 38 + 100 * Math.exp(-t * 9); return Math.sin(2 * Math.PI * f * t) * exp(i, 2.4) * 1.5; }, 0.55);
  const f = lp(1800); add(at, 0.6, i => f(rnd()) * exp(i, 9) * 1.6, 0.35);
}
function riser(at, dur) { // 문제 장면 끝, 긴장 상승
  const f = lp(200); let ph = 0;
  add(at, dur, (i, n) => { const p = i / n; ph += 2 * Math.PI * (90 + 700 * p * p) / SR; return (f(rnd(), 200 + 4000 * p) * 1.2 + Math.sin(ph) * 0.5) * p * p; }, 0.3);
}
function chime(at) { [880, 1108.7].forEach((f, k) => add(at + k * 0.12, 0.5, i => Math.sin(2 * Math.PI * f * i / SR) * exp(i, 7), 0.16)); }

// ---------- 곡 ----------
const BPM = 100, B = 60 / BPM;   // 한 박 0.6초
const chords = [ // 2마디(8박)씩 순환
  { p: [220, 261.63, 329.63, 392], b: 55 },     // Am7
  { p: [174.61, 220, 261.63, 329.63], b: 43.65 }, // Fmaj7
  { p: [130.81 * 2, 164.81 * 2, 196 * 2, 246.94 * 2], b: 65.41 }, // Cmaj7 (한 옥타브 위)
  { p: [196, 246.94, 293.66, 329.63], b: 49 },  // G6
];
const FULL = T.boomAt; // 8초부터 드럼 전체 진입
const END = T.duration - 1.6;
const nBeats = Math.floor(T.duration / B) + 1;
for (let k = 0; k < nBeats; k++) {
  const at = k * B; if (at > END) break;
  const bar = Math.floor(k / 4), beat = k % 4, ch = chords[Math.floor(bar / 2) % 4];
  const full = at >= FULL - 0.01;
  const vol = full ? 1 : 0.55;
  if (k % 8 === 0) pad(at, B * 8.3, ch.p, full ? 0.045 : 0.035);
  // 베이스: 1·3박 길게, '3-and' 에 짧게
  if (beat === 0 || beat === 2) bass(at, ch.b, B * 1.6, full ? 0.28 : 0.16);
  if (full && beat === 2) bass(at + B * 0.5, ch.b, B * 0.4, 0.18);
  if (full) {
    if (beat === 0 || beat === 2) kick(at, 0.9);
    if (beat === 3 && bar % 2 === 1) kick(at + B * 0.5, 0.6);
    if (beat === 1 || beat === 3) snare(at, 0.5);
    hat(at, 0.16); hat(at + B * 0.5, 0.1, 0.03);
    // 아르페지오(16분) — 살짝만
    for (let s = 0; s < 4; s++) { const idx = (k * 4 + s) % 7; const f = ch.p[[0, 1, 2, 3, 2, 1, 2][idx]] * 2; pluck(at + s * B / 4, f, 0.06, 0.3, s % 2 ? 0.4 : -0.4); }
  } else if (at >= T.scenes.problem[0]) {
    hat(at, 0.12); hat(at + B * 0.5, 0.07, 0.03); // 문제 장면: 초조한 하이햇만
  }
}
riser(T.boomAt - 1.6, 1.6);
boom(T.boomAt);

// ---------- 효과음 배치 ----------
for (const ty of T.typing) for (let i = 0; i < ty.text.length; i++) click(ty.at + i / ty.cps + rnd() * 0.004);
for (const w of T.whooshes) if (w > 0) whoosh(w);
for (const p of T.prompts) blip(p);
blip(T.changedAt);
buzz(T.errorAt);
for (const o of T.oks) ding(o);
for (const f of T.files) pop(f);
tick(T.replyAt);
for (const s of T.steps) tick(s);
chime(T.askAt);
for (const c of T.cards) pop(c);
ding(T.ctaAt, 1760);

// ---------- 마스터: 페이드·소프트클립·WAV ----------
const fadeIn = 0.3 * SR, fadeOut = 1.8 * SR;
const out = Buffer.alloc(N * 4);
let peak = 0;
for (let i = 0; i < N; i++) {
  let g = 1;
  if (i < fadeIn) g = i / fadeIn;
  if (i > N - fadeOut) g = Math.min(g, (N - i) / fadeOut);
  const l = Math.tanh(L[i] * 1.4 * g) * 0.82, r = Math.tanh(R[i] * 1.4 * g) * 0.82;
  peak = Math.max(peak, Math.abs(l), Math.abs(r));
  out.writeInt16LE(Math.round(l * 32767), i * 4);
  out.writeInt16LE(Math.round(r * 32767), i * 4 + 2);
}
const h = Buffer.alloc(44);
h.write('RIFF', 0); h.writeUInt32LE(36 + out.length, 4); h.write('WAVE', 8); h.write('fmt ', 12);
h.writeUInt32LE(16, 16); h.writeUInt16LE(1, 20); h.writeUInt16LE(2, 22); h.writeUInt32LE(SR, 24);
h.writeUInt32LE(SR * 4, 28); h.writeUInt16LE(4, 32); h.writeUInt16LE(16, 34); h.write('data', 36); h.writeUInt32LE(out.length, 40);
fs.writeFileSync('mix.wav', Buffer.concat([h, out]));
console.log('mix.wav', (T.duration).toFixed(1) + 's', 'peak', peak.toFixed(2));
