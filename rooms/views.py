from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib import messages
from django.conf import settings
from urllib.parse import quote
import json
from pathlib import Path
from .models import Room, Booking
from .forms import BookingForm, BookingRequestForm


def _load_static_json(name: str):
    base = Path(settings.BASE_DIR) / 'static_data'
    fp = base / f'{name}.json'
    if not fp.exists():
        return None
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)


def room_list(request):
    """Display all rooms either from DB or static file."""
    if getattr(settings, 'USE_STATIC_DATA', False):
        data = _load_static_json('rooms') or []
        # Normalize amenities into a list for templates
        normalized = []
        for r in data:
            amenities = r.get('amenities', [])
            if isinstance(amenities, str):
                amenities_list = [a.strip() for a in amenities.split(',') if a.strip()]
            elif isinstance(amenities, list):
                amenities_list = [str(a).strip() for a in amenities if str(a).strip()]
            else:
                amenities_list = []
            r['amenities_list'] = amenities_list
            r['image_url'] = r.get('image')
            normalized.append(r)
        # Expect list of dicts with keys: id, name, description, price, amenities, image
        context = {'rooms': normalized, 'static_mode': True}
        return render(request, 'rooms/room_list.html', context)
    else:
        rooms = Room.objects.filter(is_visible=True)
        context = {'rooms': rooms, 'static_mode': False}
        return render(request, 'rooms/room_list.html', context)


def room_detail(request, pk):
    """Display room details and booking form (DB or static)."""
    static_mode = getattr(settings, 'USE_STATIC_DATA', False)

    if static_mode:
        data = _load_static_json('rooms') or []
        room = next((r for r in data if str(r.get('id')) == str(pk)), None)
        if not room:
            raise Http404('Room not found')
        amenities = room.get('amenities', [])
        if isinstance(amenities, str):
            room['amenities_list'] = [a.strip() for a in amenities.split(',') if a.strip()]
        elif isinstance(amenities, list):
            room['amenities_list'] = [str(a).strip() for a in amenities if str(a).strip()]
        else:
            room['amenities_list'] = []
        room['image_url'] = room.get('image')
        FormClass = BookingRequestForm
    else:
        room = get_object_or_404(Room, pk=pk, is_visible=True)
        FormClass = BookingForm

    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            # Build WhatsApp message without saving to DB in static mode
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            special_request = form.cleaned_data.get('special_request')

            room_name = room['name'] if static_mode else room.name
            room_price = room['price'] if static_mode else room.price

            message = (
                f"🏨 *New Booking Request*\n\n"
                f"*Room:* {room_name}\n"
                f"*Guest Name:* {name}\n"
                f"*Email:* {email}\n"
                f"*Phone:* {phone}\n"
                f"*Check-in:* {check_in.strftime('%B %d, %Y')}\n"
                f"*Check-out:* {check_out.strftime('%B %d, %Y')}\n"
            )

            if special_request:
                message += f"*Special Request:* {special_request}\n"

            message += f"\n*Total Price:* ${room_price} per night"

            whatsapp_url = f"https://wa.me/{settings.WHATSAPP_PHONE}?text={quote(message)}"
            messages.success(request, 'Booking request submitted! Redirecting to WhatsApp...')
            return redirect(whatsapp_url)
    else:
        form = FormClass()

    context = {
        'room': room,
        'form': form,
        'static_mode': static_mode,
    }
    return render(request, 'rooms/room_detail.html', context)
