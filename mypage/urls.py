from django.urls import path
from . import views

app_name = "mypage"

urlpatterns = [
    path("", views.index, name="index"),
    path("mypage/<str:username>", views.mypage, name="mypage"),
    path(
        "mypage/review_edit/<str:username>/<int:review_id>",
        views.review_edit,
        name="review_edit",
    ),
    path(
        "mypage/<str:username>/<int:review_id>/delete",
        views.review_delete,
        name="review_delete",
    ),
    path(
        "movie/<int:movie_id>/review_create",
        views.review_create,
        name="review_create",
    ),  # 이 부분은 무비 폴더에서 만들어야 하는데 충돌날거 같아 임시로 만들었습니다
]
