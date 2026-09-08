// scene.html 을 Chrome 으로 열어 프레임마다 PNG 로 찍는다.
// 사용: node render.js            → frames/ 에 전체 프레임
//       node render.js 1.5 9 20   → preview/ 에 해당 초의 프레임만(미리보기)
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const T = require('./timeline');

(async () => {
  const preview = process.argv.slice(2).map(Number);
  const wide = !!process.env.WIDE;
  const outDir = preview.length ? 'preview' : (wide ? 'frames-wide' : 'frames');
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir);
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    headless: true,
    args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  await page.setViewport(wide ? { width: 1920, height: 1080 } : { width: 1080, height: 1920 });
  await page.goto('file://' + path.resolve('scene.html') + (wide ? '?wide' : ''));
  await page.evaluate(() => document.fonts.ready);
  const times = preview.length ? preview : Array.from({ length: Math.round(T.duration * T.fps) }, (_, i) => i / T.fps);
  let i = 0;
  for (const t of times) {
    await page.evaluate(t => window.render(t), t);
    const name = preview.length ? `t${t.toFixed(2)}.png` : `f${String(i).padStart(5, '0')}.png`;
    await page.screenshot({ path: path.join(outDir, name), type: 'png' });
    i++;
    if (i % 100 === 0) console.log(`${i}/${times.length}`);
  }
  await browser.close();
  console.log('done', times.length, 'frames →', outDir);
})();
