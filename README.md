# WebApp
## This is a web application built to assist with utility management and utility billing.

### Run the application locally:
* You must have a .env file located at django-project/config/settings/ with the following information
    * SECRET_KEY
* First run `docker-compose -f docker-compose/docker-compose.local.yml build` to build the Docker image
* Then run `docker-compose -f docker-compose/docker-compose.local.yml up` to run the application

### Test the application locally:
* You must have a .env file located at django-project/config/settings/ with the following information
    * SECRET_KEY
* First run `docker-compose -f docker-compose/docker-compose.local.yml` build to build the Docker image
* Then run `docker-compose -f docker-compose/docker-compose.local.yml run app sh -c "python manage.py test && flake8"` to run the unit tests and linter
