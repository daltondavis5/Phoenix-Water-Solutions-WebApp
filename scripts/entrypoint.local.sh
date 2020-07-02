#!/bin/sh

# if any errors are encountered, exit
set -e

python manage.py wait_for_db
# python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver 0.0.0.0:8000
