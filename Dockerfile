FROM python:3.8
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD [ "uwsgi", "--socket", "0.0.0.0:3000", "--protocol", "http", "--ini", "uwsgi.ini"]
