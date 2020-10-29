from django.contrib import admin
from django.urls import path, include
from .views import *
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name='home'),
    path('contact/',Contact,name='contact'),
    path('aboutus/',aboutUs,name='about'),
    path('', include('accounts.urls', namespace='accounts')),
    # path('chatbot/', include('chatbot.urls', namespace='chatbot')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('discussions/', include('discussions.urls', namespace='discussions')),
    path('quizzes/', include('quizzes.urls', namespace='quizzes')),
    path('',include('django.contrib.auth.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)