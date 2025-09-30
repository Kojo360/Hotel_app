# 📘 Complete Guide: Adding Rooms & Restaurant Menu Items

## 🏨 AGYEI TWUM LODGE - Admin Management Guide

This guide will show you exactly how to add rooms with amenities and restaurant menu items to your hotel website.

---

## 📋 Table of Contents

1. [Getting Started - Creating Admin Account](#step-1-create-admin-account)
2. [Accessing the Admin Panel](#step-2-access-admin-panel)
3. [Adding Rooms with Amenities](#step-3-adding-rooms)
4. [Adding Restaurant Menu Items](#step-4-adding-menu-items)
5. [Managing Images](#step-5-managing-images)
6. [Tips & Best Practices](#tips-and-best-practices)

---

## Step 1: Create Admin Account

### If you DON'T have an admin account yet:

1. **Open PowerShell/Terminal** in VS Code (Ctrl + `)

2. **Run this command:**
   ```powershell
   python manage.py createsuperuser
   ```

3. **Follow the prompts:**
   ```
   Username: admin
   Email address: your-email@example.com
   Password: [enter a secure password]
   Password (again): [confirm password]
   ```

4. **You'll see:** `Superuser created successfully.`

### If you ALREADY have an admin account:
Skip to Step 2!

---

## Step 2: Access Admin Panel

### Opening the Admin Dashboard:

1. **Make sure your server is running:**
   ```powershell
   python manage.py runserver
   ```
   
   You should see:
   ```
   Starting development server at http://127.0.0.1:8000/
   ```

2. **Open your web browser**

3. **Go to the admin URL:**
   ```
   http://127.0.0.1:8000/admin/
   ```

4. **Log in** with your superuser credentials:
   - Username: `admin` (or whatever you created)
   - Password: [your password]

5. **You should see the Django Administration page** with sections like:
   - Authentication and Authorization
   - Pages
   - Restaurant
   - Rooms

---

## Step 3: Adding Rooms

### 3.1 Navigate to Rooms Section

1. **On the admin dashboard**, find the **"ROOMS"** section
2. Click on **"Rooms"** (you'll see "+ Add" and "Change" links)
3. Click **"+ Add"** or the **"ADD ROOM"** button

### 3.2 Fill in Room Details

You'll see a form with these fields:

#### **Name** (Required)
- Enter the room name
- Examples:
  - "Deluxe Suite"
  - "Presidential Suite"
  - "Standard Double Room"
  - "Family Suite"
  - "Executive Single Room"

#### **Description** (Required)
- Write a detailed description of the room
- Example:
  ```
  Spacious and elegantly furnished suite featuring a king-size bed, 
  stunning ocean view, private balcony, marble bathroom with rain 
  shower, luxury amenities, and modern entertainment system. Perfect 
  for couples seeking a romantic getaway.
  ```

#### **Price** (Required)
- Enter the price per night
- Enter numbers only (no currency symbols)
- Examples: `150.00`, `299.99`, `450.00`

#### **Amenities** (Required)
- **IMPORTANT**: Enter amenities separated by commas
- Examples:
  ```
  King Bed, Ocean View, Private Balcony, WiFi, Smart TV, Mini Bar, Safe, Coffee Maker, Air Conditioning
  ```
  ```
  Two Queen Beds, Mountain View, WiFi, TV, Mini Fridge, Hair Dryer, Iron, Work Desk
  ```
  ```
  Queen Bed, City View, Free WiFi, Flat Screen TV, Coffee Maker, Air Conditioning, Room Service
  ```

**Popular Amenities to Include:**
- Bed types: King Bed, Queen Bed, Twin Beds, Double Bed
- Views: Ocean View, Mountain View, City View, Garden View, Pool View
- Technology: WiFi, Smart TV, Flat Screen TV, Bluetooth Speaker
- Comfort: Air Conditioning, Heating, Ceiling Fan, Blackout Curtains
- Bathroom: Private Bathroom, Rain Shower, Bathtub, Hair Dryer, Luxury Toiletries
- Convenience: Mini Bar, Mini Fridge, Coffee Maker, Safe, Iron & Ironing Board
- Furniture: Work Desk, Seating Area, Balcony, Sofa
- Services: Room Service, Daily Housekeeping, Turndown Service

#### **Image** (Optional)
- Click **"Choose File"** to upload a room photo
- **Recommended:**
  - Format: JPG or PNG
  - Size: At least 800x600 pixels
  - Good quality, well-lit photos
- If you don't have a photo yet, leave it blank (placeholder image will show)

#### **Is visible** (Required)
- ✅ **Checked** = Room appears on the website
- ❌ **Unchecked** = Room is hidden (for rooms under renovation, etc.)
- **Default**: Checked

### 3.3 Save the Room

1. **Click the "SAVE" button** at the bottom
2. You'll see a success message: "The room [Room Name] was added successfully."
3. The room now appears on your website at: `http://127.0.0.1:8000/rooms/`

### 3.4 Add More Rooms

Repeat the process to add all your rooms. Here are some example room configurations:

**Example 1: Deluxe Suite**
- Name: `Deluxe Suite`
- Price: `299.99`
- Amenities: `King Bed, Ocean View, Private Balcony, WiFi, Smart TV, Mini Bar, Safe, Coffee Maker, Air Conditioning, Rain Shower, Seating Area`
- Description: Luxurious suite with breathtaking ocean views...

**Example 2: Standard Room**
- Name: `Standard Double Room`
- Price: `149.99`
- Amenities: `Queen Bed, WiFi, TV, Coffee Maker, Air Conditioning, Private Bathroom, Work Desk`
- Description: Comfortable and cozy room perfect for business travelers...

**Example 3: Family Suite**
- Name: `Family Suite`
- Price: `399.99`
- Amenities: `King Bed, Two Twin Beds, Living Room, Kitchenette, WiFi, Two TVs, Mini Fridge, Balcony, Air Conditioning`
- Description: Spacious suite ideal for families with separate sleeping areas...

---

## Step 4: Adding Menu Items

### 4.1 Navigate to Restaurant Section

1. **On the admin dashboard**, find the **"RESTAURANT"** section
2. Click on **"Menu items"**
3. Click **"+ Add"** or the **"ADD MENU ITEM"** button

### 4.2 Fill in Menu Item Details

You'll see a form with these fields:

#### **Name** (Required)
- Enter the dish name
- Examples:
  - "Grilled Atlantic Salmon"
  - "Caesar Salad"
  - "Chocolate Lava Cake"
  - "Cappuccino"

#### **Description** (Required)
- Write a mouth-watering description
- Examples:
  ```
  Fresh Atlantic salmon grilled to perfection, served with roasted 
  vegetables, garlic mashed potatoes, and lemon butter sauce.
  ```
  ```
  Crisp romaine lettuce tossed with our homemade Caesar dressing, 
  parmesan cheese, and garlic croutons.
  ```
  ```
  Warm chocolate cake with a molten center, served with vanilla 
  ice cream and fresh berries.
  ```

#### **Price** (Required)
- Enter the price
- Enter numbers only
- Examples: `12.99`, `28.50`, `9.99`

#### **Image** (Optional)
- Click **"Choose File"** to upload a food photo
- **Recommended:**
  - Format: JPG or PNG
  - Size: At least 800x600 pixels
  - High-quality, appetizing food photography
- If no image, a placeholder will show

#### **Category** (Required)
- **Select from dropdown:**
  - **Appetizer** - Starters, salads, soups
  - **Main Course** - Main dishes, entrees
  - **Dessert** - Sweet treats, desserts
  - **Beverage** - Drinks, coffee, tea, juices

**Category Examples:**

**Appetizers:**
- Caesar Salad
- French Onion Soup
- Bruschetta
- Spring Rolls
- Shrimp Cocktail

**Main Courses:**
- Grilled Salmon
- Ribeye Steak
- Chicken Parmesan
- Vegetable Stir Fry
- Pasta Carbonara

**Desserts:**
- Chocolate Lava Cake
- Tiramisu
- Cheesecake
- Ice Cream Sundae
- Fruit Tart

**Beverages:**
- Cappuccino
- Fresh Orange Juice
- Iced Tea
- Mineral Water
- House Wine

#### **Is available** (Required)
- ✅ **Checked** = Item appears on menu
- ❌ **Unchecked** = Item hidden (for seasonal items, out of stock)
- **Default**: Checked

### 4.3 Save the Menu Item

1. **Click the "SAVE" button** at the bottom
2. You'll see: "The menu item [Item Name] was added successfully."
3. The item appears on: `http://127.0.0.1:8000/restaurant/`

### 4.4 Add More Menu Items

Create a complete menu with items in each category:

**Sample Menu Structure:**

**Appetizers (5-8 items):**
1. Caesar Salad - $12.99
2. French Onion Soup - $8.99
3. Bruschetta - $10.99
4. Shrimp Cocktail - $14.99
5. Spring Rolls - $9.99

**Main Courses (8-12 items):**
1. Grilled Salmon - $28.99
2. Ribeye Steak - $38.99
3. Chicken Parmesan - $22.99
4. Lobster Thermidor - $45.99
5. Vegetable Lasagna - $18.99
6. BBQ Ribs - $26.99

**Desserts (4-6 items):**
1. Chocolate Lava Cake - $9.99
2. Tiramisu - $8.99
3. Cheesecake - $8.99
4. Crème Brûlée - $10.99

**Beverages (6-10 items):**
1. Cappuccino - $4.99
2. Espresso - $3.99
3. Fresh Orange Juice - $5.99
4. Iced Tea - $3.99
5. House Wine - $8.99

---

## Step 5: Managing Images

### Best Practices for Images:

#### For Room Photos:
- **Resolution**: Minimum 1200x800 pixels
- **Format**: JPG (smaller file size) or PNG (if transparency needed)
- **Quality**: High quality, well-lit, professionally shot if possible
- **Content**: Show the room from different angles, highlight features
- **File Size**: Keep under 2MB for faster loading

#### For Food Photos:
- **Resolution**: Minimum 800x600 pixels
- **Format**: JPG recommended
- **Quality**: High quality, good lighting, appetizing presentation
- **Content**: Close-up of the dish, garnished nicely
- **File Size**: Keep under 1MB

### How to Upload Images:

**Method 1: During Creation**
1. When adding a room/menu item, click "Choose File" under the Image field
2. Browse to your image file
3. Select it and click "Open"
4. Save the room/menu item

**Method 2: After Creation**
1. Go to the list of rooms or menu items
2. Click on the item name to edit it
3. Scroll to the Image field
4. Click "Choose File" and select your image
5. Click "Save"

**Method 3: Bulk Update**
1. Add items without images first
2. Go back and add images later when you have them ready

### Where Images Are Stored:
- Room images: `d:\hotel_app\media\rooms\`
- Menu images: `d:\hotel_app\media\menu\`

---

## Step 6: Editing & Managing

### Editing Existing Items:

1. **Go to admin panel**: `http://127.0.0.1:8000/admin/`
2. **Click on "Rooms" or "Menu items"**
3. **Click on the item name** you want to edit
4. **Make your changes**
5. **Click "SAVE"**

### Deleting Items:

1. **Go to the item edit page**
2. **Scroll to bottom**
3. **Click "Delete" button** (red)
4. **Confirm deletion**

### Bulk Actions:

1. **On the list page**, check the boxes next to items
2. **Select action** from dropdown (e.g., "Delete selected items")
3. **Click "Go"**
4. **Confirm action**

### Hiding Items Temporarily:

**For Rooms:**
- Edit the room
- Uncheck "Is visible"
- Save (room won't appear on website but data is preserved)

**For Menu Items:**
- Edit the item
- Uncheck "Is available"
- Save (item won't appear on menu)

---

## Tips and Best Practices

### 📝 Writing Good Descriptions:

**Rooms:**
- Mention bed type and size
- Highlight unique features (view, balcony, etc.)
- Include comfort features (AC, heating)
- Mention capacity (sleeps how many)
- Keep it 2-3 sentences, clear and enticing

**Menu Items:**
- Describe main ingredients
- Mention cooking method (grilled, baked, etc.)
- Include accompaniments (sides, sauces)
- Use appetizing adjectives (fresh, tender, crispy)
- Keep it concise but descriptive

### 💰 Pricing Strategy:

- Use consistent decimal places (.99 or .00)
- Price competitively based on your market
- Consider bundling (room + breakfast)
- Update seasonally if needed

### 📸 Photography Tips:

**Rooms:**
- Shoot during the day with natural light
- Clean and stage the room first
- Multiple angles: bed, bathroom, view
- Show amenities in use

**Food:**
- Natural lighting is best
- Use clean, simple plates/backgrounds
- Fresh ingredients look better
- Show portion size accurately

### 🎯 Organization:

**Rooms:**
- Start with 3-5 room types
- Add more as you expand
- Keep naming consistent (Standard, Deluxe, Suite)
- Order by price (budget to luxury)

**Menu:**
- Balance categories (don't overload one category)
- Include vegetarian/vegan options
- Mark popular items in description
- Update seasonally

---

## Quick Reference Checklists

### ✅ Adding a Room Checklist:
- [ ] Room name (clear and descriptive)
- [ ] Price (per night, no currency symbol)
- [ ] Description (2-3 sentences)
- [ ] Amenities (comma-separated list)
- [ ] Image uploaded (optional but recommended)
- [ ] "Is visible" checked
- [ ] Saved successfully

### ✅ Adding a Menu Item Checklist:
- [ ] Item name (dish name)
- [ ] Price (no currency symbol)
- [ ] Description (appetizing, descriptive)
- [ ] Category selected (Appetizer, Main, Dessert, or Beverage)
- [ ] Image uploaded (optional but recommended)
- [ ] "Is available" checked
- [ ] Saved successfully

---

## Common Issues & Solutions

### Issue: "Can't log in to admin"
**Solution:**
- Make sure you created a superuser: `python manage.py createsuperuser`
- Check username and password
- Make sure server is running

### Issue: "Admin page not loading"
**Solution:**
- Check server is running: `python manage.py runserver`
- Go to correct URL: `http://127.0.0.1:8000/admin/`
- Check for errors in terminal

### Issue: "Images not appearing on website"
**Solution:**
- Make sure you uploaded the image in admin
- Check file size (should be under 5MB)
- Check image format (JPG or PNG)
- Hard refresh browser: Ctrl + F5

### Issue: "Amenities showing as one long text"
**Solution:**
- Make sure you separated amenities with commas
- Example: `WiFi, TV, Mini Bar` (not `WiFi TV Mini Bar`)

### Issue: "Room/Menu item not showing on website"
**Solution:**
- Check "Is visible" or "Is available" is checked
- Click "Save" after making changes
- Refresh the website page

---

## Example Workflow

### Complete Setup (30-45 minutes):

**Step 1: Create Admin Account (2 minutes)**
```powershell
python manage.py createsuperuser
```

**Step 2: Add 5 Rooms (15 minutes)**
- Deluxe Suite - $299.99
- Standard Room - $149.99
- Family Suite - $399.99
- Executive Single - $179.99
- Presidential Suite - $599.99

**Step 3: Add 15 Menu Items (20 minutes)**
- 4 Appetizers
- 6 Main Courses
- 3 Desserts
- 2 Beverages

**Step 4: Upload Images (10 minutes)**
- Go back and add images to rooms
- Add images to menu items

**Step 5: Test Website (5 minutes)**
- Visit rooms page
- Visit restaurant page
- Test booking form
- Check mobile view

---

## Advanced Tips

### Creating Special Offers:
- Add "SPECIAL OFFER" in room description
- Use promotional pricing
- Update "Is visible" to create flash sales

### Seasonal Menu Updates:
- Uncheck "Is available" for off-season items
- Add seasonal specials
- Update descriptions with seasonal ingredients

### Managing Bookings:
- Check "Bookings" in admin to see customer requests
- View booking details: guest name, dates, contact info
- Export booking data if needed

---

## Quick Start Commands

```powershell
# Start server
python manage.py runserver

# Create admin account
python manage.py createsuperuser

# Open admin in browser
# http://127.0.0.1:8000/admin/

# View website
# http://127.0.0.1:8000/
```

---

## Support & Resources

### Django Admin Documentation:
- https://docs.djangoproject.com/en/stable/ref/contrib/admin/

### Your Website URLs:
- **Home**: http://127.0.0.1:8000/
- **Rooms**: http://127.0.0.1:8000/rooms/
- **Restaurant**: http://127.0.0.1:8000/restaurant/
- **Admin**: http://127.0.0.1:8000/admin/

---

## You're Ready! 🎉

Follow this guide step-by-step, and you'll have your rooms and restaurant menu fully set up in less than an hour!

**Start with:**
1. Create admin account
2. Add 2-3 rooms
3. Add 5-6 menu items
4. Test on the website
5. Add more content gradually

**Remember:** You can always edit, add, or remove items anytime through the admin panel!

---

**Last Updated**: September 30, 2025  
**For**: AGYEI TWUM LODGE  
**Status**: Ready to use! 🚀
