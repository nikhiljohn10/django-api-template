rm -f db.sqlite3
find . -name __pycache__ -exec rm -rf {} +
find ./api/migrations -type f ! -name __init__.py -exec rm -rf {} +
pip install -Ur requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username "admin" --email ""
echo "Username: admin"
echo "Login URL: http://127.0.0.1:8000/api/v1/auth/login/"
