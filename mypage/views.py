from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from mypage.forms import ReviewForm
from mypage.models import Movie, Review

# 영화 목록 페이지
def index(request):
    movie_list = Movie.objects.all()
    context = {"movie_list": movie_list}
    return render(request, "mypage/movie_listl.html", context)

# 마이페이지: 본인이 작성한 리뷰만 조회
@login_required(login_url=reverse_lazy("common:login"))
def mypage(request, username):
    if request.user.username != username:
        return redirect("/")
    review_list = Review.objects.filter(author=username)
    context = {"review_list": review_list}
    return render(request, "mypage/my_review_list.html", context)


# rating_choices에 반개 여부 포함시켜서 넘겨주기
rating_choices = ["5", "4", "3", "2", "1"]

# 리뷰 작성 페이지 (상세페이지 포함)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewForm()
    return render(request, "mypage/movie_detail.html", {
        "movie": movie,
        "form": form,
        "rating_choices": rating_choices,  
    })

        

# 리뷰 작성 처리
@login_required(login_url=reverse_lazy("common:login"))
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created_at = timezone.now()
            review.author = request.user.username
            review.movie = movie
            review.save()
            return redirect("mypage:movie_detail", movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, "mypage/movie_detail.html", {
        "movie": movie,
        "form": form,
        "rating_choices": rating_choices,
    })
    
# 리뷰 수정
@login_required(login_url=reverse_lazy("common:login"))
def review_edit(request, username, review_id):
    if request.user.username != username:
        return redirect("/")

    review = get_object_or_404(Review, id=review_id)
    movie = review.movie

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            rForm = form.save(commit=False)
            rForm.created_at = timezone.now()
            rForm.save()
            return redirect("mypage:mypage", username=username)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "mypage/review_edit.html",
        {"form": form, "movie": movie, "review_id": review_id},
    )

# 리뷰 삭제
@login_required(login_url=reverse_lazy("common:login"))
def review_delete(request, username, review_id):
    if request.user.username != username:
        return redirect("/")
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        review.delete()
        return redirect("mypage:mypage", username=username)
