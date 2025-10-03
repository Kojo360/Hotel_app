# Hotel App - Deployment Guide

## ✅ Current Setup (Working on Vercel)

This Django hotel management app is successfully deployed on Vercel with:
- **Database**: PostgreSQL (Neon via Vercel)
- **Static Files**: Collected to `staticfiles/` and served via WhiteNoise
- **Image Handling**: URL-based (admins paste HTTPS image URLs, not file uploads)
- **Migrations**: Applied during build when `DATABASE_URL` is available

---

## 🚀 Quick Deploy Steps

### 1. Prerequisites
- GitHub account with this repository
- Vercel account (free tier works)
- Vercel Postgres database created (see Environment Variables below)

### 2. Connect to Vercel
1. Go to [vercel.com](https://vercel.com) and log in
2. Click "Add New Project"
3. Import your `Hotel_app` repository from GitHub
4. Vercel will auto-detect the Python runtime

### 3. Configure Environment Variables
In Vercel Project Settings → Environment Variables, add these (scope: Production & Build):

**Required:**
```
DATABASE_URL = postgresql://user:pass@host/db?sslmode=require
SECRET_KEY = your-secret-key-here-change-this
DEBUG = False
ALLOWED_HOSTS = your-site.vercel.app,.vercel.app
CSRF_TRUSTED_ORIGINS = https://your-site.vercel.app
```

**Optional:**
```
WHITENOISE_USE_FINDERS = True
USE_STATIC_DATA = False
WHATSAPP_PHONE = 1234567890
```

### 4. Deploy
- Push to `main` branch → Vercel auto-deploys
- Or use Vercel dashboard "Redeploy" button

### 5. Create Admin User
After first successful deployment, create a superuser:

```powershell
# Set your production DATABASE_URL
$env:DATABASE_URL = "postgresql://..."

# Create superuser
python manage.py createsuperuser
```

---

## 📂 Project Structure

```
Hotel_app/
├── api/
│   └── index.py          # Vercel serverless entry point
├── hotel_app/
│   ├── settings.py       # Django settings (DB, static, media config)
│   └── urls.py
├── rooms/                # Room management app
├── restaurant/           # Restaurant menu app
├── bar/                  # Bar menu app
├── pages/                # Static pages app
├── templates/            # HTML templates
├── staticfiles/          # Collected static files (built by collectstatic)
├── build.sh              # Build script (runs collectstatic + migrate)
├── vercel.json           # Vercel deployment config
└── requirements.txt      # Python dependencies
```

---

## 🔧 How It Works

### Build Process (`build.sh`)
1. Install Python dependencies from `requirements.txt`
2. Run `python manage.py collectstatic --noinput` → outputs to `staticfiles/`
3. If `DATABASE_URL` is set during build, run `python manage.py migrate --noinput`

### Vercel Configuration (`vercel.json`)
- **Serverless function**: `api/index.py` handles all Django requests
- **Static build**: Runs `build.sh` and serves `staticfiles/`
- **Routes**: 
  - `/static/*` → served from `staticfiles/`
  - `/media/*` → served from `media/` (not used since we use URL-based images)
  - `/*` → routed to Django app via `api/index.py`

### Image Handling
- **Models use `URLField`** instead of `ImageField` to avoid serverless filesystem issues
- **Admin forms** force URL input (no file uploads)
- **Templates** use `.image_url` property to display images
- **Admins** paste HTTPS image URLs (e.g., from Unsplash, Cloudinary, etc.)

### Database
- Production uses **Vercel Postgres (Neon)** with connection pooling
- Migrations run automatically during build if `DATABASE_URL` is set at build scope
- Local development uses SQLite by default

---

## 🛠️ Local Development

### Setup
```powershell
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Test with Production Database (Optional)
```powershell
# Set production DB URL temporarily
$env:DATABASE_URL = "postgresql://..."

# Run any Django command against production DB
python manage.py showmigrations
python manage.py createsuperuser
```

---

## 📝 Adding Content via Admin

### 1. Access Admin
Visit: `https://your-site.vercel.app/admin`

### 2. Add Rooms
1. Go to **Rooms** → **Add Room**
2. Fill in: Name, Description, Price, Amenities (comma-separated)
3. **Image**: Paste an HTTPS URL (e.g., `https://images.unsplash.com/...`)
4. Check "Is visible" to show on site
5. Save

### 3. Add Restaurant Menu Items
1. Go to **Restaurant** → **Menu Items** → **Add**
2. Fill in: Name, Description, Price, Category
3. **Image**: Paste HTTPS URL
4. Check "Is available"
5. Save

### 4. Add Bar Items
1. Go to **Bar** → **Bar Items** → **Add**
2. Fill in: Name, Description, Price, Category, Volume, Alcohol Content
3. **Image**: Paste HTTPS URL
4. Check "Is available"
5. Save

**Image Sources:**
- [Unsplash](https://unsplash.com) - Free high-quality images
- [Pexels](https://pexels.com) - Free stock photos
- Your own CDN/cloud storage (S3, Cloudinary, etc.)

---

## 🔄 Updating the Site

### Code Changes
1. Make changes locally
2. Test with `python manage.py runserver`
3. Commit and push to GitHub
4. Vercel auto-deploys the new version

### Database Changes (Migrations)
```powershell
# Create migration after model changes
python manage.py makemigrations

# Apply locally
python manage.py migrate

# Commit migration files
git add */migrations/*.py
git commit -m "Add migration for X"
git push

# Vercel will run migrations during build if DATABASE_URL is set at build scope
```

---

## 🐛 Troubleshooting

### Build Fails
1. Check Vercel build logs for errors
2. Ensure all environment variables are set (especially `DATABASE_URL`)
3. Verify `requirements.txt` has all dependencies
4. Check `build.sh` runs successfully locally

### 500 Errors After Deployment
1. Check Vercel Function logs (Deployment → Function Logs)
2. Verify migrations are applied:
   ```powershell
   $env:DATABASE_URL = "..."
   python manage.py showmigrations
   ```
3. Check environment variables are set correctly
4. Ensure `ALLOWED_HOSTS` includes your Vercel domain

### Images Not Showing
1. Verify image URL is valid HTTPS
2. Check URL is accessible in a browser
3. Ensure `.image_url` property is used in templates (not `.image.url`)

### Static Files Not Loading
1. Verify `collectstatic` ran during build (check build logs)
2. Ensure `WHITENOISE_USE_FINDERS=True` is set if needed
3. Check static file URLs point to `/static/...`

---

## 🔐 Security Checklist

- ✅ `DEBUG=False` in production
- ✅ `SECRET_KEY` is unique and secret
- ✅ `ALLOWED_HOSTS` configured correctly
- ✅ `CSRF_TRUSTED_ORIGINS` set to your domain
- ✅ Database credentials not committed to git
- ✅ Environment variables stored securely in Vercel

---

## 📚 Additional Resources

- [Vercel Python Documentation](https://vercel.com/docs/functions/runtimes/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)
- [Neon Postgres](https://neon.tech/docs)

---

## 💡 Optional Enhancements

### Enable File Uploads (S3)
If you want admins to upload images instead of pasting URLs:

1. Add to `requirements.txt`:
   ```
   django-storages[boto3]
   boto3
   ```

2. Add environment variables:
   ```
   AWS_ACCESS_KEY_ID = your-key
   AWS_SECRET_ACCESS_KEY = your-secret
   AWS_STORAGE_BUCKET_NAME = your-bucket
   AWS_S3_REGION_NAME = us-east-1
   ```

3. The app will automatically use S3 storage when `AWS_STORAGE_BUCKET_NAME` is set

### Custom Domain
1. Go to Vercel Project Settings → Domains
2. Add your custom domain
3. Update DNS records as instructed
4. Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`

---

**Status**: ✅ Fully deployed and operational on Vercel
**Last Updated**: October 3, 2025
