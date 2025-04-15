from django.shortcuts import get_object_or_404, redirect, render

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


def mypage(request, username):
    # print(username)
    review_list = Review.objects.filter(author=username)
    context = {"review_list": review_list}
    return render(request, "mypage/my_review_list.html", context)


def review_edit(request, username, review_id):
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


def review_delete(request, username, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
        return redirect("mypage:mypage", username=username)
