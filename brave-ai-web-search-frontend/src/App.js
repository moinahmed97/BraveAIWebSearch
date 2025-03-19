import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    // Replace with your backend endpoint
    const response = await fetch('http://localhost:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });

    const data = await response.json();
    setResults(data.results);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Brave AI Web Search</h1>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your search query"
        />
        <button onClick={handleSearch}>Search</button>
        <div>
          {results.map((result, index) => (
            <div key={index}>{result}</div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;