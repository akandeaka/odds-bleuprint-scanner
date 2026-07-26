from odds_engine import interpret_odds

def scan_fixtures(fixtures, season_stage, league_type):
    results = []
    for match in fixtures:
        odds = match.get("odds")
        prediction = interpret_odds(odds, season_stage, league_type)
        if prediction:
            results.append({
                "match": match.get("name"),
                "odds": odds,
                "prediction": prediction,
                "season_stage": season_stage,
                "league_type": league_type
            })
    return results
