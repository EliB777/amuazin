import wave
from pathlib import Path

# קריאה של הקבצים פלוס נתיב
class Reader:
    def get_path(self, folder: Path):
        with wave.open(str(folder), "rb"):
            folder = Path(folder)
            return folder.glob("*.wav")
