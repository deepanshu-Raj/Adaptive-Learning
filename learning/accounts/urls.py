from django.urls import path,include
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from .forms import *
from .views import *
from .forms import *
app_name = 'accounts'

urlpatterns = [
    
    #one for logout also!!
    path('',login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', logout, name='logout'),
    
    path('coursedetail/<int:course_id>/',coursedetail, name='coursedetail'),
    path('contact/<int:stu_id>/',contact, name='contact'),
    path('contactsave',contactsave, name='contactsave'),
    path('stcontact', stcontact, name='stcontact'),

    path('activate/<uidb64>/<token>/',activate,name='activate'),

    path('reset_password/',
        PasswordResetView.as_view(template_name='password_reset.html',
            form_class=EmailValidationOnForgotPassword),name='password_reset'),

    path('password_reset/done/',
        PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
        name="password_reset_confirm"),

    path('reset/done/',
        PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
        name='password_reset_complete'),

    path('dashstu/', dashstu, name='dashstu'),
    path('dashteach/', dashteach, name='dashteach'),
    path('dashboard/', dashboard, name='dashboard'),
    path('quizteach/', quizteach, name='quizteach'),
    path('quizstu/', quizstu, name='quizstu'),
    path('addquestion/', addquestion, name='addquestion'),
    
]
