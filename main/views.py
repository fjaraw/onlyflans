from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, 'index.html')
def about(req):
    return render(req, 'about.html')
def welcome(req):
    return render(req, 'welcome.html')