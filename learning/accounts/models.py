from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userdetail(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    bio = models.CharField(max_length=100)
    mob = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    teacher = models.BooleanField()
    city = models.CharField(max_length=30,null=True,blank=False)
    count = models.IntegerField(null=True,blank=False)
    plan = models.CharField(max_length=20,null=True,blank=False)

    def __str__(self):
        return self.email

class Contact(models.Model):
    stu = models.ForeignKey(User, related_name='stu', on_delete=models.CASCADE,blank=True, null=True)
    teacher = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    date = models.DateTimeField()
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True, null=True)


