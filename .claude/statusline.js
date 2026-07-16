#!/usr/bin/env node
// Claude Code statusline (jq-free, Node-based)
// Format: <model> │ <used>k/<ctx>k │ S:<5h>% W:<week>%

let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  let d = {};
  try {
    d = JSON.parse(raw);
  } catch (e) {
    // If JSON can't be parsed, dump for inspection and exit quietly.
    try {
      require("fs").writeFileSync(
        require("os").homedir() + "/.claude/statusline-debug.json",
        raw
      );
    } catch (_) {}
    process.stdout.write("statusline: invalid input");
    return;
  }

  const model =
    (d.model && (d.model.display_name || d.model.id)) || "Unknown";

  // Current root folder name (basename of the working directory)
  const dir =
    (d.workspace && (d.workspace.current_dir || d.workspace.project_dir)) ||
    d.cwd ||
    "";
  const folder = dir
    ? dir.replace(/[\\/]+$/, "").split(/[\\/]/).pop()
    : "";

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

  // If rate_limits is entirely absent, dump JSON so keys can be inspected.
  if (five === null && week === null && !d.rate_limits) {
    try {
      require("fs").writeFileSync(
        require("os").homedir() + "/.claude/statusline-debug.json",
        raw
      );
    } catch (_) {}
  }

  // green < 50, yellow < 80, red >= 80
  const colorPct = (label, val) => {
    if (val === null) return `${label}:--`;
    const code = val < 50 ? 32 : val < 80 ? 33 : 31;
    return `\x1b[${code}m${label}:${val}%\x1b[0m`;
  };

  let line = `${model} │ ${usedK}k/${ctxK}k │ ${colorPct("S", five)} ${colorPct("W", week)}`;
  if (folder) line += ` │ \x1b[36m${folder}\x1b[0m`;
  process.stdout.write(line);
});
