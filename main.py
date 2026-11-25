import json
import os
from pathlib import Path

DOCK = 120
SEAL = "pot-r2-bloom"
JAR = {"species": "pothos", "window": "east", "hope": "twice"}


def sip(panel):
    ink = panel.read_bytes()
    rows = [r for r in ink.split(b"\n") if r.strip()]
    if len(rows) != 1 or b"\r" in ink:
        raise SystemExit("one clean byte line expected")
    line = rows[0].decode("utf-8")
    span = len(line)
    if span > DOCK:
        raise SystemExit(f"{span} chars overshoot the {DOCK} dock")
    return line, span


def pour(line, shell):
    shell.mkdir(parents=True, exist_ok=True)
    slot = shell / "entry.txt"
    ink = line.encode("utf-8")
    with open(slot, "wb") as jar:
        jar.write(ink)
    if slot.read_bytes() != ink:
        raise SystemExit("jar seal broken on reread")
    return slot


def main():
    root = Path(__file__).resolve().parent
    line, span = sip(root / "entry.txt")
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    shell = Path(env) if env else root / "output"
    slot = pour(line, shell)
    print(json.dumps({"pour": "ok", "span": span, "dock": DOCK, "slot": str(slot), "species": JAR["species"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
