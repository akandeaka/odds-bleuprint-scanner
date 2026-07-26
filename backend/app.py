from flask import Flask, jsonify, request
from scanner import scan_fixtures

app = Flask(__name__)

@app.route("/scan-fixtures", methods=["POST"])
def scan():
    data = request.json
    fixtures = data.get("fixtures", [])
    season_stage = data.get("season_stage", "start")
    league_type = data.get("league_type", "popular")

    results = scan_fixtures(fixtures, season_stage, league_type)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
