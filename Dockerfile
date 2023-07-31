FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY Requirements.txt /code/
RUN pip install -r Requirements.txt
COPY . /code/