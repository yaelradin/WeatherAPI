import pytest
from api_client import get_weather_data
from processor import process_weather_data


# בדיקה לפונקציית העיבוד (Processor)
def test_process_weather_data_calculation():
    # יצירת נתונים "מזוייפים" שמדמים תשובת API
    fake_api_response = {
        "latitude": 32.0,
        "longitude": 34.0,
        "hourly": {
            "time": ["2026-05-01T00:00", "2026-05-01T01:00"],
            "temperature_2m": [20.0, 30.0]
        }
    }

    result = process_weather_data(fake_api_response)

    # בדיקה שהממוצע חושב נכון (20 ו-30 ממוצעם 25)
    assert result["overall_statistics"]["period_average"] == 25.0[cite: 1]
    assert result["metadata"]["latitude"] == 32.0[cite: 1]


# בדיקה ל-API Client עם שימוש ב-Mock
def test_api_client_with_mock(requests_mock):
    lat, lon = 32.0, 34.0
    start, end = "2026-05-01", "2026-05-02"
    url = "https://api.open-meteo.com/v1/forecast"

    # הגדרת ה-Mock: כשהקוד ינסה לפנות לכתובת הזו, הוא יקבל את ה-JSON שנבחר כאן
    requests_mock.get(url, json={"test": "success"})[cite: 1]

    response = get_weather_data(lat, lon, start, end)

    assert response == {"test": "success"}[cite: 1]