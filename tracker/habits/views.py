from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sleep(request):
    return HttpResponse("Sleep view")

def wake(request):
    return HttpResponse("wake view")

def dip(request):
    return HttpResponse("dip view")