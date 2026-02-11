import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
      : 'http://localhost:8000/api/teams/';
    
    console.log('Teams API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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
      <h2>Teams</h2>
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No teams found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Members</th>
                <th scope="col">Created At</th>
              </tr>
            </thead>
            <tbody>
              {teams.map(team => {
                // Calculate member count
                const memberCount = team.members ? (Array.isArray(team.members) ? team.members.length : 0) : 0;
                
                return (
                  <tr key={team.id || team._id}>
                    <td>{team.id || team._id}</td>
                    <td><strong>{team.name}</strong></td>
                    <td>{team.description}</td>
                    <td>
                      <span className="badge bg-success">{memberCount} {memberCount === 1 ? 'member' : 'members'}</span>
                      {memberCount > 0 && team.members && (
                        <div className="mt-1">
                          <small className="text-muted">{team.members.join(', ')}</small>
                        </div>
                      )}
                    </td>
                    <td>{new Date(team.created_at).toLocaleDateString()}</td>
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

export default Teams;
