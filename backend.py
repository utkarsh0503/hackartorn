from flask import Flask, request, jsonify
import pickle
import nltk
from nltk.tokenize import word_tokenize
from flask_restful import Api, Resource

# Load the model
with open('disease_predictor.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)
api = Api(app)

# Initialize NLTK
nltk.download('punkt')

# Sample health tips and medication reminders
health_tips = [
    "Stay hydrated.",
    "Exercise regularly.",
    "Get enough sleep.",
    "Eat a balanced diet."
]

medication_reminders = {
    "morning": ["Take your blood pressure medication.", "Take your vitamins."],
    "afternoon": ["Take your cholesterol medication."],
    "evening": ["Take your diabetes medication.", "Take your allergy medication."]
}

# Helper function to predict disease
def predict_disease(symptoms):
    input_data = [1 if symptom in symptoms else 0 for symptom in ['symptom1', 'symptom2', 'symptom3']]
    prediction = model.predict([input_data])[0]
    return "flu" if prediction == 0 else "cold"

class SymptomChecker(Resource):
    def post(self):
        data = request.get_json()
        symptoms = data['symptoms']
        symptoms = word_tokenize(symptoms.lower())
        disease = predict_disease(symptoms)
        return jsonify({"predicted_disease": disease})

class MedicationReminder(Resource):
    def get(self, time_of_day):
        return jsonify({"medications": medication_reminders.get(time_of_day, [])})

class HealthTips(Resource):
    def get(self):
        return jsonify({"tips": health_tips})

api.add_resource(SymptomChecker, '/check_symptoms')
api.add_resource(MedicationReminder, '/medication_reminder/<string:time_of_day>')
api.add_resource(HealthTips, '/health_tips')

if __name__ == '__main__':
    app.run(debug=True)
