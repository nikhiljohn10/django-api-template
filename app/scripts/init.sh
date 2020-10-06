pip install -Ur requirements.txt
cd app
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser