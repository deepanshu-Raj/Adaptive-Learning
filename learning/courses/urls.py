from django.urls import path

from .views import *
app_name = 'courses'

urlpatterns = [
    path('allcourse',allcourse, name='allcourse'),
    path('addcourse',addcourse , name='addcourse'),
    path('addmaterial', addmaterial, name='addmaterial'),
]