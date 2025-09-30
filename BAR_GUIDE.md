# 🍹 Bar Management Guide - AGYEI TWUM LODGE

## Adding Bar Items (Beverages & Alcohol)

The Bar page showcases all your beverages including alcoholic drinks, soft drinks, juices, and more!

---

## Quick Start

### Access Bar Admin:
1. Go to: http://127.0.0.1:8000/admin/
2. Click "**Bar Items**" under **BAR & BEVERAGES** section
3. Click "**+ Add Bar Item**"

### View Bar Page:
http://127.0.0.1:8000/bar/

---

## Adding a Bar Item

### Required Fields:

#### **Name** (Required)
- The drink/beverage name
- Examples:
  - "Heineken Beer"
  - "Mojito"
  - "Jack Daniels Whiskey"
  - "Fresh Orange Juice"
  - "Cappuccino"

#### **Description** (Required)
- Describe the drink
- Examples:
  ```
  Classic Dutch lager with a smooth, crisp taste and balanced bitterness
  ```
  ```
  Refreshing cocktail made with white rum, fresh mint leaves, lime juice, sugar, and soda water
  ```
  ```
  Premium Tennessee whiskey aged in charred oak barrels for a smooth, mellow flavor
  ```

#### **Price** (Required)
- Enter price without currency symbol
- Examples: `5.99`, `14.99`, `45.00`

#### **Category** (Required)
Select from dropdown:
- **Beer** - All beer varieties
- **Wine** - Red, white, rosé, sparkling wines
- **Spirits & Liquor** - Whiskey, vodka, rum, gin, tequila, brandy
- **Cocktails** - Alcoholic mixed drinks
- **Mocktails** - Non-alcoholic cocktails
- **Soft Drinks** - Sodas, colas, sparkling water
- **Juices** - Fresh juices, smoothies
- **Hot Beverages** - Coffee, tea, hot chocolate

#### **Alcohol Content** (Optional)
- Specify alcohol percentage or indicate non-alcoholic
- Examples:
  - `5% ABV`
  - `40% ABV`
  - `12.5% ABV`
  - `Non-alcoholic`
  - `Alcohol-free`

#### **Volume** (Optional)
- Serving size or bottle size
- Examples:
  - `330ml` (beer bottle)
  - `750ml bottle` (wine)
  - `1 shot` (spirits)
  - `1 glass`
  - `250ml`
  - `1 pint`

#### **Image** (Optional)
- Upload beverage photo
- Recommended: 800x600px, JPG/PNG
- Shows placeholder if no image

#### **Is available** (Required)
- ✅ **Checked** = Shows on bar menu
- ❌ **Unchecked** = Hidden (out of stock, seasonal)

#### **Is featured** (Optional)
- ✅ **Checked** = Shows in featured section at top
- ❌ **Unchecked** = Shows in regular category
- Use for signature drinks, house specials, promotions

---

## Sample Bar Items

### Beer Examples:

**Local Lager**
```
Name: Star Beer
Price: 4.99
Category: Beer
Alcohol Content: 5.2% ABV
Volume: 330ml
Description: Ghana's favorite lager beer, light and refreshing
```

**Imported Beer**
```
Name: Heineken
Price: 5.99
Category: Beer
Alcohol Content: 5% ABV
Volume: 330ml
Description: Premium Dutch lager with signature crisp taste
```

### Wine Examples:

**Red Wine**
```
Name: Cabernet Sauvignon
Price: 38.99
Category: Wine
Alcohol Content: 13.5% ABV
Volume: 750ml bottle
Description: Full-bodied red wine with notes of black cherry and oak
```

**White Wine**
```
Name: Chardonnay
Price: 32.99
Category: Wine
Alcohol Content: 13% ABV
Volume: 750ml bottle
Description: Elegant white wine with citrus and vanilla notes
```

### Spirits Examples:

**Whiskey**
```
Name: Jack Daniels
Price: 12.99
Category: Spirits & Liquor
Alcohol Content: 40% ABV
Volume: 1 shot
Description: Tennessee whiskey with smooth, charred oak flavor
```

**Vodka**
```
Name: Absolut Vodka
Price: 11.99
Category: Spirits & Liquor
Alcohol Content: 40% ABV
Volume: 1 shot
Description: Premium Swedish vodka, pure and smooth
```

**Rum**
```
Name: Captain Morgan Spiced Rum
Price: 10.99
Category: Spirits & Liquor
Alcohol Content: 35% ABV
Volume: 1 shot
Description: Caribbean rum with hints of vanilla and spice
```

### Cocktail Examples:

**Mojito**
```
Name: Classic Mojito
Price: 14.99
Category: Cocktails
Alcohol Content: 12% ABV
Volume: 1 glass
Description: Refreshing mix of white rum, mint, lime, sugar, and soda
Is Featured: ✓
```

**Margarita**
```
Name: Frozen Margarita
Price: 15.99
Category: Cocktails
Alcohol Content: 15% ABV
Volume: 1 glass
Description: Tequila, lime juice, and triple sec blended with ice
```

**Piña Colada**
```
Name: Piña Colada
Price: 16.99
Category: Cocktails
Alcohol Content: 13% ABV
Volume: 1 glass
Description: Tropical blend of rum, pineapple, and coconut cream
```

### Mocktail Examples:

**Virgin Mojito**
```
Name: Virgin Mojito
Price: 8.99
Category: Mocktails
Alcohol Content: Non-alcoholic
Volume: 1 glass
Description: Refreshing mint, lime, and soda without alcohol
```

**Fruit Punch**
```
Name: Tropical Fruit Punch
Price: 9.99
Category: Mocktails
Alcohol Content: Non-alcoholic
Volume: 1 glass
Description: Vibrant mix of tropical fruits with a splash of grenadine
```

