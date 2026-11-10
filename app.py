
from flask import Flask, render_template, jsonify
from network_monitor import check_connection

app = Flask(__name__)

devices = [
    "1.1.1.1",
    "8.8.8.8",
    "google.com"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/devices")
def get_devices():
    results = []

    for device in devices:
        results.append(check_connection(device))

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
