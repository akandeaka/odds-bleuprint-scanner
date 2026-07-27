import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def fetch_soccerway_europe():
    url = "https://int.soccerway.com/matches/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
    except Exception:
        print("Soccerway fetch failed. Using manual fallback.")
        use_manual_fallback()
        return

    soup = BeautifulSoup(response.text, "html.parser")
    fixtures = []

    # Example parsing logic (adjust to real Soccerway HTML)
    for row in soup.select("table.matches tbody tr"):
        teams = row.select_one(".team-a, .team-b")
        odds = row.select_one(".odds")

        if teams and odds:
            name = teams.get_text(strip=True)
            try:
                odd_value = float(odds.get_text(strip=True))
            except:
                continue

            fixtures.append({
                "name": name,
                "odds": odd_value
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
