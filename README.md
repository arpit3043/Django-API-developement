# [OneFin_assignment](https://docs.google.com/document/d/1IYGW6CZB5nQ3DmNgBotI10h0bnGep1r5g2D_ZRaFMDc/edit#heading=h.b9f6ujmuzlha)
OneFin assignment for building movie-collection api for web application with JWT authentication.
We need to develop a web application which allows people to create collections of movies they like. 
There are three parts to this:
- Integration with an API which serves a list of movies and their genres, details are specified here.
- Use the API to list movies for the users of your web application. They should be able to see the list of movies and add any movie which they like into their collections. Each user can create multiple collections and multiple movies into the collections. Develop APIs for this application per specification below. No frontend is required to be developed.
- We also want to have a monitoring system of counting the number of requests done to your project. Write a custom middleware for counting all requests coming to your server too, and an API to monitor it too. Details here.

# Project Set Up Installation
    run below command in your terminal 
    git clone https://github.com/arpit3043/OneFin-Assignment.git
    create and activate virtual environment
    1. python -m venv venv 
    2. venv/Scripts/activate
    Install all dependency or packages
    3.pip install -r requirements.txt
make migrations and migrate
```
python manage.py makemigrations
python manage.py migrate
```
Start the server

```
python manage.py runserver
```

I have used python-decouple library to hide our confidential data 
To follow more about this, do follow .env_sample file and create your own .env file
with all environment variable that is mentioned in .env_sample file

# For hiding your credentials I used decouple library as shown below
    In settings.py[
    from decouple import config
    SECRET_KEY = config('SECRET_KEY')

# create database in postgreSQL and configure the NAME with database name in .env file like
    NAME=onefin
    USER=postgres
    PASSWORD=your Database password here
    HOST=localhost
# For running the project execute below command in terminal
    create database in postgreSQL and configure the NAME with database name in .env file
    1. python manage.py makemigrations
    2. python manage.py migrate
    3. python manage.py runserver

## References:
[Django REST API – CRUD with DRF](https://www.geeksforgeeks.org/django-rest-api-crud-with-drf/)
[JWT Authentication with Django REST Framework](https://www.geeksforgeeks.org/jwt-authentication-with-django-rest-framework/)
[YouTube](https://www.youtube.com/)

## Authors

- [@arpit3043](https://www.github.com/arpit3043)
