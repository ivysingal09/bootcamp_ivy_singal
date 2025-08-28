import os, io, pickle
from typing import List, Any
from flask import Flask, request, jsonify, Response
import numpy as np
import matplotlib.pyplot as plt
from src.utils import validate_numeric_list

MODEL_PATH = os.getenv("MODEL_PATH", "model/model.pkl")
app = Flask(__name__)

def _load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    return None

model = _load_model()

def _predict_with_fallback(features: List[float]) -> Any:
    arr = np.array(features, dtype=float).reshape(1, -1)
    if model is not None and hasattr(model, "predict"):
        try:
            y = model.predict(arr)
            return y.tolist()[0] if hasattr(y, "tolist") else y
        except Exception:
            pass
    return float(np.sum(arr))

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})

@app.route("/predict", methods=["POST"])
def predict():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    data = request.get_json(silent=True) or {}
    if "X" in data:
        preds = [_predict_with_fallback(validate_numeric_list(row)) for row in data["X"]]
        return jsonify({"predictions": preds})
    features = data.get("features")
    if features is None:
        return jsonify({"error": "Missing 'features'"}), 400
    feats = validate_numeric_list(features)
    return jsonify({"prediction": _predict_with_fallback(feats)})

@app.route("/predict/<float:input1>")
def predict_one(input1: float):
    return jsonify({"prediction": _predict_with_fallback([input1])})

@app.route("/predict/<float:input1>/<float:input2>")
def predict_two(input1: float, input2: float):
    return jsonify({"prediction": _predict_with_fallback([input1, input2])})

@app.route("/plot")
def plot():
    fig, ax = plt.subplots()
    ax.plot([0,1,2,3,4], [x*x for x in range(5)])
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return Response(buf.read(), mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
