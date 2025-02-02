from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load data from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Convert list to dictionary for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get names from query params
    marks = [marks_dict.get(name, "Not Found") for name in names]
    return jsonify({"marks": marks})

# Vercel requires this as the entry point
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)
