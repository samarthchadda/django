1.      create new project , in cmd,
	django-admin startproject weatherapp

2. 	create new app , in cmd ,
	python manage.py startapp weath

3. 	add app to the project (in settings.py), 	
	add 'weath'  in INSTALLED_APPS

4. 	Then do migrations 
	python manage.py migrate 

5.   	create superuser,
	python manage.py createsuperuser

6.   	add template into the project

7. 	call the APIs,  using api keys etc

8. 	install the requests
	pip install requests

