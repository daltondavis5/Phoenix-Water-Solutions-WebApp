# WebApp
## This is a web application built to assist with utility management and utility billing.

### Run the application locally:
* You must have a .env file located at django-project/config/settings/ with the following information
    * SECRET_KEY
* First run `docker-compose -f docker-compose/docker-compose.local.yml build` to build the Docker image
* Then run `docker-compose -f docker-compose/docker-compose.local.yml up` to run the application
* Visit localhost:8000 to ensure the application is running properly

### Test the application locally:
* You must have a .env file located at django-project/config/settings/ with the following information
    * SECRET_KEY
* First run `docker-compose -f docker-compose/docker-compose.local.yml build` to build the Docker image
* Then run `docker-compose -f docker-compose/docker-compose.local.yml run app sh -c "python manage.py test"` to run the unit tests

### Test the nginx integration locally:
* You must have a .env file located at django-project/config/settings/ with the following information
    * SECRET_KEY
* First run `docker build -t local-pause -f Fargate/Dockerfile-local-awsvpc .` to build the image that replicates the AWSVPC network mode
* Then run `docker run -d -p 8080:8080 -p 8000:8000 -p 5432:5432 --name local-pause --cap-add=NET_ADMIN local-pause` to run the awsvpc image
* Finally, run `docker-compose -f docker-compose/docker-compose.local-staging.yml up --build` to launch a local db, nginx, gunicorn, and the app
* Visit localhost:8080 to ensure the application is running properly
