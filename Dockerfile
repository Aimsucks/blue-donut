FROM nikolaik/python-nodejs:python3.8-nodejs12

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./package.json /app/package.json
RUN npm install

COPY . /app/
