import os
import datetime
from flask import *
from utils.helpers import *
from dotenv import load_dotenv


app = Flask(__name__)
application = app


@app.route("/")
def index():
    with open("entries.json", "r") as f:
        data = json.load(f)

    return render_template("index.html", entries=data)


@app.route("/api/entry", methods=["POST"])
def add_entry():
    if not authenticate(request):
        return jsonify({"error": "Unauthorized"}), 401

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(data)
    try:
        add_entry_to_json(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"message": "Entry added"}), 201


@app.route("/entries.json")  # endpoint to serve json data, useful for dynamic updates
def get_entries():
    with open("entries.json", "r") as f:
        entries = json.load(f)
    return jsonify(entries)


if __name__ == "__main__":
    app.run()
