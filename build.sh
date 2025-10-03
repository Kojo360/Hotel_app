#!/bin/bash
set -euo pipefail

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# If DATABASE_URL is available during build, run migrations so the
# production DB schema matches the code that was just deployed.
if [ -n "${DATABASE_URL-}" ]; then
	echo "Running migrations during build..."
	python manage.py migrate --noinput
else
	echo "DATABASE_URL not set during build; skipping migrations."
fi

# Apply database migrations if DATABASE_URL is available during build.
if [ -z "$DATABASE_URL" ]; then
	echo "DATABASE_URL not set during build; skipping migrations"
else
	echo "Running migrations during build..."
	python manage.py migrate --noinput
fi
