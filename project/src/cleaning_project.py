import os
import pandas as pd

def load_prices(path):
    df = pd.read_csv(path)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.sort_values("Date")
    return df

def preprocess_prices(df):
    price_col = "Adj Close" if "Adj Close" in df.columns else ("Close" if "Close" in df.columns else None)
    if price_col is None:
        raise ValueError("No price column found (expected 'Adj Close' or 'Close').")
    df[price_col] = pd.to_numeric(df[price_col], errors="coerce")
    df["daily_return"] = df[price_col].pct_change()
    return df

def save_processed(df, filename):
    base = os.getenv("DATA_DIR", "project/data")
    out = os.path.join(base, "processed", filename)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    df.to_csv(out, index=False)
    return out
