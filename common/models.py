# common/models.py

from django.db import models

class Movie(models.Model):
    title = models.CharField("제목", max_length=200)
    director = models.CharField("감독", max_length=100)
    genre = models.CharField("장르", max_length=100)
    release_date = models.DateField("개봉일")
    poster = models.URLField("포스터", max_length=500, blank=True, null=True)
    rating = models.DecimalField("별점", max_digits=3, decimal_places=1)
    description = models.TextField("내용")
    create_date = models.DateTimeField("등록일", auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    author = models.CharField("작성자", max_length=100)
    content = models.TextField("리뷰 내용")
    score = models.PositiveSmallIntegerField("평점", default=0)
    created_at = models.DateTimeField("작성일", auto_now_add=True)

    def __str__(self):
        return f"[{self.movie.title}] {self.author}님의 리뷰"
