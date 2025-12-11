# extract.py
import json
import time
import requests
import random
from datetime import datetime, timedelta
from pathlib import Path

# Define Base Paths
BASE_DIR = Path(__file__).resolve().parents[0]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# API Endpoints (Fictional)
DELIVERY_API_URL = "https://api.swiftshipexpress.in/v1/deliveries/live"
TRAFFIC_API_URL = "https://api.swiftshipexpress.in/v1/traffic/routes"

# --- Mock Data Generators (To simulate API when offline) ---
def generate_mock_delivery_data():
    cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]
    data = []
    for i in range(5): # Simulate 5 shipments
        source = random.choice(cities)
        dest = random.choice([c for c in cities if c != source])
        dispatch = datetime.now() - timedelta(hours=random.randint(1, 48))
        
        data.append({
            "shipment_id": f"SWIFT-{random.randint(10000, 99999)}",
            "source_city": source,
            "destination_city": dest,
            "dispatch_time": dispatch.isoformat(),
            "expected_delivery_time": (dispatch + timedelta(hours=random.randint(5, 24))).isoformat(),
            "actual_delivery_time": None if random.random() > 0.5 else (dispatch + timedelta(hours=random.randint(5, 26))).isoformat(),
            "package_weight_kg": round(random.uniform(0.5, 20.0), 2),
            "delivery_agent_id": f"AGT-{random.randint(100, 999)}"
        })
    return data

def generate_mock_traffic_data():
    cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]
    data = []
    for city in cities:
        data.append({
            "city_name": city,
            "traffic_congestion_score": random.randint(1, 10),
            "average_speed_kmh": random.randint(10, 60),
            "weather_warnings": random.choice(["None", "Heavy Rain", "Fog", "Heatwave"])
        })
    return data

# --- Main Extraction Logic ---

def fetch_data_with_retry(url: str, retries: int = 3, delay: int = 2, mock_fallback: bool = True):
    """
    Fetch API data with retry logic. Falls back to mock data if URL fails.
    """
    for attempt in range(1, retries + 1):
        try:
            print(f"   Trying connection to {url} (Attempt {attempt})...")
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            if attempt < retries:
                time.sleep(delay)
            else:
                print(f"⚠️ Connection failed. Switching to MOCK MODE for demonstration.")
                if mock_fallback:
                    if "deliveries" in url:
                        return generate_mock_delivery_data()
                    elif "traffic" in url:
                        return generate_mock_traffic_data()
                return None

def extract_delivery_data():
    print(f"⏳ Requesting Live Delivery Data...")
    data = fetch_data_with_retry(DELIVERY_API_URL)
    
    if data:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = RAW_DIR / f"delivery_{timestamp}.json"
        filename.write_text(json.dumps(data, indent=2))
        print(f"✅ Extracted {len(data)} delivery records to: {filename}")
        return str(filename)

def extract_traffic_data():
    print(f"⏳ Requesting Route Traffic Data...")
    data = fetch_data_with_retry(TRAFFIC_API_URL)
    
    if data:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = RAW_DIR / f"traffic_{timestamp}.json"
        filename.write_text(json.dumps(data, indent=2))
        print(f"✅ Extracted {len(data)} traffic records to: {filename}")
        return str(filename)

if __name__ == "__main__":
    extract_delivery_data()
    print("-" * 30)
    extract_traffic_data()


#     # extract.py

# """

# Extract module for the SwiftShip Express ETL pipeline.
 
# Responsibilities:

# - Fetch raw JSON from two APIs:

#     1) Live Delivery API:   https://api.swiftshipexpress.in/v1/deliveries/live

#     2) Route Traffic API:   https://api.swiftshipexpress.in/v1/traffic/routes

# - Implement retry logic with exponential backoff (default 3 attempts).

# - Save raw API responses to `data/raw/` with timestamped filenames.

# - Return a dict of saved file paths for downstream steps.
 
# Usage:

#     from extract import fetch_all_raw

