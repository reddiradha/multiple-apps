from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_first(request):
    return HttpResponse('<h1>this is first function in app2</h1>')

def app2_second(request):
    return HttpResponse('<h2>this is second function in app2</h2>')
