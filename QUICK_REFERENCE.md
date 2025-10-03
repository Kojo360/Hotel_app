# 🚀 Quick Reference Card - Adding Content

## Access Admin Panel
1. Start server: `python manage.py runserver`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with your admin credentials

---

## 🛏️ ROOMS Quick Add

**Required Fields:**
- Name: e.g., "Deluxe King Suite"
- Description: 2-4 sentences about the room
- Price: e.g., 150.00 (per night)
- Amenities: Comma-separated list

**Optional:**
- Image: 1200x800px recommended
- Is visible: ✅ to show on website

**Example Amenities:**
```
Free Wi-Fi, King bed, Air conditioning, TV, Mini-bar, Safe, Work desk, Coffee maker, Shower, City view
```

---

## 🍽️ RESTAURANT Quick Add

**Required Fields:**
- Name: e.g., "Grilled Salmon"
- Description: Describe the dish
- Category: Appetizer/Main/Dessert/Beverage
- Price: e.g., 24.99

**Optional:**
- Image: 800x800px recommended
- Is available: ✅ to show on menu

**Categories:**
- Appetizer (starters, salads)
- Main Course (entrées)
- Dessert (sweets)
- Beverage (drinks)

---

## 🍺 BAR Quick Add

**Required Fields:**
- Name: e.g., "Mojito"
- Description: Describe the drink
- Category: Select from dropdown
- Price: e.g., 12.00

**Optional but Recommended:**
- Alcohol content: "12% ABV" or "Non-alcoholic"
- Volume: "330ml bottle" or "Glass (150ml)"
- Image: 600x800px recommended
- Is available: ✅ to show on menu
- Is featured: ✅ to highlight as special

**Categories:**
- Beer
- Wine
- Spirits & Liquor
- Cocktails
- Soft Drinks
- Juices
- Hot Beverages
- Mocktails

---

## 💡 Pro Tips

### Descriptions
- Use 2-4 sentences
- Include key ingredients
- Highlight special features
- Use appealing language

### Prices
- Always use 2 decimals: 25.00 (not 25)
- Be consistent across similar items
- Consider your target market

### Images
- Use high quality photos
- Keep under 2MB per file
- JPG or PNG format
- Professional lighting

### Visibility
- Use checkboxes to hide items temporarily
- Great for sold out or seasonal items
- Hidden items don't appear on website

---

## 📊 Recommended Starting Numbers

**Rooms:** 3-5 different types
**Restaurant Menu:** 
- 4-6 Appetizers
- 8-10 Main Courses  
- 4-6 Desserts
- 4-6 Beverages

**Bar Menu:**
- 8-10 Cocktails
- 4-6 Beers
- 6-8 Wines
- 10-15 Spirits
- 4-6 Mocktails
- 5-8 Non-alcoholic drinks

---

## 🔗 Quick Links

**Admin Sections:**
- Rooms: http://127.0.0.1:8000/admin/rooms/room/
- Restaurant: http://127.0.0.1:8000/admin/restaurant/menuitem/
- Bar: http://127.0.0.1:8000/admin/bar/baritem/

**Public Pages:**
- Rooms: http://127.0.0.1:8000/rooms/
- Restaurant: http://127.0.0.1:8000/restaurant/
- Bar: http://127.0.0.1:8000/bar/

---

## ⚡ Common Commands

```powershell
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Change password
python manage.py changepassword admin
```

---

**Need detailed instructions?** See `ADMIN_CONTENT_GUIDE.md`
