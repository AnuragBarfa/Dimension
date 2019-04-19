from django.shortcuts import render
from login.forms import RegistrationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login # view also have name login so import this login function as other name
# from django.contrib.auth.decorators import login_required
#
# # Create your views here.
def login(request):
  return render(request, 'registration/login.html')

def register(request):
  return render(request, 'registration/signup.html')
def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        print("valid")
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                return render(request, 'home/home.html')
    return render(request, 'registration/signup.html',{'form':form})
def home(request):
  return render(request, 'home/home.html')
