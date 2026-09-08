// frames/ + mix.wav → ../womc-promo.mp4   (전체 순서: node render.js && node audio.js && node build.js)
const { execFileSync } = require('child_process');
const ff = require('ffmpeg-static');
const T = require('./timeline');
const wide = !!process.env.WIDE;   // WIDE=1 node build.js → 가로형
execFileSync(ff, ['-y', '-hide_banner', '-loglevel', 'error',
  '-framerate', String(T.fps), '-i', (wide ? 'frames-wide' : 'frames') + '/f%05d.png', '-i', 'mix.wav',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', String(T.fps),
  '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', wide ? '../womc-promo-가로형.mp4' : '../womc-promo.mp4'], { stdio: 'inherit' });
console.log('→', wide ? '../womc-promo-가로형.mp4' : '../womc-promo.mp4');
