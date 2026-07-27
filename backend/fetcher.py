import requests
from bs4 import BeautifulSoup
import json
from datetime import date

SOCCERWAY_URL = "https://int.soccerway.com/matches/"

def fetch_soccerway_europe():
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(SOCCERWAY_URL, headers=headers, timeout=20)
        response.raise_for_status()
    except Exception:
        print("Soccerway fetch failed. Using manual fallback.")
        use_manual_fallback()
        return

    soup = BeautifulSoup(response.text, "html.parser")
    fixtures = []

    # NOTE: You must adjust these selectors to match Soccerway's real HTML.
    # This is a template structure.
    for row in soup.select("table.matches tbody tr"):
        teams = row.select_one(".team-a, .team-b")
        home_odd = row.select_one(".odds .odd_1")
        draw_odd = row.select_one(".odds .odd_x")
        away_odd = row.select_one(".odds .odd_2")

        if teams and home_odd and draw_odd and away_odd:
            name = teams.get_text(strip=True)

            try:
                home = float(home_odd.get_text(strip=True))
                draw = float(draw_odd.get_text(strip=True))
                away = float(away_odd.get_text(strip=True))
            except ValueError:
                continue

            fixtures.append({
                "name": name,
                "home": home,
                "draw": draw,
                "away": away
            })

    save_fixtures(fixtures)


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


if __name__ == "__main__":
    fetch_soccerway_europe()
