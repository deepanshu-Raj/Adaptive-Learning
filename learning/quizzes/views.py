from django.shortcuts import render
from .models import *
from courses.models import *

#Teacher's end for assignment creation.
def createAssignment(request):
	if request.method == 'POST':
		CA = CreateAssignment()
		
		# add CA.info = ??

		#CA.info = Course.objects.filter(Course.name==request.POST['info']).first()
		#print(CA.info)
		CA.created_on = request.POST.get('created_on')
		CA.title = request.POST['title']
		CA.desc = request.POST['desc']
		CA.task  = request.POST['task']
		#CA.save()
		return render(request,'thanks.html',{
			'courses':Course.objects.all(),
			'message':'You have successfully created the assignment!'
			})
	else:
		return render(request,'createAssignment.html',{
				'courses':Course.objects.all()
			})