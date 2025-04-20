from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load('model/disease_model.pkl')

# Same symptom list used in training
symptom_list = [
    'fever', 'cough', 'fatigue', 'headache', 'nausea', 'vomiting', 'diarrhea',
    'dizziness', 'chest pain', 'joint pain', 'shortness of breath', 'rash',
    'weight loss', 'night sweats', 'high blood pressure', 'low hemoglobin',
    'vision problems', 'palpitations', 'sore throat', 'abdominal pain',
    'back pain', 'runny nose', 'constipation', 'loss of appetite', 'anxiety'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '').strip()

        print(f"Received symptoms: {symptoms}")

        if not symptoms:
            return jsonify({'risk': 'Please enter some symptoms'}), 200

        features = symptoms_to_features(symptoms)
        prediction = model.predict([features])[0]
        return jsonify({'risk': prediction}), 200

    except Exception as e:
        print("Prediction error:", str(e))
        return jsonify({'risk': 'Server error occurred'}), 200  # Still return 200 to avoid breaking UI

def symptoms_to_features(symptom_text):
    text = symptom_text.lower()
    return [1 if symptom in text else 0 for symptom in symptom_list]

if __name__ == "__main__":
    # Render automatically provides the PORT environment variable
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))