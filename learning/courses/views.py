from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

def allcourse(request):
    query = request.GET.get('q', None)
    if query:
        results = Course.objects.filter(Q(name__icontains=query) | Q(subject__icontains=query))
        return render(request, 'allcourse.html', {'course': results})
    else:
        cour = Course.objects.all()
        return render(request, 'allcourse.html', {'course': cour})

@login_required
def addcourse(request):
    if request.method == 'POST':
        cc = Course()
        cc.name = request.POST['name']
        cc.author = request.user
        cc.desc = request.POST['desc']
        cc.subject = request.POST['subject']
        cc.date = datetime.datetime.now().date()
        cc.img = request.FILES['image']
        cc.save()
    cour = Course.objects.filter(author=request.user)
    return render(request,'addcourse.html',{'course':cour})


@login_required
def addmaterial(request):
    mat = Material()
    nam = request.POST['course']
    cour = get_object_or_404(Course, author=request.user, name=nam)
    mat.course = cour
    mat.type = "Material"
    mat.file = request.FILES['material']
    mat.desc = request.POST['desc']
    mat.date = datetime.datetime.now().date()
    mat.save()
    cour = Course.objects.filter(author=request.user)
    return render(request, 'addcourse.html', {'course': cour})
