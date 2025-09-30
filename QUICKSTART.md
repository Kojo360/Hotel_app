# 🏨 Hotel Management Web Application

A complete Django-based hotel management system with admin dashboard and public website.

## 🚀 Quick Start (5 Minutes)

### Option 1: Automated Setup (Recommended)

Run the PowerShell setup script:

```powershell
.\setup.ps1
```

This will automatically:
- Create virtual environment
- Install dependencies
- Set up environment variables
- Create database
- Prompt you to create admin user
- Start the server (optional)

### Option 2: Manual Setup

1. **Create and activate virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Copy environment file:**
   ```powershell
   copy .env.example .env
   ```
   Then edit `.env` and set your `WHATSAPP_PHONE` number.

4. **Create database:**
   ```powershell
   python manage.py migrate
   ```

5. **Create admin user:**
   ```powershell
   python manage.py createsuperuser
   ```

6. **Run the server:**
   ```powershell
   python manage.py runserver
   ```

## 🌐 Access the Application

- **Public Website**: http://127.0.0.1:8000/
- **Admin Dashboard**: http://127.0.0.1:8000/admin/

## 📋 First Steps After Setup

1. **Login to Admin Dashboard** at http://127.0.0.1:8000/admin/
2. **Add Some Rooms**:
   - Click "Rooms" → "Add Room"
   - Fill in name, description, price, amenities
   - Upload an image (optional)
   - Make sure "Is visible" is checked
   - Save

3. **Add Menu Items** (optional):
   - Click "Menu items" → "Add menu item"
   - Add food items with prices and images

4. **Test the Public Website**:
   - Visit http://127.0.0.1:8000/
   - Browse rooms
   - Try booking a room
   - Check WhatsApp integration

## 📁 Project Structure

```
hotel_app/
├── hotel_app/          # Project settings
│   ├── settings.py     # Configuration
│   └── urls.py         # Main URL routing
├── rooms/              # Room management
│   ├── models.py       # Room & Booking models
│   ├── views.py        # Room views
│   ├── forms.py        # Booking form
│   └── admin.py        # Admin customization
├── restaurant/         # Menu management
│   ├── models.py       # MenuItem model
│   ├── views.py        # Menu views
│   └── admin.py        # Admin customization
├── pages/              # Static pages
│   ├── models.py       # Complaint model
│   ├── views.py        # Home & Contact views
│   ├── forms.py        # Complaint form
│   └── admin.py        # Admin customization
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── pages/          # Homepage & contact
│   ├── rooms/          # Room templates
│   └── restaurant/     # Menu templates
├── static/             # CSS, JS, images
└── media/              # User uploads
```

## ✨ Key Features

### For Admins:
- ✅ Manage rooms (add, edit, delete)
- ✅ Toggle room visibility
- ✅ Manage restaurant menu
- ✅ View booking requests
- ✅ View customer complaints
- ✅ Upload images for rooms and menu

### For Customers:
- ✅ Browse available rooms
- ✅ Book rooms via WhatsApp
- ✅ View restaurant menu
- ✅ Contact hotel
- ✅ Submit complaints
- ✅ View location on map

## 🔧 Configuration

Edit `.env` file to configure:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
WHATSAPP_PHONE=1234567890
```

Replace `WHATSAPP_PHONE` with your actual WhatsApp number (with country code, no + or spaces).

## 📚 Documentation

- **SETUP.md** - Detailed setup instructions
- **README.md** - Complete project documentation
- **USER_STORIES_IMPLEMENTATION.md** - Feature implementation details

## 🐛 Troubleshooting

**Import Errors?**
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Database Issues?**
```powershell
python manage.py migrate
```

**WhatsApp Not Working?**
- Check your `WHATSAPP_PHONE` in `.env`
- Format: country code + number (e.g., 1234567890)
- No spaces or special characters

## 🚀 Production Deployment

See **SETUP.md** for production deployment checklist.

## 🎯 Next Steps

1. Customize hotel name and branding
2. Add real hotel photos
3. Update contact information
4. Configure your WhatsApp number
5. Update Google Maps location
6. Add more rooms and menu items

## 📞 Support

For issues or questions, see the documentation files or check Django's official documentation at https://docs.djangoproject.com/

---

**Built with Django 4.2 | Bootstrap 5 | Python 3.8+**

Enjoy managing your hotel! 🏨✨
