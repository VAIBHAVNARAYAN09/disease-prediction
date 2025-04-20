# Early Disease Prediction System for Rural Areas

## Project Overview

In many rural regions, timely access to quality healthcare remains a significant challenge due to a lack of infrastructure, medical personnel, and awareness. This project, "Early Disease Prediction System for Rural Areas", aims to bridge that gap by offering an accessible and intelligent solution that empowers individuals to take early steps in understanding their health.

The system is a web-based AI platform where users can input basic health information and symptoms to receive early predictions of potential diseases such as diabetes, anemia, and hypertension. This predictive insight helps users seek medical attention before conditions worsen.

What makes this project unique is its localization capability—offering a multilingual interface to cater to non-English-speaking users—and its integration with location-based services to suggest the nearest available health centers. The solution is optimized for mobile use, ensuring accessibility for users even in low-resource environments.

This full-stack application is built using modern web technologies:

- Frontend: React.js
- Backend: Express.js with Node.js
- Machine Learning API: Flask (Python)
- Model: Decision Tree Classifier

It is fully deployed online and ready for real-world testing and demonstration.

## Tech Stack

- Frontend: React.js
- Backend: Node.js with Express
- Machine Learning API: Flask (Python)
- Machine Learning Model: Decision Tree Classifier
- Deployment:
  - Frontend: Vercel
  - Backend & ML API: Render
- Version Control: Git & GitHub

## Features

- Symptom-based AI Prediction: Users input symptoms to get disease predictions using trained ML models
- Common Disease Detection: Currently supports diabetes, anemia, and hypertension
- Nearby Health Center Suggestions: Uses location data to suggest accessible health facilities
- Multilingual Support: Interface available in multiple regional languages
- Mobile-Responsive UI: Works smoothly on phones, tablets, and desktops
- Scalable & Modular Architecture: Easily extendable for future diseases or new ML models

## Deployment

The application is live and available 24/7:

- Frontend (Vercel): [https://disease-prediction-sandy.vercel.app/](https://disease-prediction-sandy.vercel.app/)
- Backend (Render): [https://disease-prediction-backend-ivjt.onrender.com/](https://disease-prediction-backend-ivjt.onrender.com/)
- ML API (Render): [https://disease-prediction-ml-api.onrender.com](https://disease-prediction-ml-api.onrender.com)

## Repository Structure

```
├── client/                # React frontend
├── server/                # Express backend
├── ml-api/                # Flask ML API
├── README.md              # Project overview and documentation
└── .gitignore
```

## How to Run Locally

1. Clone the repository
2. Install dependencies in each subproject (client, server, ml-api)
3. Start the Flask API, Express server, and React frontend individually
4. Access the application at `http://localhost:3000`


