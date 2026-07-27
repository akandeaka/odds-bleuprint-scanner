from flask import Flask, jsonify
import json
from scanner import scan_fixtures

app = Flask(__name__)

@app.route("/scan-fixtures", methods=["GET"])
def scan():
    # Load automatically fetched fixtures
    with open("fixtures.json") as f:
        data = json.load(f)

    fixtures = data.get("fixtures", [])
    season_stage = "start"      # default for Europe
    league_type = "popular"     # default for Europe

    results = scan_fixtures(fixtures, season_stage, league_type)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
