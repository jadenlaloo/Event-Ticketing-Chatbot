"""
Chatbot Engine - Handles conversation logic and NLP
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
    
    def get_greeting(self):
        """Return initial greeting message"""
        greetings = [
            "Hey there! 👋 I'm TicketBot, your friendly event assistant!",
            "Welcome! 🎉 I'm here to help you find amazing events!",
            "Hi! 🌟 Ready to discover some awesome events?"
        ]
        return random.choice(greetings) + "\n\nWhat's your name?"
    
    def detect_mood(self, text):
        """Detect mood from user input"""
        text_lower = text.lower()
        
        mood_keywords = {
            "excited": ["excited", "pumped", "thrilled", "can't wait", "hyped"],
            "happy": ["happy", "great", "good", "wonderful", "fantastic", "amazing"],
            "relaxed": ["relaxed", "chill", "calm", "peaceful", "easy"],
            "stressed": ["stressed", "anxious", "worried", "overwhelmed", "pressure"],
            "sad": ["sad", "down", "upset", "unhappy", "depressed", "low"],
            "bored": ["bored", "boring", "nothing to do", "dull"],
            "curious": ["curious", "interested", "wondering", "explore"],
            "motivated": ["motivated", "inspired", "driven", "ambitious"],
            "tired": ["tired", "exhausted", "sleepy", "drained", "fatigue"],
            "adventurous": ["adventurous", "adventure", "explore", "new things"],
            "romantic": ["romantic", "love", "date", "partner"],
            "playful": ["playful", "fun", "games", "play"],
            "creative": ["creative", "art", "create", "artistic"],
            "peaceful": ["peaceful", "zen", "tranquil", "serene"],
            "nostalgic": ["nostalgic", "memories", "old times", "remember"],
            "ambitious": ["ambitious", "goals", "success", "career"]
        }
        
        for mood, keywords in mood_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return mood
        return None
    
    def detect_category(self, text):
        """Detect event category preference from user input"""
        text_lower = text.lower()
        
        category_keywords = {
            "technology": ["tech", "technology", "ai", "coding", "software", "computer"],
            "music": ["music", "concert", "live", "band", "singing", "acoustic"],
            "business": ["business", "startup", "entrepreneur", "pitch", "networking"],
            "wellness": ["wellness", "meditation", "yoga", "mindfulness", "health"],
            "gaming": ["gaming", "games", "esports", "arcade", "video games"],
            "food": ["food", "eating", "cuisine", "foodie", "restaurant", "taste"],
            "art": ["art", "exhibition", "gallery", "creative", "painting"],
            "comedy": ["comedy", "funny", "laugh", "standup", "jokes"]
        }
        
        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return category
        return None
    
    def get_events_by_mood(self, mood):
        """Get events that match the user's mood"""
        matching_events = []
        for event in EVENTS:
            if mood in event["mood"]:
                matching_events.append(event)
        
        # If no exact match, return some random events
        if not matching_events:
            matching_events = random.sample(EVENTS, min(3, len(EVENTS)))
        
        return matching_events
    
    def get_events_by_category(self, category):
        """Get events by category"""
        return [e for e in EVENTS if e["category"] == category]
    
    def format_event_list(self, events):
        """Format events for display"""
        result = ""
        for i, event in enumerate(events, 1):
            result += f"\n**{i}. {event['name']}** 🎫\n"
            result += f"   📅 {event['date']} at {event['time']}\n"
            result += f"   📍 {event['venue']}\n"
            result += f"   💰 ${event['price']:.2f}\n"
            result += f"   💺 {event['available_seats']} seats available\n"
        return result
    
    def extract_number(self, text):
        """Extract number from text"""
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        
        word_to_num = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "first": 1, "second": 2,
            "third": 3, "fourth": 4, "fifth": 5
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
    
    def process_message(self, user_input):
        """Process user message and return bot response"""
        user_input = user_input.strip()
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = ""
        
        if self.state == "greeting":
            # Extract name from input
            self.user_data["name"] = user_input.split()[0].title() if user_input else "Friend"
            response = f"Nice to meet you, {self.user_data['name']}! 😊\n\n"
            response += "I have a special feature - I can recommend events based on your mood! 🎭\n\n"
            response += "**How are you feeling today?**\n"
            response += "(e.g., excited, relaxed, stressed, curious, adventurous...)"
            self.state = "mood_check"
            
        elif self.state == "mood_check":
            detected_mood = self.detect_mood(user_input)
            
            if detected_mood:
                self.user_data["mood"] = detected_mood
                response = f"I sense you're feeling **{detected_mood}**! "
                
                # Add empathetic response based on mood
                empathy_responses = {
                    "stressed": "Don't worry, I've got the perfect events to help you unwind! 🌈",
                    "sad": "Let's find something to lift your spirits! 💪",
                    "excited": "Love the energy! Let's channel that excitement! ⚡",
                    "bored": "Time to shake things up! 🎲",
                    "tired": "How about something relaxing and refreshing? 🍃",
                    "happy": "Great vibes! Let's keep them going! 🎉"
                }
                response += empathy_responses.get(detected_mood, "Let me find the perfect events for you! ✨")
                
                matching_events = self.get_events_by_mood(detected_mood)
                self.current_events = matching_events
                
                response += f"\n\nBased on your mood, here are my top picks:"
                response += self.format_event_list(matching_events)
                response += "\n\n**Which event interests you?** (Enter the number)"
                self.state = "event_selection"
            else:
                response = "I couldn't quite catch your mood. 🤔\n"
                response += "No worries! Let me show you all our awesome events:\n"
                self.current_events = EVENTS
                response += self.format_event_list(EVENTS)
                response += "\n\n**Which event catches your eye?** (Enter the number)"
                self.state = "event_selection"
                
        elif self.state == "event_selection":
            num = self.extract_number(user_input)
            
            if num and 1 <= num <= len(self.current_events):
                selected = self.current_events[num - 1]
                self.user_data["selected_event"] = selected
                
                response = f"Excellent choice! 🎯\n\n"
                response += f"**{selected['name']}**\n"
                response += f"_{selected['description']}_\n\n"
                response += f"📅 Date: {selected['date']}\n"
                response += f"⏰ Time: {selected['time']}\n"
                response += f"📍 Venue: {selected['venue']}\n"
                response += f"💰 Price: ${selected['price']:.2f} per ticket\n\n"
                response += "**How many tickets would you like?** (1-10)"
                self.state = "ticket_count"
            else:
                response = f"Please enter a number between 1 and {len(self.current_events)}! 🔢"
                
        elif self.state == "ticket_count":
            num = self.extract_number(user_input)
            event = self.user_data["selected_event"]
            
            if num and 1 <= num <= 10:
                if num <= event["available_seats"]:
                    self.user_data["num_tickets"] = num
                    total = num * event["price"]
                    
                    response = f"Perfect! {num} ticket(s) for **{event['name']}**\n\n"
                    response += f"💵 **Total: ${total:.2f}**\n\n"
                    response += "Please enter your **email address** to receive your tickets:"
                    self.state = "email_collection"
                else:
                    response = f"Sorry, only {event['available_seats']} seats available! 😅\n"
                    response += "Please enter a smaller number:"
            else:
                response = "Please enter a number between 1 and 10! 🎫"
                
        elif self.state == "email_collection":
            email = self.extract_email(user_input)
            
            if email:
                self.user_data["email"] = email
                event = self.user_data["selected_event"]
                num_tickets = self.user_data["num_tickets"]
                total = num_tickets * event["price"]
                
                response = f"🎉 **BOOKING CONFIRMED!** 🎉\n\n"
                response += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                response += f"**{event['name']}**\n"
                response += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                response += f"👤 Name: {self.user_data['name']}\n"
                response += f"📧 Email: {email}\n"
                response += f"🎫 Tickets: {num_tickets}\n"
                response += f"📅 Date: {event['date']} at {event['time']}\n"
                response += f"📍 Venue: {event['venue']}\n"
                response += f"💰 Total Paid: ${total:.2f}\n"
                response += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                response += "✅ Your **QR Code ticket** has been generated!\n"
                response += "📱 Show this at the venue entrance.\n\n"
                response += "_Thank you for booking with TicketBot!_ 🙏\n\n"
                response += "**Would you like to book another event?** (yes/no)"
                self.state = "booking_complete"
            else:
                response = "That doesn't look like a valid email. 📧\n"
                response += "Please enter a valid email address (e.g., name@example.com):"
                
        elif self.state == "booking_complete":
            if any(word in user_input.lower() for word in ["yes", "yeah", "sure", "yep", "another"]):
                response = f"Awesome, {self.user_data['name']}! 🎉\n\n"
                response += "**How are you feeling now?** Let me find more events for you!"
                self.state = "mood_check"
                self.user_data["selected_event"] = None
                self.user_data["num_tickets"] = 1
                self.user_data["email"] = None
            else:
                response = f"Thanks for using TicketBot, {self.user_data['name']}! 👋\n\n"
                response += "Have an amazing time at your event! 🎊\n"
                response += "See you next time! 😊"
                self.state = "ended"
                
        elif self.state == "ended":
            response = "Starting a new conversation...\n\n"
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
