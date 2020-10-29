from django.shortcuts import render
from .models import *
from courses.models import *

#Teacher's end for assignment creation.
def createAssignment(request):
	if request.method == 'POST':
		CA = CreateAssignment()

		CA.info = Course.objects.filter(name=request.POST['info']).first()
		CA.created_on = request.POST.get('created_on')
		CA.title = request.POST['title']
		CA.desc = request.POST['desc']
		CA.task  = request.POST.get('task')
		CA.save()
		return render(request,'thanks.html',{
			'courses':Course.objects.all(),
			'message':'You have successfully created the assignment!'
			})
	else:
		return render(request,'createAssignment.html',{
				'courses':Course.objects.all()
			})

# Home page for the quiz - complete
def QuizHome(request):
	if request.method == 'POST':
		CQ1 = CreateQuiz_1()
		
		CQ1.date = request.POST.get('created_on')
		CQ1.title = request.POST['title']
		CQ1.desc = request.POST['desc']
		CQ1.data = Course.objects.filter(name = request.POST['info']).first()
		CQ1.save()
		return render(request,'quizHome.html',{
			'message':'Your Data has been saved successfully!! Now, You can Now Add problems!!'
			})
	else:
		return render(request,'quizHome.html',{
			'courses':Course.objects.all()
			})

#pass data successfully added message here.

#You need to link the user seeting the quiz!!  - !!ISSUE!!
def QuizMain(request):
	if request.method == 'POST':
		CQ2 = CreateQuiz_2()
		if request.POST.get('save'):
			
			#CQ2.data = CreateQuiz_1.objects.filter(pk=reques.POST['quiz_id']).first()
			CQ2.question = request.POST['question']
			CQ2.option1 = request.POST['option1']
			CQ2.option2 = request.POST['option2']
			CQ2.option3 = request.POST['option3']
			CQ2.option4 = request.POST['option4']
			CQ2.answer = request.POST['answer']
			#CQ2.save()

			return render(request,'quizMain.html',{

				})

		elif request.POST.get('exit'):
			
			# CQ2.data = ??
			CQ2.question = request.POST['question']
			CQ2.option1 = request.POST['option1']
			CQ2.option2 = request.POST['option2']
			CQ2.option3 = request.POST['option3']
			CQ2.option4 = request.POST['option4']
			CQ2.answer = request.POST['answer']
			#CQ2.save()

			return render(request,'thanks.html',{
				'message':'You have successfully created the quiz!'
				})

	else:
		return render(request,'quizMain.html',{

			})

def submitAssignment(request):
	return render(request,'submitAssignment.html',{})


def takequiz(request, quiz_id):
	quiz = CreateQuiz_1.objects.filter(pk=quiz_id).first();
	question = Exam.objects.filter(quiz=quiz)
	return render(request, 'quiz.html',{'questions': question, 'quiz': quiz})

def storeresult(request):
	res = Result()
	res.student = request.user
	quiz = CreateQuiz_1.objects.filter(pk=request.POST['quiz_id'])
	res.quiz =quiz
	res.score = request.POST['score']
	res.save()

