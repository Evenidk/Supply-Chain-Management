import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Shipments from './Shipments';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/shipments" element={<Shipments />} />
        <Route path="/" element={
          <div className="container">
            <h1>Welcome to Supply Chain Visibility</h1>
            <p>Track your shipments in real-time.</p>
          </div>
        } />
      </Routes>
    </Router>
  );
}

export default App;
