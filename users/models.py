from django.contrib.auth.models import AbstractUser
from django.db import models
from instructor.models import Instructor

class CustomUser(AbstractUser):
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.CASCADE, verbose_name='강사')

    def __str__(self):
        return self.username
