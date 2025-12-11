# transform.py
import json
import pandas as pd
from pathlib import Path
import os
from datetime import datetime

# Define Paths
BASE_DIR = Path(__file__).resolve().parents[0]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def get_latest_file(prefix):
    """
    Helper to find the most recent file in raw directory starting with a prefix.
    """
    files = list(RAW_DIR.glob(f"{prefix}_*.json"))
    if not files:
        return None
    # Sort by creation time (or filename timestamp) and pick the last one
    return max(files, key=os.path.getctime)

def transform_data():
    print("🔄 Starting Data Transformation...")

    # 1. Load the latest Raw Data
    delivery_file = get_latest_file("delivery")
    traffic_file = get_latest_file("traffic")

    if not delivery_file or not traffic_file:
        print("❌ Error: Missing raw data files. Run extract.py first.")
        return

    print(f"   Loading {delivery_file.name}...")
    with open(delivery_file, 'r') as f:
        delivery_data = json.load(f)

    print(f"   Loading {traffic_file.name}...")
    with open(traffic_file, 'r') as f:
        traffic_data = json.load(f)

    # 2. Convert to Pandas DataFrames
    df_delivery = pd.DataFrame(delivery_data)
    df_traffic = pd.DataFrame(traffic_data)

    # 3. Data Cleaning & Type Conversion
    # Convert timestamp strings to datetime objects
    df_delivery['dispatch_time'] = pd.to_datetime(df_delivery['dispatch_time'])
    df_delivery['expected_delivery_time'] = pd.to_datetime(df_delivery['expected_delivery_time'])
    df_delivery['actual_delivery_time'] = pd.to_datetime(df_delivery['actual_delivery_time'])

    # 4. Merge Data (Enrichment)
    # We join Delivery Data with Traffic Data on 'destination_city' -> 'city_name'
    print("   Merging Delivery and Traffic data...")
    merged_df = pd.merge(
        df_delivery, 
        df_traffic, 
        left_on='destination_city', 
        right_on='city_name', 
        how='left' # Keep all deliveries even if traffic data is missing
    )

    # Drop the redundant 'city_name' column after merge
    merged_df.drop(columns=['city_name'], inplace=True)

    # 5. Feature Engineering (Calculations)
    
    # A. Calculate Delay in Minutes (Actual - Expected)
    # If actual is null (package not arrived), delay is NaN
    merged_df['delay_minutes'] = (merged_df['actual_delivery_time'] - merged_df['expected_delivery_time']).dt.total_seconds() / 60
    
    # B. Label Traffic Risk
    # Logic: Score 1-3 (Low), 4-7 (Medium), 8-10 (High)
    def classify_risk(score):
        if pd.isna(score): return "Unknown"
        if score >= 8: return "High"
        if score >= 4: return "Medium"
        return "Low"

    merged_df['traffic_risk'] = merged_df['traffic_congestion_score'].apply(classify_risk)

    # 6. Save Processed Data
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = PROCESSED_DIR / f"enriched_data_{timestamp}.csv"
    
    merged_df.to_csv(output_file, index=False)
    print(f"✅ Transformation Complete! Data saved to:")
    print(f"   {output_file}")
    
    # Preview the data
    print("\n--- Data Preview (Top 3 Rows) ---")
    print(merged_df[['shipment_id', 'destination_city', 'traffic_congestion_score', 'delay_minutes', 'traffic_risk']].head(3))

if __name__ == "__main__":
    transform_data()