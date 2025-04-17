from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from mypage.forms import ReviewForm
from mypage.models import Movie, Review
from django.utils import timezone

# Create your views here.


def index(request):
    # return HttpResponse("안녕하세요파이보입니다")
    movie_list = Movie.objects.all()
    # answer_list = Answer.objects.all()
    context = {"movie_list": movie_list}
    return render(request, "mypage\movie_listl.html", context)


@login_required(login_url=reverse_lazy("common:login"))
def mypage(request, username):
    # print(username)
    if request.user.username != username:
        return redirect("/")  # 권한 없음
    review_list = Review.objects.filter(author=username)
    context = {"review_list": review_list}
    return render(request, "mypage/my_review_list.html", context)


@login_required(login_url=reverse_lazy("common:login"))
def review_edit(request, username, review_id):
    if request.user.username != username:
        return redirect("/")  # 권한 없음
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)  # 🔥 기존 리뷰에 덮어쓰기
        if form.is_valid():
            rForm = form.save(commit=False)
            rForm.created_at = timezone.now()  # 필요 시 수정 시간 업데이트
            rForm.save()
            return redirect("mypage:mypage", username=username)
    else:
        form = ReviewForm(instance=review)  # 🔥 기존 내용 불러오기
        subject = review.movie.title

    return render(
        request,
        "mypage/review_edit.html",
        {"form": form, "subject": review.movie.title, "review_id": review_id},
    )


@login_required(login_url=reverse_lazy("common:login"))
def review_delete(request, username, review_id):
    if request.user.username != username:
        return redirect("/")  # 권한 없음
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
        return redirect("mypage:mypage", username=username)


def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # 🔒 로그인 체크
    if not request.user.is_authenticated:
        form = ReviewForm()
        return redirect("common:login")
    if request.method == "POST":

        form = ReviewForm(request.POST)  # 🔥 기존 리뷰에 덮어쓰기
        if form.is_valid():
            rForm = form.save(commit=False)
            rForm.created_at = timezone.now()  # 필요 시 수정 시간 업데이트
            rForm.author = request.user
            rForm.movie = movie
            rForm.save()
            return redirect("mypage:review_create", movie_id=movie_id)
    else:
        # movie
        form = ReviewForm()
        return render(
            request,
            "mypage/movie_detail.html",
            {"movie": movie, "form": form},
        )
