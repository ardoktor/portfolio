#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

    try:
        from django.core.management import execute_from_command_line
        from django.contrib.auth import get_user_model
        import django

        # Setup Django manually to allow database access before command execution
        django.setup()

        # Create superuser only if it doesn't exist
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpassword123")
            print("✅ Superuser created.")
        else:
            print("ℹ️ Superuser already exists, skipping creation.")

    except Exception as e:
        print(f"⚠️ Skipped superuser creation: {e}")

    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()
