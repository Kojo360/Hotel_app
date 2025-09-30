from django.shortcuts import render
from .models import MenuItem


def menu_list(request):
    """Display restaurant menu items grouped by category"""
    menu_items = MenuItem.objects.filter(is_available=True)
    
    # Group items by category
    categories = {
        'appetizer': menu_items.filter(category='appetizer'),
        'main': menu_items.filter(category='main'),
        'dessert': menu_items.filter(category='dessert'),
        'beverage': menu_items.filter(category='beverage'),
    }
    
    context = {
        'categories': categories
    }
    return render(request, 'restaurant/menu_list.html', context)
