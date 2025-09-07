from pathlib import Path

dir = Path(r"C:\Users\elibl\podcasts-20250907T074357Z-1-001\podcasts")

file = sorted(dir.glob(".wav"))
for f in file:
    pass