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

def count_tokens(text: str) -> int:
    text = (text or "").strip()
    return len(text.split()) if text else 0

# count for detect lists
def detect_counts(text: str) -> tuple[int, int]:
    result = detector.detect((text or "").lower())
    hostile_map = result.get("hostile", {})
    less_map    = result.get("less_hostile", {})
    count_hostile = sum(int(v) for v in hostile_map.values())
    count_less_hostile   = sum(int(v) for v in less_map.values())
    return count_hostile, count_less_hostile

# sum for all worrds
def sum_of_detected(count_hostile: int, count_less_hostile: int) -> int:
    return (2 * count_hostile) + count_less_hostile

# חישוב באחוזים לפי כמות המילים שנמצאו חלקי המילים של הטקסט
def percent(weighted: int, total_tokens: int) -> float:
    total = max(total_tokens, 1)
    return round(100.0 * (weighted / total), 2)

# מחשב אם זה מופלל לפי אחוזים או מינימום של סך מילים
def decide_level(bds_percent: float, weighted: int) -> tuple[bool, str]:
    is_bds = (bds_percent >= THRESHOLD) or (weighted >= MIN_HITS_MEDIUM)
    if (bds_percent >= HIGH_MIN) or (weighted >= MIN_HITS_HIGH):
        level = "high"
    elif (bds_percent >= MEDIUM_MIN) or (weighted >= MIN_HITS_MEDIUM):
        level = "medium"
    else:
        level = "none"
    return bool(is_bds), level

# העשרה אחרי סיווג
def enrich(msg: dict, transcript_field: str = "transcript") -> dict:

    text = msg.get(transcript_field) or ""
    count_hostile, count_less_hostile = detect_counts(text)
    weighted = sum_of_detected(count_hostile, count_less_hostile)
    pct = percent(weighted, count_tokens(text))
    is_bds, level = decide_level(pct, weighted)

    out = dict(msg)
    out["bds_percent"] = pct
    out["is_bds"] = is_bds
    out["bds_threat_level"] = level
    # בדיקה
    # out["bds_score_weighted"] = int(weighted)
    # out["bds_hits_strong"] = int(strong_hits)
    # out["bds_hits_weak"] = int(weak_hits)

    return out