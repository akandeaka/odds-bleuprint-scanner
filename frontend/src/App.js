import React, { useEffect, useState } from "react";
import MatchCard from "./components/MatchCard";
import { fetchScannedFixtures } from "./services/api";

function App() {
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    async function loadMatches() {
      try {
        const data = await fetchScannedFixtures();
        setMatches(data);
      } catch (err) {
        console.error("Failed to load matches", err);
      }
    }
    loadMatches();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Odds Blueprint Scanner (Europe / Bet365)</h1>
      {matches.length === 0 && <p>No matches found for today.</p>}
      {matches.map((match, index) => (
        <MatchCard key={index} match={match} />
      ))}
    </div>
  );
}

export default App;
