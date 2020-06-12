FROM python3.8-alpine

ENV PYTHONUNBUFFERED 1

ARG ENV_ARG
COPY requirements/$ENV_ARG.txt /requirements.txt
COPY requirements/base.txt /base.txt
RUN pip install -r /requirements.txt

RUN mkdir /django-project
WORKDIR /django-project
COPY ./django-project /django-project

ARG DB_HOST_ARG
ARG DB_NAME_ARG
ARG DB_USER_ARG
ARG DB_PASS_ARG
ARG DEBUG_ARG=True

ENV DB_HOST=$DB_HOST_ARG
ENV DB_NAME=$DB_NAME_ARG
ENV DB_USER=$DB_USER_ARG
ENV DB_PASS=$DB_PASS_ARG
ENV DEBUG=$DEBUG_ARG
ENV DJANGO_SETTINGS_MODULE=config.settings.$ENV_ARG

CMD python manage.py wait_for_db && \
    python manage.py runserver 0.0.0.0:8000

# CMD python manage.py wait_for_db && \
#     python manage.py migrate && \
#     python manage.py runserver 0.0.0.0:8000
