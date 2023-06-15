#!/bin/sh

python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 manage.py collectstatic

# python manage.py migrate

python3 manage.py runserver 0.0.0.0:8000

# gunicorn --bind 0.0.0.0:8000 config.wsgi:application
