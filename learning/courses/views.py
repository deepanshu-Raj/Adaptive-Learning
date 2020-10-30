from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
import datetime

from quizzes.models import *

from quizzes.models import CreateAssignment

from quizzes.models import SubmitAssignment

@login_required
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


@login_required
def detail(request,course_id):
    cour = Course.objects.filter(pk=course_id).first()
    taken = Enroll.objects.filter(student=request.user, course=cour).first()
    if taken:
        return render(request, 'detail.html',{'course':cour, 'taken':True})
    return render(request, 'detail.html',{'course':cour, 'taken':False})


@login_required
def enrollment(request, course_id):
    cour = Course.objects.filter(pk=course_id).first()
    enr = Enroll()
    enr.course = cour
    enr.student = request.user
    enr.save()
    material = Material.objects.filter(course=cour)
    tests = Test.objects.filter(course=cour)
    return render(request, 'courmat.html', {'course': cour, 'material': material, 'tests': tests})

@login_required
def courmat(request, course_id):
    cour = Course.objects.filter(pk=course_id).first()
    material = Material.objects.filter(course=cour)
    assign = CreateAssignment.objects.filter(info=cour)
    test = CreateQuiz_1.objects.filter(info=cour)
    return render(request,'courmat.html', {'course':cour, 'material': material, 'tests': test, 'assign': assign})

@login_required
def show(request, file_id):
    file = Material.objects.filter(pk=file_id).first()
    return render(request, 'show.html', {'mat': file})
@login_required
def assignment(request,assign_id):
    assign = CreateAssignment.objects.filter(pk=assign_id).first()
    return render(request, 'assignment.html', {'assign': assign})
@login_required
def submit(request,assign_id):
    assign = CreateAssignment.objects.filter(pk=assign_id).first()
    sub = SubmitAssignment()
    sub.studentResponse = request.FILES['work']
    sub.data = assign
    sub.course = assign.info
    sub.student = request.user
    sub.save()
    assign = CreateAssignment.objects.filter(pk=assign_id).first()
    return redirect('accounts:dashstu')
