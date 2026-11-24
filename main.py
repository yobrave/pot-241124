"""Fortune in a pot: probe the fortune line, emit it to the gate output."""
import json
import os
import pathlib

SEED = "entry.txt"
POT_CAP = 120


def probe(text: str) -> dict:
    slim = " ".join(text.split())
    seen = {
        "slim_len": len(slim),
        "seed_bytes": len(text.encode("utf-8")),
        "pot_fits": len(slim) <= POT_CAP,
        "germinates": slim != "",
        "no_wind": text.strip().count("\n") == 0 and len(text.encode("utf-8")) < POT_CAP + 2,
    }
    seen["planted"] = seen["pot_fits"] and seen["germinates"] and seen["no_wind"]
    return seen


def emit() -> int:
    home = pathlib.Path(__file__).resolve().parent
    raw = (home / SEED).read_text(encoding="utf-8")
    seen = probe(raw)
    bed = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or home / "bed")
    bed.mkdir(parents=True, exist_ok=True)
    (bed / SEED).write_bytes(raw.encode("utf-8"))
    print(json.dumps({"seed": "houseplant-fortune", "probe": seen, "bed": str(bed)}))
    return 0 if seen["planted"] else 1


if __name__ == "__main__":
    raise SystemExit(emit())
