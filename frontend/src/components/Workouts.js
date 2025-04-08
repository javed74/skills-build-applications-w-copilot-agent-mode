import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    axios.get('https://organic-acorn-g7pwg5pgwpc964p-8000.app.github.dev/api/workouts')
      .then(response => setWorkouts(response.data))
      .catch(error => console.error('Error fetching workouts:', error));
  }, []);

  return (
    <div>
      <h1>Workouts</h1>
      <ul>
        {workouts.map(workout => (
          <li key={workout.id}>{workout.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
