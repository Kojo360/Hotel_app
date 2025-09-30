# Hotel Management System - Setup Script for Windows
# Run this script in PowerShell to set up the project

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Hotel Management System - Setup Script" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Create virtual environment
Write-Host "Step 1: Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "Virtual environment already exists. Skipping..." -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "Virtual environment created successfully!" -ForegroundColor Green
}
Write-Host ""

# Step 2: Activate virtual environment and install dependencies
Write-Host "Step 2: Installing dependencies..." -ForegroundColor Yellow
Write-Host "Activating virtual environment..." -ForegroundColor Gray
& .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Write-Host "Dependencies installed successfully!" -ForegroundColor Green
Write-Host ""

# Step 3: Create .env file if it doesn't exist
Write-Host "Step 3: Setting up environment variables..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host ".env file already exists. Skipping..." -ForegroundColor Green
} else {
    Copy-Item ".env.example" ".env"
    Write-Host ".env file created from example. Please update it with your settings!" -ForegroundColor Green
    Write-Host "  - Set your SECRET_KEY" -ForegroundColor Gray
    Write-Host "  - Set your WHATSAPP_PHONE number" -ForegroundColor Gray
}
Write-Host ""

# Step 4: Run migrations
Write-Host "Step 4: Creating database..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate
Write-Host "Database created successfully!" -ForegroundColor Green
Write-Host ""

# Step 5: Create superuser prompt
Write-Host "Step 5: Create admin superuser" -ForegroundColor Yellow
Write-Host "You'll need to create an admin account to manage the hotel." -ForegroundColor Gray
$createUser = Read-Host "Do you want to create a superuser now? (y/n)"
if ($createUser -eq "y" -or $createUser -eq "Y") {
    python manage.py createsuperuser
    Write-Host "Superuser created successfully!" -ForegroundColor Green
} else {
    Write-Host "You can create a superuser later by running: python manage.py createsuperuser" -ForegroundColor Yellow
}
Write-Host ""

# Step 6: Final instructions
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Edit the .env file with your settings (SECRET_KEY, WHATSAPP_PHONE)" -ForegroundColor White
Write-Host "2. Run the development server:" -ForegroundColor White
Write-Host "   python manage.py runserver" -ForegroundColor Gray
Write-Host "3. Open your browser and go to:" -ForegroundColor White
Write-Host "   http://127.0.0.1:8000/ (Main website)" -ForegroundColor Gray
Write-Host "   http://127.0.0.1:8000/admin/ (Admin dashboard)" -ForegroundColor Gray
Write-Host ""
Write-Host "Happy hotel managing! 🏨" -ForegroundColor Green
Write-Host ""

# Prompt to start server
$startServer = Read-Host "Do you want to start the development server now? (y/n)"
if ($startServer -eq "y" -or $startServer -eq "Y") {
    Write-Host ""
    Write-Host "Starting development server..." -ForegroundColor Yellow
    Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
    Write-Host ""
    python manage.py runserver
}
