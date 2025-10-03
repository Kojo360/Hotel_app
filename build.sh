#!/bin/bash
set -euo pipefail

# Pick the python executable (defaults to python3)
PYTHON_BIN=${PYTHON_BIN:-python3}

# Install dependencies
$PYTHON_BIN -m pip install --upgrade pip
$PYTHON_BIN -m pip install -r requirements.txt

# Collect static files
$PYTHON_BIN manage.py collectstatic --noinput

# If DATABASE_URL is available during build, run migrations so the
# production DB schema matches the code that was just deployed.
if [ -n "${DATABASE_URL-}" ]; then
	echo "Running migrations during build..."
	$PYTHON_BIN manage.py migrate --noinput
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
