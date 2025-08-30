import os
from pathlib import Path
from flask import Flask, request, jsonify
import pandas as pd
import joblib

BASE_DIR   = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "rf_time_pipeline_stage10b.joblib"
FEAT_CSV   = BASE_DIR / "data" / "processed" / "IYR_features_project.csv"

def _exists(p: Path) -> bool:
    try:
        return p.exists()
    except Exception:
        return False

if not _exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
if not _exists(FEAT_CSV):
    raise FileNotFoundError(f"Features CSV not found at {FEAT_CSV}")
model = joblib.load(MODEL_PATH)
sample = pd.read_csv(FEAT_CSV, nrows=50)
EXCLUDE = {"Date", "y", "y_next", "y_actual", "target", "label"}
FEATURE_COLS = [c for c in sample.columns if c not in EXCLUDE]

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_path": str(MODEL_PATH),
        "feat_csv": str(FEAT_CSV),
        "model_exists": _exists(MODEL_PATH),
        "feat_csv_exists": _exists(FEAT_CSV),
        "feature_cols": FEATURE_COLS,
    })

@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts either:
      - {"features": {...}} a single dict
      - {"features": [{...}, {...}]} a list of dicts
    If payload omitted, uses the last row from FEAT_CSV.
    """
    payload = request.get_json(silent=True) or {}
    feats = payload.get("features")

    if feats is None:
        # fallback: use last row from CSV
        df_all = pd.read_csv(FEAT_CSV)
        X = df_all[FEATURE_COLS].tail(1)
        used = "last_row_from_csv"
    else:
        if isinstance(feats, dict):
            feats = [feats]
        df = pd.DataFrame(feats)
        # ensure all expected columns present
        for c in FEATURE_COLS:
            if c not in df.columns:
                df[c] = None
        X = df[FEATURE_COLS]
        used = "request_body"

    pred = model.predict(X)
    return jsonify({
        "used": used,
        "n": len(X),
        "prediction": pred.tolist()
    })

if __name__ == "__main__":
    # Helpful prints in console so you can see it’s wired right
    print(">> BASE_DIR :", BASE_DIR)
    print(">> MODEL    :", MODEL_PATH, "exists?", _exists(MODEL_PATH))
    print(">> FEAT_CSV :", FEAT_CSV,   "exists?", _exists(FEAT_CSV))
    print(">> FEATURES :", FEATURE_COLS)
    app.run(host="127.0.0.1", port=5000, debug=True)
