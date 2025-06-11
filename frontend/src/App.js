// src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [event, setEvent]     = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    fetch('/api/events')
      .then(res => {
        if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
        return res.json();
      })
      .then(data => {setEvent(data);})
      .catch(err => {
        console.error('Fetch error:', err);
        setError(err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  // Render logic
  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div style={{ color: 'red' }}>Error: {error.message}</div>;
  }
  if (event.length === 0) {
    return <div>No events found.</div>;
  }

  return (
    <div className="App" style={{ padding: '2rem' }}>
      <h1>WebLayers Demo</h1>
      <h2>Event Info</h2>
      <div style={{ marginBottom: '1rem' }}>
        <strong>{new Date(event.timestamp).toLocaleString()}</strong><br/>
        IP: {event.client_ip}<br/>
       Message: {event.message}
     </div>
    </div>
  );
}

export default App;