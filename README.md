# Django REST API Template

Django REST API Template for Github Projects


## Development

### Installation

```

# Dependencies for postgresql client
sudo apt update && \
sudo apt upgrade -y && \
sudo apt install -y libpq-dev python3-dev && \
sudo apt autoremove

# Installing template
git clone https://github.com/nikhiljohn10/django-api-template.git
cd django-api-template/app
python3 -m venv venv && . venv/bin/activate && . scripts/django

# To develop
api_dev

# Edit .env file before deploying

# To deploy
api_deploy
```


### Commands

 - **api_init** : Initialise api server
 - **api_dev** : Run development server
 - **api_deploy** : Deploy api server using gunicorn
 - **migrate_db** : Migrate database
 - **load_data** : Load dummy data in to database
 

```
For demo, use the following:

Username: admin/alice/bob/lucy
Password: @dmin1234
Login URL: http://localhost:8000/api/v1/auth/login/
```
