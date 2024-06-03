from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Home")

def register(request):
    return HttpResponse("Register") 

def my_login(request):
    return HttpResponse("Login") 

def dashboard(request):
    return HttpResponse("Dashboard")