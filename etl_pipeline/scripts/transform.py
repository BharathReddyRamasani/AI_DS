import os
import pandas as pd
import numpy as np 

def transform_data(raw_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    staged_dir = os.path.join(base_dir, "data", "staged")
    os.makedirs(staged_dir, exist_ok=True)

    df = pd.read_csv(raw_path)

    # Convert TotalCharges to numeric (spaces -> NaN)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing numeric with median
    numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values
    categorical_cols = df.select_dtypes(include="object").columns
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")

    # tenure_group
    df["tenure_group"] = pd.cut(
        df["tenure"], bins=[-1, 12, 36, 60, np.inf],
        labels=["New", "Regular", "Loyal", "Champion"]
    )

    # monthly_charge_segment
    df["monthly_charge_segment"] = pd.cut(
        df["MonthlyCharges"], bins=[-1, 30, 70, np.inf],
        labels=["Low", "Medium", "High"]
    )

    # has_internet_service
    df["has_internet_service"] = df["InternetService"].replace({
        "No": 0,
        "DSL": 1,
        "Fiber optic": 1
    })

    # is_multi_line_user
    df["is_multi_line_user"] = np.where(df["MultipleLines"] == "Yes", 1, 0)

    # contract_type_code
    df["contract_type_code"] = df["Contract"].map({
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    })

    # Drop unused
    df.drop(["customerID", "gender"], axis=1, inplace=True)

    # Save final cleaned dataset
    cleaned_path = os.path.join(staged_dir, "telco_churn_cleaned_transform.csv")
    df.to_csv(cleaned_path, index=False)

    print(f"✨ Clean transformation complete!")
    print(f"📁 Saved at: {cleaned_path}")
    return cleaned_path


if __name__ == "__main__":
    from extract import extract_data
    raw_path = extract_data()
    transform_data(raw_path)