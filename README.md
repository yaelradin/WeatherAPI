# Weather Data Pipeline CLI Tool



## Overview

A modular Python-based command-line tool designed to fetch weather data from the Open-Meteo API. The tool processes raw hourly data, applies local caching to optimize performance, and exports structured results to JSON or CSV formats.



## Features

* **Data Retrieval:** Fetches weather data using the Open-Meteo public API (no authentication required).

* **Data Processing:** Normalizes API responses and calculates daily metrics such as average, maximum, and minimum temperatures.

* **Local Caching:** Implements a file-based cache (JSON/SQLite) to prevent redundant API calls for identical parameters.

* **Robust CLI:** Supports arguments for location (lat/lon), date ranges, and output formats.

* **Error Handling:** Explicitly handles API failures, network timeouts, and invalid inputs to prevent silent failures.



## Project Structure

The project is organized into separate modules to ensure single responsibility:

* `main.py`: The entry point for the CLI tool.

* `api_client.py`: Handles HTTP integration and request construction.

* `processor.py`: Manages data normalization, type coercion, and aggregation logic.

* `cache_manager.py`: Controls local persistence and cache key strategy.

* `exporter.py`: Handles structured file writing (JSON/CSV).

* `tests/`: Unit tests covering validation, transformations, and caching.



## Installation & Setup

1. **Prerequisites:** Python 3.10 or higher.

2. **Install Dependencies:**

   ```bash

   pip install -r requirements.txt
   
## Usage Examples

### 1. Export weather data to JSON
Run the following command to fetch weather for a specific location and date range:
```bash
   python main.py --lat 32.08 --lon 34.78 --start 2026-05-01 --end 2026-05-04 --format json
```

### 2. Export weather data to CSV
Run the following command to fetch weather for a specific location and date range:
```bash
   python main.py --lat 32.08 --lon 34.78 --start 2026-05-01 --end 2026-05-04 --format csv
```


# Implementation Notes

## Assumptions
- **Daily Aggregation:** I assumed that for the purpose of a weather pipeline, users are most interested in daily summaries (min/max/avg) rather than raw hourly data.
- **Cache Key:** I assumed that latitude and longitude should be rounded to a reasonable precision to ensure the cache is effective while remaining accurate.
- **Date Format:** I assumed all input dates follow the ISO 8601 format (YYYY-MM-DD) as per standard API integrations.

## Potential Improvements (with more time)
- **Database Caching:** Replace the current file-based JSON cache with an SQLite database for better performance and scalability.
- **Retry Logic:** Implement a retry mechanism with exponential backoff for the HTTP client to handle temporary network fluctuations.
- **Logging:** Add a structured logging system (using Python's `logging` module) instead of simple print statements for better production monitoring.
- **Expanded Variables:** Add support for more weather variables like wind speed, humidity, or UV index.

## Known Limitations
- **API Rate Limiting:** The tool does not currently monitor or handle Open-Meteo's rate limits (though they are generous for public use).
- **Single-Threaded:** The data processing is currently synchronous; for very large date ranges, asynchronous requests (using `httpx` or `aiohttp`) would be more efficient.
- **CLI Validation:** While basic validation is implemented, more complex geo-coordinate validation (ensuring points are within specific global bounds) could be added.