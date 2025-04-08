import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);

  useEffect(() => {
    axios.get('https://organic-acorn-g7pwg5pgwpc964p-8000.app.github.dev/api/leaderboard')
      .then(response => setLeaders(response.data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {leaders.map(leader => (
          <li key={leader.id}>{leader.name}: {leader.score}</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
