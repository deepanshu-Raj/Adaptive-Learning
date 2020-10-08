from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User

def allcourse(request):
    query = request.GET.get('q', None)
    if query:
        results = Course.objects.filter(Q(name__icontains=query) | Q(subject__icontains=query))
        return render(request, 'allcourse.html', {'course': results})
    else:
        cour = Course.objects.all()
        return render(request, 'allcourse.html', {'course': cour})


def addcourse(request):
    if request.method == 'POST':
        cc = Course()
        cc.name = request.POST['name']
        cc.author = request.user
        cc.desc = request.POST['desc']
        cc.date = request.POST['date']
        cc.img = request.FILES['image']
        cc.save()
    return render(request,'addcourse.html')
