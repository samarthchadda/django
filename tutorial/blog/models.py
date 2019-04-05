from django.db import models

# Create your models here.

class PostModel(models.Model):    #we are writing python class that inherits everything from django models.Model  (models is class And Model is function)
	# id = models.AutoField(primary_key=True)      it is present by default

	#changing the type of field
	id = models.BigAutoField(primary_key=True)

	active = models.BooleanField(null=True)   #can be empty in the database 
	active1 = models.BooleanField(default=True)    #all the previous and future values are true ,  unless we change them
	
	title = models.CharField(max_length=30,default="Samarth",verbose_name='Post Model')    #for 30 characters
	content = models.TextField(null=True,blank=True)

	pass

#now add these things using admin.py


'''
python manage.py makemigrations -- run everytime we change models.py    ,   it set ups the database changes
python manage.py migrate    --     it then runs the database changes

'''