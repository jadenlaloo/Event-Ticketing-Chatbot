"""
Sample events database for the Event Ticketing Chatbot
"""

EVENTS = [
    {
        "id": 1,
        "name": "Tech Innovators Summit 2026",
        "category": "technology",
        "mood": ["excited", "curious", "motivated"],
        "date": "2026-03-15",
        "time": "10:00 AM",
        "venue": "Silicon Valley Convention Center",
        "price": 49.99,
        "available_seats": 150,
        "description": "Join industry leaders discussing AI, blockchain, and the future of tech."
    },
    {
        "id": 2,
        "name": "Acoustic Nights - Live Music",
        "category": "music",
        "mood": ["relaxed", "happy", "romantic"],
        "date": "2026-03-20",
        "time": "7:00 PM",
        "venue": "The Blue Note Lounge",
        "price": 25.00,
        "available_seats": 80,
        "description": "An intimate evening of acoustic performances by upcoming artists."
    },
    {
        "id": 3,
        "name": "GenZ Startup Pitch Night",
        "category": "business",
        "mood": ["excited", "motivated", "ambitious"],
        "date": "2026-03-25",
        "time": "6:00 PM",
        "venue": "Innovation Hub Downtown",
        "price": 15.00,
        "available_seats": 100,
        "description": "Watch GenZ entrepreneurs pitch their revolutionary ideas."
    },
    {
        "id": 4,
        "name": "Mindfulness and Wellness Retreat",
        "category": "wellness",
        "mood": ["stressed", "tired", "peaceful"],
        "date": "2026-04-01",
        "time": "9:00 AM",
        "venue": "Serenity Gardens",
        "price": 35.00,
        "available_seats": 40,
        "description": "A day of meditation, yoga, and mental wellness workshops."
    },
    {
        "id": 5,
        "name": "Retro Gaming Championship",
        "category": "gaming",
        "mood": ["excited", "playful", "nostalgic"],
        "date": "2026-04-10",
        "time": "2:00 PM",
        "venue": "Arcade Arena",
        "price": 20.00,
        "available_seats": 200,
        "description": "Compete in classic arcade games and win amazing prizes."
    },
    {
        "id": 6,
        "name": "Street Food Festival",
        "category": "food",
        "mood": ["hungry", "adventurous", "happy"],
        "date": "2026-04-15",
        "time": "11:00 AM",
        "venue": "Central Park",
        "price": 10.00,
        "available_seats": 500,
        "description": "Taste cuisines from around the world at this foodie paradise."
    },
    {
        "id": 7,
        "name": "AI Art Exhibition",
        "category": "art",
        "mood": ["curious", "creative", "inspired"],
        "date": "2026-04-20",
        "time": "10:00 AM",
        "venue": "Modern Art Museum",
        "price": 18.00,
        "available_seats": 120,
        "description": "Explore the intersection of artificial intelligence and creativity."
    },
    {
        "id": 8,
        "name": "Comedy Night Live",
        "category": "comedy",
        "mood": ["sad", "stressed", "bored"],
        "date": "2026-04-25",
        "time": "8:00 PM",
        "venue": "Laugh Factory",
        "price": 30.00,
        "available_seats": 150,
        "description": "Laugh your worries away with top stand-up comedians."
    }
]

MOODS = [
    "excited", "happy", "relaxed", "stressed", "sad", "bored", 
    "curious", "motivated", "tired", "adventurous", "romantic",
    "playful", "creative", "peaceful", "nostalgic", "ambitious"
]

CATEGORIES = ["technology", "music", "business", "wellness", "gaming", "food", "art", "comedy"]
