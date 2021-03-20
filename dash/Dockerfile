
FROM python:3.8.3


WORKDIR /app


RUN pip install pipenv
#RUN pipenv install --deploy --system
RUN pipenv install

ADD . /app

EXPOSE 8050

#CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:server"]
CMD ["python", "main.py"]
