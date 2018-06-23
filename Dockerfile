FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN apt-get update \
    && apt-get install -y mysql-client python3-dev \
    && rm -rf /var/lib/apt/lists/*
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD ./webadmin/ /code/