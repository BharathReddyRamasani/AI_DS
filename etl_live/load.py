# load.py
import os
import math
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client
from time import sleep

# Load Environment Variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[0]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise SystemExit("Please set SUPABASE_URL and SUPABASE_KEY in your .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

TABLE_NAME = "shipments"

# SQL to create the table matching SwiftShip Express data
CREATE_TABLE_SQL = f"""
CREATE TABLE IF NOT EXISTS public.{TABLE_NAME} (
    id BIGSERIAL PRIMARY KEY,
    shipment_id TEXT,
    source_city TEXT,
    destination_city TEXT,
    dispatch_time TIMESTAMP,
    expected_delivery_time TIMESTAMP,
    actual_delivery_time TIMESTAMP,
    package_weight_kg DOUBLE PRECISION,
    delivery_agent_id TEXT,
    traffic_congestion_score INTEGER,
    average_speed_kmh DOUBLE PRECISION,
    weather_warnings TEXT,
    delay_minutes DOUBLE PRECISION,
    traffic_risk TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
"""

def create_table_if_not_exists():
    """
    Try to create table via SQL RPC if available. If RPC not available,
    print SQL so user can run it in Supabase SQL UI.
    """
    try:
        print("🔧 Attempting to create table in Supabase (if permitted)...")
        # Note: 'execute_sql' RPC function must exist in your Supabase instance for this to work directly.
        # Otherwise, you must run the SQL manually in the Dashboard.
        supabase.rpc("execute_sql", {"query": CREATE_TABLE_SQL}).execute()
        print("✅ create_table_if_not_exists: RPC executed.")
    except Exception as e:
        print(f"⚠️  Could not create table via RPC: {e}")
        print("ℹ️  Please run the following SQL in your Supabase SQL editor if table doesn't exist:")
        print(CREATE_TABLE_SQL)

def _read_processed_csv(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    # Convert timestamps to string for Supabase insert (ISO 8601)
    time_cols = ['dispatch_time', 'expected_delivery_time', 'actual_delivery_time']
    for col in time_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").astype(str)
            # Handle "NaT" strings resulting from null dates
            df[col] = df[col].replace('NaT', None)

    return df

def load_to_supabase(csv_path: str, batch_size: int = 100):
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Processed CSV not found at {csv_path}")

    df = _read_processed_csv(csv_path)
    total = len(df)
    print(f"📦 Loading {total} rows into Supabase table '{TABLE_NAME}' in batches of {batch_size} ...")

    # convert NaN to None for JSON serialization (Postgres handles None as NULL)
    df = df.where(pd.notnull(df), None)
    records = df.to_dict(orient="records")

    for i in range(0, total, batch_size):
        batch = records[i:i + batch_size]
        try:
            # Insert data
            res = supabase.table(TABLE_NAME).insert(batch).execute()
            
            # Check for errors in response (handling different supabase-py versions)
            if hasattr(res, "error") and res.error:
                print(f"⚠️  Batch {i//batch_size + 1} error: {res.error}")
            else:
                end = min(i + batch_size, total)
                print(f"✅ Inserted rows {i+1}-{end} of {total}")
                
        except Exception as e:
            print(f"⚠️  Exception while inserting batch {i//batch_size + 1}: {e}")
            # Exponential backoff retry
            print("Retrying after 3s ...")
            sleep(3)
            try:
                supabase.table(TABLE_NAME).insert(batch).execute()
                print("✅ Retry success")
            except Exception as e2:
                print(f"❌ Retry failed: {e2}")
                continue

    print("🎯 Load complete.")

if __name__ == "__main__":
    # Find the latest enriched CSV file
    processed_files = sorted([str(p) for p in PROCESSED_DIR.glob("enriched_data_*.csv")])
    
    if not processed_files:
        raise SystemExit("No processed CSV found. Run transform.py first.")
    
    latest_file = processed_files[-1]
    
    create_table_if_not_exists()
    load_to_supabase(latest_file, batch_size=50)