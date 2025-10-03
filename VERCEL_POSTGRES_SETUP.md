# 🚀 Step-by-Step: Deploy with Vercel Postgres

## 📋 Overview

You've chosen to use **Vercel Postgres** - excellent choice! This gives you:
- ✅ Built-in PostgreSQL database on Vercel
- ✅ Full admin panel functionality
- ✅ Automatic connection string management
- ✅ Easy integration with your Vercel project

---

## ⚙️ Prerequisites Completed

✅ **requirements.txt** updated with PostgreSQL support  
✅ **settings.py** configured for production database  

---

## 🎯 Step 1: Push Your Code to GitHub

First, commit and push your latest changes:

```powershell
# Add all changes
git add .

# Commit with a message
git commit -m "Prepare for Vercel deployment with Postgres"

# Push to GitHub
git push origin main
```

---

## 🚀 Step 2: Create Vercel Project

### Option A: Using Vercel Website (Recommended)

1. **Go to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Sign up or log in (use GitHub for easy integration)

2. **Import Your Repository**
   - Click **"Add New..."** → **"Project"**
   - Select **"Import Git Repository"**
   - Choose your `Hotel_app` repository
   - Click **"Import"**

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

4. **Click "Deploy"** (Don't worry if it fails - we'll configure it next)

### Option B: Using Vercel CLI

```powershell
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Link your project
vercel link

# Deploy
vercel --prod
```

---

## 🗄️ Step 3: Add Vercel Postgres Database

This is where the magic happens!

### Create the Database:

1. **Go to Your Project Dashboard**
   - Click on your project in Vercel dashboard
   - Click on the **"Storage"** tab

2. **Create Postgres Database**
   - Click **"Create Database"**
   - Select **"Postgres"**
   - Click **"Continue"**

3. **Choose Your Region**
   - Select the region closest to your users
   - **Recommended:** Same region as your deployment

4. **Name Your Database**
   - Database Name: `hotel-app-db` (or any name you prefer)
   - Click **"Create"**

5. **Wait for Creation**
   - It takes about 30-60 seconds
   - Vercel automatically creates the database and connection string

### What Happens Automatically:

✅ Vercel creates a PostgreSQL database  
✅ Generates secure connection credentials  
✅ **Automatically adds `POSTGRES_URL` to your environment variables**  
✅ Makes the database accessible only to your Vercel project  

---

## 🔧 Step 4: Configure Environment Variables

Now we need to set up environment variables for your app.

### Go to Project Settings:

1. In your Vercel project dashboard
2. Click **"Settings"** tab
3. Click **"Environment Variables"** in the left sidebar

### Add These Variables:

**Important:** The `POSTGRES_URL` should already be there from Step 3. Now add the rest:

#### 1. DATABASE_URL (Map from POSTGRES_URL)

**Name:** `DATABASE_URL`  
**Value:** Click "Reference" and select `POSTGRES_URL`  
**Environment:** All (Production, Preview, Development)

> **Note:** This maps the Vercel Postgres connection string to Django's expected variable name.

#### 2. SECRET_KEY

**Name:** `SECRET_KEY`  
**Value:** Generate a secure key using this command:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it as the value.  
**Environment:** All

#### 3. DEBUG

**Name:** `DEBUG`  
**Value:** `False`  
**Environment:** Production

#### 4. ALLOWED_HOSTS

**Name:** `ALLOWED_HOSTS`  
**Value:** `.vercel.app` (or your custom domain)  
**Environment:** All

> **Note:** If you have a custom domain like `myhotel.com`, use: `.vercel.app,myhotel.com`

#### 5. CSRF_TRUSTED_ORIGINS

**Name:** `CSRF_TRUSTED_ORIGINS`  
**Value:** `https://your-project-name.vercel.app`  
**Environment:** All

> **Replace:** `your-project-name` with your actual Vercel project URL

#### 6. WHATSAPP_PHONE

**Name:** `WHATSAPP_PHONE`  
**Value:** Your WhatsApp number with country code (e.g., `233123456789`)  
**Environment:** All

#### 7. USE_STATIC_DATA

**Name:** `USE_STATIC_DATA`  
**Value:** `False`  
**Environment:** All

> **Important:** Set to `False` to use the database, not JSON files

### Environment Variables Summary:

```
DATABASE_URL = [Reference to POSTGRES_URL]
SECRET_KEY = [Your generated secret key]
DEBUG = False
ALLOWED_HOSTS = .vercel.app
CSRF_TRUSTED_ORIGINS = https://your-project-name.vercel.app
WHATSAPP_PHONE = 233123456789
USE_STATIC_DATA = False
```

### Save All Variables:

Click **"Save"** after adding each variable.

---

## 🚀 Step 5: Redeploy Your Application

After adding environment variables:

