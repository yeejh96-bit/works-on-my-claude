# womc 홍보 숏폼 소스

`../womc-promo.mp4` (1080×1920, 30fps, 약 32초) 를 만드는 코드다. 실제 녹화가 아니라 HTML 로 터미널 화면을 재현해 프레임을 찍고, 음악·효과음은 코드로 합성한다.

- `timeline.js` 장면 구간·타이핑·효과음 시각. 화면과 소리가 같이 읽는다.
- `scene.html` 장면 디자인. 브라우저로 열면 그냥 재생돼 미리 볼 수 있다.
- `render.js` Chrome 으로 프레임을 찍는다. `node render.js 5 12` 처럼 초를 주면 그 프레임만 `preview/` 에 찍는다.
- `audio.js` 배경음악·효과음 → `mix.wav`
- `build.js` 프레임 + 소리 → mp4

다시 만들기:
```
npm install
node render.js && node audio.js && node build.js
```

가로형(`../womc-promo-가로형.mp4`, 1920×1080)은 같은 장면을 두 칸(왼쪽 자막·오른쪽 터미널)으로 다시 놓은 것이다. `scene.html` 의 `body.wide` CSS 가 배치를 바꾼다. 브라우저에서 `scene.html?wide` 로 열면 미리 볼 수 있다.
```
WIDE=1 node render.js && WIDE=1 node build.js
```
(소리는 세로형과 같은 `mix.wav` 를 쓴다.)
