from django import forms
from mypage.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "score"]
