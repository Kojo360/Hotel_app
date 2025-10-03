# Hotel Management Web Application

A Django-based hotel management system that allows admins to manage rooms and restaurant menus, while users can browse, book rooms, and submit complaints.

## Features

### Admin Features
- Manage hotel rooms (add, edit, delete, toggle visibility)
- Manage restaurant menu items with images
- View booking requests via WhatsApp
- View customer complaints

### User Features
- Browse available rooms with images and amenities
- Submit booking requests (sent to WhatsApp)
- View restaurant menu
- Submit complaints via contact form
- View hotel contact information and location

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root with the following:**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   WHATSAPP_PHONE=your-whatsapp-number-with-country-code
   ```

5. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Main website: http://127.0.0.1:8000/
   - Admin dashboard: http://127.0.0.1:8000/admin/

## Project Structure

```
hotel_app/
├── hotel_app/          # Main project settings
├── rooms/              # Room management and bookings
├── restaurant/         # Menu management
├── pages/              # Homepage and contact pages
├── static/             # CSS, JS, images
├── media/              # User uploaded images
└── templates/          # HTML templates
```

## Usage

### Admin Dashboard
1. Login at `/admin/` with your superuser credentials
2. Manage rooms: Add/edit room details, upload images, set prices
3. Toggle room visibility to control what users see
4. Manage restaurant menu items
5. View submitted complaints

### User Experience
1. Browse rooms on the Rooms page
2. Click "Book Now" to fill out a booking form
3. Booking details are sent to the hotel's WhatsApp
4. Browse restaurant menu with pictures
5. Submit complaints via the Contact page

## WhatsApp Integration

When a user submits a booking, they are redirected to WhatsApp with a pre-filled message containing:
- Room name
- Guest name and contact
- Check-in and check-out dates
- Special requests

The admin receives this message directly on WhatsApp for confirmation.

## Technologies Used

- Django 4.2
- Bootstrap 5
- Django Crispy Forms
- SQLite (default, can be changed to PostgreSQL/MySQL)
- Pillow (for image handling)

## 📚 Documentation

Comprehensive guides are available to help you manage your hotel website:

### For Content Managers

- **[Admin Content Guide](ADMIN_CONTENT_GUIDE.md)** - Complete guide on how to add rooms, menu items, and bar items with detailed examples
- **[Quick Reference](QUICK_REFERENCE.md)** - Quick reference card for adding content
- **[Sample Content](SAMPLE_CONTENT.md)** - Ready-to-use example content you can copy and paste
- **[Workflow Guide](WORKFLOW_GUIDE.md)** - Step-by-step workflows and best practices

### Quick Start for Admins

1. **Create your admin account:**
   ```powershell
   python manage.py createsuperuser
   ```

2. **Start the server:**
   ```powershell
   python manage.py runserver
   ```

3. **Access the admin panel:**
   - Go to http://127.0.0.1:8000/admin/
   - Login with your credentials

4. **Start adding content:**
   - Add 3-5 rooms
   - Add 10-15 restaurant menu items
   - Add 15-20 bar items

For detailed instructions, see the [Admin Content Guide](ADMIN_CONTENT_GUIDE.md).

## License

This project is open source and available for educational purposes.
