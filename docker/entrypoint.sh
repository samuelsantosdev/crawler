#!/bin/sh

cd /app
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/users.json
python manage.py test
exec "$@"