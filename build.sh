#!/usr/bin/env bash
# Render build script

set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata initial_data || echo "Fixture already loaded or not found"

echo "Creating superuser if not exists..."
python manage.py createsuperuser --noinput || echo "Superuser exists or not configured"

echo "Build complete!"