### Soft Drink Examples:

```
Name: Coca-Cola
Price: 3.99
Category: Soft Drinks
Volume: 330ml
Description: Classic refreshing cola
```

```
Name: Sprite
Price: 3.99
Category: Soft Drinks
Volume: 330ml
Description: Crisp lemon-lime soda
```

### Juice Examples:

```
Name: Fresh Orange Juice
Price: 6.99
Category: Juices
Volume: 250ml
Description: Freshly squeezed oranges, no added sugar
```

```
Name: Pineapple Juice
Price: 6.99
Category: Juices
Volume: 250ml
Description: Fresh tropical pineapple juice
```

### Hot Beverage Examples:

```
Name: Irish Coffee
Price: 9.99
Category: Hot Beverages
Alcohol Content: 10% ABV
Volume: 1 cup
Description: Hot coffee with Irish whiskey and whipped cream
```

```
Name: Hot Chocolate
Price: 5.99
Category: Hot Beverages
Alcohol Content: Non-alcoholic
Volume: 1 cup
Description: Rich, creamy hot chocolate with marshmallows
```

---

## Bar Categories Explained

### 🍺 Beer
- All types of beer (lager, ale, stout, IPA)
- Local and imported brands
- Bottles, cans, draft

### 🍷 Wine
- Red, white, rosé, sparkling
- By bottle or glass
- Various regions and vintages

### 🥃 Spirits & Liquor
- Whiskey, vodka, rum, gin, tequila
- Cognac, brandy, liqueurs
- Premium and standard brands

### 🍸 Cocktails
- Mixed alcoholic drinks
- Classic cocktails
- House specialties
- Signature drinks

### 🥤 Mocktails
- Non-alcoholic cocktails
- Virgin versions of popular drinks
- Creative alcohol-free mixes

### 🥫 Soft Drinks
- Sodas and colas
- Sparkling water
- Energy drinks
- Iced tea/lemonade

### 🍊 Juices
- Fresh fruit juices
- Smoothies
- Blended drinks

### ☕ Hot Beverages
- Coffee drinks (espresso, cappuccino, latte)
- Tea varieties
- Hot chocolate
- Irish coffee, hot toddy

---

## Pro Tips

### Pricing Strategy:
- **Beer**: $3-$7 per bottle
- **Wine (glass)**: $8-$15
- **Wine (bottle)**: $25-$60+
- **Spirits (shot)**: $8-$15
- **Cocktails**: $12-$18
- **Mocktails**: $6-$12
- **Soft Drinks**: $2-$5
- **Juices**: $5-$8
- **Hot Beverages**: $3-$10

### Best Practices:
1. **Group similar items** - Makes menu easier to browse
2. **Mark featured drinks** - Highlight signature items
3. **Include alcohol content** - Important for customers
4. **Specify serving size** - Clear expectations
5. **Update seasonally** - Rotate special drinks
6. **Use high-quality images** - Make drinks look appealing

### Descriptions:
- Mention main ingredients
- Describe taste profile (smooth, crisp, fruity, etc.)
- Include origin/brand for premium items
- Note if it's a house special

---

## Admin Features

### List View Shows:
- Name
- Category
- Price
- Volume
- Alcohol content
- Availability status
- Featured status

### Quick Actions:
- **Check/uncheck "Is available"** directly in list
- **Check/uncheck "Is featured"** directly in list
- **Filter by category** to find items quickly
- **Search by name** to locate specific drinks

### Bulk Operations:
1. Select multiple items (checkboxes)
2. Choose action (delete, hide, etc.)
3. Click "Go"

---

## Organizing Your Bar Menu

### Recommended Structure:

**Featured Section (3-5 items)**
- Signature cocktails
- House specials
- Premium selections

**Alcoholic Beverages**
- Beer (5-10 varieties)
- Wine (8-12 selections)
- Spirits (10-15 options)
- Cocktails (8-12 recipes)

**Non-Alcoholic**
- Mocktails (4-6 options)
- Soft Drinks (5-8 options)
- Juices (4-6 fresh options)
- Hot Beverages (4-6 options)

**Total: 50-80 bar items for a complete menu**

---

## Quick Commands

```powershell
# View bar items count
python manage.py shell -c "from bar.models import BarItem; print(f'Total bar items: {BarItem.objects.count()}')"

# View by category
python manage.py shell -c "from bar.models import BarItem; [print(f'{c[1]}: {BarItem.objects.filter(category=c[0]).count()}') for c in BarItem.CATEGORY_CHOICES]"
```

---

## URLs

- **Bar Page**: http://127.0.0.1:8000/bar/
- **Admin**: http://127.0.0.1:8000/admin/bar/baritem/

---

## Common Questions

**Q: How do I mark a drink as "out of stock"?**
A: Uncheck "Is available" and save. It won't show on the bar menu.

**Q: Can I have multiple featured items?**
A: Yes! Check "Is featured" for any drinks you want highlighted.

**Q: What if I don't have a volume?**
A: Leave it blank. The field is optional.

**Q: Should I list cocktail ingredients?**
A: Yes, in the description. Customers like to know what's in their drink.

**Q: How do I organize drink prices?**
A: Generally: Soft drinks < Mocktails < Beer < Cocktails < Wine < Premium spirits

---

## Your Bar is Ready! 🍹

Visit your bar page: http://127.0.0.1:8000/bar/

You should see 8 sample items already loaded!

**Next Steps:**
1. Add more beverages in your style
2. Upload drink photos
3. Mark signature cocktails as featured
4. Adjust prices for your market
5. Add seasonal specials

**Cheers!** 🥂
