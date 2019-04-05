from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render


#function based view

#these will handle a request and return a HttpResponse
# def home (request):
# 	# print(request)
# 	# print(dir(request))
	
# 	return HttpResponse("<html><head><style>h1{color:red;}</style></head<body><h1>Hello World</h1></body></html>")    #it will return HTML code 


def home(request):
	# response = HttpResponse(content_type="application/json")     #response object
	response = HttpResponse(content_type="text/html")  
	response.write("<p>Here's the text of the webpage")
	response.write("<h1> Response Objects</h1>")
	print(response.status_code)
	#all other data above it will be removed , only this will be displayed
	response.content = 'some new content'      
	response.write("<p>displayed</p>")

	#changing status code (to 404 page not found)
	response.status_code = 404         #default is 200

	return response



def redirect_somewhere(request):

	return HttpResponseRedirect("/some/path")     #can be a url like http://joincfe.com




	