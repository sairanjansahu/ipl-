from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('<marquee><h1>MSD IS THE BEST FINISHER IN THE WORLD</h1></marquee>')

def raina(request):
    return HttpResponse('<marquee><h1> SURESH RAINA IS KNOWN AS MR IPL</h1></marquee>')