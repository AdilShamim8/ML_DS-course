from pathlib import Path

folder = Path("docs")
file = "manual.txt"
full_path = folder / file  # Safe, cross-platform

print(full_path)  # docs/manual.txt (Mac/Linux) OR docs\manual.txt (Windows)