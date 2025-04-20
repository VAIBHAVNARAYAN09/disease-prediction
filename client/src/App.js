import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SymptomChecker from './pages/SymptomChecker';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SymptomChecker />} />
      </Routes>
    </Router>
  );
}
export default App;
