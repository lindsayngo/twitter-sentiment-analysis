#!/usr/bin/env python
import os
import sys
from backend.main import twitter_api
#from chrontab import ChronTab

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
'''
    chron = ChronTab()
    job.new = chron.new(command='python update.py')
    job.day.every(1)
    chron.write()
'''


