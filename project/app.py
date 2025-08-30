import os
from pathlib import Path
import json
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import joblib

# --- Paths ---
from pathlib import Path
import os

# Base directory = the folder where app.py lives
BASE_DIR = Path(__file__).resolve().parent

# Paths to data and model (robust, no double "project/")
FEAT_PATH = BASE_DIR / "data" / "processed" / "IYR_features_project.csv"
MODEL_PATH = Path(os.getenv("MODEL_PATH", BASE_DIR / "model" / "rf_time_pipeline_stage10b.joblib"))

# Safety check
if not FEAT_PATH.exists():
    raise FileNotFoundError(f"Features file not found at {FEAT_PATH}")
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

app = Flask(__name__)

# --- Load model once ---
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
model = joblib.load(MODEL_PATH)

# Infer feature columns from the training/features file
if not FEAT_PATH.exists():
    raise FileNotFoundError(f"Features file not found at {FEAT_PATH}")
df_train = pd.read_csv(FEAT_PATH)
# columns used in Stage 10b (all except Date and the target we created there)
feature_cols = [c for c in df_train.columns if c not in ["Date", "target_close_t1"]]

def _coerce_dataframe(d):
    """Coerce incoming dict to a single-row DataFrame with correct column order."""
    x = pd.DataFrame([d])
    # add any missing columns with NaN
    for col in feature_cols:
        if col not in x.columns:
            x[col] = np.nan
    # restrict to known features in correct order
    x = x[feature_cols]
    # simple impute NaNs with previous day mean if available (fallback: 0)
    x = x.fillna(x.mean(numeric_only=True)).fillna(0)
    return x

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": True,
        "n_features": len(feature_cols)
    })

@app.post("/predict")
def predict():
    """
    JSON body: { "features": { "<col1>": value, "<col2>": value, ... } }
    Returns: { "prediction": float, "n_features": int }
    """
    data = request.get_json(silent=True) or {}
    feats = data.get("features", {})
    if not isinstance(feats, dict) or len(feats) == 0:
        return jsonify({"error": "Provide JSON like {\"features\": {\"col\": val, ...}}"}), 400
    x = _coerce_dataframe(feats)
    y_hat = float(model.predict(x)[0])
    return jsonify({"prediction": y_hat, "n_features": len(feature_cols)})

@app.get("/predict_from_latest")
def predict_from_latest():
    """
    Convenience endpoint: take the last row of IYR_features_project.csv and predict next-day Close.
    """
    df = pd.read_csv(FEAT_PATH).sort_values("Date")
    x = df.iloc[[-1]][feature_cols]  # last row, only feature columns
    x = x.fillna(x.mean(numeric_only=True)).fillna(0)
    y_hat = float(model.predict(x)[0])
    return jsonify({
        "date_used": str(df["Date"].iloc[-1]) if "Date" in df.columns else None,
        "prediction": y_hat,
        "n_features": len(feature_cols)
    })

if __name__ == "__main__":
    # For local dev only. Use a production server (gunicorn) to deploy.
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
