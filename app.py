"""
Event Ticketing Chatbot - Main Streamlit Application
A GenAI for GenZ Competition Project by Intel

Features:
- Mood-based event recommendations
- Conversational ticket booking
- QR Code ticket generation
- Retro minimalist design
"""

import streamlit as st
from chatbot_engine import ChatbotEngine
from ticket_generator import get_qr_bytes, get_ticket_bytes

# Page configuration
st.set_page_config(
    page_title="TicketBot - Event Ticketing Chatbot",
    page_icon="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 256 256'><rect fill='white'/><path d='M128 24A104 104 0 1 0 232 128 104.11 104.11 0 0 0 128 24Zm0 192a88 88 0 1 1 88-88 88.1 88.1 0 0 1-88 88Z'/></svg>",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for retro minimalist theme
st.markdown("""
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.0.3/src/regular/style.css" />
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Space Grotesk', monospace !important;
    }
    
    .stApp {
        background: 
            radial-gradient(circle, #d0d0d0 1px, transparent 1px);
        background-size: 20px 20px;
        background-color: #f5f5f5;
    }
    
    .main-header {
        text-align: left;
        padding: 40px 60px;
        margin-bottom: 10px;
        position: relative;
    }
    
    .main-header h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 4rem;
        font-weight: 700;
        color: #000000;
        margin: 0;
        line-height: 1.0;
    }
    
    .main-header p {
        font-family: 'Space Mono', monospace !important;
        font-size: 1rem;
        color: #333333;
        margin-top: 15px;
        max-width: 500px;
    }
    
    .block-container {
        padding-left: 60px !important;
        padding-right: 60px !important;
        max-width: 1400px !important;
    }
    
    .window-card {
        background: #ffffff;
        border: 2px solid #000000;
        border-radius: 8px;
        margin: 15px 0;
        overflow: hidden;
        box-shadow: 4px 4px 0px #000000;
    }
    
    .window-header {
        background: #000000;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .window-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #ffffff;
        border: none;
    }
    
    .window-title {
        color: #ffffff;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.85rem;
        margin-left: 10px;
    }
    
    .window-content {
        padding: 20px;
    }
    
    .chat-message-user {
        background: #000000;
        color: #ffffff;
        padding: 15px 20px;
        border-radius: 8px 8px 0 8px;
        margin: 10px 0;
        max-width: 85%;
        margin-left: auto;
        font-family: 'Space Mono', monospace !important;
        border: 2px solid #000000;
    }
    
    .chat-message-bot {
        background: #ffffff;
        color: #000000;
        padding: 15px 20px;
        border-radius: 8px 8px 8px 0;
        margin: 10px 0;
        max-width: 85%;
        font-family: 'Space Mono', monospace !important;
        border: 2px solid #000000;
        box-shadow: 3px 3px 0px #000000;
    }
    
    .stButton > button {
        background: #000000 !important;
        color: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        padding: 10px 25px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        box-shadow: 3px 3px 0px #333333 !important;
    }
    
    .stButton > button:hover {
        background: #ffffff !important;
        color: #000000 !important;
        transform: translate(2px, 2px) !important;
        box-shadow: 1px 1px 0px #333333 !important;
    }
    
    .stDownloadButton > button {
        background: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        padding: 10px 25px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        box-shadow: 3px 3px 0px #000000 !important;
        width: 100% !important;
    }
    
    .stDownloadButton > button:hover {
        background: #000000 !important;
        color: #ffffff !important;
        transform: translate(2px, 2px) !important;
        box-shadow: 1px 1px 0px #000000 !important;
    }
    
    .stTextInput > div > div > input {
        background: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        font-family: 'Space Mono', monospace !important;
        padding: 12px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #000000 !important;
        box-shadow: 3px 3px 0px #000000 !important;
    }
    
    .ticket-card {
        background: #ffffff;
        border: 2px solid #000000;
        padding: 25px;
        border-radius: 8px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 4px 4px 0px #000000;
    }
    
    .ticket-card h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700;
        color: #000000;
        margin-bottom: 10px;
    }
    
    .feature-tag {
        display: inline-block;
        background: #ffffff;
        border: 2px solid #000000;
        padding: 10px 20px;
        margin: 5px 10px 5px 0;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.9rem;
        border-radius: 4px;
        color: #000000;
        box-shadow: 3px 3px 0px #000000;
    }
    
    .sidebar-content {
        font-family: 'Space Mono', monospace !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stChatMessage {
        background: transparent !important;
    }
    
    [data-testid="stChatMessageContent"] {
        background: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 8px !important;
        box-shadow: 3px 3px 0px #000000 !important;
    }
    
    .footer-text {
        text-align: center;
        padding: 30px;
        font-family: 'Space Mono', monospace !important;
        color: #666666;
        font-size: 0.85rem;
        border-top: 1px solid #cccccc;
        margin-top: 40px;
    }
    
    /* Floating retro icons */
    .floating-icon {
        position: fixed;
        z-index: 0;
        opacity: 0.7;
        pointer-events: none;
    }
    
    .icon-1 {
        top: 120px;
        right: 80px;
        width: 120px;
    }
    
    .icon-2 {
        top: 350px;
        right: 200px;
        width: 100px;
    }
    
    .icon-3 {
        bottom: 150px;
        right: 100px;
        width: 90px;
    }
    
    .icon-4 {
        top: 200px;
        left: 70%;
        width: 110px;
    }
    
    .icon-5 {
        bottom: 250px;
        left: 65%;
        width: 85px;
    }
    
    .icon-6 {
        top: 500px;
        right: 350px;
        width: 95px;
    }
</style>
""", unsafe_allow_html=True)

# Add floating retro icons
import base64
import os

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

icons_folder = "icons new"
icon_files = [
    "books.jpeg",
    "download (1).jpeg", 
    "download (2).jpeg",
    "Download premium png of PNG Retro cassette tape illustration_ by Hein about music png, cassett tape halftone, vintage paper background, vintage cassette tape illustration, and background 17874012.jpeg",
    "Download premium png of PNG Vintage monochrome globe illustration by Hein about globe, retro world map, world, background, and png 17873929.jpeg",
    "download.jpeg"
]

# Create floating icons HTML
floating_icons_html = ""
for i, icon_file in enumerate(icon_files):
    icon_path = os.path.join(icons_folder, icon_file)
    if os.path.exists(icon_path):
        img_base64 = get_image_base64(icon_path)
        floating_icons_html += f'<img src="data:image/jpeg;base64,{img_base64}" class="floating-icon icon-{i+1}" />'

st.markdown(floating_icons_html, unsafe_allow_html=True)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatbotEngine()
    st.session_state.messages = []
    st.session_state.show_ticket = False
    
    greeting = st.session_state.chatbot.get_greeting()
    st.session_state.messages.append({"role": "bot", "content": greeting})

# Header
st.markdown("""
<div class="main-header">
    <h1>Hello.<br>I'm TicketBot.</h1>
    <p>An AI-powered event ticketing assistant with mood-based recommendations.</p>
</div>
""", unsafe_allow_html=True)

# Feature tags
st.markdown("""
<div style="margin-bottom: 40px; padding-left: 60px;">
    <span class="feature-tag">Mood-Based Picks</span>
    <span class="feature-tag">QR Tickets</span>
    <span class="feature-tag">Instant Booking</span>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="window-card">
        <div class="window-header">
            <div class="window-dot"></div>
            <div class="window-dot"></div>
            <span class="window-title">about.txt</span>
        </div>
        <div class="window-content">
            <h3 style="margin-top: 0;">About TicketBot</h3>
            <p style="font-family: 'Space Mono', monospace; font-size: 0.9rem; line-height: 1.6;">
                TicketBot is an intelligent event ticketing chatbot that understands your mood and recommends matching events.
            </p>
            <p style="font-family: 'Space Mono', monospace; font-size: 0.9rem; line-height: 1.6;">
                <strong>Features:</strong><br>
                - Mood detection<br>
                - Smart recommendations<br>
                - Conversational booking<br>
                - QR code tickets
            </p>
            <p style="font-family: 'Space Mono', monospace; font-size: 0.85rem; color: #666;">
                Built for GenAI for GenZ Competition | Intel
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Start New Chat"):
        st.session_state.chatbot.reset()
        st.session_state.messages = []
        st.session_state.show_ticket = False
        greeting = st.session_state.chatbot.get_greeting()
        st.session_state.messages.append({"role": "bot", "content": greeting})
        st.rerun()

# Chat container
st.markdown("""
<div class="window-card">
    <div class="window-header">
        <div class="window-dot"></div>
        <div class="window-dot"></div>
        <span class="window-title">chat-session.log</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message-user">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message-bot">{message["content"].replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

# Show QR ticket if booking is complete
if st.session_state.chatbot.state == "booking_complete":
    booking_data = st.session_state.chatbot.get_booking_data()
    
    if booking_data:
        st.markdown("""
        <div class="window-card">
            <div class="window-header">
                <div class="window-dot"></div>
                <div class="window-dot"></div>
                <span class="window-title">ticket.png</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            <div class="ticket-card">
                <h3>Your Ticket is Ready</h3>
                <p style="font-family: 'Space Mono', monospace; color: #666;">Scan the QR code at the venue</p>
            </div>
            """, unsafe_allow_html=True)
            
            qr_bytes, ticket_id = get_qr_bytes(booking_data)
            st.image(qr_bytes, caption=f"Ticket ID: {ticket_id}", use_container_width=True)
            
            ticket_bytes, _ = get_ticket_bytes(booking_data)
            st.download_button(
                label="Download Full Ticket",
                data=ticket_bytes,
                file_name=f"ticket_{ticket_id}.png",
                mime="image/png",
                use_container_width=True
            )

# Chat input
user_input = st.chat_input("Type your message here...", key="chat_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = st.session_state.chatbot.process_message(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()

# Footer
st.markdown("""
<div class="footer-text">
    Made for GenAI for GenZ Competition | Intel<br>
    2026 TicketBot
</div>
""", unsafe_allow_html=True)
