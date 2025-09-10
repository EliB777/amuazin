from app.config import THRESHOLD,MEDIUM_MIN,HIGH_MIN,MIN_HITS_MEDIUM, MIN_HITS_HIGH,HOSTILE,LESS_HOSTILE
from part_B.decode_base64 import decode_base64_list
from part_B.detector import Detector


# hostile = (
#     "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUs"
#     "TmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMs"
#     "QmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
# )
# less_hostile = (
#     "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZ"
#     "SBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
# )

hostile = decode_base64_list(HOSTILE)
less_hostile =decode_base64_list(LESS_HOSTILE)
detector = Detector(hostile,less_hostile)