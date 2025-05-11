from pathlib import Path
lang = "" # "" for all
num = 4

for file in sorted(Path(f"pal/outputs{num}/").glob(f"*{lang}.txt")):
    with file.open("r", encoding="utf-8") as f:
        acc = f.readlines()[-1].strip()
        print(f"{file.name[:-(4+len(lang)+(lang!=""))]} Run {num}: {acc}")