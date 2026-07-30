import requests
from bs4 import BeautifulSoup
import json
from datetime import date

# Soccerway fixtures page
SOCCERWAY_URL = "https://int.soccerway.com/matches/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Telegram bot setup
TELEGRAM_TOKEN = "your_bot_token_here"
CHAT_ID = "your_chat_id_here"

def fetch_soccerway_europe():
    try:
        response = requests.get(SOCCERWAY_URL, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except Exception:
        print("Soccerway fetch failed. Using manual fallback.")
        use_manual_fallback()
        return

    soup = BeautifulSoup(response.text, "html.parser")
    fixtures = []

    # Adjusted selectors based on Soccerway’s current HTML
    for match in soup.select("div.match"):   # each match block
        home_team = match.select_one(".team-a")
        away_team = match.select_one(".team-b")
        odds = match.select(".odds-value")

        if home_team and away_team and len(odds) == 3:
            try:
                home = float(odds[0].get_text(strip=True))
                draw = float(odds[1].get_text(strip=True))
                away = float(odds[2].get_text(strip=True))
            except ValueError:
                continue

            fixtures.append({
                "match": f"{home_team.get_text(strip=True)} vs {away_team.get_text(strip=True)}",
                "home": home,
                "draw": draw,
                "away": away,
                # Example criteria calculation
                "criteria_passed": calculate_criteria(home, draw, away)
            })

    save_fixtures(fixtures)
    send_to_telegram(fixtures)


def calculate_criteria(home, draw, away):
    """Example criteria logic — adjust to your rules"""
    passed = 0
    if home < 2.5: passed += 1
    if draw > 3.0: passed += 1
    if away < 3.5: passed += 1
    if home + away < 5.0: passed += 1
    return passed


def save_fixtures(fixtures):
    with open("fixtures.json", "w") as f:
        json.dump({
            "date": str(date.today()),
            "fixtures": fixtures
        }, f, indent=2)
    print("Fixtures saved successfully.")


def use_manual_fallback():
    with open("manual_fixtures.json") as f:
        manual = json.load(f)
    with open("fixtures.json", "w") as f:
        json.dump(manual, f, indent=2)
    print("Manual fixtures loaded as fallback.")
    send_to_telegram(manual["fixtures"])


def send_to_telegram(fixtures):
    # Only send matches that passed 4 criteria
    filtered = [m for m in fixtures if m.get("criteria_passed", 0) >= 4]

    if not filtered:
        text = "No matches passed the criteria today."
    else:
        text = "\n\n".join([
            f"🏆 {m['match']}\n"
            f"Home: {m['home']} | Draw: {m['draw']} | Away: {m['away']}\n"
            f"Prediction: {m.get('prediction','N/A')}\n"
            f"Criteria passed: {m['criteria_passed']}"
            for m in filtered
        ])

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})


if __name__ == "__main__":
    fetch_soccerway_europe()
