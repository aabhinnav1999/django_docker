FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /django_folder
COPY ./myproject .
RUN pip3 install -r requirements.txt