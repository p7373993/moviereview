from django.shortcuts import render

from mypage.models import Movie

# Create your views here.


def index(request):
    # return HttpResponse("안녕하세요파이보입니다")
    movie_list = Movie.objects.all()
    # answer_list = Answer.objects.all()
    context = {"movie_list": movie_list}
    return render(request, "mypage\movie_listl.html", context)
