#!/bin/sh
echo "yes" | python manage.py flush
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 &
python manage.py process_tasks 