from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import json
from .models import MenuItem


def _load_static_json(name: str):
    base = Path(settings.BASE_DIR) / 'static_data'
    fp = base / f'{name}.json'
    if not fp.exists():
        return None
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)


def menu_list(request):
    """Display restaurant menu items grouped by category, from DB or static JSON."""
    static_mode = getattr(settings, 'USE_STATIC_DATA', False)

    if static_mode:
        raw_items = _load_static_json('restaurant') or []
        data = []
        for item in raw_items:
            item['image_url'] = item.get('image')
            data.append(item)
        # data expected as list of dicts with keys: name, description, price, image, category
        categories = {
            'appetizer': [i for i in data if i.get('category') == 'appetizer'],
            'main': [i for i in data if i.get('category') == 'main'],
            'dessert': [i for i in data if i.get('category') == 'dessert'],
            'beverage': [i for i in data if i.get('category') == 'beverage'],
        }
    else:
        menu_items = MenuItem.objects.filter(is_available=True)
        categories = {
            'appetizer': menu_items.filter(category='appetizer'),
            'main': menu_items.filter(category='main'),
            'dessert': menu_items.filter(category='dessert'),
            'beverage': menu_items.filter(category='beverage'),
        }

    context = {
        'categories': categories,
        'static_mode': static_mode,
    }
    return render(request, 'restaurant/menu_list.html', context)
