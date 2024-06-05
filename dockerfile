FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /django_folder
COPY ./django .
RUN pip3 install -r requirements.txt