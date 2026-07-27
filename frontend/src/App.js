import React from "react";

function MatchCard({ match }) {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        margin: "10px 0",
        padding: "10px",
        borderRadius: "6px"
      }}
    >
      <h3>{match.match}</h3>
      <p>
        <strong>Home:</strong> {match.home} &nbsp;
        <strong>Draw:</strong> {match.draw} &nbsp;
        <strong>Away:</strong> {match.away}
      </p>
      <p>
        <strong>Prediction:</strong> {match.prediction}
      </p>
      <p>
        <strong>Season Stage:</strong> {match.season_stage} &nbsp;
        <strong>League Type:</strong> {match.league_type}
      </p>
    </div>
  );
}

export default MatchCard;
