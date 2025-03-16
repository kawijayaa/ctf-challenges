import os
from pathlib import Path

paths = sorted(Path("../src/caches/").iterdir(), key=os.path.getmtime)

for file in paths:
    with open(file, "rb") as f:
        print(f.read()[20:21].decode("utf-8"), end="")
