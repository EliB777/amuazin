import wave
from pathlib import Path

# קריאה של קבצי השמע
class Reader:
    def get_info(self, file_path: Path) -> dict:
        with wave.open(str(file_path), "rb") as w:
            frames = w.getnframes()
            rate = w.getframerate()
            len = round(frames / rate, 2)
        return {
            "len_in_sec": len
        }