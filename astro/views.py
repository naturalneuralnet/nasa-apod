from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
# These are controllers
def index(request):
    return render(request, 'index.html')


def picture(request):
    #pull data from third party rest api
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')    
    #convert reponse data into json
    data = response.json()
    print(data['url'])    
    return HttpResponse( response)
    