from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return HttpResponse ("hello worls")

def about(request):
    return HttpResponse ("about")

def privacy(request):
    return HttpResponse ("privacy")

def hello(request, number):
    return HttpResponse("hello" + str(number))

def render123(request):
    return render(request, "index.html")