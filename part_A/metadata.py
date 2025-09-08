from pathlib import Path
import time

# create metadata
class buildMeta:
    def build(self, file_path: Path, wav_info: dict) -> dict:
        p = Path(file_path)
        stat = p.stat()
        return {
            "id": str(int(time.time() * 1000)),
            "path": str(p),
            "name": p.name,
            "size": stat.st_size,
            "date": stat.st_mtime,
            "len_in_sec": wav_info["len_in_sec"]

        }