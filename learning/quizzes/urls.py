from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "quizzes"

urlpatterns = [
    path('createAssignment/',createAssignment,name="cassgn"),
    path('quizhome/',QuizHome,name='qhome'),
    path('quizmain/',QuizMain,name='qmain'),
    path('submitAssignment/',submitAssignment,name='sassgn'),
    path('takequiz/<int:quiz_id>/', takequiz, name='takequiz'),
    path('storeresult', storeresult, name='storeresult'),
    path('addques/<int:quiz_id>/', addques, name='addques'),
    path('assignstu', assignstu, name='assignstu'),
]