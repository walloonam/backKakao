# 베이스 이미지로 Python 3 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일 복사
COPY . .

# 스크립트 실행
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

