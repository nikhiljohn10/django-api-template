#!/bin/bash

. ./scripts/loaddata.sh
rm -f db.sqlite3
find . -name __pycache__ -exec rm -rf {} +
find ./api/migrations -type f ! -name __init__.py -exec rm -rf {} +
pip install -U pip
pip install -Ur requirements.txt
python manage.py makemigrations
python manage.py migrate
load_data
echo
echo
echo "Username: admin"
echo "Password: @dmin1234"
echo "Login URL: http://127.0.0.1:8000/api/v1/auth/login/"
echo
echo
python manage.py runserver 0.0.0.0:8000
