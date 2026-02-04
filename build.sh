#!/usr/bin/env bash
# Render build script

set -o errexit

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Running migrations ==="
python manage.py migrate --run-syncdb

echo "=== Loading initial data ==="
python manage.py loaddata main/fixtures/initial_data.json -v 2 || {
    echo "Fixture load failed, trying alternate path..."
    python manage.py loaddata initial_data -v 2
}

echo "=== Checking loaded data ==="
python manage.py shell -c "
from main.models import Project
print(f'Projects in database: {Project.objects.count()}')
for p in Project.objects.all():
    print(f'  - {p.title}')
"

echo "=== Creating superuser ==="
python manage.py createsuperuser --noinput || echo "Superuser exists or env vars not set"

echo "=== Build complete ==="
