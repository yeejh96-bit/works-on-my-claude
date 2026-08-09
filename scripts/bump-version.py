"""버전을 한 번에 올린다.

실행:  py scripts/bump-version.py 2.0.0        (Windows)
       python3 scripts/bump-version.py 2.0.0   (Mac/Linux)

버전 숫자가 박혀 있는 자리가 여러 곳이라 손으로 고치면 반드시 하나를 빠뜨린다.
(빠뜨리면 check-sync.py 가 DRIFT 로 잡지만, 애초에 빠뜨리지 않는 게 낫다.)

고치는 곳:
1) .claude-plugin/plugin.json 의 "version"
2) README.md 첫 줄 제목 끝의 vX.Y.Z
3) womc:skeleton-version=X.Y.Z 표식 전부 (commands/womc.md · CLAUDE.md)
   — 개수를 세지 않고 정규식으로 전부 바꾼다.

바꾼 뒤에는 반드시 check-sync.py 를 돌린다(이 스크립트가 마지막에 안내한다).
--dry-run 을 주면 무엇을 바꿀지 보여주기만 하고 파일은 건드리지 않는다.
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent


# 줄바꿈을 그대로 두고 읽고 쓴다 (이 저장소는 LF 인데 plugin.json 만 CRLF 라, 섞이면 diff 가 통째로 뜬다)
def read(path: Path) -> str:
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def save(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


# 버전 표식(womc:skeleton-version=x.y.z)이 들어 있는 파일들 — check-sync.py 와 같은 목록
VERSION_MARKER_FILES = [
    "commands/womc.md",
    "CLAUDE.md",
]

args = [a for a in sys.argv[1:] if a != "--dry-run"]
dry_run = "--dry-run" in sys.argv

if len(args) != 1 or not re.fullmatch(r"\d+\.\d+\.\d+", args[0]):
    print("사용법: py scripts/bump-version.py <새버전>   예) py scripts/bump-version.py 2.0.0")
    sys.exit(2)

new = args[0]

plugin_path = ROOT / ".claude-plugin/plugin.json"
old = json.loads(read(plugin_path))["version"]

if tuple(int(x) for x in new.split(".")) <= tuple(int(x) for x in old.split(".")):
    print(f"[!] 새 버전({new}) 이 현재 버전({old}) 보다 높지 않다. 내리는 건 손으로 한다.")
    sys.exit(2)

print(f"{old}  ->  {new}{'   (--dry-run: 파일 안 고침)' if dry_run else ''}\n")
changed = 0


def apply(path: Path, text: str, label: str, count: int):
    global changed
    changed += count
    print(f"  {count}곳  {label}")
    if not dry_run:
        save(path, text)


# 1) plugin.json — 다른 필드 순서·서식을 건드리지 않도록 텍스트로 치환한다
text = read(plugin_path)
new_text, n = re.subn(r'("version"\s*:\s*)"[^"]+"', rf'\g<1>"{new}"', text, count=1)
if n:
    apply(plugin_path, new_text, ".claude-plugin/plugin.json 의 version", n)
else:
    print("  [!] plugin.json 에서 version 을 못 찾음")

# 2) README.md 첫 줄 제목
readme_path = ROOT / "README.md"
text = read(readme_path)
head, sep, rest = text.partition("\n")
new_head, n = re.subn(r"v\d+\.\d+\.\d+", f"v{new}", head, count=1)
if n:
    apply(readme_path, new_head + sep + rest, "README.md 제목 버전", n)
else:
    print("  [!] README.md 첫 줄에서 vX.Y.Z 를 못 찾음")

# 3) 골격 버전 표식 전부
for rel in VERSION_MARKER_FILES:
    path = ROOT / rel
    text = read(path)
    new_text, n = re.subn(
        r"(womc:skeleton-version=)\d+\.\d+\.\d+", rf"\g<1>{new}", text
    )
    if n:
        apply(path, new_text, f"{rel} 의 womc:skeleton-version 표식", n)
    else:
        print(f"  [!] {rel} 에 womc:skeleton-version 표식이 없음")

print(f"\n{'바꿀' if dry_run else '바꾼'} 자리 {changed}곳.")
print("다음: PYTHONIOENCODING=utf-8 py scripts/check-sync.py  로 전 항목 OK 인지 확인한다.")
