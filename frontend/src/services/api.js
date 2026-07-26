export async function fetchFixtures() {
  const response = await fetch("http://localhost:5000/scan-fixtures", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      fixtures: [
        { name: "Arsenal vs Fulham", odds: 1.19 },
        { name: "Bayern vs Dortmund", odds: 1.72 },
        { name: "Ajax vs PSV", odds: 3.60 }
      ],
      season_stage: "start",
      league_type: "popular"
    })
  });
  return response.json();
}
