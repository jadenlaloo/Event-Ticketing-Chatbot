"""
Event Ticketing Chatbot - Main Streamlit Application
A GenAI for GenZ Competition Project by Intel

Features:
- Mood-based event recommendations
- Conversational ticket booking
- QR Code ticket generation
"""

import streamlit as st
from chatbot_engine import ChatbotEngine
from ticket_generator import get_qr_bytes, get_ticket_bytes

# Page configuration
st.set_page_config(
    page_title="🎫 TicketBot - Event Ticketing Chatbot",
    page_icon="🎫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for chat interface
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 20px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 18px;
        border-radius: 20px 20px 5px 20px;
        margin: 10px 0;
        max-width: 80%;
        margin-left: auto;
    }
    
    .bot-message {
        background: #f0f2f6;
        color: #1a1a2e;
        padding: 12px 18px;
        border-radius: 20px 20px 20px 5px;
        margin: 10px 0;
        max-width: 80%;
    }
    
    .ticket-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        font-weight: bold;
        transition: transform 0.3s;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
    }
    
    .feature-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 5px 15px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatbotEngine()
    st.session_state.messages = []
    st.session_state.show_ticket = False
    
    # Add initial greeting
    greeting = st.session_state.chatbot.get_greeting()
    st.session_state.messages.append({"role": "bot", "content": greeting})

# Header
st.markdown("""
<div class="main-header">
    <h1>🎫 TicketBot</h1>
    <p style="font-size: 18px;">Your AI-Powered Event Ticketing Assistant</p>
    <div>
        <span class="feature-badge">🎭 Mood-Based Recommendations</span>
        <span class="feature-badge">📱 QR Code Tickets</span>
        <span class="feature-badge">💬 Conversational Booking</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar with info
with st.sidebar:
    st.markdown("### 🌟 About TicketBot")
    st.markdown("""
    TicketBot is an intelligent event ticketing chatbot that:
    
    - 🎭 **Understands your mood** and recommends matching events
    - 💬 **Converses naturally** for a seamless booking experience
    - 🎫 **Generates QR tickets** instantly
    - 📱 **Works on any device**
    
    ---
    
    **Built for:**  
    GenAI for GenZ Competition by Intel
    
    **Tech Stack:**
    - Python
    - Streamlit
    - QR Code Generation
    - NLP-based Chat Engine
    """)
    
    if st.button("🔄 Start New Conversation"):
        st.session_state.chatbot.reset()
        st.session_state.messages = []
        st.session_state.show_ticket = False
        greeting = st.session_state.chatbot.get_greeting()
        st.session_state.messages.append({"role": "bot", "content": greeting})
        st.rerun()

# Chat container
chat_container = st.container()

with chat_container:
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div style="display: flex; justify-content: flex-end;">
                <div class="user-message">{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message["content"])

# Show QR ticket if booking is complete
if st.session_state.chatbot.state == "booking_complete":
    booking_data = st.session_state.chatbot.get_booking_data()
    
    if booking_data:
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            <div class="ticket-card">
                <h3>🎉 Your Ticket is Ready!</h3>
                <p>Scan the QR code at the venue</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Generate and display QR code
            qr_bytes, ticket_id = get_qr_bytes(booking_data)
            st.image(qr_bytes, caption=f"Ticket ID: {ticket_id}", use_container_width=True)
            
            # Download button for full ticket
            ticket_bytes, _ = get_ticket_bytes(booking_data)
            st.download_button(
                label="📥 Download Full Ticket",
                data=ticket_bytes,
                file_name=f"ticket_{ticket_id}.png",
                mime="image/png",
                use_container_width=True
            )

# Chat input
user_input = st.chat_input("Type your message here...", key="chat_input")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get bot response
    response = st.session_state.chatbot.process_message(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
    
    # Rerun to update UI
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: white; padding: 20px;">
    <p>Made with ❤️ for GenAI for GenZ Competition | Intel</p>
    <p style="font-size: 12px;">© 2026 TicketBot</p>
</div>
""", unsafe_allow_html=True)
