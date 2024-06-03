from django.shortcuts import render, redirect
from . forms import CreateUserForm

def homepage(request):
    return render(request, 'chance/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('my-login')
        
    context = {'registerform': form}

    return render(request, 'chance/register.html', context=context) 

def my_login(request):
    return render(request, 'chance/my-login.html') 

def dashboard(request):
    return render(request, 'chance/dashboard.html')