from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return HttpResponse('<marquee><h1>rohit is the best opener in the world</h1></marquee>')

def sky(request):
    return HttpResponse('<marquee><h1>sky is no1 t20 player in the world</h1></marquee>')