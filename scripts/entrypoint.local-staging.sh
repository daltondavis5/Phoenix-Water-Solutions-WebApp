#!/bin/sh

# if any errors are encountered, exit
set -e

python manage.py collectstatic --noinput

python manage.py wait_for_db
python manage.py migrate

python manage.py test

gunicorn config.wsgi:application --bind 0.0.0.0:8000
