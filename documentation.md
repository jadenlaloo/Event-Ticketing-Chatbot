# Event Ticketing Chatbot - Complete Documentation

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Project Structure](#project-structure)
7. [Usage Guide](#usage-guide)
8. [API Integrations](#api-integrations)
9. [Development](#development)
10. [Deployment](#deployment)
11. [Troubleshooting](#troubleshooting)

---

## Project Overview

Event Ticketing Chatbot is a GenAI-powered ticket booking application built for the GenAI for GenZ Competition by Intel. The application uses conversational AI to help users discover events based on their mood and seamlessly book tickets with QR code generation.

The chatbot provides a retro minimalist design with an intuitive conversational interface that guides users through the entire ticketing process from mood-based event discovery to ticket confirmation and download.

**Key Capabilities:**
- Conversational mood-based event recommendations
- Intelligent ticket booking flow
- QR code ticket generation
- Image optimization for performance
- Real-time streaming chat interface

---

## Features

### Core Features

1. **Mood-Based Event Discovery**
   - Natural language mood detection
   - AI-powered event recommendations based on user emotions
   - Support for diverse emotional states (excited, relaxed, stressed, adventurous, etc.)

2. **Conversational Ticket Booking**
   - Multi-step guided booking process
   - Natural language understanding
   - Flexible input validation
   - Session state management

3. **QR Code Ticket Generation**
   - Unique ticket IDs per booking
   - QR code embedding on tickets
   - Retro-styled ticket design with event details
   - PNG format for easy distribution

4. **Image Optimization**
   - Background image compression using ScaleDown API
   - Non-blocking optimization (doesn't affect user experience)
   - Automatic fallback to original images if optimization fails

5. **Retro Minimalist Design**
   - Grid background pattern
   - Window-style cards with title bars
   - Space Grotesk and Space Mono typography
   - Streamlit-based responsive UI

---

## Tech Stack

### Backend
- **Python 3.14+**
- **Streamlit** - Web application framework
- **Groq API** - AI/LLM integration (Llama 3.1 8B Instant model)
- **Pillow** - Image generation and manipulation
- **qrcode** - QR code generation
- **python-dateutil** - Date/time utilities
- **requests** - HTTP client for API calls

### Frontend
- **Streamlit** - Full-stack web framework
- **HTML/CSS** - Custom styling via Streamlit markdown
- **Phosphor Icons** - Icon library

### External APIs
- **Groq API** - Generative AI for conversational responses
- **ScaleDown API** - Image optimization and compression

### Version Control
- **Git** - Source code management
- **GitHub** - Remote repository hosting

---

## Installation

### Prerequisites
- Python 3.10 or higher
- Git
- API keys for Groq and ScaleDown (free tiers available)

### Step 1: Clone Repository
```bash
git clone https://github.com/jadenlaloo/Event-Ticketing-Chatbot.git
cd "Event Ticketing Chatbot"
```

### Step 2: Create Python Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys (See Configuration section)

### Step 5: Run Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your default browser.

---

## Configuration

### API Keys Setup

#### Option 1: Streamlit Secrets (Recommended for Streamlit Cloud)

Create `.streamlit/secrets.toml` in the project root:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
SCALEDOWN_API_KEY = "your_scaledown_api_key_here"
```

The `.streamlit/secrets.toml` file is in `.gitignore` and will not be committed to version control.

#### Option 2: Environment Variables

Set environment variables on your system:

```bash
# Windows PowerShell
$env:GROQ_API_KEY = "your_groq_api_key_here"
$env:SCALEDOWN_API_KEY = "your_scaledown_api_key_here"

# macOS/Linux
export GROQ_API_KEY="your_groq_api_key_here"
export SCALEDOWN_API_KEY="your_scaledown_api_key_here"
```

### Getting API Keys

**Groq API:**
1. Visit https://console.groq.com
2. Sign up for a free account
3. Create an API key in the API Keys section
4. Free tier includes 6000 tokens per minute

**ScaleDown API:**
1. Visit https://scaledown.io
2. Sign up for a free account
3. Generate an API key
4. Used for background image optimization

---

## Project Structure

```
Event Ticketing Chatbot/
├── app.py                          # Main Streamlit application
├── chatbot_engine.py               # Chatbot logic and AI integration
├── events_data.py                  # Event data and mood mappings
├── ticket_generator.py             # QR code and ticket image generation
├── documentation.md                # This file
├── README.md                       # Quick start guide
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── .streamlit/
│   └── secrets.toml               # API keys (not committed)
├── icons new/                      # Retro icon assets
└── __pycache__/                    # Python cache (not committed)
```

### File Descriptions

#### app.py
Main Streamlit application file containing:
- Page configuration and theming
- Custom CSS for retro minimalist design
- Chat interface components
- Message history management
- QR code and ticket display

#### chatbot_engine.py
Core chatbot logic including:
- `ChatbotEngine` class - Main chatbot orchestrator
- Groq API integration and error handling
- Mood detection from natural language
- Multi-step conversation state machine
- Event recommendations based on mood
- Booking data management

#### events_data.py
Static event data and mood mappings:
- Event database with details (date, time, venue, price, etc.)
- Mood-to-event mapping for recommendations
- Category definitions
- Sample event data

#### ticket_generator.py
Ticket processing with:
- QR code generation using event details
- Ticket image creation with event information
- ScaleDown API integration for image optimization
- Async image optimization in background threads
- Bytes serialization for Streamlit display/download

---

## Usage Guide

### User Flow

1. **Greeting**
   - Bot introduces itself as TicketBot
   - Asks for user's name

2. **Mood Detection**
   - User describes how they're feeling
   - AI detects mood from natural language
   - System finds matching events

3. **Event Selection**
   - Bot displays up to 6 relevant events
   - User selects event by number
   - Bot shows detailed event information

4. **Ticket Quantity**
   - User specifies number of tickets (1-10)
   - System checks availability
   - Total price calculated

5. **Email Collection**
   - User provides email address
   - System validates email format
   - Creates booking confirmation

6. **Ticket Generation**
   - Unique ticket ID generated
   - QR code embedded with booking details
   - Ticket image created with visual styling
   - QR code displayed for scanning at venue
   - Full ticket available for download as PNG

7. **Continuation**
   - User can book another event
   - Or end conversation

### Chat Commands

The chatbot accepts natural language input. Examples:

- **Mood Expression**: "I'm feeling excited and want to dance"
- **Event Selection**: "I'll take option 2" or "Show me the second one"
- **Quantity**: "I need 5 tickets" or "Just one ticket please"
- **Email**: "contact@example.com"

---

## API Integrations

### Groq API Integration

**Purpose**: AI-powered conversational responses

**Model**: llama-3.1-8b-instant
- Fast and efficient
- Optimized for natural conversation
- Sub-second response times

**Integration Points**:
- Greeting generation
- Mood-aware responses
- Event recommendation explanations
- Booking confirmations
- Error handling messages

**Configuration**:
- Timeout: 10 seconds
- Max tokens: 400 per response
- Temperature: 0.7 (balanced creativity)

**Error Handling**:
- Rate limit detection (429 errors)
- Graceful fallback to template responses
- Console logging for debugging

**Rate Limits** (Free Tier):
- 6000 tokens per minute
- If exceeded, system uses fallback responses
- Upgrade to Dev tier for higher limits

### ScaleDown API Integration

**Purpose**: Background image optimization and compression

**Integration Points**:
- After QR code generation
- After ticket image creation
- Runs in background threads (non-blocking)

**Error Handling**:
- Fails silently (doesn't interrupt user)
- Returns original image if optimization fails
- Console logging for monitoring

**Optimization Benefits**:
- Reduced file sizes
- Faster download times
- Better performance on slow connections
- Automatic format optimization

---

## Development

### Running with Debug Output

To see API calls and debug information:

```bash
streamlit run app.py --logger.level=debug
```

### Testing Individual Components

**Test Mood Detection**:
```python
from chatbot_engine import ChatbotEngine

bot = ChatbotEngine()
mood = bot.detect_mood("I'm feeling excited and energetic")
print(mood)  # Should print: "excited"
```

**Test Event Recommendations**:
```python
from chatbot_engine import ChatbotEngine
from events_data import EVENTS

bot = ChatbotEngine()
events = bot.get_events_by_mood("happy")
print(f"Found {len(events)} matching events")
```

**Test Ticket Generation**:
```python
from ticket_generator import create_ticket_image, get_ticket_bytes

booking_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "event": "Concert Night",
    "date": "2026-03-15",
    "time": "8:00 PM",
    "venue": "City Hall",
    "tickets": 2,
    "total": 100.00
}

ticket_bytes, ticket_id = get_ticket_bytes(booking_data)
print(f"Generated ticket ID: {ticket_id}")
```

### Adding New Events

Edit `events_data.py`:

```python
{
    "id": 1,
    "name": "Concert Night",
    "category": "Music",
    "mood": ["excited", "energetic", "social"],
    "date": "2026-03-15",
    "time": "8:00 PM",
    "venue": "City Hall",
    "price": 50.00,
    "available_seats": 500,
    "description": "High-energy music festival featuring local and international artists"
}
```

### Adding New Mood Keywords

Edit `chatbot_engine.py` in the `detect_mood()` method:

```python
mood_keywords = {
    "your_mood": ["keyword1", "keyword2", "keyword3"],
    # ... existing moods
}
```

### Creating Custom CSS Themes

Modify the CSS section in `app.py`:
- `.window-card` - Card styling
- `.main-header` - Header styling
- `.ticket-card` - Ticket display styling
- Background patterns and colors

---

## Deployment

### Local Development Server

```bash
streamlit run app.py
```

### Streamlit Community Cloud

1. Push code to GitHub public repository
2. Visit https://share.streamlit.io
3. Connect GitHub account
4. Select repository and branch
5. Streamlit automatically deploys

**Important**: Ensure `.streamlit/secrets.toml` is in `.gitignore` before deploying. Add secrets in Streamlit Cloud dashboard:

1. Go to app settings
2. Secrets tab
3. Add GROQ_API_KEY and SCALEDOWN_API_KEY in TOML format

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:

```bash
docker build -t ticketbot .
docker run -p 8501:8501 \
  -e GROQ_API_KEY="your_key" \
  -e SCALEDOWN_API_KEY="your_key" \
  ticketbot
```

### Environment Variables for Production

Set these on your deployment platform:

```
GROQ_API_KEY=<your_groq_key>
SCALEDOWN_API_KEY=<your_scaledown_key>
```

---

## Troubleshooting

### Issue: "streamlit: command not found"

**Solution**: Install Streamlit or use Python module syntax:
```bash
pip install streamlit
# or
python -m streamlit run app.py
```

### Issue: Port 8501 already in use

**Solution**: Use different port:
```bash
streamlit run app.py --server.port 8502
```

Or kill existing process:
```bash
# Windows
Get-Process python | Stop-Process -Force

# macOS/Linux
pkill -f streamlit
```

### Issue: API Key not found error

**Solution**:
1. Verify `.streamlit/secrets.toml` exists
2. Check file format (TOML, not JSON)
3. Verify key names match: `GROQ_API_KEY`, `SCALEDOWN_API_KEY`
4. Restart Streamlit: `Ctrl+C` then re-run command

### Issue: "Rate limit exceeded" from Groq API

**Solution**:
- Free tier: 6000 tokens per minute
- Wait 1-2 minutes and try again
- Upgrade to Dev tier at https://console.groq.com/settings/billing
- Reduce conversation history length in `chatbot_engine.py`

### Issue: ScaleDown optimization not working

**Solution**:
- Non-blocking failure (doesn't affect user experience)
- Check ScaleDown API key validity
- Verify API endpoint availability
- Original images will be used as fallback

### Issue: Tickets not generating

**Solution**:
1. Check Pillow installation: `pip install --upgrade Pillow`
2. Verify booking_data contains all required fields
3. Check available disk space
4. Review console output for specific errors

### Issue: Git push fails

**Solution**:
1. Verify GitHub credentials: `git config --global user.email "your_email@example.com"`
2. Check `.gitignore` includes `secrets.toml`
3. Pull latest changes: `git pull origin main`
4. Resolve conflicts if any
5. Try push again

### Issue: Chatbot not responding

**Solution**:
1. Verify internet connection
2. Check Groq API status and key validity
3. Review API rate limits
4. Check console for error messages
5. Restart Streamlit application

---

## Performance Optimization

### Response Speed
- Groq API typically responds in 500ms-2s
- Streamlit UI updates instantly
- QR code generation: < 100ms
- Ticket image creation: < 500ms

### Image Optimization
- ScaleDown compresses images in background
- Average reduction: 40-60% file size
- Doesn't block user interactions
- Automatic fallback if optimization fails

### Database/Caching
- Event data loaded once at startup
- Conversation history limited to 10 messages
- Session state persists within browser session
- No external database required

---

## Security Considerations

### API Key Protection
- `.streamlit/secrets.toml` is git-ignored
- Environment variables used for production
- Never commit credentials to repository
- Use Streamlit Cloud secrets for hosted deployments

### User Data
- Email addresses used only for booking confirmation
- No persistent user data storage (session-based)
- QR codes contain public ticket information only
- No password authentication required

### Image Security
- Ticket images are public (by design)
- ScaleDown API handles images securely
- No sensitive personal data in QR codes beyond booking ID

---

## Future Enhancements

Potential features for future versions:

1. **Payment Integration**
   - Stripe/PayPal integration
   - Booking payment processing

2. **Email Confirmation**
   - Automated confirmation emails with ticket attachment
   - SMS notifications

3. **Persistent Storage**
   - User accounts and booking history
   - Favorite events/preferences

4. **Real-time Inventory**
   - Dynamic seat availability
   - Waitlist functionality

5. **Enhanced Analytics**
   - Usage statistics
   - Popular moods/events
   - Booking conversion rates

6. **Multi-language Support**
   - Language detection
   - Translations for UI and chatbot

7. **Advanced Mood Detection**
   - Sentiment analysis for more nuanced emotions
   - Image-based mood detection

8. **Integration Improvements**
   - Venue APIs for real-time event data
   - Social media sharing for booked events

---

## Support and Contribution

### Bug Reports
Found an issue? Create a GitHub issue with:
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
- Screenshots if applicable

### Adding Features
1. Fork repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Make changes and commit
4. Push to branch
5. Create pull request with description

### Code Style
- Follow PEP 8 Python guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and modular

---

## Version History

- **1.0.0** (2026-02-20)
  - Initial release with Groq AI integration
  - ScaleDown API image optimization
  - QR code ticket generation
  - Mood-based event recommendations

---

## License

This project was created for the GenAI for GenZ Competition by Intel (2026).

---

## Contact and Attribution

**Project**: Event Ticketing Chatbot
**Competition**: GenAI for GenZ by Intel
**Date**: 2026
**Repository**: https://github.com/jadenlaloo/Event-Ticketing-Chatbot

---

**Last Updated**: February 20, 2026
