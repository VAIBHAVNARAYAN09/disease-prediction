import React, { useState } from 'react';
import axios from 'axios';
import './SymptomChecker.css';
import doctorImg from './assets/doctor.png'; // Add an image to `assets` folder
import healthIcon from './assets/health-icon.png'; // Another optional image

const SymptomChecker = () => {
  const [symptoms, setSymptoms] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleCheck = async () => {
    console.log("Sending symptoms:", symptoms);

    try {
      const res = await axios.post('http://localhost:5001/predict', {
        symptoms: symptoms,
      });

      console.log("Received response:", res.data);
      setPrediction(res.data.risk);
    } catch (err) {
      console.error("Error during prediction:", err);
      setPrediction('Error connecting to server');
    }
  };

  return (
    <div className="symptom-checker">
      <img src={doctorImg} alt="Doctor" className="header-img" />
      <h2>Symptom Checker</h2>
      <p className="subtext">Describe your symptoms and we'll assess your health risk.</p>
      <textarea
        placeholder="e.g., fever, sore throat, headache"
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
      />
      <button onClick={handleCheck}>Check My Risk</button>
      {prediction && (
        <div className="result">
          <img src={healthIcon} alt="Health Icon" className="icon" />
          <p><strong>Predicted Risk:</strong> {prediction}</p>
        </div>
      )}
    </div>
  );
};

export default SymptomChecker;
