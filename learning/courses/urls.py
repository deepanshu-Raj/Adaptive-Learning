from django.urls import path

from .views import *
app_name = 'courses'

urlpatterns = [
    path('allcourse',allcourse, name='allcourse'),
    path('addcourse',addcourse , name='addcourse'),
    path('addmaterial', addmaterial, name='addmaterial'),
    path('detail/<int:course_id>/', detail, name='detail'),
    path('enrollment/<int:course_id>/', enrollment, name='enrollment'),
    path('courmat/<int:course_id>/', courmat, name='courmat'),
    path('show/<int:file_id>/', show, name='show'),
    path('submit/<int:assign_id>/', submit, name='submit'),
    path('assignment/<int:assign_id>/', assignment, name='assignment'),
]