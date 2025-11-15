import json
import random
import uuid

DATA_FILE = 'reservations.json'

# Load or initialize reservation database
def load_reservations():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_reservations(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_response(user_input):
    user_input = user_input.lower()

    if "book" in user_input:
        return "Sure! Please enter your name, source, destination, and travel date (e.g., John, NYC, LA, 2025-07-10)"

    elif "," in user_input:
        parts = user_input.split(',')
        if len(parts) == 4:
            name, src, dest, date = [p.strip() for p in parts]
            booking_id = str(uuid.uuid4())[:8]
            booking = {
                "id": booking_id,
                "name": name,
                "source": src,
                "destination": dest,
                "date": date
            }
            data = load_reservations()
            data.append(booking)
            save_reservations(data)
            return f"✅ Ticket booked successfully! Your Booking ID is {booking_id}"
        else:
            return "❌ Invalid format. Please use: Name, Source, Destination, Date"

    elif "check booking" in user_input:
        return "Please enter your Booking ID to check status."

    elif len(user_input.strip()) == 8:  # assuming UUID length
        data = load_reservations()
        for entry in data:
            if entry["id"] == user_input.strip():
                return f"📄 Booking Found: {entry}"
        return "❌ No booking found with that ID."

    elif "train" in user_input or "available" in user_input:
        trains = ["Express 101", "FastTrack 202", "Metro 303"]
        return f"🚆 Available Trains: {', '.join(trains)}"

    return "🤖 I'm sorry, I didn't understand that. Try asking about booking, availability, or checking a booking."
