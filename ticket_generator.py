"""
QR Code Ticket Generator - Creates unique QR tickets for bookings
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import io
import hashlib
from datetime import datetime

def generate_ticket_id(booking_data):
    """Generate a unique ticket ID"""
    unique_string = f"{booking_data['name']}{booking_data['event']}{booking_data['email']}{datetime.now().isoformat()}"
    return hashlib.md5(unique_string.encode()).hexdigest()[:12].upper()

def generate_qr_code(booking_data):
    """Generate QR code containing ticket information"""
    ticket_id = generate_ticket_id(booking_data)
    
    # Create ticket info string for QR code
    qr_data = f"""
🎫 EVENT TICKET
━━━━━━━━━━━━━━
Ticket ID: {ticket_id}
Event: {booking_data['event']}
Date: {booking_data['date']}
Time: {booking_data['time']}
Venue: {booking_data['venue']}
Guest: {booking_data['name']}
Tickets: {booking_data['tickets']}
Total: ${booking_data['total']:.2f}
━━━━━━━━━━━━━━
Valid for entry
    """
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create QR code image with custom colors
    qr_image = qr.make_image(fill_color="#1a1a2e", back_color="#ffffff")
    
    return qr_image, ticket_id

def create_ticket_image(booking_data):
    """Create a complete ticket image with QR code"""
    qr_image, ticket_id = generate_qr_code(booking_data)
    
    # Create ticket canvas
    ticket_width = 600
    ticket_height = 400
    
    # Create gradient-like background
    ticket = Image.new('RGB', (ticket_width, ticket_height), '#667eea')
    draw = ImageDraw.Draw(ticket)
    
    # Draw gradient effect (simplified)
    for i in range(ticket_height):
        ratio = i / ticket_height
        r = int(102 + (118 - 102) * ratio)
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (109 - 234) * ratio)
        draw.line([(0, i), (ticket_width, i)], fill=(r, g, b))
    
    # Add white rounded rectangle for content area
    margin = 20
    draw.rounded_rectangle(
        [margin, margin, ticket_width - margin, ticket_height - margin],
        radius=15,
        fill='white'
    )
    
    # Resize and paste QR code
    qr_size = 150
    qr_image = qr_image.resize((qr_size, qr_size))
    qr_position = (ticket_width - qr_size - 40, (ticket_height - qr_size) // 2)
    ticket.paste(qr_image, qr_position)
    
    # Add text (using default font as custom fonts may not be available)
    draw = ImageDraw.Draw(ticket)
    
    # Title
    draw.text((40, 40), "🎫 EVENT TICKET", fill='#1a1a2e')
    
    # Event name
    event_name = booking_data['event']
    if len(event_name) > 25:
        event_name = event_name[:22] + "..."
    draw.text((40, 80), event_name, fill='#333333')
    
    # Details
    y_offset = 120
    details = [
        f"📅 {booking_data['date']} at {booking_data['time']}",
        f"📍 {booking_data['venue'][:30]}",
        f"👤 {booking_data['name']}",
        f"🎫 {booking_data['tickets']} ticket(s)",
        f"💰 ${booking_data['total']:.2f}"
    ]
    
    for detail in details:
        draw.text((40, y_offset), detail, fill='#555555')
        y_offset += 30
    
    # Ticket ID
    draw.text((40, ticket_height - 60), f"ID: {ticket_id}", fill='#888888')
    
    return ticket, ticket_id

def get_qr_bytes(booking_data):
    """Get QR code as bytes for display in Streamlit"""
    qr_image, ticket_id = generate_qr_code(booking_data)
    
    # Convert to bytes
    img_bytes = io.BytesIO()
    qr_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes, ticket_id

def get_ticket_bytes(booking_data):
    """Get complete ticket as bytes for download"""
    ticket_image, ticket_id = create_ticket_image(booking_data)
    
    # Convert to bytes
    img_bytes = io.BytesIO()
    ticket_image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes, ticket_id
