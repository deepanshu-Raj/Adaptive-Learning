from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Course(models.Model):
    name=models.CharField(max_length=30)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    subject=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    img=models.ImageField(upload_to='courses/',blank=True,null=True)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    type=models.CharField(max_length=20)
    date=models.DateTimeField()
    file = models.FileField(upload_to='material/', blank=True, null=True)
    desc=models.CharField(max_length=60)


class Test(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    date=models.DateTimeField()
    file=models.FileField(upload_to='test/')


class Enroll(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    done = models.IntegerField(default=0, blank=True, null=True)

