#!/bin/sh

# # 첫 번째 명령어
# echo "Making Django migrations..."
# python manage.py makemigrations

# # 두 번째 명령어
# echo "Applying migrations..."
# python manage.py migrate

# 세 번째 명령어
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
