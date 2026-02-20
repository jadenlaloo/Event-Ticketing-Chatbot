"""
Chatbot Engine - Powered by Groq AI
Uses Llama model for natural conversations with mood-based event recommendations
"""

import re
import os
import json
from groq import Groq
from events_data import EVENTS, MOODS, CATEGORIES

# Try to import streamlit for secrets (deployment)
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False

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
        self.groq_client = None
        self._init_groq()
        
    def _init_groq(self):
        """Initialize Groq client"""
        # Try Streamlit secrets first (for deployment), then environment variable
        api_key = None
        if HAS_STREAMLIT:
            try:
                api_key = st.secrets.get("GROQ_API_KEY")
            except:
                pass
        
        if not api_key:
            api_key = os.environ.get("GROQ_API_KEY")
            
        if api_key:
            self.groq_client = Groq(api_key=api_key)
        else:
            print("Warning: GROQ_API_KEY not found. Using fallback responses.")
    
    def _get_system_prompt(self):
        """Get the system prompt for the AI"""
        events_info = json.dumps([{
            "id": e["id"],
            "name": e["name"],
            "category": e["category"],
            "mood": e["mood"],
            "date": e["date"],
            "time": e["time"],
            "venue": e["venue"],
            "price": e["price"],
            "available_seats": e["available_seats"],
            "description": e["description"]
        } for e in EVENTS], indent=2)
        
        return f"""You are TicketBot, a friendly and helpful event ticketing assistant with a retro minimalist personality. Your responses should be:
- Concise but warm (2-4 sentences typically)
- No emojis ever
- Natural and conversational
- Empathetic to the user's mood

You help users discover events based on their mood and book tickets. Here are the available events:
{events_info}

Current conversation state: {self.state}
User data collected so far: {json.dumps(self.user_data)}
Current events being shown: {json.dumps([e["name"] for e in self.current_events]) if self.current_events else "None"}

IMPORTANT RULES:
1. In "greeting" state: Greet the user and ask for their name. Be warm and introduce yourself as TicketBot.
2. In "mood_check" state: Ask about their mood/feelings in a natural way. Acknowledge their name.
3. In "event_selection" state: After detecting mood, show empathy and recommend events from the list that match their mood. List them with numbers.
4. In "ticket_count" state: Confirm their event choice and ask how many tickets (1-10).
5. In "email_collection" state: Confirm ticket count and ask for email address.
6. In "booking_complete" state: Confirm the booking with all details and ask if they want another event.
7. In "ended" state: Thank them warmly.

When recommending events, ONLY recommend events from the provided list. Include the number, name, date, time, venue, and price.

Keep responses SHORT - no more than 4-5 lines unless listing events."""
    
    def _call_groq(self, user_message):
        """Call Groq API for a response with timeout"""
        if not self.groq_client:
            return None
            
        messages = [
            {"role": "system", "content": self._get_system_prompt()}
        ]
        
        # Add conversation history (last 10 messages)
        for msg in self.conversation_history[-10:]:
            messages.append({
                "role": "user" if msg["role"] == "user" else "assistant",
                "content": msg["content"]
            })
        
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = self.groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=0.7,
                max_tokens=400,
                timeout=10  # 10 second timeout
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e).lower()
            # Handle rate limit gracefully
            if "rate_limit" in error_str or "429" in error_str:
                print(f"API rate limit hit. Please wait a moment and try again.")
            else:
                print(f"Groq API error: {e}")
            return None
    
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
        """Return initial greeting message"""
        response = self._call_groq("Generate a warm, concise greeting introducing yourself as TicketBot. Ask for the user's name. Keep it to 2-3 sentences max. No emojis.")
        if response:
            return response
        
        # Emergency fallback if API fails
        return "Hello. I'm TicketBot.\n\nI help you discover events based on how you're feeling. What's your name?"
    
    def detect_mood(self, text):
        """Detect mood from user input"""
        text_lower = text.lower()
        
        mood_keywords = {
            "excited": ["excited", "pumped", "thrilled", "can't wait", "hyped", "psyched", "stoked"],
            "happy": ["happy", "great", "good", "wonderful", "fantastic", "amazing", "awesome", "joyful"],
            "energetic": ["energetic", "energized", "active", "lively", "dynamic", "vibrant"],
            "relaxed": ["relaxed", "chill", "calm", "peaceful", "easy", "laid back", "mellow"],
            "stressed": ["stressed", "anxious", "worried", "overwhelmed", "pressure", "tense", "nervous"],
            "sad": ["sad", "down", "upset", "unhappy", "depressed", "low", "blue", "heartbroken"],
            "bored": ["bored", "boring", "nothing to do", "dull", "uninterested", "restless"],
            "tired": ["tired", "exhausted", "sleepy", "drained", "fatigue", "worn out", "burnt out"],
            "lonely": ["lonely", "alone", "isolated", "by myself", "need company"],
            "curious": ["curious", "interested", "wondering", "explore", "want to learn", "intrigued"],
            "creative": ["creative", "artistic", "artsy", "imaginative", "want to create"],
            "motivated": ["motivated", "driven", "determined", "focused", "goal oriented"],
            "adventurous": ["adventurous", "adventure", "explore", "new things", "try something new"],
            "romantic": ["romantic", "love", "date", "partner", "couple"],
            "social": ["social", "want to meet", "hang out", "make friends", "people", "party"],
            "nostalgic": ["nostalgic", "memories", "old times", "remember", "throwback", "retro"],
            "competitive": ["competitive", "want to win", "challenge", "beat", "compete"],
            "playful": ["playful", "fun", "games", "play", "silly"]
        }
        
        for mood, keywords in mood_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return mood
        return None
    
    def get_events_by_mood(self, mood):
        """Get events that match the user's mood"""
        matching_events = []
        for event in EVENTS:
            if mood in event["mood"]:
                matching_events.append(event)
        
        if not matching_events:
            import random
            matching_events = random.sample(EVENTS, min(5, len(EVENTS)))
        
        return matching_events[:6]
    
    def extract_number(self, text):
        """Extract number from text"""
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        
        word_to_num = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5,
            "a": 1, "single": 1, "couple": 2, "pair": 2
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
    
    def _format_events_list(self, events):
        """Format events list for display"""
        result = ""
        for i, event in enumerate(events, 1):
            result += f"{i}. {event['name']}\n"
            result += f"   {event['date']} at {event['time']}\n"
            result += f"   {event['venue']}\n"
            result += f"   ${event['price']:.2f} | {event['available_seats']} seats\n\n"
        return result
    
    def process_message(self, user_input):
        """Process user message and return bot response - All responses from Groq API"""
        user_input = user_input.strip()
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = ""
        
        if self.state == "greeting":
            self.user_data["name"] = user_input.split()[0].title() if user_input else "Friend"
            
            # Always use AI for response
            ai_prompt = f"The user said their name is '{user_input}'. Greet them warmly using their name ({self.user_data['name']}), then explain your unique mood-based event recommendation feature, and ask how they're feeling today. Keep it conversational and under 4 sentences. No emojis."
            response = self._call_groq(ai_prompt)
            
            if not response:  # Emergency fallback
                response = f"Nice to meet you, {self.user_data['name']}. I recommend events based on your mood. How are you feeling today?"
            
            self.state = "mood_check"
            
        elif self.state == "mood_check":
            detected_mood = self.detect_mood(user_input)
            
            if detected_mood:
                self.user_data["mood"] = detected_mood
                matching_events = self.get_events_by_mood(detected_mood)
                self.current_events = matching_events
                
                # Generate AI empathy response about the mood
                ai_prompt = f"The user is feeling {detected_mood}. Respond with empathy in 1-2 sentences, then say you'll show them matching events. Keep it natural and warm. No emojis."
                ai_empathy = self._call_groq(ai_prompt)
                
                if ai_empathy:
                    response = ai_empathy + "\n\n"
                else:
                    response = f"I sense you're feeling {detected_mood}. Here are some events that might be perfect:\n\n"
                
                response += self._format_events_list(matching_events)
                response += "Which event interests you? (Enter the number)"
                
                self.state = "event_selection"
            else:
                # Couldn't detect mood - ask AI to respond naturally
                ai_prompt = f"The user said '{user_input}' but I couldn't detect a specific mood. Respond warmly saying you'll show them popular events. Keep it to 1-2 sentences. No emojis."
                ai_response = self._call_groq(ai_prompt)
                
                self.current_events = EVENTS[:8]
                
                if ai_response:
                    response = ai_response + "\n\n"
                else:
                    response = "I'd love to help you find the perfect event!\n\n"
                
                response += self._format_events_list(self.current_events)
                response += "Which one catches your interest? (Enter the number)"
                self.state = "event_selection"
                
        elif self.state == "event_selection":
            num = self.extract_number(user_input)
            
            if num and 1 <= num <= len(self.current_events):
                selected = self.current_events[num - 1]
                self.user_data["selected_event"] = selected
                
                # AI confirms selection and shows details
                ai_prompt = f"The user selected event #{num}: {selected['name']}. Acknowledge their choice positively in 1 sentence, then present the event details below it. No emojis."
                ai_intro = self._call_groq(ai_prompt)
                
                if ai_intro:
                    response = ai_intro + "\n\n"
                else:
                    response = "Great choice!\n\n"
                
                response += f"--- {selected['name']} ---\n\n"
                response += f"{selected['description']}\n\n"
                response += f"Date: {selected['date']}\n"
                response += f"Time: {selected['time']}\n"
                response += f"Venue: {selected['venue']}\n"
                response += f"Price: ${selected['price']:.2f} per ticket\n\n"
                response += "How many tickets would you like? (1-10)"
                
                self.state = "ticket_count"
            else:
                # Invalid number - AI responds
                ai_prompt = f"The user entered '{user_input}' which isn't a valid event number (valid range: 1-{len(self.current_events)}). Ask them politely to enter a valid number. Keep it brief. No emojis."
                response = self._call_groq(ai_prompt)
                
                if not response:
                    response = f"Please enter a valid number between 1 and {len(self.current_events)}."
                
        elif self.state == "ticket_count":
            num = self.extract_number(user_input)
            event = self.user_data["selected_event"]
            
            if num and 1 <= num <= 10:
                if num <= event["available_seats"]:
                    self.user_data["num_tickets"] = num
                    total = num * event["price"]
                    
                    # AI confirms ticket count
                    ai_prompt = f"The user wants {num} ticket(s) for {event['name']} at ${event['price']:.2f} each (total ${total:.2f}). Confirm this briefly and ask for their email address. 2 sentences max. No emojis."
                    response = self._call_groq(ai_prompt)
                    
                    if not response:
                        response = f"Got it. {num} ticket(s) for {event['name']}.\nTotal: ${total:.2f}\n\nPlease enter your email address:"
                    
                    self.state = "email_collection"
                else:
                    # Not enough seats - AI responds
                    ai_prompt = f"Unfortunately only {event['available_seats']} seats are left, but the user requested {num}. Explain this politely and ask for a smaller number. Keep it brief. No emojis."
                    response = self._call_groq(ai_prompt)
                    
                    if not response:
                        response = f"Unfortunately, only {event['available_seats']} seats are left. Please enter a smaller number:"
            else:
                # Invalid number - AI responds
                ai_prompt = f"The user entered '{user_input}' which isn't a valid ticket count (must be 1-10). Ask them politely to enter a valid number. Keep it brief. No emojis."
                response = self._call_groq(ai_prompt)
                
                if not response:
                    response = "Please enter a number between 1 and 10."
                
        elif self.state == "email_collection":
            email = self.extract_email(user_input)
            
            if email:
                self.user_data["email"] = email
                event = self.user_data["selected_event"]
                num_tickets = self.user_data["num_tickets"]
                total = num_tickets * event["price"]
                
                # Structured confirmation (keep this as is for clarity)
                response = "--- BOOKING CONFIRMED ---\n\n"
                response += f"Event: {event['name']}\n"
                response += f"Name: {self.user_data['name']}\n"
                response += f"Email: {email}\n"
                response += f"Tickets: {num_tickets}\n"
                response += f"Date: {event['date']} at {event['time']}\n"
                response += f"Venue: {event['venue']}\n"
                response += f"Total: ${total:.2f}\n\n"
                response += "Your QR code ticket has been generated.\nShow it at the venue entrance.\n\n"
                response += "Would you like to book another event? (yes/no)"
                self.state = "booking_complete"
            else:
                # Invalid email - AI responds
                ai_prompt = f"The user entered '{user_input}' which doesn't look like a valid email address. Ask them politely to provide a valid email (like name@example.com). Keep it brief. No emojis."
                response = self._call_groq(ai_prompt)
                
                if not response:
                    response = "That doesn't look like a valid email. Please enter a valid email address (e.g., name@example.com):"
                
        elif self.state == "booking_complete":
            positive_words = ["yes", "yeah", "sure", "yep", "another", "more", "definitely", "ok", "okay"]
            if any(word in user_input.lower() for word in positive_words):
                # User wants another event - AI responds
                ai_prompt = f"The user ({self.user_data['name']}) wants to book another event. Respond enthusiastically and ask about their current mood. Keep it to 2 sentences. No emojis."
                response = self._call_groq(ai_prompt)
                
                if not response:
                    response = f"Awesome, {self.user_data['name']}! How are you feeling now?"
                
                self.state = "mood_check"
                self.user_data["selected_event"] = None
                self.user_data["num_tickets"] = 1
                self.user_data["email"] = None
            else:
                # User is done - AI says goodbye
                ai_prompt = f"The user ({self.user_data['name']}) is done booking. Say a warm, friendly goodbye and wish them well at their event. Keep it to 2 sentences max. No emojis."
                response = self._call_groq(ai_prompt)
                
                if not response:
                    response = f"Thank you for using TicketBot, {self.user_data['name']}. Enjoy your event!"
                
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
