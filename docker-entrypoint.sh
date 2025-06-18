#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

echo "Apply database makemigrations"
python manage.py makemigrations --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
