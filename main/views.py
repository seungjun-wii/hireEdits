from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.

def home(response):
    return render(response, "main/homepage.html", {})

def about(response):
    return render(response, "main/about.html", {})

def opport(response):
    return render(response, "main/opport.html", {})