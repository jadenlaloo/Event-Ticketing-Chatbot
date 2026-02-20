"""
Sample events database for the Event Ticketing Chatbot
Extended with more events and mood associations
"""

EVENTS = [
    {
        "id": 1,
        "name": "Tech Innovators Summit 2026",
        "category": "technology",
        "mood": ["excited", "curious", "motivated", "ambitious", "inspired"],
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
        "mood": ["relaxed", "happy", "romantic", "peaceful", "calm", "mellow"],
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
        "mood": ["excited", "motivated", "ambitious", "driven", "inspired", "confident"],
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
        "mood": ["stressed", "tired", "peaceful", "anxious", "overwhelmed", "burnt out", "exhausted"],
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
        "mood": ["excited", "playful", "nostalgic", "competitive", "energetic", "fun"],
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
        "mood": ["hungry", "adventurous", "happy", "curious", "social", "excited"],
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
        "mood": ["curious", "creative", "inspired", "thoughtful", "contemplative", "artistic"],
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
        "mood": ["sad", "stressed", "bored", "down", "lonely", "gloomy"],
        "date": "2026-04-25",
        "time": "8:00 PM",
        "venue": "Laugh Factory",
        "price": 30.00,
        "available_seats": 150,
        "description": "Laugh your worries away with top stand-up comedians."
    },
    {
        "id": 9,
        "name": "Sunrise Yoga by the Beach",
        "category": "wellness",
        "mood": ["peaceful", "calm", "spiritual", "centered", "mindful", "refreshed"],
        "date": "2026-04-05",
        "time": "6:00 AM",
        "venue": "Ocean View Beach",
        "price": 15.00,
        "available_seats": 50,
        "description": "Start your day with calming yoga poses as the sun rises over the ocean."
    },
    {
        "id": 10,
        "name": "Electronic Music Festival",
        "category": "music",
        "mood": ["excited", "energetic", "hyped", "wild", "party", "pumped"],
        "date": "2026-05-01",
        "time": "4:00 PM",
        "venue": "Downtown Arena",
        "price": 75.00,
        "available_seats": 5000,
        "description": "Experience the biggest EDM artists under one roof. Non-stop beats all night."
    },
    {
        "id": 11,
        "name": "Book Club Meetup - Sci-Fi Edition",
        "category": "social",
        "mood": ["curious", "intellectual", "thoughtful", "nerdy", "introverted", "bookish"],
        "date": "2026-03-28",
        "time": "5:00 PM",
        "venue": "City Library Hall",
        "price": 5.00,
        "available_seats": 30,
        "description": "Discuss the latest sci-fi novels with fellow book enthusiasts."
    },
    {
        "id": 12,
        "name": "Outdoor Movie Night",
        "category": "entertainment",
        "mood": ["relaxed", "romantic", "chill", "laid back", "cozy", "date night"],
        "date": "2026-04-12",
        "time": "8:00 PM",
        "venue": "Riverside Park",
        "price": 12.00,
        "available_seats": 200,
        "description": "Watch classic films under the stars with blankets and popcorn."
    },
    {
        "id": 13,
        "name": "Marathon Training Workshop",
        "category": "sports",
        "mood": ["motivated", "determined", "athletic", "disciplined", "healthy", "active"],
        "date": "2026-03-22",
        "time": "7:00 AM",
        "venue": "City Sports Complex",
        "price": 25.00,
        "available_seats": 100,
        "description": "Train with professional coaches and prepare for your next marathon."
    },
    {
        "id": 14,
        "name": "Paint and Sip Night",
        "category": "art",
        "mood": ["creative", "relaxed", "social", "fun", "artistic", "playful"],
        "date": "2026-04-08",
        "time": "7:00 PM",
        "venue": "Canvas Studio",
        "price": 40.00,
        "available_seats": 25,
        "description": "Create your own masterpiece while enjoying drinks with friends."
    },
    {
        "id": 15,
        "name": "Networking Mixer for Creatives",
        "category": "business",
        "mood": ["ambitious", "social", "professional", "motivated", "confident", "outgoing"],
        "date": "2026-04-18",
        "time": "6:30 PM",
        "venue": "The Loft Space",
        "price": 20.00,
        "available_seats": 75,
        "description": "Connect with designers, artists, and creative professionals in your area."
    },
    {
        "id": 16,
        "name": "Jazz Brunch Sunday",
        "category": "music",
        "mood": ["relaxed", "sophisticated", "happy", "mellow", "classy", "peaceful"],
        "date": "2026-04-06",
        "time": "11:00 AM",
        "venue": "The Grand Hotel",
        "price": 55.00,
        "available_seats": 60,
        "description": "Enjoy a luxurious brunch accompanied by live jazz performances."
    },
    {
        "id": 17,
        "name": "Escape Room Challenge",
        "category": "gaming",
        "mood": ["adventurous", "excited", "competitive", "curious", "thrilled", "playful"],
        "date": "2026-04-14",
        "time": "3:00 PM",
        "venue": "Mystery Mansion",
        "price": 35.00,
        "available_seats": 40,
        "description": "Solve puzzles and escape before time runs out. Can you crack the code?"
    },
    {
        "id": 18,
        "name": "Photography Walk - City Lights",
        "category": "art",
        "mood": ["creative", "curious", "artistic", "inspired", "contemplative", "observant"],
        "date": "2026-04-22",
        "time": "7:00 PM",
        "venue": "Downtown District",
        "price": 15.00,
        "available_seats": 20,
        "description": "Capture the beauty of the city at night with fellow photographers."
    },
    {
        "id": 19,
        "name": "Open Mic Poetry Night",
        "category": "art",
        "mood": ["emotional", "expressive", "creative", "sad", "introspective", "deep"],
        "date": "2026-04-30",
        "time": "8:00 PM",
        "venue": "The Spoken Word Cafe",
        "price": 8.00,
        "available_seats": 50,
        "description": "Share your poetry or listen to powerful spoken word performances."
    },
    {
        "id": 20,
        "name": "Rooftop Dance Party",
        "category": "music",
        "mood": ["excited", "party", "energetic", "social", "wild", "celebratory", "free"],
        "date": "2026-05-10",
        "time": "9:00 PM",
        "venue": "Sky Lounge Rooftop",
        "price": 45.00,
        "available_seats": 150,
        "description": "Dance the night away with stunning city views and top DJs."
    }
]

MOODS = [
    "excited", "happy", "relaxed", "stressed", "sad", "bored", 
    "curious", "motivated", "tired", "adventurous", "romantic",
    "playful", "creative", "peaceful", "nostalgic", "ambitious",
    "anxious", "overwhelmed", "energetic", "calm", "lonely",
    "inspired", "confident", "social", "introspective", "wild",
    "mellow", "determined", "artistic", "intellectual", "spiritual",
    "burnt out", "exhausted", "hyped", "pumped", "competitive",
    "contemplative", "emotional", "expressive", "celebratory", "free"
]

CATEGORIES = [
    "technology", "music", "business", "wellness", "gaming", 
    "food", "art", "comedy", "social", "entertainment", "sports"
]
