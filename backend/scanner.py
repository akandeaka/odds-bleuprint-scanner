from odds_engine import interpret_odds

def scan_fixtures(fixtures, season_stage, league_type):
    results = []

    for match in fixtures:
        home = match.get("home")
        draw = match.get("draw")
        away = match.get("away")

        # Interpret based on home odd (you can expand later)
        prediction = interpret_odds(home, season_stage, league_type)

        if prediction:
            results.append({
                "match": match.get("name"),
                "home": home,
                "draw": draw,
                "away": away,
                "prediction": prediction,
                "season_stage": season_stage,
                "league_type": league_type
            })

    return results
