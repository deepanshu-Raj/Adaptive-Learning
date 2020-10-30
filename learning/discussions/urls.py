from django.urls import path, include
from django.conf.urls.static import static
from . import views

app_name = 'discussions'

urlpatterns = [
    path('upvote', views.upVote, name="upVote"),
    path('postComment', views.postComment, name="postComment"),
    path('createPost', views.createPost, name="createPost"),
    path('newPost', views.newPost, name="newPost"),
    path('',views.discussionHome, name='discussionHome'),
    path('<str:slug>',views.discussionPost, name='discussionPost'),
]