from django.db import models
from django.utils import timezone
# Create your models here.
class OnedayClass(models.Model):
    name = models.CharField(max_length=20, verbose_name='클래스명')
    image = models.ImageField(verbose_name='사진', upload_to='class/img/')
    start_date = models.DateTimeField(verbose_name='시작 날짜')
    end_date = models.DateTimeField(verbose_name='종료 날짜')
    place = models.CharField(max_length=50, verbose_name='장소')
    price = models.CharField(max_length=30, verbose_name='비용')
    sns = models.CharField(max_length=100,
        help_text="SNS 아이디를 입력해주세요",
        verbose_name='SNS 아이디')
    description = models.TextField(verbose_name='간단한 설명')

    def __str__(self):
        return self.name

class OnedayClassReview(models.Model):
    onedayclass = models.ForeignKey('OnedayClass', on_delete=models.CASCADE, related_name='onedayclass_reviews')
    user = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
