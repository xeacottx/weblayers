import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [events, setEvents] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const apiBase = process.env.REACT_APP_API_URL || '';

  console.log('Using API base URL:', apiBase);

  fetch(`${apiBase}/api/events`)
    .then((res) => {
      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }
      return res.json();
    })
    .then((data) => {
      // handle the fetched data
      console.log('Fetched data:', data);
    })
    .catch((err) => {
      console.error('Error fetching events:', err);
    });

  return (
    <div className="app-container">
      <h1>Welcome to WebLayers</h1>
      <p>This is a visualization of what happens when you click a link.</p>
      <img src="/diagram-placeholder.svg" alt="Layer Diagram" style={{ maxWidth: '100%' }} />

      <div style={{ marginTop: '2rem' }}>
        <h2>Event Info</h2>
        {loading && <p>Loading...</p>}
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        {events && (
          <pre style={{ background: '#eee', padding: '1rem' }}>
            {JSON.stringify(events, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}

export default App;