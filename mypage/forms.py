from django import forms
from mypage.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "score"]  # 평점과 내용
        widgets = {
            "content": forms.Textarea(attrs={"rows": 5, "cols": 40}),
            "score": forms.HiddenInput(),  # 별점은 숨겨서 처리
        }