#     files = fetch_all_raw()

#     # files -> {"deliveries": "/path/to/...", "traffic": "/path/to/..."}
 
# Environment variables (optional):

# - DELIVERIES_API_URL (defaults to the example URL)

# - TRAFFIC_API_URL    (defaults to the example URL)

# - DELIVERIES_API_KEY (optional, if your API requires auth)

# - TRAFFIC_API_KEY    (optional)

# - RAW_DIR            (optional override for where to store raw files)

# - MAX_RETRIES        (optional, default 3)

# - TIMEOUT_SECONDS    (optional, default 10)

# """
 
# import json

# import os

# import time

# from datetime import datetime

# from pathlib import Path

# from typing import Any, Dict, Optional
 
# import requests

# from dotenv import load_dotenv
 
# load_dotenv()
 
# # --- Configuration (can be overridden via environment) ---

# DELIVERIES_API_URL = os.getenv(

#     "DELIVERIES_API_URL", "https://api.swiftshipexpress.in/v1/deliveries/live"

# )

# TRAFFIC_API_URL = os.getenv(

#     "TRAFFIC_API_URL", "https://api.swiftshipexpress.in/v1/traffic/routes"

# )
 
# DELIVERIES_API_KEY = os.getenv("DELIVERIES_API_KEY")  # optional

# TRAFFIC_API_KEY = os.getenv("TRAFFIC_API_KEY")  # optional
 
# RAW_DIR = Path(os.getenv("RAW_DIR", Path(__file__).resolve().parents[0] / "data" / "raw"))

# RAW_DIR.mkdir(parents=True, exist_ok=True)
 
# MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

# TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "10"))
 
# # --- Helper functions ---
 
 
# def _now_ts() -> str:

#     """Return compact timestamp for filenames (UTC)."""

#     return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
 
 
# def _save_raw(payload: Any, api_name: str, suffix: str = "json") -> str:

#     """

#     Save payload (JSON-serializable) to a timestamped file under RAW_DIR.

#     Returns absolute file path as string.

#     """

#     ts = _now_ts()

#     filename = f"{api_name}_raw_{ts}.{suffix}"

#     path = RAW_DIR / filename
 
#     # Ensure the payload is serializable; if it's already a Response object or bytes,

#     # attempt to get JSON/text first.

#     try:

#         if isinstance(payload, (dict, list)):

#             content = payload

#         else:

#             # fallback: attempt to convert to JSON-like structure

#             content = payload

#         with open(path, "w", encoding="utf-8") as f:

#             json.dump(content, f, ensure_ascii=False, indent=2, default=str)

#         return str(path.resolve())

#     except Exception as e:

#         # As a last resort, write string representation

#         alt_path = RAW_DIR / f"{api_name}_raw_{ts}.txt"

#         with open(alt_path, "w", encoding="utf-8") as f:

#             f.write(f"Failed to JSON-dump payload: {e}\n\nrepr(payload):\n{repr(payload)}")

#         return str(alt_path.resolve())
 
 
# def _make_headers(api_key: Optional[str]) -> Dict[str, str]:

#     headers = {"Accept": "application/json"}

#     if api_key:

#         # Common patterns: Authorization: Bearer <key> or X-API-Key

#         # Try Bearer by default, students can change if their API uses a different header.

#         headers["Authorization"] = f"Bearer {api_key}"

#     return headers
 
 
# def _fetch_with_retries(

#     url: str,

#     api_name: str,

#     api_key: Optional[str] = None,

#     params: Optional[Dict[str, Any]] = None,

#     max_retries: int = MAX_RETRIES,

#     timeout_seconds: int = TIMEOUT_SECONDS,

# ) -> Dict[str, Any]:

#     """

#     Fetch a JSON response from URL with retry + exponential backoff.

#     Returns the JSON payload on success.

#     Raises RuntimeError after exhausting retries.

#     """

#     headers = _make_headers(api_key)

#     attempt = 0

#     last_exc: Optional[Exception] = None
 
