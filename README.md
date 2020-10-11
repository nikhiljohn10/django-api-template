<p align="center"><img src="assets/images/logo.png" alt="Django API logo"></p>

# Django REST API Template

Django REST API Template for Github Projects

## Using Demo API Server

```
# Clone repo
git clone https://github.com/nikhiljohn10/django-api-template.git

# Run demo server
cd django-api-template && . app/bin/install && api demo

```

Demo username: **admin**

Demo password: **@dmin1234**

Demo url: http://localhost:8000/

## Developing
With 'Use this template' button on Github, you can create a new repo in your profile with this project as template. This method is suggested if you only wish to use the template. 

*Fork the repo for contributing to this repo* 

```
# Dependencies for postgresql client (Only needed if it is enabled)
sudo apt update && sudo apt upgrade -y && sudo apt autoremove
sudo apt install -y libpq-dev python3-dev

# Clone repo using one of the three methods below
git clone git@github.com:nikhiljohn10/django-api-template.git
gh repo clone nikhiljohn10/django-api-template
cd django-api-template

# Change branch
git checkout develop

# Installing API manager
. app/bin/install

# To run development server
api setup
api user yourname yourname@example.com
api run
```

## API Manager Commands
Use `cd` command to change to project top-level directory before using the following commands.

* **Install** - `. app/bin/install`
* **Reactivate** - `apim`
* **Uninstall** - `apim-uninstall`

**Note:** API Manage only exist inside your currect terminal session. If you close the terminal after installation, you need to run install command again to reactivate the virtual environment.

## API Manager Usage

```
Usage: $ api OPTION

OPTIONS:

    -c | clean        : Clean up project to start fresh
    -i | install      : Install python dependencies
    -m | migrate      : Migrate database
    -o | demo         : Load demo data in to database
    -s | setup        : Initialise and configure API server
    -u | user [U] [E] : Add superuser with U:username and E:email as arguments
    -r | run          : Run development API server
    -d | deploy       : Deploy API server using gunicorn
    -h | help         : Display help
    -x | exit         : Exit API Manager

```

**Note:** Above commands will only work if API manager is active inside the top-level directory (Here it is `django-api-template`). For example, the prompt will say `(API) django-api-template$` is API manager is active inside your project folder.

#### Docker
- **start_psql**  : Deploy postgresql standalone docker container
- **stop_psql**   : Stop postgresql container
- **kill_psql**   : Remove postgresql container

## Contribute
Check out [CONTRIBUTING.md](https://github.com/nikhiljohn10/django-api-template/blob/main/CONTRIBUTING.md) for information about getting involved.

## Code of Conduct
Everyone interacting in the this project's codebases, issue trackers, etc are
expected to follow the [Code of Conduct](https://github.com/nikhiljohn10/django-api-template/blob/main/CODE_OF_CONDUCT.md).

## License
This project is licensed under [MIT License](https://github.com/nikhiljohn10/django-api-template/blob/main/LICENSE)
