from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import random
import pandas as pd

# Set random seed for reproducibility
random.seed(42)

# Expanded symptom list
symptom_list = [
    'fever', 'cough', 'fatigue', 'headache', 'nausea', 'vomiting', 'diarrhea',
    'dizziness', 'chest pain', 'joint pain', 'shortness of breath', 'rash',
    'weight loss', 'night sweats', 'high blood pressure', 'low hemoglobin',
    'vision problems', 'palpitations', 'sore throat', 'abdominal pain',
    'back pain', 'runny nose', 'constipation', 'loss of appetite', 'anxiety'
]

# Expanded disease symptom mapping
disease_symptoms = {
    'Diabetes': ['fatigue', 'vision problems', 'weight loss', 'nausea'],
    'Hypertension': ['high blood pressure', 'headache', 'chest pain', 'dizziness'],
    'Anemia': ['low hemoglobin', 'fatigue', 'dizziness', 'palpitations'],
    'COVID-19': ['fever', 'cough', 'fatigue', 'sore throat', 'shortness of breath'],
    'Flu': ['fever', 'cough', 'headache', 'fatigue', 'runny nose'],
    'Malaria': ['fever', 'nausea', 'vomiting', 'joint pain', 'headache'],
    'Typhoid': ['fever', 'abdominal pain', 'diarrhea', 'fatigue'],
    'Asthma': ['shortness of breath', 'chest pain', 'cough', 'palpitations'],
    'Migraine': ['headache', 'nausea', 'vomiting', 'dizziness'],
    'Tuberculosis': ['cough', 'weight loss', 'night sweats', 'fever'],
    'Depression': ['fatigue', 'anxiety', 'loss of appetite'],
    'Arthritis': ['joint pain', 'fatigue', 'back pain'],
    'Constipation': ['abdominal pain', 'constipation'],
    'Allergy': ['rash', 'cough', 'runny nose']
}

# Generate synthetic data
data, labels = [], []

for disease, symptoms in disease_symptoms.items():
    for _ in range(100):  # 100 samples per disease
        feature_vector = [0] * len(symptom_list)
        indices = [symptom_list.index(sym) for sym in symptoms]
        for i in indices:
            feature_vector[i] = 1
        # Add noise
        noise_indices = random.sample(range(len(symptom_list)), k=2)
        for ni in noise_indices:
            if ni not in indices:
                feature_vector[ni] = random.choice([0, 1])
        data.append(feature_vector)
        labels.append(disease)

# DataFrame for analysis (optional)
df = pd.DataFrame(data, columns=symptom_list)
df['disease'] = labels

# Split and train
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Accuracy report
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(clf, 'disease_model.pkl')
print("Model trained and saved as model/disease_model.pkl")
