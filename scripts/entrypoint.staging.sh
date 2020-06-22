#!/bin/sh

# if any errors are encountered, exit
set -e

python manage.py collectstatic --noinput

python manage.py wait_for_db
python manage.py migrate

if [ "$DEBUG" == "False" ]
then
    gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    python manage.py test
    echo "Did not launch gunicorn becuase DEBUG is True"
fi
