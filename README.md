# Hotel Management System# Hotel Management Web Application



A modern Django-based hotel management web application for managing rooms, restaurant menus, and bar inventory with an admin interface and customer-facing pages.A Django-based hotel management system that allows admins to manage rooms and restaurant menus, while users can browse, book rooms, and submit complaints.



## 🌟 Features## Features



- **Room Management**: Display and manage hotel rooms with pricing, amenities, and availability### Admin Features

- **Restaurant Menu**: Dynamic menu system with categories and pricing- Manage hotel rooms (add, edit, delete, toggle visibility)

- **Bar Menu**: Beverage inventory with categories, pricing, and alcohol content- Manage restaurant menu items with images

- **Admin Interface**: Easy-to-use Django admin for content management- View booking requests via WhatsApp

- **Booking System**: Room booking with WhatsApp integration- View customer complaints

- **Responsive Design**: Mobile-friendly Bootstrap 5 interface

- **URL-based Images**: Serverless-friendly image handling (paste HTTPS URLs, no uploads)### User Features

- Browse available rooms with images and amenities

## 🚀 Live Site- Submit booking requests (sent to WhatsApp)

- View restaurant menu

**Production**: [https://hotel-app-five-nu.vercel.app](https://hotel-app-five-nu.vercel.app)- Submit complaints via contact form

- View hotel contact information and location

## 📚 Documentation

## Setup Instructions

- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Complete deployment guide for Vercel

- **[ADMIN_CONTENT_GUIDE.md](ADMIN_CONTENT_GUIDE.md)** - Guide for managing content via admin### Prerequisites

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick reference for common tasks- Python 3.8 or higher

- pip (Python package manager)

## 🛠️ Tech Stack

### Installation Steps

- **Backend**: Django 5.2.7, Python 3.12+

- **Database**: PostgreSQL (Neon via Vercel)1. **Create a virtual environment:**

- **Frontend**: Bootstrap 5, Crispy Forms   ```bash

- **Deployment**: Vercel (serverless Python)   python -m venv venv

- **Static Files**: WhiteNoise   ```

- **Forms**: django-crispy-forms with Bootstrap 5

2. **Activate the virtual environment:**

## ⚡ Quick Start (Local Development)   - Windows: `venv\Scripts\activate`

   - macOS/Linux: `source venv/bin/activate`

```bash

# Clone repository3. **Install dependencies:**

git clone https://github.com/Kojo360/Hotel_app.git   ```bash

cd Hotel_app   pip install -r requirements.txt

   ```

# Install dependencies

pip install -r requirements.txt4. **Create a `.env` file in the project root with the following:**

   ```

# Run migrations   SECRET_KEY=your-secret-key-here

python manage.py migrate   DEBUG=True

   WHATSAPP_PHONE=your-whatsapp-number-with-country-code

# Create superuser   ```

python manage.py createsuperuser

5. **Apply migrations:**

# Run development server   ```bash

python manage.py runserver   python manage.py makemigrations

```   python manage.py migrate

   ```

Visit: `http://127.0.0.1:8000/`  

Admin: `http://127.0.0.1:8000/admin/`6. **Create a superuser (admin):**

   ```bash

## 📦 Dependencies   python manage.py createsuperuser

   ```

Core dependencies (see `requirements.txt`):

- Django 5.2.77. **Run the development server:**

- psycopg2-binary (PostgreSQL adapter)   ```bash

- python-decouple (environment variables)   python manage.py runserver

- dj-database-url (database URL parsing)   ```

- whitenoise (static file serving)

- django-crispy-forms + crispy-bootstrap5 (form styling)8. **Access the application:**

- Pillow (image processing)   - Main website: http://127.0.0.1:8000/

   - Admin dashboard: http://127.0.0.1:8000/admin/

## 🔐 Environment Variables

## Project Structure

Required for production (see `DEPLOYMENT.md` for details):

```

```envhotel_app/

DATABASE_URL=postgresql://...├── hotel_app/          # Main project settings

SECRET_KEY=your-secret-key├── rooms/              # Room management and bookings

DEBUG=False├── restaurant/         # Menu management

ALLOWED_HOSTS=your-domain.vercel.app├── pages/              # Homepage and contact pages

CSRF_TRUSTED_ORIGINS=https://your-domain.vercel.app├── static/             # CSS, JS, images

```├── media/              # User uploaded images

└── templates/          # HTML templates

## 📝 Project Structure```



```## Usage

Hotel_app/

├── api/index.py              # Vercel serverless entry### Admin Dashboard

├── hotel_app/                # Django project settings1. Login at `/admin/` with your superuser credentials

├── rooms/                    # Room management app2. Manage rooms: Add/edit room details, upload images, set prices

├── restaurant/               # Restaurant menu app3. Toggle room visibility to control what users see

├── bar/                      # Bar menu app4. Manage restaurant menu items

├── pages/                    # Static pages5. View submitted complaints

├── templates/                # HTML templates

├── static/                   # Static assets (CSS, JS, images)### User Experience

├── staticfiles/              # Collected static files (generated)1. Browse rooms on the Rooms page

├── build.sh                  # Build script for Vercel2. Click "Book Now" to fill out a booking form

├── vercel.json               # Vercel configuration3. Booking details are sent to the hotel's WhatsApp

└── requirements.txt          # Python dependencies4. Browse restaurant menu with pictures

```5. Submit complaints via the Contact page



## 👥 Contributing## WhatsApp Integration



1. Fork the repositoryWhen a user submits a booking, they are redirected to WhatsApp with a pre-filled message containing:

2. Create a feature branch (`git checkout -b feature/YourFeature`)- Room name

3. Commit changes (`git commit -m 'Add YourFeature'`)- Guest name and contact

4. Push to branch (`git push origin feature/YourFeature`)- Check-in and check-out dates

5. Open a Pull Request- Special requests



## 📄 LicenseThe admin receives this message directly on WhatsApp for confirmation.



This project is open source and available under the [MIT License](LICENSE).## Technologies Used



## 🤝 Support- Django 4.2

- Bootstrap 5

For issues, questions, or contributions:- Django Crispy Forms

- Open an [Issue](https://github.com/Kojo360/Hotel_app/issues)- SQLite (default, can be changed to PostgreSQL/MySQL)

- Submit a [Pull Request](https://github.com/Kojo360/Hotel_app/pulls)- Pillow (for image handling)



---## 📚 Documentation



**Status**: ✅ Deployed and operational  Comprehensive guides are available to help you manage your hotel website:

**Last Updated**: October 3, 2025

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