1. **Go to "Deployments" tab**
2. Click the **three dots (...)** on the latest deployment
3. Click **"Redeploy"**
4. Check **"Use existing Build Cache"** (optional)
5. Click **"Redeploy"**

**Or** push a new commit:

```powershell
git commit --allow-empty -m "Trigger redeploy with Postgres"
git push origin main
```

Vercel will automatically deploy.

### Wait for Deployment:

- Monitor the build logs
- Should take 1-2 minutes
- Look for "✅ Ready" status

---

## 🗃️ Step 6: Run Database Migrations

Your database is empty! We need to create tables.

### Method A: Using Vercel CLI (Recommended)

```powershell
# Pull environment variables locally
vercel env pull .env.local

# Now the DATABASE_URL is available
# Run migrations against production database
python manage.py migrate

# You should see:
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   ... [more migrations] ...
```

### Method B: Using Vercel Function

If CLI doesn't work, create a temporary migration endpoint:

1. Create `api/migrate.py`:

```python
from django.core.management import execute_from_command_line
from django.http import JsonResponse
import os
import sys

def handler(request):
    """Run migrations (REMOVE AFTER FIRST USE!)"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_app.settings')
    
    # Set up Django
    import django
    django.setup()
    
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    return JsonResponse({'status': 'Migrations completed'})
```

2. Deploy and visit: `https://your-app.vercel.app/api/migrate`

3. **IMPORTANT:** Delete this file after running migrations!

### Method C: Using Local Connection

```powershell
# Get your connection string from Vercel
# Settings → Environment Variables → POSTGRES_URL → Reveal

# Set it locally (replace with your actual URL)
$env:DATABASE_URL="postgres://username:password@host/database"

# Run migrations
python manage.py migrate
```

---

## 👤 Step 7: Create Superuser (Admin Account)

You need an admin account to access `/admin/` on production.

### Using Vercel CLI:

```powershell
# Make sure .env.local is pulled (from Step 6)
vercel env pull .env.local

# Create superuser
python manage.py createsuperuser

# Enter:
# - Username: admin
# - Email: your-email@example.com
# - Password: [secure password]
# - Password (again): [confirm]
```

### Alternative: Django Shell in Production

If you have shell access, you can create a user programmatically:

```python
python manage.py shell

# In the shell:
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@example.com', 'your-secure-password')
exit()
```

---

## ✅ Step 8: Verify Your Deployment

### Test These URLs:

1. **Homepage:**  
   `https://your-project-name.vercel.app/`
   - Should load without errors

2. **Admin Panel:**  
   `https://your-project-name.vercel.app/admin/`
   - Login with your superuser credentials
   - Should see Django admin dashboard

3. **Rooms Page:**  
   `https://your-project-name.vercel.app/rooms/`
   - Currently empty (no rooms added yet)
   - Should not show errors

4. **Restaurant Page:**  
   `https://your-project-name.vercel.app/restaurant/`
   - Currently empty
   - Should not show errors

5. **Bar Page:**  
   `https://your-project-name.vercel.app/bar/`
   - Currently empty
   - Should not show errors

---

## 📝 Step 9: Add Content Through Admin Panel

Now the fun part - add your content!

### Access Admin Panel:

1. Go to `https://your-project-name.vercel.app/admin/`
2. Login with your superuser account
3. You'll see the Django admin dashboard

### Add Rooms:

1. Click **"Rooms"** → **"Rooms"** → **"+ Add Room"**
2. Fill in:
   - Name: e.g., "Deluxe King Suite"
   - Description: Detailed room description
   - Price: e.g., 189.00
   - Amenities: Comma-separated list
   - Image: Upload or use URL
   - ✅ Check "Is visible"
3. Click **"Save"**
4. Repeat for more rooms

### Add Restaurant Menu:

1. Click **"Restaurant"** → **"Menu items"** → **"+ Add Menu item"**
2. Fill in name, description, category, price
3. Upload image (optional)
4. ✅ Check "Is available"
5. Click **"Save"**

### Add Bar Items:

1. Click **"Bar"** → **"Bar items"** → **"+ Add Bar item"**
2. Fill in name, description, category, price
3. Add alcohol content and volume
4. Upload image (optional)
5. ✅ Check "Is available"
6. ✅ Check "Is featured" for special drinks
7. Click **"Save"**

### Verify on Public Site:

- Visit `/rooms/` - your rooms should appear!
- Visit `/restaurant/` - menu items should show!
- Visit `/bar/` - bar items should display!

---

## 🖼️ Step 10: Handle Images

Since Vercel is serverless, uploaded images need special handling.

### Option 1: Use Image URLs (Easiest)

Instead of uploading images, paste URLs from:
- **Unsplash:** `https://images.unsplash.com/photo-xxx?w=1200`
- **Your own CDN or storage**

