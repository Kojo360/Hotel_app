from django.shortcuts import render
from .models import BarItem


def bar_menu(request):
    """Display bar menu items grouped by category"""
    bar_items = BarItem.objects.filter(is_available=True)
    
    # Get featured items
    featured_items = bar_items.filter(is_featured=True)
    
    # Group items by category
    categories = {
        'beer': bar_items.filter(category='beer'),
        'wine': bar_items.filter(category='wine'),
        'spirits': bar_items.filter(category='spirits'),
        'cocktail': bar_items.filter(category='cocktail'),
        'mocktail': bar_items.filter(category='mocktail'),
        'soft_drink': bar_items.filter(category='soft_drink'),
        'juice': bar_items.filter(category='juice'),
        'hot_beverage': bar_items.filter(category='hot_beverage'),
    }
    
    context = {
        'featured_items': featured_items,
        'categories': categories
    }
    return render(request, 'bar/bar_menu.html', context)

