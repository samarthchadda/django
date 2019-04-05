from django.db import models

class Todo(models.Model):

	text  = models.CharField(max_length = 40)
	complete = models.BooleanField(default=False)  #todo is actually complete or not


	#returning text as representation of todo
	def __str__(self):
		return self.text


#now register this on admin.py
