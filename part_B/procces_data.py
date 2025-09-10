# from pathlib import Path
#
# class SimpleEnrich:
#
#     def _init_(self):
#         self.short_sec = 10
#         self.long_sec  = 60
#
#     def add(self, data: dict) -> dict:
#         d = dict(data)
#
#
#         dur = float(d.get("duration_sec", 0.0))
#         if dur < self.short_sec:
#             d["duration_bucket"] = "short"
#         elif dur <= self.long_sec:
#             d["duration_bucket"] = "medium"
#         else:
#             d["duration_bucket"] = "long"
#
#
#         p = Path(d.get("file_path", ""))
#         d["parent_dir"] = p.parent.name if p.parent.name else ""
#
#         return d