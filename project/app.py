# project/app.py
import os
from pathlib import Path
import pandas as pd
from flask import Flask, request, jsonify
import joblib

# -----------------------------
# Paths (robust & simple)
# -----------------------------
# Base dir = repo root (parent of project/)
BASE_DIR = Path(__file__).resolve().parent.parent  

FEAT_PATH = BASE_DIR / "project" / "data" / "processed" / "IYR_features_project.csv"
MODEL_PATH = Path(os.getenv("MODEL_PATH", BASE_DIR / "project" / "model" / "rf_time_pipeline_stage10b.joblib"))
# -----------------------------
# Load data & model (fail fast)
# -----------------------------
if not FEAT_PATH.exists():
    raise FileNotFoundError(f"Features file not found at {FEAT_PATH}")
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

df = pd.read_csv(FEAT_PATH)
model = joblib.load(str(MODEL_PATH))

# Determine feature columns expected by the model.
# Prefer model.feature_names_in_ when available (scikit-learn >=1.0); otherwise, infer by dropping common non-feature columns.
if hasattr(model, "feature_names_in_"):
    FEATURE_COLS = list(model.feature_names_in_)
else:
    NON_FEATURE = {"Date", "date", "y", "y_actual", "y_pred", "target",
                   "Close", "Adj Close", "Open", "High", "Low", "Volume"}
    FEATURE_COLS = [c for c in df.columns if c not in NON_FEATURE]

# Keep only columns that actually exist in df (in case the model was trained on a subset)
FEATURE_COLS = [c for c in FEATURE_COLS if c in df.columns]

app = Flask(__name__)

# -----------------------------
# Helpers
# -----------------------------
def _ensure_frame(payload: dict | None) -> pd.DataFrame:
    """
    Accepts JSON payload in either of these shapes:
      1) {"features": {"ma_7": ..., "vol_21": ..., ...}}
      2) {"row": {"ma_7": ..., "vol_21": ..., ...}}
      3) If payload is None or empty, fall back to the *last* row of df.
    Returns a 1-row DataFrame with FEATURE_COLS.
    """
    if payload and isinstance(payload, dict):
        row = payload.get("features") or payload.get("row")
        if isinstance(row, dict):
            X = pd.DataFrame([row])
        else:
            # user passed something else; ignore and use last row
            X = df.tail(1).copy()
    else:
        X = df.tail(1).copy()

    # Restrict to feature columns; if a column is missing in payload, fill with NaN (your pipeline can impute)
    for col in FEATURE_COLS:
        if col not in X.columns:
            X[col] = pd.NA

    # Order columns for the model
    X = X[FEATURE_COLS]
    return X

# -----------------------------
# Routes
# -----------------------------
@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_path": str(MODEL_PATH),
        "features_path": str(FEAT_PATH),
        "n_rows_available": int(len(df)),
        "n_feature_cols": len(FEATURE_COLS),
        "feature_sample": FEATURE_COLS[:10],
    })

@app.post("/predict")
def predict():
    """
    POST JSON examples:

    - Use latest row:
        {}

    - Provide a full/partial feature dict:
        {
          "features": {
            "ma_7": 0.12, "ma_21": 0.10, "vol_21": 0.008, ...
          }
        }
    """
    payload = request.get_json(silent=True)
    X = _ensure_frame(payload)

    try:
        y_pred = model.predict(X)[0]
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {repr(e)}"}), 400

    return jsonify({
        "prediction": float(y_pred),
        "used_features": FEATURE_COLS,
        "n_features": len(FEATURE_COLS),
    })

@app.get("/predict_last")
def predict_last():
    X = df.tail(1)[FEATURE_COLS]
    try:
        y_pred = model.predict(X)[0]
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {repr(e)}"}), 400

    return jsonify({
        "prediction": float(y_pred),
        "row_index": int(df.index[-1]),
        "n_features": len(FEATURE_COLS),
    })

# -----------------------------
# Entrypoint
# -----------------------------
if __name__ == "__main__":
    # Helpful startup prints
    print("BASE_DIR  :", BASE_DIR)
    print("FEAT_PATH :", FEAT_PATH, "exists?", FEAT_PATH.exists())
    print("MODEL_PATH:", MODEL_PATH, "exists?", MODEL_PATH.exists())
    print("n_rows    :", len(df))
    print("n_features:", len(FEATURE_COLS))
    app.run(host="127.0.0.1", port=5000, debug=True)
