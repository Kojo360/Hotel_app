from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Complaint
from .forms import ComplaintForm


def home(request):
    """Homepage with hotel information"""
    context = {
        'whatsapp_phone': settings.WHATSAPP_PHONE
    }
    return render(request, 'pages/home.html', context)


def contact(request):
    """Contact page with complaint form"""
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been submitted successfully! We will get back to you soon.')
            return redirect('pages:contact')
    else:
        form = ComplaintForm()
    
    context = {
        'form': form,
        'whatsapp_phone': settings.WHATSAPP_PHONE
    }
    return render(request, 'pages/contact.html', context)
