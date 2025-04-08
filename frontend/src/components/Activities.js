import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    axios.get('https://organic-acorn-g7pwg5pgwpc964p-8000.app.github.dev/api/activities')
      .then(response => setActivities(response.data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
