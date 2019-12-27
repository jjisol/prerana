from django import forms
from .models import Center, CenterReview

class CenterReviewForm(forms.ModelForm):
    class Meta:
        model = CenterReview
        fields = ('text', )

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'리뷰를 작성해주세요.','class':'form-control','rows':5}),
        }
