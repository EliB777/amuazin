from pathlib import Path
import time ,wave

# create metadata
class buildMeta:
    def build(self, file_path: Path) -> dict:
        p = Path(file_path)
        stat = p.stat()

        # מחשב את זמן ההקלטה
        with wave.open(str(p), "rb") as w:
            frames = w.getnframes()
            rate = w.getframerate()
            len_in_sec = round(frames / rate, 2)

        return {
            "id": str(int(time.time() * 1000)),
            "path": str(p),
            "name": p.name,
            "size": stat.st_size,
            "date": stat.st_mtime,
            "len_in_sec": len_in_sec

        }
    print("build")
