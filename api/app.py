from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True) or {}
    feats = data.get("features")
    if not isinstance(feats, list):
        return jsonify({"error": "Send JSON like {'features': [0.1, 0.2, ...]}"}), 400
    # TODO: load your pickled model and compute prediction
    # placeholder: sum of features
    return jsonify({"prediction": sum(feats)})
if __name__ == "__main__":
    # Local run:  python api/app.py
    app.run(host="0.0.0.0", port=5000, debug=True)
