cd app
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
gunicorn -w 3 -b 0.0.0.0:8000 config.wsgi