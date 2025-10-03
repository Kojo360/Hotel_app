# 🚀 Vercel Deployment Guide for Hotel App

## ⚠️ IMPORTANT: Database Limitations on Vercel

**Critical Information:** Vercel is a **serverless platform** and does **NOT support SQLite databases**. Any rooms you add to your local `db.sqlite3` will **NOT** appear on Vercel.

---

## 📊 Two Deployment Options

### **Option 1: Static Data Mode** (Quick & Free) ✅ RECOMMENDED FOR DEMO
### **Option 2: Production Database** (Full Features) 💪 RECOMMENDED FOR REAL USE

---

## 🎯 Option 1: Static Data Mode (Easiest)

Your app is **already configured** for this! It will load content from JSON files instead of a database.

### How It Works:

- Rooms loaded from: `static_data/rooms.json`
- Menu items from: `static_data/restaurant.json`
- Bar items from: `static_data/bar.json`

### Steps to Deploy with Static Mode:

#### 1. Edit JSON Files Locally

**Add your rooms to `static_data/rooms.json`:**

```json
[
  {
    "id": 1,
    "name": "Deluxe King Suite",
    "description": "Experience luxury in our 450 sq ft suite featuring premium bedding, modern furnishings, and stunning city views. Perfect for business travelers or couples.",
    "price": "189.00",
    "amenities": "King-size bed, Free Wi-Fi, 55\" Smart TV, Air conditioning, Mini-bar, Coffee maker, Work desk, Safe, Bathrobes, Premium toiletries",
    "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1200&h=800&fit=crop"
  },
  {
    "id": 2,
    "name": "Standard Double Room",
    "description": "Comfortable 320 sq ft room with two full-size beds, modern amenities, and cozy atmosphere. Ideal for friends or small families.",
    "price": "129.00",
    "amenities": "Two full-size beds, Free Wi-Fi, Flat-screen TV, Air conditioning, Work desk, Coffee maker, Daily housekeeping",
    "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&h=800&fit=crop"
  }
]
```

**Similarly update:**
- `static_data/restaurant.json` (menu items already there)
- `static_data/bar.json` (bar items already there)

#### 2. Push to GitHub

```bash
git add .
git commit -m "Update static data for deployment"
git push
```

#### 3. Deploy to Vercel

**Method A: Vercel CLI**

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel --prod
```

**Method B: Vercel Website**

1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Vercel will auto-detect settings from `vercel.json`

#### 4. Set Environment Variable in Vercel

**Critical Step:** In Vercel dashboard:

1. Go to your project → **Settings** → **Environment Variables**
2. Add:
   - **Name:** `USE_STATIC_DATA`
   - **Value:** `True`
   - **Environment:** Production
3. Add other required variables:
   - **Name:** `SECRET_KEY`
   - **Value:** (generate a secure key)
   - **Name:** `ALLOWED_HOSTS`
   - **Value:** `.vercel.app,yourdomain.com`
   - **Name:** `WHATSAPP_PHONE`
   - **Value:** Your WhatsApp number with country code

4. **Redeploy** for changes to take effect

#### 5. Test Your Deployment

Visit your Vercel URL and check:
- ✅ Rooms page shows your rooms
- ✅ Restaurant menu displays
- ✅ Bar menu displays
- ✅ Booking forms work

### ✅ Pros of Static Mode:
- ✅ **Free** - No database costs
- ✅ **Fast** - Direct JSON reads
- ✅ **Simple** - No database setup
- ✅ **Perfect for demos** or small hotels

### ❌ Cons of Static Mode:
- ❌ **No admin panel** on production
- ❌ Must edit JSON files manually
- ❌ Need to redeploy to update content
- ❌ Can't accept online bookings to database

---

## 💪 Option 2: Production Database (Full Features)

For a **real hotel website**, use a proper database so you can:
- Use the admin panel in production
- Add/edit content without redeploying
- Store bookings in database
- Have dynamic content management

### Recommended Database Providers:

#### **1. Supabase (PostgreSQL)** ⭐ RECOMMENDED
- **Free tier:** Yes (500MB database)
- **Easy setup:** Very easy
- **Website:** [supabase.com](https://supabase.com)

#### **2. Neon (PostgreSQL)**
- **Free tier:** Yes (500MB)
- **Easy setup:** Easy
- **Website:** [neon.tech](https://neon.tech)

#### **3. Railway (PostgreSQL)**
- **Free tier:** Limited ($5 credit)
- **Easy setup:** Easy
- **Website:** [railway.app](https://railway.app)

#### **4. PlanetScale (MySQL)**
- **Free tier:** Yes (5GB)
- **Easy setup:** Medium
- **Website:** [planetscale.com](https://planetscale.com)

---

## 🗄️ Setup with Supabase (Step-by-Step)

### Step 1: Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up
2. Click **"New Project"**
3. Enter:
   - **Project name:** hotel-app-db
   - **Database password:** (save this!)
   - **Region:** Choose closest to your users
4. Click **"Create new project"** (takes 2-3 minutes)

### Step 2: Get Connection String

1. In your Supabase project, go to **Settings** → **Database**
2. Scroll to **Connection string** → **URI**
3. Copy the connection string (looks like):
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxx.supabase.co:5432/postgres
   ```
4. Replace `[YOUR-PASSWORD]` with your actual password

### Step 3: Update Requirements

Make sure `requirements.txt` includes:
```
psycopg2-binary
```

If not, add it and redeploy.

### Step 4: Configure Vercel Environment Variables

In Vercel dashboard → Settings → Environment Variables, add:

