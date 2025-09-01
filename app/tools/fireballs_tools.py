from typing import List, Optional, Dict
from statistics import mean, median

from app.models.fireball_model import FireballRecord

def normalize_coordinates(records: List[FireballRecord]) -> List[FireballRecord]:
    normalized = []
    for r in records:
        lat = r.lat
        lon = r.lon
        lat_dir = getattr(r, "lat_dir", None)
        lon_dir = getattr(r, "lon_dir", None)

        if lat is not None and lon is not None:
            if lat_dir == "S":
                lat = -lat
            if lon_dir == "W":
                lon = -lon
            if lon > 180:
                lon -= 360

        # On recrée un FireballRecord normalisé
        normalized.append(FireballRecord(
            **{**r.model_dump(), "lat": lat, "lon": lon}
        ))
    return normalized

def compute_stats(values: List[Optional[float]]) -> Dict[str, Optional[float]]:
    clean_values = [v for v in values if v is not None]
    if not clean_values:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "average": None,
            "median": None
        }
    return {
        "count": len(clean_values),
        "min": min(clean_values),
        "max": max(clean_values),
        "average": mean(clean_values),
        "median": median(clean_values)
    }

def get_continent(lat: Optional[float], lon: Optional[float]) -> str:
    if lat is None or lon is None:
        return "Unknown"
    # Antarctica
    if lat < -60:
        return "Antarctica"
    # America (Nord + Sud)
    if -60 <= lat <= 85 and -170 <= lon <= -30:
        return "America"
    if -60 <= lat <= 15 and -30 <= lon <= -20:
        return "America"
    # Europe
    if 35 <= lat <= 72 and -25 <= lon <= 60:
        return "Europe"
    # Africa
    if -35 <= lat <= 37 and -20 <= lon <= 55:
        return "Africa"
    # Asia
    if -10 <= lat <= 80 and 55 <= lon <= 180:
        return "Asia"
    # Oceania
    if -50 <= lat <= 0 and 110 <= lon <= 180:
        return "Oceania"
    return "Other"
