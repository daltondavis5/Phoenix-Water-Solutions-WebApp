FROM python:3.8-alpine

# add scripts to the path of the running container
ENV PATH="/scripts:${PATH}"
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

ARG ENV_ARG

COPY requirements/$ENV_ARG.txt /requirements.txt
COPY requirements/base.txt /base.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Copy Django project
RUN mkdir /django-project
COPY ./django-project /django-project

# Install Front-end dependencies
COPY ./package.json /package.json
RUN apk add --update npm
RUN npm install

# build static files
COPY ./webpack.config.js ./.babelrc /
RUN npm run build

WORKDIR /django-project

# copy the entrypoint script into the image and get executable permissions
COPY ./scripts/entrypoint.$ENV_ARG.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/*

# create user
RUN adduser -D user
USER user

ARG DB_HOST_ARG
ARG DB_NAME_ARG
ARG DB_USER_ARG
ARG DB_PASS_ARG
ARG DEBUG_ARG=False
ARG SECRET_KEY_ARG

ENV DB_HOST=$DB_HOST_ARG
ENV DB_NAME=$DB_NAME_ARG
ENV DB_USER=$DB_USER_ARG
ENV DB_PASS=$DB_PASS_ARG
ENV DEBUG=$DEBUG_ARG
ENV SECRET_KEY=$SECRET_KEY_ARG
ENV DJANGO_SETTINGS_MODULE=config.settings.$ENV_ARG

EXPOSE 8000
ENTRYPOINT [ "entrypoint.sh" ]

# CMD python manage.py wait_for_db && \
#     python manage.py runserver 0.0.0.0:8000
#
# CMD python manage.py wait_for_db && \
#     gunicorn config.wsgi:application --bind 0.0.0.0:8000
