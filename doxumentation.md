# Event Ticketing Chatbot Documentation

**A GenAI for GenZ Competition Project by Intel**

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Installation & Setup](#installation--setup)
5. [Configuration](#configuration)
6. [File Structure](#file-structure)
7. [API Integrations](#api-integrations)
8. [Usage Guide](#usage-guide)
9. [Development](#development)
10. [Troubleshooting](#troubleshooting)

---

## Project Overview

The **Event Ticketing Chatbot** is an intelligent conversational AI application built with Streamlit that helps users discover and book event tickets based on their mood and preferences. Using advanced AI from Groq and image optimization from ScaleDown, the application provides a seamless, modern ticketing experience with a retro minimalist design aesthetic.

### Key Highlights

- 🤖 **AI-Powered Conversations** - Uses Groq's Llama 3.1 model for natural, context-aware responses
- 🎫 **Smart Ticket Generation** - Creates QR code tickets with automatic image optimization
- 😊 **Mood-Based Recommendations** - Suggests events based on user's current emotional state
- 🎨 **Retro Minimalist UI** - Beautiful, responsive design with a nostalgic aesthetic
- ⚡ **Fast & Lightweight** - Background optimizations ensure smooth user experience

---

## Features

### Core Features

1. **Conversational Ticketing**
   - Natural language chat interface
   - Multi-turn conversations with state management
   - Emotion detection from text input

2. **Event Discovery**
   - 20+ pre-loaded events across multiple categories
   - Mood-matched recommendations
   - Events span different genres: concerts, sports, theater, comedy, etc.

3. **Ticket Management**
   - Unique ticket ID generation via MD5 hashing
   - QR code generation for entry verification
   - Multi-ticket booking support (1-10 tickets)
   - Email confirmation required

4. **Image Optimization**
   - ScaleDown API integration for automatic compression
   - Background optimization (non-blocking)
   - Graceful fallback on API failure

5. **State Management**
   - Conversation history tracking
   - Multi-stage booking flow
   - Session persistence

### Conversation States

The chatbot progresses through these states:

- **greeting** - Initial greeting, collect user's name
- **mood_check** - Ask about user's emotional state
- **event_selection** - Show mood-matched events
- **ticket_count** - Ask number of tickets needed
- **email_collection** - Collect email address
- **booking_complete** - Show confirmation & QR code
- **ended** - Thank user and offer to restart

---

## Architecture

### System Components

```
┌─────────────────────────────────────────┐
│        Streamlit Frontend (UI)          │
│     - Chat interface                    │
│     - Event display                     │
│     - QR code visualization             │
└────────────┬────────────────────────────┘
             │
┌────────────▼────────────────────────────┐
│      Application Layer (app.py)         │
│     - Session management                │
│     - Message routing                   │
│     - File downloads                    │
└────────────┬────────────────────────────┘
             │
      ┌──────┴──────┬──────────┬──────────┐
      │             │          │          │
      ▼             ▼          ▼          ▼
┌──────────┐  ┌──────────┐ ┌────────┐ ┌─────────┐
│ Chatbot  │  │ Ticket   │ │Events  │ │Groq API │
│ Engine   │  │Generator │ │Data    │ │(Llama)  │
└──────────┘  └──────────┘ └────────┘ └─────────┘
      │             │
      │             ▼
      │        ┌─────────────────┐
      │        │ScaleDown API    │
      │        │(Image Optim.)   │
      │        └─────────────────┘
      │
      ▼
┌──────────────────┐
│Conversation      │
│History & State   │
└──────────────────┘
```

### Technology Stack

- **Frontend Framework**: Streamlit
- **AI Model**: Groq (Llama 3.1 8B Instant)
- **Image Processing**: Pillow, QRcode
- **Image Optimization**: ScaleDown API
- **Python Version**: 3.10+
- **Request Handling**: Requests library

---

## Installation & Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Groq API Key (free from https://console.groq.com)
- ScaleDown API Key (free from https://scaledown.io)

### Step 1: Clone the Repository

```bash
git clone https://github.com/jadenlaloo/Event-Ticketing-Chatbot.git
cd Event-Ticketing-Chatbot
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
SCALEDOWN_API_KEY = "your_scaledown_api_key_here"
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

---

## Configuration

### API Keys

Store API keys in one of these ways:

1. **`.streamlit/secrets.toml`** (recommended for development)
   ```toml
   GROQ_API_KEY = "gsk_..."
   SCALEDOWN_API_KEY = "your_key..."
   ```

2. **Environment Variables**
   ```bash
   # Windows
   set GROQ_API_KEY=gsk_...
   set SCALEDOWN_API_KEY=...

   # macOS/Linux
   export GROQ_API_KEY=gsk_...
   export SCALEDOWN_API_KEY=...
   ```

### Streamlit Configuration

The app uses a custom CSS theme. Modify styling in `app.py` lines 22-656 for UI customization.

### Event Data

Modify `events_data.py` to add or change available events. Each event requires:

```python
{
    "id": 1,
    "name": "Event Name",
    "category": "Category",
    "mood": ["happy", "excited"],  # List of matching moods
    "date": "2026-03-15",
    "time": "19:00",
    "venue": "Venue Name",
    "price": 49.99,
    "available_seats": 100,
    "description": "Event description"
}
```

---

## File Structure

```
Even Ticketing Chatbot/
├── app.py                      # Main Streamlit application
├── chatbot_engine.py           # AI conversation logic & state management
├── ticket_generator.py         # QR code & ticket image generation
├── events_data.py              # Event database & mood mappings
├── requirements.txt            # Python dependencies
├── doxumentation.md            # This file
├── README.md                   # Quick start guide
├── .gitignore                  # Git ignore rules
├── .streamlit/
│   └── secrets.toml            # API keys (NOT committed)
├── icons new/                  # Decorative SVG icons
└── __pycache__/                # Python cache (ignored)
```

---

## API Integrations

### Groq API

**Purpose**: Generate natural, context-aware conversational responses

**Configuration**:
- Model: `llama-3.1-8b-instant`
- Temperature: 0.7 (balanced creativity)
- Max Tokens: 400 per response
- Timeout: 10 seconds

**Usage in Code**:
```python
response = self.groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages,
    temperature=0.7,
    max_tokens=400,
    timeout=10
)
```

**Rate Limits**: 
- Free tier: 6,000 tokens/minute
- Dev tier: Higher limits available

**Error Handling**: 
- Graceful fallback to templated responses on rate limit
- Automatic retry logic with clear error messages

### ScaleDown API

**Purpose**: Optimize ticket images for better performance and file size

**Configuration**:
- Runs in background threads (non-blocking)
- Timeout: 5 seconds per image
- Supports PNG format optimization

**Usage in Code**:
```python
def optimize_image_with_scaledown(image_bytes):
    response = requests.post(
        'https://api.scaledown.io/v1/optimize',
        files={'image': ('ticket.png', image_bytes, 'image/png')},
        headers={'X-API-Key': api_key},
        timeout=5
    )
```

**Features**:
- Silent failures (doesn't interrupt user experience)
- Thread-based optimization
- Automatic fallback to original image

---

## Usage Guide

### For Users

1. **Start the Chat**
   - Open the app and greet TicketBot
   - Tell it your name

2. **Describe Your Mood**
   - Share how you're feeling
   - Use natural language (e.g., "I'm really excited!", "feeling stressed")

3. **Browse Events**
   - View mood-matched recommendations
   - Select an event by entering its number

4. **Complete Booking**
   - Choose number of tickets (1-10)
   - Provide email address
   - Download your QR code ticket

5. **Use Your Ticket**
   - Show QR code at venue entrance
   - Download full ticket PNG for backup

### For Developers

#### Adding a New Event

Edit `events_data.py`:

```python
EVENTS = [
    # ... existing events ...
    {
        "id": 21,
        "name": "Summer Music Festival",
        "category": "Music",
        "mood": ["happy", "excited", "energetic"],
        "date": "2026-07-12",
        "time": "18:00",
        "venue": "Central Park",
        "price": 75.00,
        "available_seats": 500,
        "description": "Three-day music festival featuring indie and pop artists"
    }
]
```

#### Customizing AI Behavior

Edit `chatbot_engine.py` `_get_system_prompt()` method to adjust:
- Tone and personality
- Response length
- Recommendation strategy
- Conversation rules

#### Modifying UI Theme

Edit `app.py` CSS section (lines 22-200+) to customize:
- Colors and backgrounds
- Fonts and sizes
- Component styling
- Animations

---

## Development

### Running Locally

```bash
# Install in development mode with update-ability
pip install -e .

# Run with auto-reload
streamlit run app.py --logger.level=debug
```

### Making Changes

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Edit relevant files
   - Test thoroughly locally

3. **Commit Changes**
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### Testing Checklist

- [ ] Greetings and initial interaction
- [ ] Mood detection across different inputs
- [ ] Event recommendation accuracy
- [ ] Ticket booking flow (all 6 states)
- [ ] QR code generation
- [ ] Email validation
- [ ] Multiple ticket selection
- [ ] Error handling (API failures)
- [ ] UI responsiveness

---

## Troubleshooting

### Streamlit Not Running

**Issue**: Port 8501 in use or connection refused

**Solution**:
```bash
# Kill existing Python processes
Get-Process python | Stop-Process -Force

# Or use different port
streamlit run app.py --server.port 8502
```

### Groq API Errors

**Issue**: "Rate limit exceeded" message

**Solution**:
- Free tier has 6,000 tokens/minute limit
- Wait 30 seconds before next message
- Upgrade to Dev tier for higher limits
- Check API key in `.streamlit/secrets.toml`

**Issue**: "GROQ_API_KEY not found"

**Solution**:
1. Verify `.streamlit/secrets.toml` exists
2. Check API key value is correct
3. Restart Streamlit after adding key
4. Try setting as environment variable as backup

### ScaleDown API Issues

**Issue**: Image optimization fails

**Solution**:
- App automatically falls back to original image
- No user-facing impact (graceful degradation)
- Check `.streamlit/secrets.toml` for correct key
- Verify internet connection

### QR Code Not Displaying

**Issue**: QR code appears blank or broken

**Solution**:
- Ensure booking data is complete
- Check email was provided
- Verify ticket_generator.py is not corrupted
- Try refreshing page

### Chat History Not Persisting

**Issue**: Messages disappear on page refresh

**Solution**:
- This is expected behavior (Streamlit resets on refresh)
- To persist, implement database backend
- Current implementation stores in `st.session_state`

---

## Deployment

### Streamlit Cloud

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy with GitHub connection
4. Add secrets in "Manage secrets" section
5. Set URL for production

### Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t ticketbot .
docker run -p 8501:8501 ticketbot
```

---

## Performance Optimization Tips

1. **Cache Conversation History**: Limit to last 10 messages (already implemented)
2. **Lazy Load Events**: Events are loaded once on startup
3. **Background Image Optimization**: ScaleDown optimization runs in threads
4. **API Timeouts**: All API calls have 5-10 second timeouts
5. **Error Handling**: Silent failures with fallbacks prevent app crashes

---

## Future Enhancements

- [ ] Database integration for persistent booking history
- [ ] Payment integration (Stripe, PayPal)
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Mobile app version
- [ ] Calendar integration
- [ ] Email confirmation system
- [ ] Recommendations based on past bookings
- [ ] User accounts and profiles
- [ ] Integration with actual ticketing systems (Ticketmaster, etc.)

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## License

This project is part of the GenAI for GenZ Competition by Intel.

---

## Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review error messages carefully

---

## Changelog

### Version 1.0.0 (Current)
- ✅ Initial release with Groq AI integration
- ✅ ScaleDown API for image optimization
- ✅ Complete ticket booking flow
- ✅ QR code generation
- ✅ Mood-based event recommendations
- ✅ Retro minimalist UI design

---

**Last Updated**: February 20, 2026
**Project Status**: Active Development
**Maintainer**: Jaden Laloo

