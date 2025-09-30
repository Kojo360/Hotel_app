# 🚀 Quick Start: Adding Content to AGYEI TWUM LODGE

## 1️⃣ CREATE ADMIN ACCOUNT (First Time Only)

```powershell
python manage.py createsuperuser
```
- Username: `admin`
- Email: `your-email@example.com`
- Password: [secure password]

---

## 2️⃣ START SERVER

```powershell
python manage.py runserver
```

---

## 3️⃣ OPEN ADMIN PANEL

**URL:** http://127.0.0.1:8000/admin/

**Login with your admin credentials**

---

## 4️⃣ ADD A ROOM

### Steps:
1. Click **"Rooms"** under ROOMS section
2. Click **"+ Add Room"** button
3. Fill in the form:

### Required Fields:
- **Name**: e.g., "Deluxe Suite"
- **Price**: e.g., `299.99` (no $ symbol)
- **Description**: 2-3 sentences about the room
- **Amenities**: Comma-separated list
  - Example: `King Bed, Ocean View, WiFi, TV, Mini Bar, Balcony, Safe`

### Optional:
- **Image**: Upload room photo (JPG/PNG, 800x600px minimum)
- **Is visible**: ✅ Keep checked to show on website

4. Click **"SAVE"**

### Room Examples:

**Budget Room:**
```
Name: Standard Double Room
Price: 149.99
Amenities: Queen Bed, WiFi, TV, Coffee Maker, Air Conditioning
Description: Comfortable room with modern amenities, perfect for short stays.
```

**Luxury Room:**
```
Name: Presidential Suite
Price: 599.99
Amenities: King Bed, Ocean View, Private Balcony, Jacuzzi, WiFi, Smart TV, Mini Bar, Safe, Living Room
Description: Ultimate luxury suite with breathtaking views, separate living area, and premium amenities.
```

---

## 5️⃣ ADD MENU ITEMS

### Steps:
1. Click **"Menu items"** under RESTAURANT section
2. Click **"+ Add Menu Item"** button
3. Fill in the form:

### Required Fields:
- **Name**: e.g., "Grilled Salmon"
- **Price**: e.g., `28.99` (no $ symbol)
- **Description**: Appetizing description
- **Category**: Select one:
  - Appetizer
  - Main Course
  - Dessert
  - Beverage

### Optional:
- **Image**: Upload food photo (JPG/PNG)
- **Is available**: ✅ Keep checked

4. Click **"SAVE"**

### Menu Item Examples:

**Appetizer:**
```
Name: Caesar Salad
Price: 12.99
Category: Appetizer
Description: Crisp romaine lettuce, parmesan cheese, croutons, homemade Caesar dressing
```

**Main Course:**
```
Name: Grilled Atlantic Salmon
Price: 28.99
Category: Main Course
Description: Fresh salmon grilled to perfection, served with roasted vegetables and lemon butter sauce
```

**Dessert:**
```
Name: Chocolate Lava Cake
Price: 9.99
Category: Dessert
Description: Warm chocolate cake with molten center, vanilla ice cream, fresh berries
```

**Beverage:**
```
Name: Cappuccino
Price: 4.99
Category: Beverage
Description: Rich espresso with steamed milk and foam, perfectly balanced
```

---

## 6️⃣ VIEW YOUR WEBSITE

**Home:** http://127.0.0.1:8000/  
**Rooms:** http://127.0.0.1:8000/rooms/  
**Restaurant:** http://127.0.0.1:8000/restaurant/  

---

## ⚡ Pro Tips

### Amenities to Use:
```
King Bed, Queen Bed, Twin Beds
Ocean View, Mountain View, City View, Garden View
WiFi, Smart TV, Flat Screen TV
Air Conditioning, Heating
Private Balcony, Terrace
Mini Bar, Mini Fridge, Coffee Maker
Safe, Work Desk, Seating Area
Private Bathroom, Rain Shower, Bathtub
Room Service, Daily Housekeeping
```

### Common Issues:

**Can't see items on website?**
- Make sure "Is visible" or "Is available" is checked ✅
- Click "Save" after changes
- Refresh browser (Ctrl + F5)

**Amenities showing as one text?**
- Use commas: `WiFi, TV, Mini Bar` ✅
- Not: `WiFi TV Mini Bar` ❌

**Image not showing?**
- Check file size (under 5MB)
- Use JPG or PNG format
- Image uploads to `media/rooms/` or `media/menu/`

---

## 📝 Quick Workflow (30 minutes)

1. **Create admin account** (2 min)
2. **Add 3-5 rooms** (10 min)
3. **Add 10-15 menu items** (15 min)
   - 3 appetizers
   - 5 main courses
   - 2 desserts
   - 2 beverages
4. **Test website** (3 min)

---

## 🎯 Sample Complete Setup

### Rooms (5 types):
1. **Standard Room** - $149.99
2. **Deluxe Room** - $199.99
3. **Suite** - $299.99
4. **Family Suite** - $399.99
5. **Presidential Suite** - $599.99

### Menu (12 items):

**Appetizers:**
- Caesar Salad - $12.99
- French Onion Soup - $8.99
- Shrimp Cocktail - $14.99

**Main Courses:**
- Grilled Salmon - $28.99
- Ribeye Steak - $38.99
- Chicken Parmesan - $22.99
- Vegetable Lasagna - $18.99
- BBQ Ribs - $26.99

**Desserts:**
- Chocolate Lava Cake - $9.99
- Tiramisu - $8.99

**Beverages:**
- Cappuccino - $4.99
- Fresh Orange Juice - $5.99

---

## 🔄 Editing Content

1. Go to admin: http://127.0.0.1:8000/admin/
2. Click on "Rooms" or "Menu items"
3. Click item name to edit
4. Make changes
5. Click "Save"

---

## ❓ Need Help?

See the complete guide: **ADMIN_GUIDE.md**

---

**Ready to start? Follow the steps above!** 🎉

1. Create admin account
2. Start server
3. Open admin panel
4. Add rooms
5. Add menu items
6. View your website

**It's that simple!** 🚀
