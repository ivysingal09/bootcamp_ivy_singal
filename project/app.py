# project/app.py
from pathlib import Path
import os
import pandas as pd
from flask import Flask, request, jsonify
import joblib

# -----------------------------
# Paths (simple & robust)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent  # .../bootcamp_ivy_singal/project
MODEL_PATH = Path(os.getenv("MODEL_PATH", BASE_DIR / "model" / "rf_time_pipeline_stage10b.joblib"))

# Optional: if present, we can use it for "predict_last", but NOT required to run
FEAT_PATH = Path(os.getenv("FEAT_PATH", BASE_DIR / "data" / "processed" / "IYR_features_project.csv"))

# -----------------------------
# Load model (required)
# -----------------------------
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
model = joblib.load(str(MODEL_PATH))

# Determine feature columns expected by the model (if available)
FEATURE_COLS = None
if hasattr(model, "feature_names_in_"):
    FEATURE_COLS = list(model.feature_names_in_)

# -----------------------------
# App
# -----------------------------
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_path": str(MODEL_PATH),
        "features_expected": FEATURE_COLS if FEATURE_COLS is not None else "infer from payload",
        "features_csv_available": FEAT_PATH.exists(),
    })

def _payload_to_frame(payload: dict) -> pd.DataFrame:
    """
    Accepts JSON payload:
        {"features": {"ma_7": ..., "vol_21": ..., ...}}
      or just a flat dict of features.

    Returns a 1-row DataFrame aligned to FEATURE_COLS if known,
    else uses all provided keys as columns.
    """
    if payload is None:
        payload = {}
    # allow {"features": {...}} or flat dict
    feats = payload.get("features", payload if isinstance(payload, dict) else {})

    if not isinstance(feats, dict) or len(feats) == 0:
        raise ValueError('Provide JSON like {"features": {"col": value, ...}}.')

    X = pd.DataFrame([feats])

    # If model knows its feature names, align to that order and fill missing with 0
    if FEATURE_COLS is not None:
        for col in FEATURE_COLS:
            if col not in X.columns:
                X[col] = 0
        X = X[FEATURE_COLS]
    else:
        # otherwise, use whatever numeric columns were provided
        X = X.select_dtypes(include="number")
        if X.shape[1] == 0:
            raise ValueError("No numeric feature columns found in payload.")

    # Basic fill for any remaining missing
    X = X.fillna(0)
    return X

@app.post("/predict")
def predict():
    try:
        payload = request.get_json(silent=True)
        X = _payload_to_frame(payload)
        y_hat = float(model.predict(X)[0])
        return jsonify({"prediction": y_hat, "n_features_used": X.shape[1]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Helpful startup prints
    print("BASE_DIR :", BASE_DIR)
    print("MODEL    :", MODEL_PATH, "exists?", MODEL_PATH.exists())
    print("FEAT_CSV :", FEAT_PATH, "exists?", FEAT_PATH.exists())
    print("FEATURES :", FEATURE_COLS if FEATURE_COLS is not None else "infer from payload")
    app.run(host="127.0.0.1", port=5000, debug=True)
