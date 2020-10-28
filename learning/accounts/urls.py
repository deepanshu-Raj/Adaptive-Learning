from django.urls import path

from .views import *
app_name = 'accounts'

urlpatterns = [
    path('',login, name='login'),
    path('register/', Register, name='register'),
    path('coursedetail/<int:course_id>/',coursedetail, name='coursedetail'),
    path('contact/<int:stu_id>/',contact, name='contact'),
    path('contactsave',contactsave, name='contactsave'),
    path('stcontact', stcontact, name='stcontact'),
]