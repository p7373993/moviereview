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
]
