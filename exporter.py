import json
import csv
import os
from typing import Dict, Any

RESULTS_DIR = "run_results"


def ensure_directory_exists():
    """יוצר את תיקיית התוצאות אם היא לא קיימת"""
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)


def save_as_json(data: Dict[str, Any], filename: str):
    """שומר את הנתונים המעובדים לקובץ JSON"""
    path = os.path.join(RESULTS_DIR, f"{filename}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Results saved to {path}")


def save_as_csv(data: Dict[str, Any], filename: str):
    """הופך את הנתונים המעובדים לטבלת CSV ושומר אותה"""
    path = os.path.join(RESULTS_DIR, f"{filename}.csv")

    # אנחנו רוצים לשמור את הפירוט היומי (הטבלה)
    daily_data = data.get("daily_breakdown", [])

    if not daily_data:
        print("No daily data to save as CSV")
        return

    # הוצאת שמות הטורים מהמפתחות של המילון הראשון
    headers = daily_data[0].keys()

    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(daily_data)

    print(f"Results saved to {path}")


def export_data(data: Dict[str, Any], format_type: str, filename: str = "weather_report"):
    """פונקציה ראשית שבוחרת את שיטת השמירה לפי הפורמט המבוקש"""
    ensure_directory_exists()

    if format_type.lower() == "csv":
        save_as_csv(data, filename)
    else:
        save_as_json(data, filename)