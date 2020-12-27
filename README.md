# recipe-app-api


Directions:
docker build .
docker-compose build
docker-compose run app sh -c "django-admin.py startproject app ."

make travis.yml file and the flake8 file and push it to github

add the repo to travis and then everytime you fail you get an email about it


To do testing (use this all the time):
docker-compose run app sh -c "python manage.py test && flake8" 

to start the core to hold all the things that this app uses to run:
docker-compose run app sh -c "python manage.py startapp core"


This line is to make the migrations of data into database 
Run this everytime you want to  change your models
located because of ===  AUTH_USER_MODEL = 'core.User (in settings.py)
docker-compose run app sh -c "python manage.py makemigrations core"
