# movies/models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

# class Movie(models.Model):
#     title = models.CharField("제목", max_length=200)
#     director = models.CharField("감독", max_length=100)
#     genre = models.CharField("장르", max_length=100)
#     release_date = models.DateField("개봉일")
#     poster = models.URLField("포스터", max_length=500, blank=True, null=True)
#     rating = models.DecimalField("별점", max_digits=3, decimal_places=1)
#     description = models.TextField("내용")
#     create_date = models.DateTimeField("등록일", auto_now_add=True)
#     movieCd = models.CharField("영화 코드", max_length=100, default="UNKNOWN")

#     def __str__(self):
#         return self.title
   
    class Meta:
        db_table = 'movies_detail'  # 테이블 이름 지정
