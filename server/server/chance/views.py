from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'chance/index.html')

def register(request):
    return render(request, 'chance/register.html') 

def my_login(request):
    return render(request, 'chance/my-login.html') 

def dashboard(request):
    return render(request, 'chance/dashboard.html')