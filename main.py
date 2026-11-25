# Fortune in a Pot: houseplant fortune one-liner, exporter round 4.
import json
import pathlib
import sys

MAXIMUM = 120
FILE_IN = "entry.txt"
COOKIE_JAR = "out"
ID = "pot4-plant-fortune-r4"

src = pathlib.Path(FILE_IN)
text = src.read_text(encoding="utf-8").strip()
if not (1 <= len(text) <= MAXIMUM):
    sys.exit("gate: %d chars not within 1..%d" % (len(text), MAXIMUM))
out = pathlib.Path(COOKIE_JAR)
out.mkdir(exist_ok=True)
(out / FILE_IN).write_bytes((text + "\n").encode("utf-8"))
print(json.dumps({"code": ID, "chars": len(text), "state": "done", "maximum": MAXIMUM}))
