import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	
	#url for the api
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=51681fd29f82ee55eb7e16c51386c137'
	# my api key =  # 51681fd29f82ee55eb7e16c51386c137

	city = 'Jaipur'

	r=requests.get(url.format(city))
	print(r.text)


	return render(request,'weath/weather.html')
	# return HttpResponse("Hello world")

