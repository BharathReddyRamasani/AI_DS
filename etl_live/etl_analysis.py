# etl_analysis.py
from dotenv import load_dotenv
import os
import pandas as pd
from supabase import create_client
from pathlib import Path
import matplotlib.pyplot as plt

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

BASE_DIR = Path(__file__).resolve().parents[0]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

TABLE_NAME = "shipments"

if not SUPABASE_URL or not SUPABASE_KEY:
    raise SystemExit("Please set SUPABASE_URL and SUPABASE_KEY in your .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def _extract_data_from_response(res):
    """
    Standard helper to extract list-of-dicts from Supabase response.
    """
    data = getattr(res, "data", None)
    if isinstance(data, list):
        return data
    return []


def fetch_table(limit: int | None = None) -> pd.DataFrame:
    """
    Fetch 'shipments' table from Supabase.
    """
    print(f"🔍 Fetching data from Supabase table '{TABLE_NAME}' ...")
    query = supabase.table(TABLE_NAME).select("*")
    if limit:
        query = query.limit(limit)
    res = query.execute()

    data = _extract_data_from_response(res)
    df = pd.DataFrame(data)

    if df.empty:
        print("⚠️  No rows extracted. Check Supabase table.")
        return df

    # --- Data Cleaning & Type Conversion ---
    # Convert timestamps
    for col in ["dispatch_time", "expected_delivery_time", "actual_delivery_time", "created_at"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Convert numeric metrics
    numeric_cols = ["delay_minutes", "traffic_congestion_score", "package_weight_kg", "average_speed_kmh"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def analyze_and_save(df: pd.DataFrame):
    if df.empty:
        print("No data to analyze.")
        return

    print("ℹ️  Data info:")
    print(df.info())

    # --- 1. High-Level Logistics Summary ---
    total_shipments = len(df)
    # Filter for valid delay numbers
    valid_delays = df[df["delay_minutes"].notnull()]
    
    summary = {
        "total_shipments": total_shipments,
        "avg_delay_minutes": round(valid_delays["delay_minutes"].mean(), 2) if not valid_delays.empty else 0,
        "max_delay_minutes": round(valid_delays["delay_minutes"].max(), 2) if not valid_delays.empty else 0,
        "late_shipments_pct": round((len(valid_delays[valid_delays["delay_minutes"] > 0]) / total_shipments) * 100, 2),
        "avg_traffic_score": round(df["traffic_congestion_score"].mean(), 2) if "traffic_congestion_score" in df.columns else 0
    }

    print("🔎 Summary metrics:")
    for k, v in summary.items():
        print(f"  - {k}: {v}")

    # Save Summary
    summary_df = pd.DataFrame([summary])
    summary_csv = PROCESSED_DIR / "analysis_summary.csv"
    summary_df.to_csv(summary_csv, index=False)
    print(f"✅ Saved analysis summary to {summary_csv}")

    # --- 2. City Performance Analysis (Avg Delay per City) ---
    if {"destination_city", "delay_minutes"}.issubset(df.columns):
        city_stats = df.groupby("destination_city", as_index=False).agg({
            "delay_minutes": "mean",
            "traffic_congestion_score": "mean",
            "shipment_id": "count"
        }).rename(columns={"shipment_id": "shipment_count"})
        
        city_stats = city_stats.sort_values("delay_minutes", ascending=False)
        city_stats_csv = PROCESSED_DIR / "city_performance.csv"
        city_stats.to_csv(city_stats_csv, index=False)
        print(f"✅ Saved city performance stats to {city_stats_csv}")

    # --- 3. Visualizations ---
    try:
        # Plot A: Delay Distribution Histogram
        if "delay_minutes" in df.columns:
            plt.figure(figsize=(8, 5))
            df["delay_minutes"].dropna().plot(kind="hist", bins=15, color="#e74c3c", edgecolor="black")
            plt.title("Distribution of Shipment Delays")
            plt.xlabel("Delay (Minutes) - Negative means Early")
            plt.ylabel("Number of Shipments")
            plt.axvline(0, color='black', linestyle='dashed', linewidth=1)
            plt.tight_layout()
            
            hist_path = PROCESSED_DIR / "delay_distribution.png"
            plt.savefig(hist_path)
            plt.close()
            print(f"✅ Saved delay histogram to {hist_path}")

        # Plot B: Average Delay by City (Bar Chart)
        if {"destination_city", "delay_minutes"}.issubset(df.columns):
            plt.figure(figsize=(10, 6))
            # Sort for better visualization
            city_group = df.groupby("destination_city")["delay_minutes"].mean().sort_values()
            city_group.plot(kind="bar", color="#3498db")
            plt.title("Average Delay by Destination City")
            plt.xlabel("City")
            plt.ylabel("Avg Delay (Minutes)")
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            
            bar_path = PROCESSED_DIR / "city_delay_chart.png"
            plt.savefig(bar_path)
            plt.close()
            print(f"✅ Saved city delay chart to {bar_path}")

        # Plot C: Traffic Score vs. Delay (Scatter Plot)
        if {"traffic_congestion_score", "delay_minutes"}.issubset(df.columns):
            plt.figure(figsize=(8, 5))
            plt.scatter(
                df["traffic_congestion_score"], 
                df["delay_minutes"], 
                alpha=0.6, 
                c=df["traffic_congestion_score"], 
                cmap='viridis'
            )
            plt.colorbar(label="Traffic Score")
            plt.title("Impact of Traffic Congestion on Delay")
            plt.xlabel("Traffic Congestion Score (1-10)")
            plt.ylabel("Delay (Minutes)")
            plt.tight_layout()
            
            scatter_path = PROCESSED_DIR / "traffic_impact.png"
            plt.savefig(scatter_path)
            plt.close()
            print(f"✅ Saved traffic impact plot to {scatter_path}")

    except Exception as e:
        print(f"⚠️  Plotting failed: {e}")


def run_analysis(limit: int | None = None):
    df = fetch_table(limit=limit)
    analyze_and_save(df)


if __name__ == "__main__":
    # Fetch all data for analysis
    run_analysis()