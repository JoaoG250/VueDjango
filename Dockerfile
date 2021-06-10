FROM python:3.8

RUN apt-get update && apt-get install -y build-essential --no-install-recommends

WORKDIR /usr/src/vuedjango/
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
