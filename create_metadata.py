from pathlib import Path
import wave, contextlib

dir = Path(r"C:\Users\elibl\podcasts-20250907T074357Z-1-001\podcasts")

file = dir.glob("*.wav")


for f in file:

    stat = f.stat()
    with contextlib.closing(wave.open(str(f), 'rb')):
        metadata = {
            "name": f.name,
            "path": str(f.resolve()),
            "size": stat.st_size,
            # "datetime": datetime. צריך תיקון
        }

