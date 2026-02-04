#!/usr/bin/env bash
# Render build script

set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Running migrations ==="
python manage.py migrate

echo "=== Loading initial data ==="
python manage.py load_initial_data

echo "=== Creating superuser ==="
python manage.py createsuperuser --noinput || echo "Superuser exists"

echo "=== Build complete ==="
