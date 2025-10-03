# 🏨 Hotel App - Complete Admin Content Management Guide

This guide explains how to add and manage content for your hotel website using the Django admin panel.

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Adding Rooms](#adding-rooms)
3. [Adding Restaurant Menu Items](#adding-restaurant-menu-items)
4. [Adding Bar Items](#adding-bar-items)
5. [Managing Images](#managing-images)
6. [Tips & Best Practices](#tips--best-practices)

---

## 🚀 Getting Started

### Step 1: Create Admin Account (First Time Only)

If you haven't created an admin account yet:

```powershell
python manage.py createsuperuser
```

**Enter the following when prompted:**
- Username: `admin` (or your preferred username)
- Email: `your-email@example.com`
- Password: [Create a secure password]
- Password confirmation: [Re-enter your password]

### Step 2: Start the Development Server

```powershell
python manage.py runserver
```

### Step 3: Access the Admin Panel

1. Open your web browser
2. Navigate to: **http://127.0.0.1:8000/admin/**
3. Log in with your admin credentials

---

## 🛏️ Adding Rooms

### Overview
Rooms are displayed on the `/rooms/` page of your website. Each room shows its name, description, price, amenities, and image.

### Step-by-Step Instructions

1. **Access the Rooms Section**
   - In the admin panel, click on **"Rooms"** under the ROOMS section
   - Click the **"+ Add Room"** button (top right)

2. **Fill in Basic Information**

   **Name** (Required)
   - Enter the room name/type
   - Examples:
     - `Deluxe King Suite`
     - `Standard Double Room`
     - `Presidential Suite`
     - `Family Room with Garden View`

   **Description** (Required)
   - Write a detailed description of the room
   - Include:
     - Room size
     - Bed configuration
     - View details
     - Special features
   - Example:
     ```
     Spacious 450 sq ft room featuring a plush king-size bed with premium 
     linens, elegant décor, and stunning city views. Perfect for business 
     travelers or couples seeking luxury and comfort. The room includes a 
     work desk, mini-bar, and a marble bathroom with rainfall shower.
     ```

   **Price** (Required)
   - Enter the nightly rate in decimal format
   - Examples: `150.00`, `89.99`, `299.00`
   - This should be per night rate

3. **Add Amenities**

   **Amenities** (Required)
   - List all amenities separated by commas
   - These will be displayed as bullet points on the website
   - Example:
     ```
     Free Wi-Fi, King-size bed, Air conditioning, Flat-screen TV, 
     Mini-bar, Safe, Work desk, Coffee maker, Rainfall shower, 
     City view, Blackout curtains, Daily housekeeping
     ```

4. **Upload Room Image**

   **Image** (Optional but Recommended)
   - Click **"Choose File"** under the Image field
   - Select a high-quality image of the room
   - **Best practices:**
     - Format: JPG or PNG
     - Minimum size: 800x600 pixels
     - Recommended: 1200x800 pixels
     - Keep file size under 2MB
     - Use professional photos

5. **Set Visibility**

   **Is visible** (Checkbox)
   - ✅ Checked: Room appears on the website
   - ⬜ Unchecked: Room is hidden from customers
   - Use this to temporarily hide rooms under maintenance

6. **Save the Room**
   - Click **"Save and add another"** to add more rooms
   - Click **"Save and continue editing"** to stay on this room
   - Click **"Save"** to return to the room list

### Example Room Entry

```
Name: Executive Ocean View Suite
Description: Experience luxury in our 600 sq ft Executive Suite overlooking 
the beautiful ocean. This spacious room features a king-size bed, separate 
living area, and a private balcony. The suite is elegantly furnished with 
contemporary décor and equipped with all modern amenities for an unforgettable stay.

Price: 275.00
Amenities: Ocean view balcony, King-size bed, Separate living area, 
Work desk, 50" Smart TV, Mini-bar, Coffee machine, Safe, Air conditioning, 
Free Wi-Fi, Bathrobes & slippers, Premium toiletries, Rainfall shower, 
Room service
Is visible: ✅ Checked
```

### Managing Existing Rooms

**To Edit a Room:**
1. Go to Rooms list in admin panel
2. Click on the room name
3. Make your changes
4. Click "Save"

**To Delete a Room:**
1. Go to Rooms list
2. Check the box next to the room(s) to delete
3. Select "Delete selected rooms" from the Action dropdown
4. Click "Go" and confirm

**Quick Toggle Visibility:**
- In the rooms list, you can quickly check/uncheck the "Is visible" column
- Click "Save" at the bottom to apply changes

---

## 🍽️ Adding Restaurant Menu Items

### Overview
Menu items are displayed on the `/restaurant/` page, organized by categories (Appetizers, Main Courses, Desserts, Beverages).

### Step-by-Step Instructions

1. **Access the Menu Section**
   - In the admin panel, click on **"Menu items"** under the RESTAURANT section
   - Click the **"+ Add Menu item"** button

2. **Enter Item Information**

   **Name** (Required)
   - Enter the dish name
   - Examples:
     - `Grilled Atlantic Salmon`
     - `Caesar Salad`
     - `Chocolate Lava Cake`
     - `Beef Wellington`

   **Description** (Required)
   - Describe the dish in detail
   - Include:
     - Main ingredients
     - Cooking method
     - Flavors/taste profile
     - Accompaniments
   - Example:
     ```
     Fresh Atlantic salmon fillet, perfectly grilled and served with 
     herb butter, roasted vegetables, and creamy mashed potatoes. 
     Garnished with lemon wedges and fresh dill.
     ```

   **Category** (Required - Dropdown)
   - Select the appropriate category:
     - **Appetizer**: Starters, salads, soups
     - **Main Course**: Main dishes, entrées
     - **Dessert**: Sweet dishes, desserts
     - **Beverage**: Drinks (soft drinks, juices, coffee, tea)

   **Price** (Required)
   - Enter the price in decimal format
   - Examples: `15.99`, `28.50`, `8.00`

3. **Upload Item Image**

   **Image** (Optional but Recommended)
   - Click "Choose File"
   - Select an appetizing photo of the dish
   - **Best practices:**
     - Professional food photography
     - Well-lit and styled
     - Format: JPG or PNG
     - Minimum: 600x600 pixels
     - Square or landscape orientation works best

4. **Set Availability**

   **Is available** (Checkbox)
   - ✅ Checked: Item appears on menu
   - ⬜ Unchecked: Item is hidden (out of stock/seasonal)

5. **Save the Menu Item**
   - Click your preferred save option

### Example Menu Items

**Appetizer Example:**
```
Name: Bruschetta al Pomodoro
Description: Toasted Italian bread topped with fresh tomatoes, garlic, 
basil, and extra virgin olive oil. Finished with balsamic glaze and 
parmesan shavings.
Category: Appetizer
Price: 9.99
Is available: ✅
```

**Main Course Example:**
```
Name: Prime Rib Eye Steak
Description: 12oz USDA Prime rib eye, grilled to perfection. Served 
with your choice of two sides: garlic mashed potatoes, grilled vegetables, 
French fries, or seasonal salad. Topped with herb butter.
Category: Main Course
Price: 42.00
Is available: ✅
```

**Dessert Example:**
```
Name: New York Cheesecake
Description: Classic creamy cheesecake with graham cracker crust, 
topped with fresh strawberry compote and whipped cream.
Category: Dessert
Price: 8.50
Is available: ✅
```

**Beverage Example:**
```
Name: Fresh Squeezed Orange Juice
Description: 100% pure orange juice, freshly squeezed daily. 
Refreshing and packed with vitamin C.
Category: Beverage
Price: 5.00
Is available: ✅
```

### Menu Organization Tips

- **Appetizers**: Start with 4-8 options
- **Main Courses**: Offer 8-12 variety dishes (meat, fish, vegetarian)
- **Desserts**: Include 4-6 sweet options
- **Beverages**: List common drinks

### Managing Menu Items

**Seasonal Items:**
- Uncheck "Is available" for seasonal items when out of season
- Re-enable when back in season

**Sold Out Items:**
- Temporarily uncheck "Is available"
- Re-enable when restocked

**Price Updates:**
- Edit the item and update the price field
- Save to apply changes

---

## 🍺 Adding Bar Items

### Overview
Bar items appear on the `/bar/` page, organized by beverage categories. The bar menu supports both alcoholic and non-alcoholic beverages.

### Step-by-Step Instructions

1. **Access the Bar Section**
   - In the admin panel, click on **"Bar items"** under the BAR section
   - Click the **"+ Add Bar item"** button

2. **Enter Basic Information**

   **Name** (Required)
   - Enter the drink name
   - Examples:
     - `Mojito`
     - `Heineken Beer`
     - `Chardonnay 2021`
     - `Espresso Martini`
     - `Fresh Lemonade`

   **Description** (Required)
   - Describe the beverage
   - For cocktails: List main ingredients
   - For wines/spirits: Include origin, taste notes
   - Example (Cocktail):
     ```
     Classic Cuban cocktail with white rum, fresh lime juice, mint 
     leaves, sugar, and soda water. Refreshing and perfectly balanced.
     ```
   - Example (Wine):
     ```
     California Chardonnay with notes of apple, pear, and vanilla. 
     Medium-bodied with a buttery finish. Pairs well with seafood and poultry.
     ```

   **Price** (Required)
   - Enter the price per serving
   - Examples: `8.00`, `12.50`, `45.00`

3. **Select Category** (Required - Dropdown)

   Choose the appropriate category:
   - **Beer**: Draft beers, bottled beers, craft beers
   - **Wine**: Red, white, rosé, sparkling wines
   - **Spirits & Liquor**: Whiskey, vodka, rum, gin, tequila
   - **Cocktails**: Mixed drinks, signature cocktails
   - **Soft Drinks**: Sodas, colas
   - **Juices**: Fresh juices, fruit drinks
   - **Hot Beverages**: Coffee, tea, hot chocolate
   - **Mocktails**: Non-alcoholic cocktails

4. **Add Alcohol Content** (Optional)

   **Alcohol content** field
   - Specify the alcohol percentage
   - Examples:
     - `40% ABV` (spirits)
     - `12% ABV` (wine)
     - `5.5% ABV` (beer)
     - `Non-alcoholic` (for mocktails, juices)
     - `25% ABV` (cocktails)
   - Leave blank for non-alcoholic beverages

5. **Specify Volume** (Optional)

   **Volume** field
   - Indicate the serving size
   - Examples:
     - `330ml bottle`
     - `750ml bottle`
     - `Glass (150ml)`
     - `Pint (568ml)`
     - `1 oz shot`
     - `12 oz serving`
     - `Carafe (1L)`

6. **Upload Image** (Optional)

   **Image** field
   - Upload a photo of the drink
   - **Best practices:**
     - Professional beverage photography
     - Clean glass, good lighting
     - Format: JPG or PNG
     - Show garnish and presentation

7. **Set Availability and Featured Status**

   **Is available** (Checkbox)
   - ✅ Checked: Item appears on bar menu
   - ⬜ Unchecked: Item is hidden

   **Is featured** (Checkbox)
   - ✅ Checked: Item is highlighted/featured on the bar page
   - ⬜ Unchecked: Regular item
   - Use this for signature drinks or specials

8. **Save the Bar Item**

### Example Bar Items

**Beer Example:**
```
Name: Corona Extra
Description: Popular Mexican lager with a light, crisp taste and a 
touch of sweetness. Best served ice cold with a lime wedge.
Category: Beer
Price: 6.50
Alcohol content: 4.6% ABV
Volume: 330ml bottle
Is available: ✅
Is featured: ⬜
```

**Wine Example:**
```
Name: Merlot Reserve 2019
Description: French Merlot from Bordeaux region. Full-bodied with 
notes of black cherry, plum, and subtle oak. Smooth tannins and 
long finish.
Category: Wine
Price: 55.00
Alcohol content: 13.5% ABV
Volume: 750ml bottle
Is available: ✅
Is featured: ✅
```

**Cocktail Example:**
```
Name: Classic Margarita
Description: Premium tequila, fresh lime juice, and triple sec, 
served on the rocks with a salted rim. Perfectly balanced sweet 
and sour.
Category: Cocktails
Price: 12.00
Alcohol content: 18% ABV
Volume: 10 oz glass
Is available: ✅
Is featured: ✅
```

**Spirits Example:**
```
Name: Jack Daniel's Tennessee Whiskey
Description: Smooth American whiskey with notes of vanilla, toasted 
oak, and caramel. Perfect neat, on the rocks, or in cocktails.
Category: Spirits & Liquor
Price: 10.00
Alcohol content: 40% ABV
Volume: 1.5 oz shot
Is available: ✅
Is featured: ⬜
```

**Mocktail Example:**
```
Name: Virgin Piña Colada
Description: Tropical non-alcoholic blend of coconut cream, 
pineapple juice, and ice. Creamy, sweet, and refreshing. 
Garnished with pineapple wedge and cherry.
Category: Mocktails
Price: 7.00
Alcohol content: Non-alcoholic
Volume: 12 oz glass
Is available: ✅
Is featured: ⬜
```

**Juice Example:**
```
Name: Fresh Mango Smoothie
Description: Pure mango pulp blended with yogurt, honey, and ice. 
Rich, creamy, and naturally sweet. Made to order with fresh ingredients.
Category: Juices
Price: 6.50
Alcohol content: Non-alcoholic
Volume: 16 oz glass
Is available: ✅
Is featured: ⬜
```

### Bar Menu Organization

**Recommended Structure:**
- **Featured Drinks**: 3-5 signature cocktails (mark as featured)
- **Cocktails**: 8-12 options (classic + house specials)
- **Beer**: 4-8 options (local, imported, craft)
- **Wine**: 6-10 options (red, white, sparkling)
- **Spirits**: 10-15 premium options
- **Mocktails**: 4-6 non-alcoholic cocktails
- **Soft Drinks & Juices**: 5-8 options
- **Hot Beverages**: 3-5 coffee/tea options

---

## 📸 Managing Images

### Image Requirements

**Optimal Specifications:**
- **Format**: JPG or PNG
- **Rooms**: 1200x800px (landscape)
- **Menu Items**: 800x800px (square) or 800x600px
- **Bar Items**: 600x800px (portrait) or 800x600px
- **File Size**: Under 2MB each
- **Quality**: High resolution, well-lit, professional

### Where to Find Images

**Free Stock Photo Resources:**
1. **Unsplash** (unsplash.com) - High-quality free images
2. **Pexels** (pexels.com) - Free stock photos
3. **Pixabay** (pixabay.com) - Free images and videos

**Search Terms:**
- Rooms: "hotel room", "luxury bedroom", "suite interior"
- Food: "restaurant food", "[dish name]", "gourmet food"
- Drinks: "cocktail", "beer glass", "wine bottle", "[drink name]"

### Uploading Images

1. In the admin form, find the **Image** field
2. Click **"Choose File"** or **"Browse"**
3. Select your image file
4. The image uploads when you save the item
5. You'll see a preview thumbnail after saving

### Updating Images

1. Edit the item
2. Click **"Choose File"** next to the current image
3. Select a new image
4. Save the changes

### Removing Images

1. Edit the item
2. Check the **"Clear"** checkbox next to the image
3. Save the changes

---

## 💡 Tips & Best Practices

### General Content Tips

1. **Be Descriptive**: Use vivid, appealing language
2. **Check Spelling**: Proofread all text before saving
3. **Use Consistent Pricing**: Format prices uniformly (e.g., always 2 decimals)
4. **Update Regularly**: Keep menu items and availability current
5. **Professional Photos**: Invest in quality images for better appeal

### Writing Effective Descriptions

**Do:**
- ✅ Use sensory language (taste, texture, aroma)
- ✅ Highlight unique features or ingredients
- ✅ Keep it concise but informative (2-4 sentences)
- ✅ Mention accompaniments or sides

**Don't:**
- ❌ Use overly technical jargon
- ❌ Make exaggerated claims
- ❌ Copy descriptions from other websites
- ❌ Leave descriptions generic or vague

### Pricing Strategy

- **Rooms**: Consider per-night rates, seasonal pricing
- **Restaurant**: Price based on portion size and ingredients
- **Bar**: Standard drink prices, premium options cost more
- **Consistency**: Ensure prices are competitive and realistic

### Visibility Management

**Use the visibility toggles strategically:**
- **Seasonal Items**: Disable when out of season
- **Renovations**: Hide rooms under maintenance
- **Stock Issues**: Temporarily hide sold-out items
- **Testing**: Hide new items until ready to launch

### Content Workflow

**Recommended Process:**
1. Gather all information (descriptions, prices, images)
2. Prepare images (resize, optimize)
3. Add multiple items in one session
4. Review all entries for consistency
5. Check the public website to verify display
6. Make adjustments as needed

### Regular Maintenance

**Weekly:**
- Review availability status
- Check for sold-out items
- Update specials or featured items

**Monthly:**
- Review pricing
- Update seasonal menu items
- Refresh images if needed
- Add new items based on customer feedback

**Quarterly:**
- Full menu review
- Update room descriptions if renovated
- Archive old/discontinued items

---

## 🔧 Troubleshooting

### Images Not Displaying?

**Check:**
1. File size is under 2MB
2. Format is JPG or PNG
3. Image uploaded successfully (thumbnail visible in admin)
4. Item is marked as "available" or "visible"

### Item Not Showing on Website?

**Verify:**
1. Item is marked as available/visible
2. Server is running (`python manage.py runserver`)
3. Clear browser cache and refresh
4. Check correct URL (/rooms/, /restaurant/, /bar/)

### Can't Log In to Admin?

**Solution:**
- Reset password using: `python manage.py changepassword <username>`
- Or create new superuser: `python manage.py createsuperuser`

---

## 📞 Quick Reference

### Admin URLs
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Rooms Management**: http://127.0.0.1:8000/admin/rooms/room/
- **Restaurant Menu**: http://127.0.0.1:8000/admin/restaurant/menuitem/
- **Bar Items**: http://127.0.0.1:8000/admin/bar/baritem/

### Public URLs
- **Rooms Page**: http://127.0.0.1:8000/rooms/
- **Restaurant Page**: http://127.0.0.1:8000/restaurant/
- **Bar Page**: http://127.0.0.1:8000/bar/

### Common Commands

```powershell
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Change admin password
python manage.py changepassword admin

# Apply database changes
python manage.py migrate
```

---

## 🎯 Getting Started Checklist

**Initial Setup:**
- [ ] Create superuser account
- [ ] Start development server
- [ ] Log in to admin panel

**Add Content:**
- [ ] Add 3-5 rooms with images
- [ ] Add 10-15 menu items across all categories
- [ ] Add 15-20 bar items across all categories
- [ ] Mark 2-3 drinks as featured

**Review:**
- [ ] Check all items display correctly on public pages
- [ ] Verify all images load properly
- [ ] Test visibility toggles
- [ ] Ensure pricing displays correctly

---

## 📚 Additional Resources

- **Django Admin Documentation**: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
- **Django Models**: https://docs.djangoproject.com/en/stable/topics/db/models/
- **Image Optimization Tools**: TinyPNG.com, ImageOptim

---

**Need Help?**

If you encounter any issues or have questions about managing content, refer to the Django documentation or check your application's README.md file.

**Last Updated**: October 2025
