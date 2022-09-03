from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.

def home(response):
    return render(response, "main/homepage.html", {})

def about(response):
    return render(response, "main/about.html", {})

def opport(response):
    return render(response, "main/opport.html", {})

def profile(response):
    return render(response, "main/profile.html", {})

def edit(response):
    return render(response, "main/edit.html", {})

def company1(response):
    return render(response, "main/comp.html", {})

def login(response):
    return render(response, "main/login.html", {})