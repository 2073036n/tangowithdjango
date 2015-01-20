from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there world! <html><a href=about/>about</a></html>')

def about(request):
    return HttpResponse('This tutorial has been put together by Timothy Ness, 2073036n. <html><a href=http://127.0.0.1:8000/rango/>index</a></html>')

