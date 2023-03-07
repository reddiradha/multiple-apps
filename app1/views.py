from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_first(request):
    return HttpResponse('<h1>this is first function in app1</h1>')

def app1_second(request):
    return HttpResponse('<marquee><h2>this is second function in app1</h2></marquee')
