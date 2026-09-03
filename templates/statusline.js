#!/usr/bin/env node
// Claude Code statusline (jq-free, Node-based)
// Format: 1줄째 <model> │ <used>k/<ctx>k │ S:<5h>% W:<week>% │ <folder> / 2줄째 <session-id>
//
// 이 스크립트의 첫 번째 약속: 무슨 일이 있어도 0으로 끝나고, 반드시 한 줄은 찍는다.
// Claude Code 는 상태줄 명령이 실패하거나(0이 아닌 종료) 아무것도 안 찍으면
// 직전 값을 남기지 않고 상태줄을 통째로 지운다. 게다가 다음 사건(새 답변·모델 변경 등)이
// 올 때까지 다시 실행하지 않으므로, 한 번 삐끗하면 상태줄이 한참 빈칸으로 남는다.
// 그래서 예외·빈 입력·stdin 지연을 전부 삼키고 대체 문구라도 출력한다.
// (settings.json 의 refreshInterval 이 두 번째 안전장치다 — 몇 초마다 스스로 되살아난다.)

const FALLBACK = "…";
let done = false;

function emit(line) {
  if (done) return;
  done = true;
  try {
    process.stdout.write(line && line.trim() ? line : FALLBACK);
  } catch (e) {
    /* 여기서 더 할 수 있는 일은 없다 */
  }
}

// 어떤 예외도 상태줄을 지우지 못하게 한다.
process.exitCode = 0;
process.on("uncaughtException", () => emit(FALLBACK));
process.on("unhandledRejection", () => emit(FALLBACK));

// stdin 이 끝나지 않아도 3초 뒤에는 무언가를 찍고 빠져나온다.
const guard = setTimeout(() => {
  emit(FALLBACK);
  try {
    process.stdin.pause();
    process.stdin.destroy();
  } catch (e) {}
}, 3000);

let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("error", () => emit(FALLBACK));
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  clearTimeout(guard);

  // 입력이 깨져도 멈추지 않는다 — 빈 객체로 두고 아래에서 기본값으로 채운다.
  let d = {};
  try {
    d = JSON.parse(raw) || {};
  } catch (e) {
    d = {};
  }

  const model =
    (d.model && (d.model.display_name || d.model.id)) || "Unknown";

  // Current root folder name (basename of the working directory)
  const dir =
    (d.workspace && (d.workspace.current_dir || d.workspace.project_dir)) ||
    d.cwd ||
    "";
  const folder = dir
    ? dir.replace(/[\/]+$/, "").split(/[\/]/).pop()
    : "";

  // Session id (useful for `claude --resume <id>`)
  const sid = d.session_id || "";

  const cw = d.context_window || {};
  const usedK = Math.round((cw.total_input_tokens || 0) / 1000);
  const ctxK = Math.round((cw.context_window_size || 0) / 1000);

  const rl = d.rate_limits || {};
  const five =
    rl.five_hour && rl.five_hour.used_percentage != null
      ? Math.round(rl.five_hour.used_percentage)
      : null;
  const week =
    rl.seven_day && rl.seven_day.used_percentage != null
      ? Math.round(rl.seven_day.used_percentage)
      : null;

  // green < 50, yellow < 80, red >= 80
  const colorPct = (label, val) => {
    if (val === null) return `${label}:--`;
    const code = val < 50 ? 32 : val < 80 ? 33 : 31;
    return `\x1b[${code}m${label}:${val}%\x1b[0m`;
  };

  let line = `${model} │ ${usedK}k/${ctxK}k │ ${colorPct("S", five)} ${colorPct("W", week)}`;
  if (folder) line += ` │ \x1b[36m${folder}\x1b[0m`;
  // Session id on its own second row
  if (sid) line += `\n\x1b[90m${sid}\x1b[0m`;
  emit(line);
});
