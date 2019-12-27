from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets={
            "title":forms.Textarea(attrs={'class':'form-control','rows':1}),
            "text":forms.Textarea(attrs={'placeholder':'게시글을 작성해주세요.','class':'form-control','rows':5}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'댓글을 작성해주세요.','class':'form-control','rows':5}),
        }
