import json
import os
import hashlib

CACHE_FILE = "cache_res/weather_cache.json"


def generate_cache_key(lat: float, lon: float, start_date: str, end_date: str) -> str:
    """יוצר מפתח ייחודי המבוסס על פרמטרי הבקשה"""
    key_string = f"{lat}_{lon}_{start_date}_{end_date}"
    # אנחנו משתמשים ב-hash כדי להפוך את המפתח למחרוזת נקייה וקצרה
    return hashlib.md5(key_string.encode()).hexdigest()


def get_cached_data(cache_key: str) -> dict | None:
    """בודק אם קיים מידע ב-Cache ומחזיר אותו"""
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, 'r') as f:
        try:
            cache = json.load(f)
            return cache.get(cache_key)
        except json.JSONDecodeError:
            return None


def save_to_cache(cache_key: str, data: dict):
    """שומר מידע חדש לתוך קובץ ה-Cache"""
    cache = {}

    # אם הקובץ כבר קיים, נטען את המידע הקיים כדי לא לדרוס אותו
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            try:
                cache = json.load(f)
            except json.JSONDecodeError:
                cache = {}

    # הוספת המידע החדש ושמירה
    cache[cache_key] = data
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=4)