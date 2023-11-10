FROM python:3.9.10

RUN mkdir -p /root/backend
WORKDIR /root/backend

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools