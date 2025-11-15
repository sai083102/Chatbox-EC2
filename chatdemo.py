import pickle
import nltk
nltk.download('punkt')

# Load the trained model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Intent response mapping
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings! How can I help you today?"],
    "book_ticket": ["Sure, I can help you book a train ticket. Please provide your name, source, destination, and date."],
    "check_booking_status": ["Please provide your booking ID to check the status."],
    "train_availability": ["Trains available: Express 101, FastTrack 202, and Metro 303."],
    "goodbye": ["Goodbye! Have a safe journey!", "See you later!", "Thanks for using TrainBot."]
}

def predict_intent(message):
    vector = vectorizer.transform([message.lower()])
    return model.predict(vector)[0]

def get_response(intent):
    return responses.get(intent, ["Sorry, I didn't understand that. Can you please rephrase?"])[0]

def chat():
    print("🚆 Welcome to TrainBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🤖: Thanks for chatting! Goodbye.")
            break
        intent = predict_intent(user_input)
        reply = get_response(intent)
        print("🤖:", reply)

if __name__ == "__main__":
    chat()
