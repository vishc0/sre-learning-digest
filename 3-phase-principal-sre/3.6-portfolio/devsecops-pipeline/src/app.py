# Minimal Flask app — exists only as a pipeline target
# Real value is in the pipeline, not the app

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "1.0.0"})

@app.route("/")
def index():
    return jsonify({"message": "DevSecOps pipeline demo app"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
