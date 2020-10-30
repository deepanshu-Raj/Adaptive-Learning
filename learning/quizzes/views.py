from django.shortcuts import render, redirect
from .models import *
from courses.models import *
from django.contrib.auth.decorators import login_required
#Teacher's end for assignment creation.
@login_required
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
@login_required
def QuizHome(request):
	if request.method == 'POST':
		CQ1 = CreateQuiz_1()
		
		CQ1.date = request.POST.get('created_on')
		CQ1.title = request.POST['title']
		CQ1.desc = request.POST['desc']
		CQ1.data = Course.objects.filter(name = request.POST['info']).first()
		CQ1.author = request.user
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
@login_required
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
@login_required
def submitAssignment(request):
	return render(request,'submitAssignment.html',{})

@login_required
def takequiz(request, quiz_id):
	quiz = CreateQuiz_1.objects.filter(pk=quiz_id).first();
	question = Exam.objects.filter(quiz=quiz)
	return render(request, 'quiz.html',{'questions': question, 'quiz': quiz})
@login_required
def storeresult(request):
	res = Result()
	res.student = request.user
	quiz = CreateQuiz_1.objects.filter(pk=request.POST['quiz_id']).first()
	res.quiz =quiz
	teacher= quiz.info.author
	res.teach = teacher
	res.score = request.POST['score']
	res.save()
	return redirect('accounts:dashstu')
@login_required
def addques(request, quiz_id):
	print('HELLLLOOOOOO')
	if request.method == 'post':
		cc = Exam()
		quiz = CreateQuiz_1.objects.filter(pk=quiz_id).first()
		cc.quiz = quiz
		cc.qno = request.POST['qno']
		cc.ques = request.POST['ques']
		cc.o1 = request.POST['o1']
		cc.o2= request.POST['o2']
		cc.o3 = request.POST['o3']
		cc.o4 = request.POST['o4']
		cc.cans = request.POST['cans']
		cc.save()
	quiz = CreateQuiz_1.objects.filter(pk=quiz_id).first()
	return render(request, 'quizMain.html', {'quiz': quiz})


@login_required
def assignstu(request):
	assign = SubmitAssignment.objects.filter(student=request.user)
	return render(request, 'assignstu.html',{'assign': assign})
