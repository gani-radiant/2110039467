// src/App.js

import React from 'react';
import './App.css';
import TopProducts from './components/TopProducts'; // Adjust path if necessary

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TopProducts />
      </header>
    </div>
  );
}

export default App;
