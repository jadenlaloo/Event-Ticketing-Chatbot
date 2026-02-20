# 🎫 TicketBot - AI-Powered Event Ticketing Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**An intelligent conversational chatbot for seamless event discovery and ticket booking**

*Built for GenAI for GenZ Competition by Intel*

</div>

---

## 🌟 Features

### 🎭 Mood-Based Event Recommendations
Unlike traditional ticketing platforms, TicketBot understands how you're feeling and recommends events that match your mood. Feeling stressed? It suggests relaxing wellness events. Excited? It finds high-energy concerts and tech summits!

### 💬 Natural Conversational Interface
No more clicking through endless menus. Simply chat with TicketBot like you would with a friend, and book your tickets through a natural conversation flow.

### 📱 Instant QR Code Tickets
Every booking generates a unique QR code ticket that can be downloaded and shown at the venue entrance. No need to wait for email confirmations!

### 🎨 Modern, GenZ-Friendly UI
Beautiful gradient design with a mobile-responsive interface that feels familiar and intuitive.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jadenlaloo/Event-Ticketing-Chatbot.git
   cd Event-Ticketing-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - The app will automatically open at `http://localhost:8501`

---

## 💡 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERACTION                         │
├─────────────────────────────────────────────────────────────┤
│  1. User starts conversation                                 │
│  2. TicketBot asks about mood                               │
│  3. NLP engine detects mood keywords                        │
│  4. Matching events are recommended                         │
│  5. User selects event and ticket quantity                  │
│  6. QR Code ticket is generated instantly                   │
└─────────────────────────────────────────────────────────────┘
```

### Conversation Flow

1. **Greeting** → Bot introduces itself and asks for your name
2. **Mood Detection** → Bot asks how you're feeling
3. **Smart Recommendations** → Events matching your mood are displayed
4. **Event Selection** → Choose your preferred event
5. **Ticket Booking** → Specify number of tickets
6. **Confirmation** → Receive QR code ticket instantly

---

## 🏗️ Project Structure

```
Event-Ticketing-Chatbot/
│
├── app.py                 # Main Streamlit application
├── chatbot_engine.py      # NLP-based conversation handler
├── ticket_generator.py    # QR code ticket generator
├── events_data.py         # Sample events database
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

---

## 🎯 Novelty Factor

What makes TicketBot unique:

| Feature | Traditional Platforms | TicketBot |
|---------|----------------------|-----------|
| Event Discovery | Category filters | Mood-based AI recommendations |
| Booking Process | Multi-page forms | Single conversation |
| Ticket Delivery | Email (delayed) | Instant QR generation |
| User Experience | Transactional | Personal & empathetic |

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **NLP Engine**: Custom keyword-based mood detection
- **QR Generation**: qrcode + Pillow libraries
- **Styling**: Custom CSS with modern gradients

---

## 📸 Screenshots

### Chat Interface
The main conversational interface where users interact with TicketBot.

### Mood-Based Recommendations  
Events are filtered and recommended based on detected user mood.

### QR Code Ticket
Instant ticket generation with downloadable QR codes.

---

## 🔮 Future Enhancements

- [ ] Integration with real payment gateways
- [ ] Email/SMS ticket delivery
- [ ] Multi-language support
- [ ] Voice input capability
- [ ] Integration with calendar apps
- [ ] Social sharing features

---

## 👨‍💻 Author

**Built for GenAI for GenZ Competition by Intel**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ and AI**

*Empowering the next generation of event experiences*

</div>
