import argparse
from api_client import get_weather_data
from cache_manager import generate_cache_key, get_cached_data, save_to_cache
from exporter import export_data
from processor import process_weather_data


# from processor import process_weather_data


def main():
    # 1. הגדרת ה-Parser שמטפל בארגומנטים מהטרמינל
    parser = argparse.ArgumentParser(description="Weather Data Pipeline Tool")

    # 2. הוספת הארגומנטים שהמשימה דורשת
    parser.add_argument("--lat", type=float, required=True, help="Latitude of the location")
    parser.add_argument("--lon", type=float, required=True, help="Longitude of the location")
    parser.add_argument("--start", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--format", choices=["json", "csv"], default="json", help="Output format")

    # 3. קריאת הארגומנטים שהמשתמש הזין
    args = parser.parse_args()

    print(f"Fetching run_results for: Lat {args.lat}, Lon {args.lon} from {args.start} to {args.end}...")

    # יצירת מפתח
    cache_key = generate_cache_key(args.lat, args.lon, args.start, args.end)
    cached_res = get_cached_data(cache_key)

    # הוצאת נתונים מזיכרון המטמון או מגישה לשרת
    if cached_res:
        print("Using cached run_results...")
        raw_data = cached_res
    else:
        print("Fetching from API...")
        raw_data = get_weather_data(args.lat, args.lon, args.start, args.end)
        if raw_data:
            save_to_cache(cache_key, raw_data)

    # הפעלת חישובים על הנתונים ושמירה בתקית ריצה
    if raw_data:
        processed_data_row = process_weather_data(raw_data)
        print("Successfully processed run_results!")

        export_data(processed_data_row,format_type=args.format,filename=cache_key)
        print("Successfully exported run_results!")

    else:

        print("Failed to fetch run_results.")


if __name__ == "__main__":
    main()