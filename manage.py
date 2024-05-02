#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

to start server:
(venv) $ python manage.py runserver

to start a new app (within this project):
1. (venv) $ python manage.py startapp newapp
2. fpl_website/settings.py add newappConfig to INSTALLED_APPS

muminali13
devprint...

"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fpl_website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
