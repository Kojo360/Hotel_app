from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from urllib.parse import quote
from .models import Room, Booking
from .forms import BookingForm


def room_list(request):
    """Display all visible rooms"""
    rooms = Room.objects.filter(is_visible=True)
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms/room_list.html', context)


def room_detail(request, pk):
    """Display room details and booking form"""
    room = get_object_or_404(Room, pk=pk, is_visible=True)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            
            # Create WhatsApp message
            message = (
                f"🏨 *New Booking Request*\n\n"
                f"*Room:* {room.name}\n"
                f"*Guest Name:* {booking.name}\n"
                f"*Email:* {booking.email}\n"
                f"*Phone:* {booking.phone}\n"
                f"*Check-in:* {booking.check_in.strftime('%B %d, %Y')}\n"
                f"*Check-out:* {booking.check_out.strftime('%B %d, %Y')}\n"
            )
            
            if booking.special_request:
                message += f"*Special Request:* {booking.special_request}\n"
            
            message += f"\n*Total Price:* ${room.price} per night"
            
            # Encode message for URL
            whatsapp_url = f"https://wa.me/{settings.WHATSAPP_PHONE}?text={quote(message)}"
            
            messages.success(request, 'Booking request submitted! Redirecting to WhatsApp...')
            return redirect(whatsapp_url)
    else:
        form = BookingForm()
    
    context = {
        'room': room,
        'form': form
    }
    return render(request, 'rooms/room_detail.html', context)
