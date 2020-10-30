from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.leaderHome, name="leader-home"),
]