from pathlib import Path

p = Path("generated_project/test_os.txt")
p.parent.mkdir(exist_ok=True)

with open(p, "w", encoding="utf-8") as f:
    f.write("hello os")

print("WRITE OK:", p.resolve())