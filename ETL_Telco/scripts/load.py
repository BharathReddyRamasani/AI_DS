import os
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv


# ------------------------------------------------------
# 1️⃣ Initialize Supabase Client
# ------------------------------------------------------
def get_supabase_client():
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("❌ Missing SUPABASE_URL or SUPABASE_KEY in .env")

    print(f"🔗 Connecting to Supabase → {url}")
    return create_client(url, key)


# ------------------------------------------------------
# 2️⃣ Create telco_churn Table If Not Exists
# ------------------------------------------------------
def create_table_if_not_exists():
    supabase = get_supabase_client()

    sql = """
    CREATE TABLE IF NOT EXISTS public.telco_churn (
        id BIGSERIAL PRIMARY KEY,

        SeniorCitizen INTEGER,
        Partner TEXT,
        Dependents TEXT,
        tenure INTEGER,
        PhoneService TEXT,
        MultipleLines TEXT,
        InternetService TEXT,
        OnlineSecurity TEXT,
        OnlineBackup TEXT,
        DeviceProtection TEXT,
        TechSupport TEXT,
        StreamingTV TEXT,
        StreamingMovies TEXT,
        Contract TEXT,
        PaperlessBilling TEXT,
        PaymentMethod TEXT,
        MonthlyCharges DOUBLE PRECISION,
        TotalCharges DOUBLE PRECISION,
        Churn TEXT,

        tenure_group TEXT,
        monthly_charge_segment TEXT,
        is_multi_line_user INTEGER,
        contract_type_code INTEGER
    );
    """

    try:
        supabase.rpc("execute_sql", {"query": sql}).execute()
        print("✅ Table 'telco_churn' created or already exists.")
    except Exception as e:
        print(f"⚠️ Could not create table automatically: {e}")
        print("➡ Please ensure 'execute_sql' RPC exists in Supabase.")


# ------------------------------------------------------
# 3️⃣ Load Data Into Supabase
# ------------------------------------------------------
def load_to_supabase(csv_path, table_name="telco_churn"):

    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), csv_path))

    if not os.path.exists(csv_path):
        print(f"❌ CSV file not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    df = df.where(pd.notnull(df), None)

    supabase = get_supabase_client()

    batch_size = 100
    total_rows = len(df)

    print(f"📊 Preparing to insert {total_rows} rows into '{table_name}'...\n")

    for start in range(0, total_rows, batch_size):
        end = min(start + batch_size, total_rows)
        batch = df.iloc[start:end].to_dict(orient="records")

        try:
            response = supabase.table(table_name).insert(batch).execute()

            if hasattr(response, "error") and response.error:
                print(f"❌ Error inserting batch {start//batch_size + 1}: {response.error}")
            else:
                print(f"✅ Inserted rows {start+1} to {end}")
        except Exception as e:
            print(f"❌ Error inserting batch {start//batch_size + 1}: {e}")

    print("\n🎯 Finished loading all rows into Supabase.\n")


# ------------------------------------------------------
# 4️⃣ Script Runner
# ------------------------------------------------------
if __name__ == "__main__":
    staged_path = "../data/staged/telco_Customer_transformed.csv"

    create_table_if_not_exists()
    load_to_supabase(staged_path)

