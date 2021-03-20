
FROM python:3.8.3


WORKDIR /app

ENV FLASK_APP=/app/engine.py


RUN pip install pipenv
RUN pipenv install --deploy --system

ADD . /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
