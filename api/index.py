# Vercel Python (serverless) entrypoint
import os
import sys
from pathlib import Path

# Ensure project is on path
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

# Default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_app.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

app = get_wsgi_application()
