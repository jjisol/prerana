from django import forms
from .models import OnedayClass, OnedayClassReview

class OnedayClassReviewForm(forms.ModelForm):
    class Meta:
        model = OnedayClassReview
        fields = ('text', )

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'리뷰를 작성해주세요.','class':'form-control','rows':5}),
        }
