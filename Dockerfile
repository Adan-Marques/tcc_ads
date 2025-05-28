FROM python:3.10.12-slim

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip &&  pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
