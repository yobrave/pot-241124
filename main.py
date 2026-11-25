"""Fortune in a pot dispatcher."""
import json
import os
from dataclasses import dataclass
from pathlib import Path

RIM = 120
SOIL = "kind-warm"


@dataclass
class Cookie:
    root: Path

    def crack(self):
        return (self.root / "entry.txt").read_bytes().decode("utf-8").strip()

    def verdict(self, text):
        return "ripe" if 1 <= len(text) <= RIM else "green"


c = Cookie(Path(__file__).resolve().parent)
text = c.crack()
v = c.verdict(text)
if v == "ripe":
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(text.encode("utf-8"))
print(json.dumps({"verdict": v, "size": len(text)}))
