from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation_token
from .models import *
from .forms import *
from courses.models import *
import datetime
from django.contrib.auth.decorators import login_required
from courses.models import Enroll, Course

from quizzes.models import Result

from quizzes.models import SubmitAssignment

from quizzes.models import CreateQuiz_1

UserModel = get_user_model()

#Signin - forgot password + signin with google accounts/github/linkedin accounts.
def login(request):
    if request.method == 'POST':
        print(request.POST.get('signin'))
        if request.POST.get('signin'):
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:

                auth.login(request, user)
                det = Userdetail.objects.filter(name=request.user).first()
                if det.teacher == True:
                    det = Userdetail.objects.filter(name=request.user).first()
                    courses = Course.objects.filter(author=request.user)
                    return render(request, 'dashboard.html', {'det': det, 'course': courses})
                else:
                    cour = Enroll.objects.filter(student=request.user)
                    det = Userdetail.objects.filter(name=request.user).first()
                    return render(request, 'studentdash.html', {'course': cour, 'det': det})

            #if username or password is incorrect.
            else:
                return render(request, 'login.html',{
                    'message':'Username or Password is incorrect'
                    })

        elif request.POST.get('signup'):
            return render(request,'register.html',{})

    else:
        return render(request,'login.html',{})

#Logout section
def logout(request):
    auth.logout(request)
    return render(request,'login.html',{})


#register a new user : signUp
def Register(request):
    if request.method == 'POST':
        UD = Userdetail()

        user_list = []
        for user in User.objects.values_list('username'):
            user_list.append(user[0])

         # if the username is already taken or not.
        if request.POST['username'] in user_list:
            return render(request,'register.html',{
                    'user_exist':'Username is already taken'
                    })

        #Check for password mismatch.
        if request.POST['pass'] == request.POST['cpass']:
            if len(request.POST['pass'])<6:
                return render(request,'register.html',{
                    'message_password':'password too short'
                    })
        else:
            return render(request,'register.html',{
                'message_password':'password mismatch'
                })

        NewUser = User.objects.create_user(username=request.POST['username'],email=request.POST['mail'],
            first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        NewUser.set_password(request.POST['pass'])
        NewUser.is_active = False
        NewUser.save()

        current_site = get_current_site(request)
        mail_subject = 'Activate Your Account'
        message = render_to_string(
            'acc_activate_email.html',{
            'user':NewUser,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(NewUser.pk)),
            'token':default_token_generator.make_token(NewUser)
            })

        to_mail = request.POST['mail']
        email_object = EmailMessage(
            subject=mail_subject,
            body=message,
            to=[to_mail]
            )
        email_object.send()

        UD.name = NewUser
        UD.fullname = request.POST['first_name']+" "+request.POST['last_name']
        UD.bio = request.POST['bio']
        UD.email = request.POST['mail']
        UD.mob = request.POST['mob']

        if request.POST['type'] == 'teacher':
            UD.teacher = True
        else:
            UD.teacher = False

        UD.save()
        return render(request,'thanks.html',{
            'message':'Bingo!! Just one step to go.You may now go ahead and verify yourself with the verification link sent to your email-id',
            'user':request.POST['first_name']
            })
    else:
        return render(request,'register.html',{

            })

#for activating the inactive account.
def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return render(request,'thanks.html',{
            'message':'Your Email has been Verified!!.You may now go ahead and login.',
            'user':user.first_name
            })
    else:
        return render(request,'error.html',{
            'error_message':'Activation Link Is Invalid!!'
            })

@login_required
def coursedetail(request,course_id):
    cour = Course.objects.filter(pk=course_id).first()
    stu = Enroll.objects.filter(course=cour)
    assign = SubmitAssignment.objects.filter(course=cour)
    return render(request, 'coursedetail.html', {'course': cour, 'student': stu, 'assign': assign})

@login_required
def contactsave(request):
    if request.method == 'POST':
        stu = User.objects.filter(pk=request.POST['student']).first()
        cc = Contact()
        cc.stu = stu
        cc.teacher = request.user
        cc.date = datetime.datetime.now().date()
        cc.subject = request.POST['sub']
        cc.message = request.POST['desc']
        cc.save()
        det = Userdetail.objects.filter(name=request.user).first()
        courses = Course.objects.filter(author=request.user)
        return render(request, 'dashboard.html', {'det': det, 'course': courses})

@login_required
def contact(request,stu_id):
    student = User.objects.filter(pk=stu_id).first()
    return render(request, 'contactstu.html',{'student': student})

@login_required
def stcontact(request):
    allPost = Contact.objects.filter(stu=request.user)
    return render(request, 'stcontact.html', {'allPost': allPost})

@login_required
def dashstu(request):
    cour = Enroll.objects.filter(student=request.user)
    det = Userdetail.objects.filter(name=request.user).first()
    return render(request, 'studentdash.html',{'course': cour, 'det':det})

@login_required
def dashteach(request):
    det = Userdetail.objects.filter(name=request.user).first()
    courses = Course.objects.filter(author=request.user)
    return render(request, 'dashboard.html', {'det': det, 'course': courses})

@login_required
def quizteach(request):
    quiz =Result.objects.filter(teach=request.user)
    return render(request, 'quizteach.html', {'quiz': quiz})

@login_required
def quizstu(request):
    quiz= Result.objects.filter(student=request.user)
    return render(request, 'quizstu.html', {'quiz': quiz})


@login_required
def dashboard(request):
    ud = Userdetail.objects.filter(name=request.user).first()
    if ud.teacher == True:
        return redirect('accounts:dashteach')
    else:
        return redirect('accounts:dashstu')
@login_required
def addquestion(request):
    quiz = CreateQuiz_1.objects.filter(author=request.user)
    return render(request, 'addquestion.html', {'quiz': quiz})