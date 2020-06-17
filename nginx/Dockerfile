# Static Assets
FROM python:3.8-alpine AS build

WORKDIR /usr/src/django-project

ARG ENV_ARG
ARG SECRET_KEY_ARG
ENV SECRET_KEY=$SECRET_KEY_ARG
ENV DJANGO_SETTINGS_MODULE=config.settings.$ENV_ARG

# Copy Python requirements files
COPY requirements/$ENV_ARG.txt /usr/src/django-project/requirements.txt
COPY requirements/base.txt /usr/src/django-project/base.txt

# Install Python dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual /usr/src/django-project/.tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /usr/src/django-project/requirements.txt
RUN apk del /usr/src/django-project/.tmp-build-deps

# Copy Python files
COPY ./django-project /usr/src/django-project

WORKDIR /usr/src/

# Install frontend dependencies
COPY ./package.json /usr/src/package.json
RUN apk add --update npm
RUN npm install

# Build frontend static files
COPY ./webpack.config.js ./.babelrc /usr/src/
RUN npm run build

WORKDIR /usr/src/django-project

# Collect static assets (placed in 'django-project/config/static/' via settings file)
RUN python manage.py collectstatic


# NGINX
FROM nginx:1.14

# Configure NGINX
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy static files
COPY --from=build /usr/src/django-project/config/static/ /var/www/html/static
RUN chown -R nginx:nginx /var/www/html
