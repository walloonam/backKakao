# 베이스 이미지로부터 시작
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY . /app/

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 마이그레이션 생성
RUN python manage.py makemigrations

# 마이그레이션 적용
RUN python manage.py migrate

# Django 애플리케이션 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
