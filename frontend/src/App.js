import React, { useState, useEffect } from "react";
import MatchCard from "./components/MatchCard";
import { fetchFixtures } from "./services/api";

function App() {
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    async function loadMatches() {
      const data = await fetchFixtures();
      setMatches(data);
    }
    loadMatches();
  }, []);

  return (
    <div>
      <h1>Odds Blueprint Scanner</h1>
      {matches.map((match, index) => (
        <MatchCard key={index} match={match} />
      ))}
    </div>
  );
}

export default App;
