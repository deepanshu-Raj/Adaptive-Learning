from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userdetail(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    mob = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    teacher = models.BooleanField()
    city = models.CharField(max_length=30)
    count = models.IntegerField()
    plan = models.CharField(max_length=20)

    def __str__(self):
        return self.email