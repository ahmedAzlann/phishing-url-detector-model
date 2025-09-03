# app.py
import os
from flask import Flask, request, jsonify
from feature_extraction import FeatureExtraction

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        fe = FeatureExtraction(url)
        features = fe.getFeaturesList()

        # Simple rule: if many -1 features => phishing
        score = features.count(-1)
        status = "phishing" if score > 5 else "safe"

        return jsonify({
            "url": url,
            "status": status,
            "score": score,
            "features": features
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway will inject PORT
    app.run(debug=True, host="0.0.0.0", port=port)