# AGYEI TWUM LODGE - Logo Upload Guide

## How to Upload Your Hotel Logo

Your hotel branding has been updated! Now you need to add your logo file.

### Step 1: Prepare Your Logo

1. **File Format**: Use PNG (with transparent background) or JPG
2. **File Name**: Name your logo file as `logo.png` or `logo.jpg`
3. **Recommended Size**: 
   - Height: 40-60 pixels (for navbar)
   - Width: Auto (maintains aspect ratio)
   - For best quality, use a high-resolution image
4. **Background**: Transparent background (PNG) works best with the current design

### Step 2: Upload the Logo

**Option A: Direct File Copy (Recommended)**
1. Open File Explorer
2. Navigate to: `d:\hotel_app\static\images\`
3. Copy your logo file into this folder
4. Rename it to `logo.png` (or keep as `logo.jpg` and update the extension below)

**Option B: Using VS Code**
1. In VS Code, open the `static/images` folder in the explorer
2. Drag and drop your logo file into this folder
3. Rename it to `logo.png`

### Step 3: Update the File Extension (if needed)

If your logo is a JPG or SVG file instead of PNG, you need to update the reference:

1. Open `templates/base.html`
2. Find this line (around line 104):
   ```html
   <img src="{% static 'images/logo.png' %}" alt="AGYEI TWUM LODGE" height="40" class="me-2" style="object-fit: contain;">
   ```
3. Change `logo.png` to your file name:
   - For JPG: `logo.jpg`
   - For SVG: `logo.svg`

### Step 4: Test the Logo

1. Save all changes
2. Refresh your browser (Ctrl + F5 for hard refresh)
3. The logo should appear in the navigation bar on all pages

### Important Notes

✅ **The logo will be accessible to ALL users** - both local and remote
   - Static files are served by Django's static file system
   - When you deploy to production, collect static files with: `python manage.py collectstatic`

✅ **No server restart needed** - Just refresh your browser after adding the file

✅ **Logo appears on every page** - It's in the base template, so it shows on all pages automatically

### Troubleshooting

**Logo doesn't appear?**
1. Check the file is in the correct folder: `d:\hotel_app\static\images\`
2. Check the file name matches exactly: `logo.png`
3. Clear browser cache (Ctrl + Shift + Delete)
4. Hard refresh the page (Ctrl + F5)

**Logo is too large or small?**
- Edit `base.html` and change `height="40"` to a different number (e.g., `height="50"` or `height="60"`)

**Logo doesn't look good?**
- Make sure you're using a high-quality image
- Use a transparent background (PNG) for best results
- Ensure the logo is wide enough to be readable at small sizes

### Current Settings

- **Logo Location**: `d:\hotel_app\static\images\logo.png`
- **Display Height**: 40px (automatically maintains aspect ratio)
- **Background**: The navbar has a dark green/brown gradient, so light-colored logos work best

### Quick Checklist

- [ ] Logo file prepared (PNG or JPG, transparent background recommended)
- [ ] File copied to `d:\hotel_app\static\images\`
- [ ] File named correctly: `logo.png`
- [ ] Browser refreshed (Ctrl + F5)
- [ ] Logo appears in navigation bar

---

**Need to change the logo later?**
Simply replace the file in `static/images/` with your new logo (keeping the same filename), and refresh your browser!
