# # movies/models.py
from django.db import models

# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     create_date = models.DateTimeField()

#     def __str__(self):
#         return self.title

# # Create your models here.
# # class Movie(models.Model):
# #     title = models.CharField("제목", max_length=200)
# #     director = models.CharField("감독", max_length=100)
# #     genre = models.CharField("장르", max_length=100)
# #     release_date = models.DateField("개봉일")
# #     poster = models.URLField("포스터", max_length=500, blank=True, null=True)
# #     rating = models.DecimalField("별점", max_digits=3, decimal_places=1)
# #     description = models.TextField("내용")
# #     create_date = models.DateTimeField("등록일", auto_now_add=True)
# #     movieCd = models.CharField("영화 코드", max_length=100, default="UNKNOWN")

# #     def __str__(self):
# #         return self.title
   
#     class Meta:
#         db_table = 'movies_movie'  # 테이블 이름 지정


# models.py
class Genre(models.Model):
    name = models.CharField(max_length=100, db_column='genre_name')

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    poster = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cast_name = models.CharField(max_length=100, db_column = 'person_name')

    def __str__(self):
        return self.name

