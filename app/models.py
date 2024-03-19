from django.db import models

class ShowModel(models.Model):
    CODENAME = models.CharField(max_length=100)  # 분류
    GUNAME = models.CharField(max_length=100)    # 자치구
    TITLE = models.CharField(max_length=255)     # 공연/행사명
    DATE = models.CharField(max_length=100)                # 날짜/시간
    PLACE = models.CharField(max_length=255)     # 장소
    ORG_NAME = models.CharField(max_length=100)  # 기관명
    USE_TRGT = models.CharField(max_length=255)  # 이용대상
    USE_FEE = models.CharField(max_length=100)   # 이용요금
    PLAYER = models.TextField()                  # 출연자정보
    PROGRAM = models.TextField()                 # 프로그램소개
    ETC_DESC = models.TextField()                # 기타내용
    ORG_LINK = models.URLField(max_length=200)   # 홈페이지 주소
    MAIN_IMG = models.URLField(max_length=200)  # 대표이미지
    RGSTDATE = models.DateField()                # 신청일
    TICKET = models.CharField(max_length=50)     # 시민/기관
    STRTDATE = models.DateField()                # 시작일
    END_DATE = models.DateField()                # 종료일
    THEMECODE = models.CharField(max_length=50)  # 테마분류
    LOT = models.FloatField()                    # 위도(X좌표)
    LAT = models.FloatField()                    # 경도(Y좌표)
    IS_FREE = models.CharField()              # 유무료
    HMPG_ADDR = models.URLField(max_length=200) # 문화포털상세URL

    def __str__(self):
        return self.TITLE
