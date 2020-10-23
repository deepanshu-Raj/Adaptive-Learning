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

