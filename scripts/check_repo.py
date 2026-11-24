import json
import pathlib
import re
import sys
root = pathlib.Path(__file__).resolve().parents[1]
errors = []
for p in root.rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue
    if p.suffix == ".json":
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p}: {e}")
    if p.suffix == ".md":
        for target in re.findall(r"\]\(([^\s)]+)\)", p.read_text(encoding="utf-8")):
            if ":" in target or target.startswith("#"):
                continue
            target = target.split("#")[0]
            if target and not (p.parent / target).exists():
                errors.append(f"{p.relative_to(root)}: missing {target}")
print("\n".join(errors) if errors else "JSON and simple relative Markdown links OK")
sys.exit(bool(errors))
