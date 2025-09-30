# Hotel App Setup Guide

## Quick Start

Follow these steps to get the hotel management web application up and running:

### 1. Install Python Dependencies

First, make sure you're in the project directory and have activated your virtual environment:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy the example environment file and update it with your values:

```powershell
copy .env.example .env
```

Edit the `.env` file and set:
- `SECRET_KEY`: A secure random string (you can generate one at https://djecrety.ir/)
- `DEBUG`: Set to `True` for development, `False` for production
- `WHATSAPP_PHONE`: Your WhatsApp number with country code (e.g., 1234567890)

### 3. Create Database and Tables

Run Django migrations to create the database:

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User

Create a superuser account to access the admin dashboard:

```powershell
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email address
- Password

### 5. Run the Development Server

Start the Django development server:

```powershell
python manage.py runserver
```

The application will be available at:
- **Main Website**: http://127.0.0.1:8000/
- **Admin Dashboard**: http://127.0.0.1:8000/admin/

### 6. Add Sample Data (Optional)

To test the application, you can:

1. Login to the admin dashboard at http://127.0.0.1:8000/admin/
2. Add some rooms with details, prices, and images
3. Add menu items to the restaurant section
4. Make rooms visible to display them on the website

## Application Features

### For Admins:
- Login at `/admin/` with your superuser credentials
- Manage rooms (add, edit, delete, toggle visibility)
- Upload room images and set amenities
- Manage restaurant menu items with pictures
- View booking requests (also sent to WhatsApp)
- View customer complaints submitted via contact form

### For Users:
- Browse available rooms with images and amenities
- Submit booking requests (redirected to WhatsApp for confirmation)
- View restaurant menu with pictures and prices
- Contact hotel and view location on map
- Submit complaints/feedback via contact form

## Troubleshooting

### Import Errors
If you see import errors, make sure you've activated the virtual environment and installed all dependencies:
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Database Errors
If you encounter database errors, try:
```powershell
python manage.py migrate
```

### Static Files Not Loading
In production, collect static files:
```powershell
python manage.py collectstatic
```

## Next Steps

1. Customize the hotel name, logo, and branding in templates
2. Update the Google Maps embed with your actual location
3. Add your actual contact information (phone, email, address)
4. Upload real photos of your hotel and rooms
5. Configure WhatsApp number for booking notifications
6. Consider deploying to a production server (Heroku, DigitalOcean, AWS, etc.)

## Production Deployment

Before deploying to production:

1. Set `DEBUG=False` in `.env`
2. Update `ALLOWED_HOSTS` in `settings.py`
3. Use a production database (PostgreSQL recommended)
4. Set up proper static file serving
5. Use environment variables for sensitive data
6. Enable HTTPS
7. Set up proper backup procedures

Enjoy your hotel management system! 🏨
