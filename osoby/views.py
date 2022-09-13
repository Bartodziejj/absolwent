from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Jesse, we need to cook.</h1>")
# Create your views here.
