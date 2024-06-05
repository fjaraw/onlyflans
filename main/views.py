from django.shortcuts import render
from django.http import HttpResponse
from main.productos import productos

# Create your views here.
def index(req):
    context = {'productos': productos}
    return render(req, 'index.html', context)
def about(req):
    return render(req, 'about.html')
def welcome(req):
    return render(req, 'welcome.html')