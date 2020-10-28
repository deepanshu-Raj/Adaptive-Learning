from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
from .models import *
from courses.models import *
import datetime



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            det = Userdetail.objects.filter(name=request.user).first()
            courses = Course.objects.filter(author=request.user)
            return render(request, 'dashboard.html', {'det': det, 'course':courses})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

# Rgistration view - complete.
def Register(request):
    if request.method == 'POST':
        UD = Userdetail()

        user_list = []
        for user in User.objects.values_list('username'):
            user_list.append(user[0])

        if request.POST['username'] in user_list:

            # work - password belongs to this user verification is left!!
            if request.POST['pass'] == request.POST['cpass']:
                UD.name = User.objects.filter(username=request.POST['username'])[0]
            else:
                return render(request,'register.html',{
                    'pwd':'(Incorrect Password Entered :Enter Correct Password !!)'
                    })
        else:
            return render(request,'register.html',{
                'user_msg':'(Please Enter Correct username!!)'
                })


        UD.fullname = request.POST['name']
        UD.bio = request.POST['bio']
        UD.email = request.POST['mail']
        UD.mob = request.POST['mob']
        
        if request.POST['type'] == 'teacher':
            UD.teacher = True
        else:
            UD.teacher = False

        print('saved')    
        #UD.save()
        return render(request,'thanks.html',{
            'message':'Bingo!! You have been Registered'
            })    
    else:
        return render(request,'register.html',{

            })

def coursedetail(request,course_id):
    cour = Course.objects.filter(pk=course_id).first()
    stu = Enroll.objects.filter(course=cour)
    return render(request, 'coursedetail.html', {'course': cour, 'student': stu})


def contactsave(request):
    if request.method == 'POST':
        stu = User.objects.filter(pk=request.POST['student']).first()
        cc = Contact()
        cc.student = stu
        cc.teacher = request.user
        cc.date = datetime.datetime.now().date()
        cc.subject = request.POST['sub']
        cc.message = request.POST['desc']
        cc.save()
        det = Userdetail.objects.filter(name=request.user).first()
        courses = Course.objects.filter(author=request.user)
        return render(request, 'dashboard.html', {'det': det, 'course': courses})


def contact(request,stu_id):
    student = User.objects.filter(pk=stu_id).first()
    return render(request, 'contact.html',{'student': student})


def stcontact(request):
    allPost = Contact.objects.filter(student=request.user)
    return render(request, 'stcontact.html', {'allPost': allPost})
