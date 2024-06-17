import requests

def chatbot():
    print("Welcome to the Smart Healthcare Assistant!")
    print("You can ask me to check symptoms, get medication reminders, or ask for health tips.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if "symptom" in user_input:
            symptoms = input("Please describe your symptoms: ")
            response = requests.post('http://127.0.0.1:5000/check_symptoms', json={"symptoms": symptoms})
            print("Assistant:", response.json()["predicted_disease"])
        
        elif "medication" in user_input:
            time_of_day = input("Please specify the time of day (morning, afternoon, evening): ").strip().lower()
            response = requests.get(f'http://127.0.0.1:5000/medication_reminder/{time_of_day}')
            print("Assistant:", response.json()["medications"])
        
        elif "tip" in user_input:
            response = requests.get('http://127.0.0.1:5000/health_tips')
            print("Assistant:", response.json()["tips"])
        
        elif user_input in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break
        
        else:
            print("Assistant: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
