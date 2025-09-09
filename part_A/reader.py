# import wave
from pathlib import Path
from typing import Iterator
# # קריאה של הקבצים פלוס נתיב
# class Reader:
#     def get_path(self, folder: Path) -> Path:
#         with wave.open(str(folder), "rb"):
#             folder = Path(folder)
#             return folder.glob("*.wav")


class Reader:
    def get_path(self, folder: Path) -> Iterator[Path]:
        folder = Path(folder)
        return folder.glob("*.wav")