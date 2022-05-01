FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN  apt-get update
RUN apt-get install -y tk
COPY . .
EXPOSE 5000
CMD [ "python", "app.py"]
# CMD [ "gunicorn", "-w", "4" , "-b", "0.0.0.0:5000","app:app"]