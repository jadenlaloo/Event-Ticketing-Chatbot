"""
QR Code Ticket Generator - Creates unique QR tickets for bookings
Optimizes images using ScaleDown API for better performance
"""

import qrcode
from PIL import Image, ImageDraw
import io
import hashlib
from datetime import datetime
import os
import requests
import threading

# Try to import streamlit for secrets (deployment)
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False

def _get_scaledown_api_key():
    """Get ScaleDown API key from Streamlit secrets or environment"""
    if HAS_STREAMLIT:
        try:
            return st.secrets.get("SCALEDOWN_API_KEY")
        except:
            pass
    
    return os.environ.get("SCALEDOWN_API_KEY")

def optimize_image_with_scaledown(image_bytes, image_format="PNG"):
    """Optimize image using ScaleDown API (non-blocking background task)"""
    api_key = _get_scaledown_api_key()
    if not api_key:
        return image_bytes
    
    try:
        # Prepare the image data
        files = {'image': ('ticket.png', image_bytes, 'image/png')}
        headers = {'X-API-Key': api_key}
        
        # Call ScaleDown API with timeout
        response = requests.post(
            'https://api.scaledown.io/v1/optimize',
            files=files,
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 200:
            # Return optimized image bytes
            return io.BytesIO(response.content)
        else:
            # If optimization fails, return original
            print(f"ScaleDown optimization skipped: {response.status_code}")
            return image_bytes
    except Exception as e:
        # Silently fail - don't interrupt user experience
        print(f"ScaleDown API error (non-blocking): {e}")
        return image_bytes

def optimize_image_async(image_bytes):
    """Optimize image in background thread"""
    thread = threading.Thread(target=optimize_image_with_scaledown, args=(image_bytes,), daemon=True)
    thread.start()

def generate_ticket_id(booking_data):
    """Generate a unique ticket ID"""
    unique_string = f"{booking_data['name']}{booking_data['event']}{booking_data['email']}{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:12].upper()

def generate_qr_code(booking_data):
    """Generate QR code containing ticket information"""
    ticket_id = generate_ticket_id(booking_data)
    
    qr_data = f"""
EVENT TICKET
---
Ticket ID: {ticket_id}
Event: {booking_data['event']}
Date: {booking_data['date']}
Time: {booking_data['time']}
Venue: {booking_data['venue']}
Guest: {booking_data['name']}
Tickets: {booking_data['tickets']}
Total: ${booking_data['total']:.2f}
---
Valid for entry
    """
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="#000000", back_color="#ffffff")
    
    return qr_image, ticket_id

def create_ticket_image(booking_data):
    """Create a complete ticket image with QR code"""
    qr_image, ticket_id = generate_qr_code(booking_data)
    
    ticket_width = 600
    ticket_height = 350
    
    ticket = Image.new('RGB', (ticket_width, ticket_height), '#ffffff')
    draw = ImageDraw.Draw(ticket)
    
    # Border
    draw.rectangle([0, 0, ticket_width-1, ticket_height-1], outline='#000000', width=3)
    
    # Header bar
    draw.rectangle([0, 0, ticket_width, 50], fill='#000000')
    
    # Window dots (retro style)
    draw.ellipse([15, 18, 28, 31], fill='#ffffff')
    draw.ellipse([35, 18, 48, 31], fill='#ffffff')
    
    # Title
    draw.text((60, 15), "EVENT TICKET", fill='#ffffff')
    
    # Resize and paste QR code
    qr_size = 140
    qr_image = qr_image.resize((qr_size, qr_size))
    qr_position = (ticket_width - qr_size - 30, 80)
    ticket.paste(qr_image, qr_position)
    
    # Event details
    y_offset = 70
    draw.text((25, y_offset), booking_data['event'][:35], fill='#000000')
    y_offset += 30
    
    draw.text((25, y_offset), f"Date: {booking_data['date']}", fill='#333333')
    y_offset += 25
    draw.text((25, y_offset), f"Time: {booking_data['time']}", fill='#333333')
    y_offset += 25
    draw.text((25, y_offset), f"Venue: {booking_data['venue'][:25]}", fill='#333333')
    y_offset += 25
    draw.text((25, y_offset), f"Guest: {booking_data['name']}", fill='#333333')
    y_offset += 25
    draw.text((25, y_offset), f"Tickets: {booking_data['tickets']}", fill='#333333')
    y_offset += 25
    draw.text((25, y_offset), f"Total: ${booking_data['total']:.2f}", fill='#333333')
    
    # Ticket ID at bottom
    draw.line([(0, ticket_height - 45), (ticket_width, ticket_height - 45)], fill='#000000', width=1)
    draw.text((25, ticket_height - 35), f"ID: {ticket_id}", fill='#666666')
    
    return ticket, ticket_id

def get_qr_bytes(booking_data):
    """Get QR code as bytes for display in Streamlit"""
    qr_image, ticket_id = generate_qr_code(booking_data)
    
    img_bytes = io.BytesIO()
    qr_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    # Optimize in background (non-blocking)
    optimize_image_async(img_bytes)
    
    return img_bytes, ticket_id

def get_ticket_bytes(booking_data):
    """Get complete ticket as bytes for download"""
    ticket_image, ticket_id = create_ticket_image(booking_data)
    
    img_bytes = io.BytesIO()
    ticket_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    # Optimize in background (non-blocking)
    optimize_image_async(img_bytes)
    
    return img_bytes, ticket_id
