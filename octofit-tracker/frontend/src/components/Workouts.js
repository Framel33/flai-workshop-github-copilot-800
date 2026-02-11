import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    
    console.log('Workouts API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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
      <h2>💪 Workout Suggestions</h2>
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No workout suggestions found.
        </div>
      ) : (
        <div className="row">
          {workouts.map(workout => {
            let difficultyColor = 'bg-success';
            if (workout.difficulty === 'Medium') difficultyColor = 'bg-warning';
            if (workout.difficulty === 'Hard') difficultyColor = 'bg-danger';
            
            return (
              <div key={workout.id || workout._id} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100">
                  <div className="card-body">
                    <h5 className="card-title">{workout.name}</h5>
                    <p className="card-text">{workout.description}</p>
                    <div className="mb-3">
                      <span className="badge bg-primary me-2">{workout.activity_type}</span>
                      <span className={`badge ${difficultyColor}`}>{workout.difficulty}</span>
                    </div>
                    <ul className="list-group list-group-flush">
                      <li className="list-group-item"><strong>⏱️ Duration:</strong> {workout.duration} minutes</li>
                      <li className="list-group-item"><strong>🔥 Calories:</strong> {workout.calories_estimate}</li>
                    </ul>
                  </div>
                  <div className="card-footer bg-transparent">
                    <button className="btn btn-primary w-100">Start Workout</button>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default Workouts;
