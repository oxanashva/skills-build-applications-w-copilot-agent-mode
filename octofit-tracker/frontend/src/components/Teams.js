import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.error('Error fetching teams:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Teams</h1>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Team Name</th>
              </tr>
            </thead>
            <tbody>
              {teams.map(team => (
                <tr key={team._id}>
                  <td>{team.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Teams;
