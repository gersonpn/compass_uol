FROM python:3.10.9

WORKDIR /app

RUN apt-get update

RUN pip install boto3

COPY desafiopt1.py /app/desafiopt1.py
COPY movies.csv /app/movies.csv
COPY series.csv /app/series.csv

CMD ["python", "desafiopt1.py"]