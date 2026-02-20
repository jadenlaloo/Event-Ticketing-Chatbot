# TicketBot - AI-Powered Event Ticketing Chatbot

An intelligent conversational chatbot for seamless event discovery and ticket booking with mood-based recommendations.

Built for GenAI for GenZ Competition by Intel

---

## Features

### Mood-Based Event Recommendations
Unlike traditional ticketing platforms, TicketBot understands how you're feeling and recommends events that match your mood. Feeling stressed? It suggests relaxing wellness events. Excited? It finds high-energy concerts and tech summits.

### Natural Conversational Interface
No more clicking through endless menus. Simply chat with TicketBot like you would with a friend, and book your tickets through a natural conversation flow.

### Instant QR Code Tickets
Every booking generates a unique QR code ticket that can be downloaded and shown at the venue entrance. No need to wait for email confirmations.

### Retro Minimalist Design
A clean, distraction-free interface inspired by classic computing aesthetics. Black and white design with window-style cards for a unique visual experience.

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/jadenlaloo/Event-Ticketing-Chatbot.git
cd Event-Ticketing-Chatbot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run app.py
```

4. Open in browser at `http://localhost:8501`

---

## How It Works

```
User Interaction Flow
---------------------
1. User starts conversation
2. TicketBot asks about mood
3. NLP engine detects mood keywords
4. Matching events are recommended
5. User selects event and ticket quantity
6. QR Code ticket is generated instantly
```

### Conversation States

| State | Description |
|-------|-------------|
| Greeting | Bot introduces itself and asks for name |
| Mood Detection | Bot asks how user is feeling |
| Event Selection | Events matching mood are displayed |
| Ticket Count | User specifies number of tickets |
| Email Collection | User provides email for ticket |
| Booking Complete | QR code ticket is generated |

---

## Project Structure

```
Event-Ticketing-Chatbot/
|
|-- app.py                 # Main Streamlit application
|-- chatbot_engine.py      # NLP-based conversation handler
|-- ticket_generator.py    # QR code ticket generator
|-- events_data.py         # Sample events database
|-- requirements.txt       # Python dependencies
|-- README.md              # Project documentation
```

---

## Novelty Factor

What makes TicketBot unique:

| Feature | Traditional Platforms | TicketBot |
|---------|----------------------|-----------|
| Event Discovery | Category filters | Mood-based AI recommendations |
| Booking Process | Multi-page forms | Single conversation |
| Ticket Delivery | Email (delayed) | Instant QR generation |
| User Experience | Transactional | Personal and empathetic |

---

## Tech Stack

- Frontend: Streamlit (Python web framework)
- NLP Engine: Custom keyword-based mood detection
- QR Generation: qrcode + Pillow libraries
- Design: Custom CSS with retro minimalist theme
- Icons: Phosphor Icons

---

## Sample Events

The chatbot includes 8 sample events across categories:
- Technology (Tech Summit)
- Music (Acoustic Nights)
- Business (Startup Pitch Night)
- Wellness (Mindfulness Retreat)
- Gaming (Retro Gaming Championship)
- Food (Street Food Festival)
- Art (AI Art Exhibition)
- Comedy (Comedy Night Live)

---

## Future Enhancements

- Integration with real payment gateways
- Email/SMS ticket delivery
- Multi-language support
- Voice input capability
- Integration with calendar apps
- Social sharing features

---

## Author

Built for GenAI for GenZ Competition by Intel

---

## License

This project is licensed under the MIT License.

---

Made with care for the GenAI for GenZ Competition | Intel | 2026
