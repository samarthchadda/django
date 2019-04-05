from django.urls import path

from . import views     #getting all the views

urlpatterns = [
    # urls('admin/', admin.site.urls),
	path('', views.index, name='index'),
    path('add',views.addTodo, name= 'add'),
    path('complete/<todo_id>',views.completeTodo, name= 'complete'),
    path('deletecomplete',views.deleteCompleted, name= 'deletecomplete11'),
    path('deleteall',views.deleteAll, name= 'deleteall')

]
