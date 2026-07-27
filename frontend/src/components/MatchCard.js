import React from "react";

function MatchCard({ match }) {
  return (
    <div className="match-card">

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
