import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Users from './components/Users';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/logo.png" alt="OctoFit Logo" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="hero-section text-center">
                <h1 className="display-4">Welcome to OctoFit Tracker</h1>
                <p className="lead">Track your fitness activities, compete with your team, and achieve your goals!</p>
              </div>
              
              <div className="row mt-4">
                <div className="col-md-6 col-lg-4 mb-4">
                  <Link to="/users" className="text-decoration-none">
                    <div className="card feature-card">
                      <div className="card-body">
                        <div className="feature-icon">👥</div>
                        <h5 className="card-title">Manage Users</h5>
                        <p className="card-text">View all registered users and their team assignments.</p>
                        <button className="btn btn-primary">View Users</button>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 col-lg-4 mb-4">
                  <Link to="/activities" className="text-decoration-none">
                    <div className="card feature-card">
                      <div className="card-body">
                        <div className="feature-icon">🏃</div>
                        <h5 className="card-title">Track Activities</h5>
                        <p className="card-text">Log your workouts and monitor your progress over time.</p>
                        <button className="btn btn-primary">View Activities</button>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 col-lg-4 mb-4">
                  <Link to="/teams" className="text-decoration-none">
                    <div className="card feature-card">
                      <div className="card-body">
                        <div className="feature-icon">🤝</div>
                        <h5 className="card-title">Join Teams</h5>
                        <p className="card-text">Create or join teams and collaborate with others.</p>
                        <button className="btn btn-primary">View Teams</button>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 col-lg-4 mb-4">
                  <Link to="/leaderboard" className="text-decoration-none">
                    <div className="card feature-card">
                      <div className="card-body">
                        <div className="feature-icon">🏆</div>
                        <h5 className="card-title">Compete</h5>
                        <p className="card-text">Check the leaderboard and see how you rank against others.</p>
                        <button className="btn btn-primary">View Leaderboard</button>
                      </div>
                    </div>
                  </Link>
                </div>
                
                <div className="col-md-6 col-lg-4 mb-4">
                  <Link to="/workouts" className="text-decoration-none">
                    <div className="card feature-card">
                      <div className="card-body">
                        <div className="feature-icon">💪</div>
                        <h5 className="card-title">Get Suggestions</h5>
                        <p className="card-text">Discover personalized workout routines tailored for you.</p>
                        <button className="btn btn-primary">Browse Workouts</button>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
