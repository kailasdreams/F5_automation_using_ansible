from flask import Flask, render_template
import json
import os

app = Flask(__name__)

JSON_FILE = "/var/lib/awx/projects/prod/f5_status.json"


@app.route("/")
def dashboard():

    data = []

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            data = json.load(f)

    return render_template(
        "index.html",
        data=data
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )

