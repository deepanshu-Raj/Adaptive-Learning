from django.db import models
from courses.models import *

#1 for creating assignment
class CreateAssignment(models.Model):

	info = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
	created_on = models.DateTimeField()
	title = models.CharField(max_length=200,null=True,blank=False)
	desc = models.TextField(null=True,blank=False)
	task = models.FileField(null=True,blank=False)

	def __str__(self):
		return self.title+'-'+self.info.subject

	class Meta:
		verbose_name_plural = 'Create Assignment'

#for saving qiuz's data : Home Page - Quizhome
class CreateQuiz_1(models.Model):
	
	info = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
	date = models.DateTimeField()
	title = models.CharField(max_length=200,null=True,blank=False)
	desc = models.TextField(null=True,blank=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Quiz Home'

#for adding questions in this Quiz - Quizmain
class CreateQuiz_2(models.Model):
	
	CHOICES = (
		('A','Option A'),
		('B','Option B'),
		('C','Option C'),
		('D','Option D')
	)

	#data has been taken from the quiz home model.
	data = models.ForeignKey(CreateQuiz_1,on_delete=models.CASCADE,null=True)
	question = models.TextField(null=True,blank=False)
	option1 = models.TextField(null=True,blank=False)
	option2 = models.TextField(null=True,blank=False)
	option3 = models.TextField(null=True,blank=False)
	option4 = models.TextField(null=True,blank=False)
	answer = models.CharField(choices=CHOICES,max_length=1,null=True,blank=False)

	class Meta:
		verbose_name_plural = 'Quiz Main'


class SubmitAssignment(models.Model):

	data = models.ForeignKey(CreateAssignment,on_delete=models.CASCADE,null=True)
	studentResponse = models.FileField(null=True,blank=False)

	class Meta:
		verbose_name_plural = 'Submit Assignment'


class SubmitQuiz(models.Model):

	subject = models.ForeignKey(Course,on_delete=models.CASCADE,null = True)
	title = models.ForeignKey(CreateQuiz_1,on_delete=models.CASCADE,null = True)
	answer = models.CharField(max_length=20,null=True,blank=False)