In the admin panel, paste the full URL in the image field.

### Option 2: Use Vercel Blob Storage

For user uploads:

1. **Enable Vercel Blob:**
   - Go to project **Storage** tab
   - Click **"Create Database"** → **"Blob"**
   - Create a Blob store

2. **Install package:**
   Add to `requirements.txt`:
   ```
   vercel-blob
   ```

3. **Update settings.py:**
   Configure Django to use Blob storage for media files

4. **Redeploy**

### Recommended Approach:

For now, use **Image URLs** from Unsplash or other services. This is simplest and free!

---

## 🎉 SUCCESS! Your Hotel App is Live

### What You Now Have:

✅ **Live website** on Vercel  
✅ **PostgreSQL database** storing your data  
✅ **Admin panel** accessible from anywhere  
✅ **Dynamic content** - add/edit without redeploying  
✅ **Professional setup** ready to scale  

### Your URLs:

- **Website:** `https://your-project-name.vercel.app`
- **Admin:** `https://your-project-name.vercel.app/admin`
- **Rooms:** `https://your-project-name.vercel.app/rooms`
- **Restaurant:** `https://your-project-name.vercel.app/restaurant`
- **Bar:** `https://your-project-name.vercel.app/bar`

---

## 🔄 Making Updates

### Update Content:
1. Go to admin panel
2. Add/edit/delete items
3. Changes appear **immediately** (no redeployment needed!)

### Update Code:
1. Make changes locally
2. Commit and push to GitHub
3. Vercel automatically redeploys

```powershell
git add .
git commit -m "Update features"
git push origin main
```

---

## 🆘 Troubleshooting

### Issue: "Application Error" on deployment

**Solution:**
1. Check Vercel deployment logs
2. Verify all environment variables are set
3. Ensure `DATABASE_URL` references `POSTGRES_URL`
4. Check `ALLOWED_HOSTS` includes `.vercel.app`

### Issue: Can't run migrations

**Solution:**
1. Verify database was created successfully
2. Check `POSTGRES_URL` exists in environment variables
3. Use `vercel env pull` to get connection string
4. Try running migrations locally against production DB

### Issue: Admin panel gives CSRF error

**Solution:**
1. Check `CSRF_TRUSTED_ORIGINS` is set correctly
2. Must include `https://` prefix
3. Should match your Vercel URL exactly

### Issue: Static files not loading

**Solution:**
1. Ensure WhiteNoise is in `MIDDLEWARE`
2. Check `vercel.json` has static file route
3. May need to run: `python manage.py collectstatic --noinput`

### Issue: Images not uploading

**Solution:**
1. Use image URLs instead of file uploads (recommended)
2. Or set up Vercel Blob storage
3. Vercel serverless doesn't support persistent file storage

---

## 📊 Monitoring Your App

### View Logs:

```powershell
# Real-time logs
vercel logs

# Or visit Vercel dashboard → Deployments → [Click deployment] → Logs
```

### Monitor Database:

1. Vercel dashboard → Storage → Your Postgres database
2. View:
   - Connection count
   - Database size
   - Query performance

---

## 💰 Costs

### Vercel Postgres Pricing:

- **Free Tier (Hobby):**
  - 256 MB storage
  - 60 compute hours/month
  - Good for small/demo projects

- **Pro Tier ($20/month):**
  - Starts at $20/month base
  - Additional charges for compute/storage
  - Good for production apps

### Recommendations:

- **Start with Free tier** to test
- **Monitor usage** in Vercel dashboard
- **Upgrade to Pro** when you need more resources

---

## 🚀 Next Steps

### Now That You're Deployed:

1. **Add your content** through admin panel
2. **Test all features** thoroughly
3. **Share your URL** with others
4. **Set up custom domain** (optional)
5. **Monitor performance** and costs

### Want a Custom Domain?

1. Buy domain from provider (Namecheap, GoDaddy, etc.)
2. In Vercel: Settings → Domains → Add Domain
3. Follow DNS configuration instructions
4. Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`

---

## 📚 Additional Resources

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Postgres Docs:** https://vercel.com/docs/storage/vercel-postgres
- **Django Deployment Checklist:** https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Vercel project created
- [ ] Vercel Postgres database created
- [ ] All environment variables configured
- [ ] Application deployed successfully
- [ ] Database migrations run
- [ ] Superuser created
- [ ] Admin panel accessible
- [ ] All pages load without errors
- [ ] Content added through admin
- [ ] Public pages display content correctly
- [ ] Booking form tested
- [ ] Images loading properly

---

**Congratulations! Your hotel app is now live on Vercel with a production PostgreSQL database! 🎉**

**Need help?** Refer back to this guide or check the Vercel documentation.

**Last Updated:** October 2025
