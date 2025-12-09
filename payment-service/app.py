from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/pay")
def pay():
    return jsonify({"message": "Payment service working"})

app.run(host="0.0.0.0", port=5003)
