from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ingest", methods=["POST"])
def ingest():
    data = request.json
    print("Received Data:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)