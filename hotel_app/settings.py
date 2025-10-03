"""
Django settings for hotel_app project.
"""

from pathlib import Path
from decouple import config
import dj_database_url
import tempfile

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-this-in-production-key-12345')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# Parse ALLOWED_HOSTS from environment
allowed_hosts_str = config('ALLOWED_HOSTS', default='')
ALLOWED_HOSTS = [h.strip() for h in allowed_hosts_str.split(',') if h.strip()] if allowed_hosts_str else ['localhost', '127.0.0.1', '.vercel.app']

# Parse CSRF_TRUSTED_ORIGINS from environment
csrf_origins_str = config('CSRF_TRUSTED_ORIGINS', default='')
CSRF_TRUSTED_ORIGINS = [o.strip() for o in csrf_origins_str.split(',') if o.strip()]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'crispy_forms',
    'crispy_bootstrap5',
    
    # Local apps
    'rooms',
    'restaurant',
    'bar',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotel_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'hotel_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600,
        ssl_require=False
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# In serverless environments (like Vercel) where collectstatic may not run,
# allow Django's staticfiles finders to serve package/app static via WhiteNoise.
# Set via env: WHITENOISE_USE_FINDERS=true for convenience.
WHITENOISE_USE_FINDERS = config('WHITENOISE_USE_FINDERS', default=False, cast=bool)

# Media files
# Prefer the repository media folder, but some serverless platforms have a
# read-only application directory (for example '/var/task' on Lambda-like
# runtimes). Attempt to create the repo media folder; if that fails, fall
# back to the system temp directory so file.save() operations won't raise
# OSError: Read-only file system at runtime.
MEDIA_URL = '/media/'
_DEFAULT_MEDIA_ROOT = BASE_DIR / 'media'
try:
    # Try to ensure the default media directory is writable.
    _DEFAULT_MEDIA_ROOT.mkdir(parents=True, exist_ok=True)
    # Quick write test to detect read-only mounts.
    test_file = _DEFAULT_MEDIA_ROOT / '.write_test'
    with open(test_file, 'w') as _f:
        _f.write('ok')
    test_file.unlink()
    MEDIA_ROOT = _DEFAULT_MEDIA_ROOT
except Exception:
    # Fallback to OS temp directory which is writable on most serverless
    # platforms for the lifetime of the request/process.
    MEDIA_ROOT = Path(tempfile.gettempdir()) / 'hotel_app_media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# WhatsApp Configuration
WHATSAPP_PHONE = config('WHATSAPP_PHONE', default='1234567890')

# Security/Proxy headers (important for Vercel/Reverse proxies)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static data mode (no database reads/writes). When true, views will
# load content from JSON files committed in the repo instead of ORM.
USE_STATIC_DATA = config('USE_STATIC_DATA', default=False, cast=bool)


# Optional object storage (S3-compatible) settings. Enable by setting
# AWS_STORAGE_BUCKET_NAME and AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
if config('AWS_STORAGE_BUCKET_NAME', default=''):
    # Avoid importing boto3 unless needed at runtime
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='')
    AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', default=f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com")
    MEDIA_URL = config('MEDIA_URL', default=f'https://{AWS_S3_CUSTOM_DOMAIN}/')
