import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`
      : 'http://localhost:8000/api/leaderboard/';
    
    console.log('Leaderboard API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="spinner-container">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <h2>🏆 Leaderboard</h2>
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No leaderboard data found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th scope="col">Rank</th>
                <th scope="col">User</th>
                <th scope="col">Team</th>
                <th scope="col">Total Calories</th>
                <th scope="col">Total Activities</th>
                <th scope="col">Total Duration (min)</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => {
                let rankBadge = '';
                if (index === 0) rankBadge = '🥇';
                else if (index === 1) rankBadge = '🥈';
                else if (index === 2) rankBadge = '🥉';
                
                return (
                  <tr key={entry.id || entry._id || index}>
                    <td><strong>{rankBadge} {entry.rank || index + 1}</strong></td>
                    <td><strong>{entry.user_name || entry.user || entry.username}</strong></td>
                    <td>
                      {entry.team ? (
                        <span className="badge bg-info">{entry.team}</span>
                      ) : (
                        <span className="text-muted">No team</span>
                      )}
                    </td>
                    <td><span className="badge bg-danger">{entry.total_calories || 0}</span></td>
                    <td><span className="badge bg-primary">{entry.total_activities || 0}</span></td>
                    <td><span className="badge bg-success">{entry.total_duration || 0}</span></td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
