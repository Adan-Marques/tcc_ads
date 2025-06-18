FROM python:3.10.12-slim

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip &&  pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

