# common/admin.py
from django.contrib import admin
from common.models import Movie, Review  # 실제 모델 정의된 곳

admin.site.register(Movie)
admin.site.register(Review)
