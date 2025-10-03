from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json
from .models import BarItem


def _load_static_json(name: str):
    base = Path(settings.BASE_DIR) / 'static_data'
    fp = base / f'{name}.json'
    if not fp.exists():
        return None
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)


def bar_menu(request):
    """Display bar menu items grouped by category (DB or static JSON)."""
    static_mode = getattr(settings, 'USE_STATIC_DATA', False)

    if static_mode:
        raw_items = _load_static_json('bar') or []
        data = []
        for item in raw_items:
            item['image_url'] = item.get('image')
            data.append(item)
        featured_items = [i for i in data if i.get('is_featured')]
        categories = {
            'beer': [i for i in data if i.get('category') == 'beer'],
            'wine': [i for i in data if i.get('category') == 'wine'],
            'spirits': [i for i in data if i.get('category') == 'spirits'],
            'cocktail': [i for i in data if i.get('category') == 'cocktail'],
            'mocktail': [i for i in data if i.get('category') == 'mocktail'],
            'soft_drink': [i for i in data if i.get('category') == 'soft_drink'],
            'juice': [i for i in data if i.get('category') == 'juice'],
            'hot_beverage': [i for i in data if i.get('category') == 'hot_beverage'],
        }
    else:
        bar_items = BarItem.objects.filter(is_available=True)
        featured_items = bar_items.filter(is_featured=True)
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
        'categories': categories,
        'static_mode': static_mode,
    }
    return render(request, 'bar/bar_menu.html', context)

