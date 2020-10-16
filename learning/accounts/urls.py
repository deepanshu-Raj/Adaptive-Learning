from django.urls import path

from .views import *
app_name = 'accounts'

urlpatterns = [
    path('',login, name='login'),
    path('register', register, name='register')

]