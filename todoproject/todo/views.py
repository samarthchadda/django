from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):

	#accessing all the objects in database that represent a todo
	todo_list = Todo.objects.order_by('id')

	#forms
	form = TodoForm()

	
	context = {'todo_list':todo_list, 'form':form}
	#now create loop in index.html list

	return render(request,'todo/index.html',context)


#decorator
@require_POST     #it views this view only accept post request
def addTodo(request):
	form = TodoForm(request.POST)     #it will take all the POST data of the form (data that is passed to the form)
									#and form action is also   POST

	# print(request.POST['text'])        #'text' field  we made in forms.py
									

	#adding data to database
	if form.is_valid():     #means if form is completed and have the type of value we want
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()

	#redirecting them back to the page,    we do not need to refresh
	return redirect('index')


def completeTodo(request,todo_id):
	todo = Todo.objects.get(pk=todo_id)     #get object of particular id 
	todo.complete = True

	todo.save()


	return redirect('index')


def deleteCompleted(request):
	#all todos that are completed
	Todo.objects.filter(complete=True).delete()              #exact value of complete column must be true, then delete them
	
	return redirect('index')


def deleteAll(request):
	Todo.objects.all().delete()

	return redirect('index')