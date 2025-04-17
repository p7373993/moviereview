from django.db import models
from django.db.models import Avg

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
    score = models.DecimalField("평점", max_digits=2, decimal_places=1, default=0.0)
    created_at = models.DateTimeField("작성일", auto_now_add=True)

    def __str__(self):
        return f"[{self.movie.title}] {self.author}님의 리뷰"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_movie_rating()

    def delete(self, *args, **kwargs):
        movie = self.movie
        super().delete(*args, **kwargs)
        self.update_movie_rating(movie)

    def update_movie_rating(self, movie_obj=None):
        movie = movie_obj if movie_obj else self.movie
        avg_score = movie.reviews.aggregate(avg=Avg('score'))['avg']
        movie.rating = round(avg_score or 0.0, 1)
        movie.save()
