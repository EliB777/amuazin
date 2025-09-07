from pathlib import Path
import wave, contextlib, json, time
from datetime import datetime

dir = Path(r"C:\Users\elibl\podcasts-20250907T074357Z-1-001\podcasts")
file = dir.glob("*.wav")
text = []

for f in file:
    stat = f.stat()
    with contextlib.closing(wave.open(str(f), 'rb')):
        metadata = {
            "name": f.name,
            "path": str(f.resolve()),
            "size": stat.st_size,
            "datetime": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            # "datetime": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(stat.st_mtime))
        }

    msg = json.dumps(metadata, ensure_ascii=False)
    text.append(msg)
    print(msg)

