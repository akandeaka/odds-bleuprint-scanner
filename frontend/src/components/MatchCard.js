import React from "react";

function MatchCard({ match }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
      <h3>{match.match}</h3>
      <p>Odds: {match.odds}</p>
      <p>Prediction: {match.prediction}</p>
      <p>Season Stage: {match.season_stage}</p>
      <p>League Type: {match.league_type}</p>
    </div>
  );
}

export default MatchCard;