#     while attempt < max_retries:

#         attempt += 1

#         try:

#             resp = requests.get(url, headers=headers, params=params, timeout=timeout_seconds)

#             # Raise for non-2xx to allow retrying on server errors

#             resp.raise_for_status()

#             # Try to parse JSON; if not possible, store text under {"raw_text": "..."}

#             try:

#                 payload = resp.json()

#             except ValueError:

#                 payload = {"raw_text": resp.text}

#             # Save raw payload and return

#             saved = _save_raw(payload, api_name, suffix="json")

#             print(f"✅ [{api_name}] Fetched and saved raw response to: {saved}")

#             return {"payload": payload, "raw_path": saved}

#         except requests.RequestException as re:

#             last_exc = re

#             print(f"⚠️ [{api_name}] Request attempt {attempt}/{max_retries} failed: {re}")

#         except Exception as e:

#             last_exc = e

#             print(f"⚠️ [{api_name}] Unexpected error on attempt {attempt}: {e}")
 
#         # backoff before next attempt

#         backoff = 2 ** (attempt - 1)

#         print(f"⏳ [{api_name}] Retrying in {backoff} seconds...")

#         time.sleep(backoff)
 
#     # Exhausted retries

#     raise RuntimeError(f"[{api_name}] Failed to fetch {url} after {max_retries} attempts") from last_exc
 
 
# # --- Public extraction functions ---
 
 
# def fetch_deliveries_live() -> Dict[str, str]:

#     """

#     Fetch live deliveries data and save raw JSON.

#     Returns dict {"payload": <parsed JSON>, "raw_path": "<path>"} on success.

#     """

#     print(f"⏳ Fetching deliveries from {DELIVERIES_API_URL} ...")

#     return _fetch_with_retries(

#         DELIVERIES_API_URL, "deliveries", api_key=DELIVERIES_API_KEY, max_retries=MAX_RETRIES

#     )
 
 
# def fetch_traffic_routes() -> Dict[str, str]:

#     """

#     Fetch traffic route data and save raw JSON.

#     Returns dict {"payload": <parsed JSON>, "raw_path": "<path>"} on success.

#     """

#     print(f"⏳ Fetching traffic routes from {TRAFFIC_API_URL} ...")

#     return _fetch_with_retries(

#         TRAFFIC_API_URL, "traffic_routes", api_key=TRAFFIC_API_KEY, max_retries=MAX_RETRIES

#     )
 
 
# def fetch_all_raw() -> Dict[str, Dict[str, str]]:

#     """

#     Fetch both deliveries and traffic data (in sequence).

#     Returns a dict with keys 'deliveries' and 'traffic' mapping to the return values of each fetch.

#     e.g.

#     {

#         "deliveries": {"payload": ..., "raw_path": "/abs/path"},

#         "traffic": {"payload": ..., "raw_path": "/abs/path"}

#     }

#     """

#     results: Dict[str, Dict[str, str]] = {}
 
#     try:

#         results["deliveries"] = fetch_deliveries_live()

#     except Exception as e:

#         # Log but continue to attempt traffic fetch; caller can decide to abort pipeline.

#         print(f"❌ Failed to fetch deliveries: {e}")

#         results["deliveries"] = {"error": str(e)}
 
#     try:

#         results["traffic"] = fetch_traffic_routes()

#     except Exception as e:

#         print(f"❌ Failed to fetch traffic routes: {e}")

#         results["traffic"] = {"error": str(e)}
 
#     return results
 
 
# # --- CLI execution for manual testing ---

# if __name__ == "__main__":

#     print("Starting extraction (deliveries + traffic)...")

#     out = fetch_all_raw()

#     print("Extraction complete. Summary:")

#     for k, v in out.items():

#         if isinstance(v, dict) and "raw_path" in v:

#             print(f" - {k}: saved -> {v['raw_path']}")

#         else:

#             print(f" - {k}: error -> {v.get('error') if isinstance(v, dict) else repr(v)}")

 