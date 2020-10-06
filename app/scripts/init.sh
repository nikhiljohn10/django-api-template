rm -f db.sqlite3
pip install -Ur requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
