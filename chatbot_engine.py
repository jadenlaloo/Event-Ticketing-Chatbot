"""
Chatbot Engine - Handles conversation logic and NLP
Enhanced with more emotions, responses, and interaction options
"""

import re
import random
from events_data import EVENTS, MOODS, CATEGORIES

class ChatbotEngine:
    def __init__(self):
        self.state = "greeting"
        self.user_data = {
            "name": None,
            "mood": None,
            "selected_event": None,
            "num_tickets": 1,
            "email": None
        }
        self.conversation_history = []
        self.current_events = []
        
    def reset(self):
        """Reset the conversation state"""
        self.state = "greeting"
        self.user_data = {
            "name": None,
            "mood": None,
            "selected_event": None,
            "num_tickets": 1,
            "email": None
        }
        self.conversation_history = []
        self.current_events = []
    
    def get_greeting(self):
        """Return initial greeting message with variation"""
        greetings = [
            "Hello. I'm TicketBot.\n\nI help you discover events based on how you're feeling. What's your name?",
            "Hey there. I'm TicketBot.\n\nI find events that match your vibe. What should I call you?",
            "Welcome. I'm TicketBot.\n\nTell me your name and I'll help you find the perfect event.",
            "Hi. TicketBot here.\n\nI specialize in mood-based event recommendations. What's your name?"
        ]
        return random.choice(greetings)
    
    def detect_mood(self, text):
        """Detect mood from user input with expanded keywords"""
        text_lower = text.lower()
        
        mood_keywords = {
            # Positive high energy
            "excited": ["excited", "pumped", "thrilled", "can't wait", "hyped", "psyched", "stoked", "amped", "fired up"],
            "happy": ["happy", "great", "good", "wonderful", "fantastic", "amazing", "awesome", "joyful", "cheerful", "blessed", "grateful"],
            "energetic": ["energetic", "energized", "active", "lively", "dynamic", "vibrant", "full of energy"],
            "hyped": ["hyped", "pumped up", "ready to go", "let's go", "bring it on"],
            "celebratory": ["celebrating", "celebratory", "party mood", "festive", "want to celebrate"],
            
            # Positive low energy
            "relaxed": ["relaxed", "chill", "calm", "peaceful", "easy", "laid back", "mellow", "chilled", "zen"],
            "happy": ["content", "satisfied", "pleased", "at peace"],
            "peaceful": ["peaceful", "serene", "tranquil", "quiet", "still"],
            "calm": ["calm", "composed", "collected", "steady", "balanced"],
            "mellow": ["mellow", "easy going", "low key", "soft"],
            
            # Negative states
            "stressed": ["stressed", "anxious", "worried", "overwhelmed", "pressure", "tense", "nervous", "on edge", "freaking out"],
            "sad": ["sad", "down", "upset", "unhappy", "depressed", "low", "blue", "heartbroken", "miserable", "grief", "crying"],
            "bored": ["bored", "boring", "nothing to do", "dull", "uninterested", "restless", "blah"],
            "tired": ["tired", "exhausted", "sleepy", "drained", "fatigue", "worn out", "burnt out", "wiped", "dead tired"],
            "lonely": ["lonely", "alone", "isolated", "by myself", "need company", "no friends", "want to meet people"],
            "anxious": ["anxious", "worried", "panicking", "panic", "scared", "afraid", "fearful"],
            "overwhelmed": ["overwhelmed", "too much", "can't handle", "drowning", "swamped"],
            "gloomy": ["gloomy", "dark", "grey", "bleak", "hopeless"],
            
            # Intellectual/Creative
            "curious": ["curious", "interested", "wondering", "explore", "want to learn", "intrigued", "fascinated"],
            "creative": ["creative", "artistic", "artsy", "imaginative", "want to create", "inspired to make"],
            "inspired": ["inspired", "motivated by", "moved", "touched"],
            "thoughtful": ["thoughtful", "thinking", "reflective", "pensive", "contemplative", "philosophical"],
            "intellectual": ["intellectual", "smart", "brainy", "nerdy", "geeky", "want to think"],
            
            # Ambitious/Driven
            "motivated": ["motivated", "driven", "determined", "focused", "goal oriented"],
            "ambitious": ["ambitious", "goals", "success", "career", "want to achieve", "hungry for success"],
            "confident": ["confident", "bold", "self assured", "ready", "capable"],
            "competitive": ["competitive", "want to win", "challenge", "beat", "compete"],
            
            # Social
            "social": ["social", "want to meet", "hang out", "make friends", "people", "crowd", "party"],
            "romantic": ["romantic", "love", "date", "partner", "couple", "valentine", "anniversary", "significant other"],
            "outgoing": ["outgoing", "extroverted", "talkative", "friendly"],
            
            # Adventure/Fun
            "adventurous": ["adventurous", "adventure", "explore", "new things", "try something new", "spontaneous", "wild"],
            "playful": ["playful", "fun", "games", "play", "silly", "goofy", "childlike"],
            "nostalgic": ["nostalgic", "memories", "old times", "remember", "throwback", "retro", "classic"],
            "thrilled": ["thrilled", "exhilarated", "adrenaline", "rush"],
            
            # Wellness
            "spiritual": ["spiritual", "soul", "inner peace", "meditation", "mindful", "centered"],
            "healthy": ["healthy", "fitness", "workout", "exercise", "active lifestyle"],
            
            # Misc
            "hungry": ["hungry", "starving", "want to eat", "foodie", "craving"],
            "free": ["free", "liberated", "carefree", "no worries", "weightless"],
            "emotional": ["emotional", "feelings", "deep", "intense", "raw"],
            "introspective": ["introspective", "self reflection", "soul searching", "thinking about life"]
        }
        
        for mood, keywords in mood_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return mood
        return None
    
    def get_empathy_response(self, mood):
        """Get varied empathetic responses based on mood"""
        empathy_map = {
            "stressed": [
                "I hear you. Let's find something to help you decompress.",
                "Stress is tough. I know just the thing to help you relax.",
                "You deserve a break. Let me find something calming for you.",
                "Take a breath. I've got some great options to help you unwind."
            ],
            "sad": [
                "I'm sorry you're feeling down. Let me brighten your day.",
                "Rough times don't last forever. Here's something to lift your spirits.",
                "Sending good vibes your way. Check out these mood boosters.",
                "Sometimes we all need a pick-me-up. I've got you covered."
            ],
            "excited": [
                "Love the energy! Let's put it to good use.",
                "That excitement is contagious! Here are some perfect matches.",
                "You're radiating good vibes! Check these out.",
                "Let's ride that wave of excitement!"
            ],
            "bored": [
                "Boredom ends now. Time to discover something amazing.",
                "Let's shake things up! Here are some exciting options.",
                "Say goodbye to boredom. These events will change that.",
                "Nothing to do? Not anymore. Check these out."
            ],
            "tired": [
                "Rest is important. Here are some low-key options for you.",
                "Sometimes you need to take it easy. These might be perfect.",
                "Feeling drained? These relaxing events could be just right.",
                "Let's find something that won't drain your battery further."
            ],
            "happy": [
                "Great to hear you're in good spirits! Let's keep it going.",
                "Happiness looks good on you. Here's more joy.",
                "Love that positive energy! Check out these events.",
                "Let's amplify those good vibes!"
            ],
            "curious": [
                "A curious mind is a beautiful thing. Let's explore.",
                "Ready to discover something new? Here you go.",
                "Curiosity leads to the best adventures. Check these out.",
                "Let's satisfy that curiosity with these options."
            ],
            "lonely": [
                "Connection is important. These events are great for meeting people.",
                "You're not alone. Here are some social events to check out.",
                "Let's find you some good company.",
                "These events are perfect for making new connections."
            ],
            "motivated": [
                "That drive will take you far! Channel it into these events.",
                "Motivation is powerful. Here's where you can put it to use.",
                "Love the determination! These events match your energy.",
                "Let's fuel that motivation with something great."
            ],
            "adventurous": [
                "Adventure awaits! Here are some thrilling options.",
                "Ready for something exciting? You're in the right place.",
                "Life's an adventure. Let's make it memorable.",
                "Your adventurous spirit will love these events."
            ],
            "romantic": [
                "Love is in the air. Here are some perfect date options.",
                "Looking for something special? These events are ideal.",
                "Romance awaits at these wonderful events.",
                "These events are perfect for creating memories together."
            ],
            "creative": [
                "Let's fuel that creativity! Check out these artistic events.",
                "Creative souls thrive at these events.",
                "Your artistic side will love these options.",
                "Time to let your creativity flow!"
            ],
            "peaceful": [
                "Seeking tranquility? These events offer just that.",
                "Inner peace is priceless. Here are some calming options.",
                "Let's maintain that peaceful state with these events.",
                "Serenity seekers unite! Check these out."
            ],
            "anxious": [
                "It's okay to feel anxious. These events might help ease your mind.",
                "Let's find something to help you feel more grounded.",
                "Anxiety is tough. Here are some calming options.",
                "Take it one step at a time. These might help."
            ],
            "nostalgic": [
                "Throwback vibes! These events will take you back.",
                "Nothing wrong with a trip down memory lane.",
                "Nostalgia hits different. Check out these classics.",
                "Let's relive some good times!"
            ],
            "social": [
                "Ready to mingle? These events are perfect for socializing.",
                "Let's get you out there! Great social events ahead.",
                "Connection time! Here are some community gatherings.",
                "These events are buzzing with great people."
            ],
            "competitive": [
                "Game on! These events will test your skills.",
                "Ready to compete? Check out these challenges.",
                "May the best win! Here are some competitive events.",
                "Your competitive spirit will thrive here."
            ],
            "playful": [
                "Let's have some fun! These events are all about good times.",
                "Playtime awaits! Check out these entertaining options.",
                "Fun is the name of the game. Here you go!",
                "Your playful side will love these events."
            ],
            "overwhelmed": [
                "One thing at a time. Let's start with something simple and enjoyable.",
                "When life gets heavy, a good event can help. Here are some options.",
                "Let's find something to help you recharge.",
                "You've got this. Here are some low-pressure options."
            ],
            "energetic": [
                "All that energy needs an outlet! Check these out.",
                "Let's burn some of that energy in the best way possible!",
                "High energy events coming right up!",
                "Your energy levels are perfect for these events!"
            ],
            "inspired": [
                "Inspiration is beautiful. Let's build on it!",
                "Feeling inspired? These events will fuel that fire.",
                "Let's turn that inspiration into action!",
                "Inspired minds create amazing things. Check these out."
            ]
        }
        
        responses = empathy_map.get(mood, [
            "I understand. Let me find the perfect events for you.",
            "Got it. Here are some events that might resonate with you.",
            "I hear you. Check out these options I found for you.",
            "Based on how you're feeling, these events could be great."
        ])
        
        return random.choice(responses)
    
    def get_events_by_mood(self, mood):
        """Get events that match the user's mood"""
        matching_events = []
        for event in EVENTS:
            if mood in event["mood"]:
                matching_events.append(event)
        
        if not matching_events:
            # Find closest match or return random selection
            matching_events = random.sample(EVENTS, min(5, len(EVENTS)))
        
        return matching_events[:6]  # Return up to 6 events
    
    def get_events_by_category(self, category):
        """Get events by category"""
        return [e for e in EVENTS if e["category"] == category]
    
    def extract_number(self, text):
        """Extract number from text"""
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        
        word_to_num = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
            "sixth": 6, "a": 1, "single": 1, "couple": 2, "few": 3, "pair": 2
        }
        
        for word, num in word_to_num.items():
            if word in text.lower():
                return num
        return None
    
    def extract_email(self, text):
        """Extract email from text"""
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        match = re.search(email_pattern, text)
        return match.group() if match else None
    
    def get_name_response(self, name):
        """Get varied response after learning name"""
        responses = [
            f"Nice to meet you, {name}.\n\nI have a unique feature - I recommend events based on your current mood.",
            f"Great to have you here, {name}.\n\nHere's the cool part - I match events to how you're feeling.",
            f"Welcome, {name}.\n\nI'm not your typical ticketing bot. I find events that match your vibe.",
            f"Hey {name}, glad you're here.\n\nMy specialty? Finding events that fit your mood perfectly."
        ]
        return random.choice(responses)
    
    def get_mood_prompt(self):
        """Get varied mood prompt"""
        prompts = [
            "\n\nSo, how are you feeling today?\n(Examples: excited, stressed, adventurous, creative, bored, happy...)",
            "\n\nWhat's your vibe right now?\n(Try: relaxed, motivated, curious, playful, tired, energetic...)",
            "\n\nTell me about your mood today.\n(Like: peaceful, ambitious, social, nostalgic, romantic...)",
            "\n\nHow would you describe your current mood?\n(Such as: happy, anxious, inspired, lonely, competitive...)"
        ]
        return random.choice(prompts)
    
    def get_selection_response(self, event):
        """Get varied response for event selection"""
        responses = [
            f"Excellent choice.\n\n",
            f"Great pick!\n\n",
            f"You've got good taste.\n\n",
            f"Solid choice.\n\n",
            f"Nice one!\n\n"
        ]
        return random.choice(responses)
    
    def get_ticket_confirmation_intro(self, num, event_name):
        """Get varied ticket confirmation intro"""
        responses = [
            f"Got it. {num} ticket(s) for {event_name}.",
            f"Perfect. {num} ticket(s) coming right up for {event_name}.",
            f"Noted. {num} ticket(s) to {event_name}.",
            f"Awesome. {num} ticket(s) for {event_name} it is."
        ]
        return random.choice(responses)
    
    def get_booking_complete_message(self):
        """Get varied booking complete message"""
        messages = [
            "Your QR code ticket has been generated.\nShow it at the venue entrance.",
            "Your digital ticket with QR code is ready.\nJust scan it at the door.",
            "Ticket generated successfully.\nYour QR code is your entry pass.",
            "All set! Your QR ticket is ready.\nPresent it when you arrive."
        ]
        return random.choice(messages)
    
    def get_thank_you_message(self, name):
        """Get varied thank you message"""
        messages = [
            f"Thank you for using TicketBot, {name}.\n\nEnjoy your event!",
            f"Thanks for choosing TicketBot, {name}.\n\nHave a fantastic time!",
            f"Appreciate you using TicketBot, {name}.\n\nHope you have a blast!",
            f"Thanks, {name}! You're all set.\n\nEnjoy and see you next time!"
        ]
        return random.choice(messages)
    
    def get_another_event_prompt(self):
        """Get varied prompt for booking another event"""
        prompts = [
            "Would you like to book another event? (yes/no)",
            "Interested in exploring more events? (yes/no)",
            "Want to discover another event? (yes/no)",
            "Feel like booking something else? (yes/no)"
        ]
        return random.choice(prompts)
    
    def process_message(self, user_input):
        """Process user message and return bot response"""
        user_input = user_input.strip()
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = ""
        
        if self.state == "greeting":
            self.user_data["name"] = user_input.split()[0].title() if user_input else "Friend"
            response = self.get_name_response(self.user_data["name"])
            response += self.get_mood_prompt()
            self.state = "mood_check"
            
        elif self.state == "mood_check":
            detected_mood = self.detect_mood(user_input)
            
            if detected_mood:
                self.user_data["mood"] = detected_mood
                response = f"I sense you're feeling {detected_mood}. "
                response += self.get_empathy_response(detected_mood)
                
                matching_events = self.get_events_by_mood(detected_mood)
                self.current_events = matching_events
                
                response += f"\n\nBased on your mood, here are my recommendations:\n\n"
                for i, event in enumerate(matching_events, 1):
                    response += f"{i}. {event['name']}\n"
                    response += f"   {event['date']} at {event['time']}\n"
                    response += f"   {event['venue']}\n"
                    response += f"   ${event['price']:.2f} | {event['available_seats']} seats\n\n"
                
                response += "Which event interests you? (Enter the number)"
                self.state = "event_selection"
            else:
                response = "Hmm, I couldn't quite pin down your mood from that.\n"
                response += "No worries though! Here are all our available events:\n\n"
                self.current_events = EVENTS[:8]
                for i, event in enumerate(self.current_events, 1):
                    response += f"{i}. {event['name']}\n"
                    response += f"   {event['date']} | ${event['price']:.2f}\n\n"
                response += "Which one catches your interest? (Enter the number)"
                self.state = "event_selection"
                
        elif self.state == "event_selection":
            num = self.extract_number(user_input)
            
            if num and 1 <= num <= len(self.current_events):
                selected = self.current_events[num - 1]
                self.user_data["selected_event"] = selected
                
                response = self.get_selection_response(selected)
                response += f"--- {selected['name']} ---\n\n"
                response += f"{selected['description']}\n\n"
                response += f"Date: {selected['date']}\n"
                response += f"Time: {selected['time']}\n"
                response += f"Venue: {selected['venue']}\n"
                response += f"Price: ${selected['price']:.2f} per ticket\n\n"
                response += "How many tickets would you like? (1-10)"
                self.state = "ticket_count"
            else:
                response = f"Please enter a valid number between 1 and {len(self.current_events)}."
                
        elif self.state == "ticket_count":
            num = self.extract_number(user_input)
            event = self.user_data["selected_event"]
            
            if num and 1 <= num <= 10:
                if num <= event["available_seats"]:
                    self.user_data["num_tickets"] = num
                    total = num * event["price"]
                    
                    response = self.get_ticket_confirmation_intro(num, event['name'])
                    response += f"\n\nTotal: ${total:.2f}\n\n"
                    response += "Please enter your email address to receive your tickets:"
                    self.state = "email_collection"
                else:
                    response = f"Unfortunately, only {event['available_seats']} seats are left.\n"
                    response += "Please enter a smaller number:"
            else:
                response = "Please enter a number between 1 and 10."
                
        elif self.state == "email_collection":
            email = self.extract_email(user_input)
            
            if email:
                self.user_data["email"] = email
                event = self.user_data["selected_event"]
                num_tickets = self.user_data["num_tickets"]
                total = num_tickets * event["price"]
                
                response = "--- BOOKING CONFIRMED ---\n\n"
                response += f"Event: {event['name']}\n"
                response += f"Name: {self.user_data['name']}\n"
                response += f"Email: {email}\n"
                response += f"Tickets: {num_tickets}\n"
                response += f"Date: {event['date']} at {event['time']}\n"
                response += f"Venue: {event['venue']}\n"
                response += f"Total: ${total:.2f}\n\n"
                response += self.get_booking_complete_message()
                response += f"\n\n{self.get_another_event_prompt()}"
                self.state = "booking_complete"
            else:
                invalid_responses = [
                    "That doesn't look like a valid email.\nPlease enter a valid email address (e.g., name@example.com):",
                    "Hmm, that email format doesn't look right.\nTry something like: yourname@email.com",
                    "I couldn't recognize that as an email.\nPlease use format: example@domain.com",
                    "That doesn't seem to be a valid email address.\nPlease try again:"
                ]
                response = random.choice(invalid_responses)
                
        elif self.state == "booking_complete":
            positive_words = ["yes", "yeah", "sure", "yep", "another", "more", "definitely", "absolutely", "yea", "ya", "ok", "okay"]
            if any(word in user_input.lower() for word in positive_words):
                continue_responses = [
                    f"Awesome, {self.user_data['name']}!",
                    f"Great, {self.user_data['name']}!",
                    f"Let's do it, {self.user_data['name']}!",
                    f"Excellent, {self.user_data['name']}!"
                ]
                response = random.choice(continue_responses)
                response += self.get_mood_prompt()
                self.state = "mood_check"
                self.user_data["selected_event"] = None
                self.user_data["num_tickets"] = 1
                self.user_data["email"] = None
            else:
                response = self.get_thank_you_message(self.user_data['name'])
                self.state = "ended"
                
        elif self.state == "ended":
            response = "Starting fresh...\n\n"
            self.reset()
            response += self.get_greeting()
            
        self.conversation_history.append({"role": "bot", "content": response})
        return response
    
    def get_booking_data(self):
        """Get current booking data for QR generation"""
        if self.user_data["selected_event"] and self.user_data["email"]:
            return {
                "name": self.user_data["name"],
                "email": self.user_data["email"],
                "event": self.user_data["selected_event"]["name"],
                "date": self.user_data["selected_event"]["date"],
                "time": self.user_data["selected_event"]["time"],
                "venue": self.user_data["selected_event"]["venue"],
                "tickets": self.user_data["num_tickets"],
                "total": self.user_data["num_tickets"] * self.user_data["selected_event"]["price"]
            }
        return None
