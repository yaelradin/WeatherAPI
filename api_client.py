import requests


def get_weather_data(lat: float, lon: float, start_date: str, end_date: str):
    # הכתובת של ה-API
    url = "https://api.open-meteo.com/v1/forecast"

    # הפרמטרים שאנחנו רוצים לשלוח
    params = {
        "latitude": lat,#רוחב
        "longitude": lon,
        "start_date": start_date,  # תאריך התחלה בפורמט YYYY-MM-DD
        "end_date": end_date,  # תאריך סיום בפורמט YYYY-MM-DD
        "hourly": "temperature_2m",  # אנחנו מבקשים טמפרטורה שעתית
        "format": "json"  # מבקשים שהתשובה תהיה בפורמט JSON
    }

    try:
        # שליחת בקשת ה-GET
        response = requests.get(url, params=params, timeout=10)

        # בדיקה אם הכל עבר בשלום (קוד 200)
        response.raise_for_status()
        import json

        print(json.dumps(response.json(), indent=4))
        # הפיכת התשובה לפורמט שפייתון מבין (מילון)
        return response.json()


    except requests.exceptions.RequestException as e:
        print(f"שגיאה בתקשורת עם ה-API: {e}")
        return None


if __name__ == "__main__":
    get_weather_data(32.08, 34.78)
