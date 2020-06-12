FROM nikolaik/python-nodejs:python3.8-nodejs12

ENV PYTHONUNBUFFERED 1

ARG REQ_FILE
COPY $REQ_FILE /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /django-project
WORKDIR /django-project
COPY ./django-project /django-project

#TODO: set DJANGO_SETTINGS env variable
ARG DB_HOST_ARG
ARG DB_NAME_ARG
ARG DB_USER_ARG
ARG DB_PASS_ARG
ARG DEBUG=True

ENV DB_HOST=$DB_HOST_ARG
ENV DB_NAME=$DB_NAME_ARG
ENV DB_USER=$DB_USER_ARG
ENV DB_PASS=$DB_PASS_ARG
ENV DEBUG=$DEBUG

CMD python manage.py wait_for_db && \
    python manage.py runserver 0.0.0.0:8000

# CMD python manage.py wait_for_db && \
#     python manage.py migrate && \
#     python manage.py runserver 0.0.0.0:8000
