import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def fetch_soccerway_europe():
    url = "https://int.soccerway.com/matches/"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    fixtures = []

    # Soccerway structure: match rows inside .matches table
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

    with open("fixtures.json", "w") as f:
        json.dump({
            "date": str(date.today()),
            "fixtures": fixtures
        }, f, indent=2)

    return fixtures

if __name__ == "__main__":
    fetch_soccerway_europe()
