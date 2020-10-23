from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "quizzes"

urlpatterns = [
    path('createassignment/',createAssignment,name="cassgn")
]