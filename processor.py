from typing import Dict, List, Any


def process_weather_data(api_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    מעבד נתוני מזג אוויר גולמיים ומחזיר סיכום סטטיסטי יומי.
    כולל Type Hints כפי שנדרש במשימה.
    """
    hourly_data = api_response.get("hourly", {})
    times = hourly_data.get("time", [])
    temps = hourly_data.get("temperature_2m", [])

    if not times or not temps:
        return {"error": "Missing run_results fields in API response"}

    # מילון עזר לאיסוף טמפרטורות לפי תאריך
    daily_groups: Dict[str, List[float]] = {}

    for i in range(len(times)):
        # הוצאת התאריך בלבד (ללא השעה) מתוך המחרוזת "2026-05-03T00:00"
        date = times[i].split("T")[0]
        temp = temps[i]

        if date not in daily_groups:
            daily_groups[date] = []
        daily_groups[date].append(temp)

    # יצירת הסיכום היומי המעובד
    daily_summaries = []
    for date, daily_temps in daily_groups.items():
        daily_summaries.append({
            "date": date,
            "avg_temp": round(sum(daily_temps) / len(daily_temps), 2),
            "max_temp": max(daily_temps),
            "min_temp": min(daily_temps)
        })

    # חישוב סטטיסטיקה כללית לכל התקופה
    total_avg = sum(temps) / len(temps)

    return {
        "metadata": {
            "latitude": api_response.get("latitude"),
            "longitude": api_response.get("longitude"),
            "unit": "Celsius"
        },
        "overall_statistics": {
            "period_average": round(total_avg, 2),
            "period_max": max(temps),
            "period_min": min(temps)
        },
        "daily_breakdown": daily_summaries
    }