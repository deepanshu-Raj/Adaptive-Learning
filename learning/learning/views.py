from django.shortcuts import render, HttpResponse, redirect

from courses.models import Course

def home(request):
    course = Course.objects.filter(author=request.user)
    return render(request, 'home.html', {'course': course})

def aboutUs(request):
	return render(request,'about.html',{})

def Contact(request):
	if request.method == 'POST':
		#work for it's backend !!
		return render(request,'../accounts/templates/thanks.html',{
			'user':first_name,
			'message':'Thank You for your invaluable feedback!!.We will reach to you as soon as possible.',
			'msg_cnt':'Your Feedback feedback has been sent successfully!!'
			})
	else:
		return render(request,'contact.html',{})