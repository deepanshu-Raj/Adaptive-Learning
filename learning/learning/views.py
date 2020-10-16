from django.shortcuts import render, HttpResponse, redirect

from courses.models import Course

def home(request):
    course = Course.objects.filter(author=request.user)
    return render(request, 'home.html', {'course': course})