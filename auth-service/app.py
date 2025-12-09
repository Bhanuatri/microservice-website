from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if data["username"] == "admin" and data["password"] == "admin123":
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

app.run(host="0.0.0.0", port=5001)