```
DATABASE_URL=postgresql://postgres:password@db.xxx.supabase.co:5432/postgres
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.vercel.app,yourdomain.com
CSRF_TRUSTED_ORIGINS=https://your-app.vercel.app
WHATSAPP_PHONE=1234567890
USE_STATIC_DATA=False
```

**Important:** Do NOT set `USE_STATIC_DATA=True` when using a database!

### Step 5: Run Migrations on Production

You have two options:

**Option A: Run Migrations Locally Against Production DB**

```bash
# Set DATABASE_URL temporarily
$env:DATABASE_URL="postgresql://postgres:password@db.xxx.supabase.co:5432/postgres"

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

**Option B: Use Vercel Dev Environment**

```bash
vercel env pull .env.local
python manage.py migrate
python manage.py createsuperuser
```

### Step 6: Deploy to Vercel

```bash
git add .
git commit -m "Add production database support"
git push
vercel --prod
```

### Step 7: Access Admin Panel

1. Go to: `https://your-app.vercel.app/admin/`
2. Login with your superuser credentials
3. Start adding rooms, menu items, and bar items!

### ✅ Pros of Production Database:
- ✅ **Full admin panel** functionality
- ✅ **Dynamic content** updates
- ✅ **Scalable** for growth
- ✅ **Professional** setup
- ✅ Can store bookings

### ❌ Cons of Production Database:
- ❌ Requires setup time
- ❌ May have costs (most have free tiers)
- ❌ Need to maintain migrations

---

## 📋 Deployment Checklist

### Before Deploying:

- [ ] Choose deployment mode (Static vs Database)
- [ ] Update JSON files (if using static mode)
- [ ] Set up database (if using database mode)
- [ ] Commit and push all changes to GitHub
- [ ] Prepare environment variables

### During Deployment:

- [ ] Import project to Vercel
- [ ] Add all environment variables
- [ ] Set `USE_STATIC_DATA=True` (static) or `False` (database)
- [ ] Run migrations (database mode only)
- [ ] Create superuser (database mode only)

### After Deployment:

- [ ] Test all pages load correctly
- [ ] Verify images display
- [ ] Test booking form
- [ ] Check admin panel (database mode)
- [ ] Test on mobile devices

---

## 🔄 Updating Content

### Static Mode:
1. Edit JSON files in `static_data/`
2. Commit and push changes
3. Vercel auto-deploys
4. Content updates in ~1 minute

### Database Mode:
1. Go to `https://your-app.vercel.app/admin/`
2. Add/edit content through admin panel
3. Changes appear immediately
4. No redeployment needed!

---

## 🖼️ Using Images

### Option 1: Use External URLs (Recommended)
- Use Unsplash, Pexels URLs
- Fast loading, no upload needed
- Example: `https://images.unsplash.com/photo-xxx?w=1200`

### Option 2: Upload to Vercel Blob Storage
- Use Vercel Blob for uploaded images
- Requires additional setup
- Costs apply after free tier

### Option 3: Use Cloudinary/ImgBB
- Free image hosting
- Get shareable URLs
- Paste URLs in your JSON/admin

---

## 🆘 Troubleshooting

### Issue: "No rooms appear on production"

**Check:**
1. Is `USE_STATIC_DATA=True` set in Vercel?
2. Did you commit the JSON files?
3. Are the JSON files properly formatted?
4. Check Vercel deployment logs for errors

### Issue: "Admin panel doesn't work"

**Solutions:**
- Static mode: Admin panel is disabled (by design)
- Database mode: Check `DATABASE_URL` is set correctly
- Run migrations on production database

### Issue: "Page loads but shows errors"

**Check:**
1. Vercel deployment logs
2. All environment variables are set
3. `ALLOWED_HOSTS` includes your domain
4. `CSRF_TRUSTED_ORIGINS` is set

### Issue: "Images not displaying"

**Solutions:**
- Use full URLs (not relative paths)
- Check image URLs are accessible
- Verify HTTPS (not HTTP)

---

## 💡 Recommendations

### For Demo/Portfolio:
**→ Use Static Mode**
- Quick to set up
- Free
- Shows your project works
- No database management

### For Real Hotel:
**→ Use Production Database**
- Professional setup
- Easy content management
- Scalable
- Admin panel functionality

### Hybrid Approach:
**→ Start with Static, Migrate Later**
1. Deploy with static mode first
2. Test and show demo
3. Add database when ready for real use
4. Switch `USE_STATIC_DATA` to `False`

---

## 🔗 Useful Links

- **Vercel Documentation:** https://vercel.com/docs
- **Supabase Docs:** https://supabase.com/docs
- **Django on Vercel Guide:** https://vercel.com/guides/deploying-django-with-vercel
- **Free Image Sources:** 
  - Unsplash: https://unsplash.com
  - Pexels: https://pexels.com

---

## 📞 Quick Reference Commands

```bash
# Deploy to Vercel
vercel --prod

# Pull environment variables
vercel env pull

# Run migrations (production DB)
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Check deployment logs
vercel logs
```

---

## ✅ Summary

| Feature | Static Mode | Database Mode |
|---------|-------------|---------------|
| **Cost** | Free | Free tier available |
| **Setup Time** | 10 minutes | 30-60 minutes |
| **Admin Panel** | ❌ No | ✅ Yes |
| **Dynamic Updates** | ❌ No (redeploy) | ✅ Yes (instant) |
| **Booking Storage** | ❌ No | ✅ Yes |
| **Best For** | Demo/Portfolio | Real Business |

---

**Need help?** Check the [README.md](README.md) and other documentation files in this repository!

**Last Updated:** October 2025
