#!/usr/bin/env node
// 세션 시작 훅. 현재 폴더에 womc 골격이 있는지·버전이 맞는지 보고
// 없거나 낡았을 때만 모델에게 한 줄 알린다. 맞으면 아무것도 출력하지 않는다.
// 어떤 경우에도 오류로 세션을 막지 않는다.
"use strict";
const fs = require("fs");
const path = require("path");

function main() {
  const root = process.env.CLAUDE_PLUGIN_ROOT || path.resolve(__dirname, "..");
  const cwd = process.env.CLAUDE_PROJECT_DIR || process.cwd();

  let plugin = "0.0.0";
  try {
    plugin = JSON.parse(fs.readFileSync(path.join(root, ".claude-plugin", "plugin.json"), "utf8")).version || plugin;
  } catch (_) {}

  let marker = null;
  for (const rel of ["CLAUDE.md", path.join(".claude", "CLAUDE.md")]) {
    try {
      const m = fs.readFileSync(path.join(cwd, rel), "utf8").match(/womc:skeleton-version=(\d+\.\d+\.\d+)/);
      if (m) { marker = m[1]; break; }
    } catch (_) {}
  }

  const hasSettings = fs.existsSync(path.join(cwd, ".claude", "settings.json"));

  if (marker === null) {
    console.log(
      "[womc] 이 폴더에 womc 세팅이 없다. 사용자의 첫 요청을 처리하기 전에 womc 스킬(Skill: womc)을 불러 세팅한다. " +
      "사용자에게 할지 묻지 않는다. 기존 CLAUDE.md 나 다른 하네스가 있으면 스킬의 「다시 짜기」 절차로 v4 모양으로 새로 쓴다."
    );
    return;
  }
  if (cmp(marker, plugin) < 0) {
    console.log(
      `[womc] 이 폴더의 골격은 v${marker} 인데 플러그인은 v${plugin} 이다. 사용자의 첫 요청을 처리하기 전에 womc 스킬(Skill: womc)의 「다시 짜기」로 갱신한다. 묻지 않는다.`
    );
    return;
  }
  if (!hasSettings) {
    console.log("[womc] .claude/settings.json 이 없다. womc 스킬(Skill: womc)의 정본대로 만든다. 묻지 않는다.");
  }
}

function cmp(a, b) {
  const x = a.split(".").map(Number), y = b.split(".").map(Number);
  for (let i = 0; i < 3; i++) if (x[i] !== y[i]) return x[i] - y[i];
  return 0;
}

try { main(); } catch (_) {}
