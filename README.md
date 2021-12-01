# python-flask-rest-example

A Flask RESTful template for performing CRUD operations on an SQLAlchemy books database.

## Run in Docker (DEV mode)

 `docker build --target dev . -t python-flask-dev`

 `docker run -it -p 5000:5000 -v ${PWD}:/work python-flask-dev sh`

 `pip install -r requirements.txt`

 `export FLASK_APP=src/api`

 `flask run -h 0.0.0 -p 5000`

Go to the browser and type: http://localhost:5000/books

## Run in Docker (PRODUCTION mode)

 `docker build . -t python-flask-prod`

 `docker run -it -p 5000:5000 python-flask-prod`

Go to the browser and type: http://localhost:5000/books
