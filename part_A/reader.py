import wave
from pathlib import Path

# קריאה של קבצי השמע
class WavReader:
    def get_info(self, file_path: Path) -> dict:
        with wave.open(str(file_path), "rb") as w:
            frames = w.getnframes()
            rate = w.getframerate()
            duration = round(frames / rate, 2)
        return {
            "duration_sec": duration
        }