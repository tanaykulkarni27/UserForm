from .forms import  (RegisterForm,LoginForm)
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from django.http import HttpResponse
from django import forms

def Register(request):
    Rgform = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if(Rgform.is_valid()):
            username   = request.POST['username']
            first_name = request.POST['first_name']
            last_name  = request.POST['last_name']
            password   = request.POST['password']
            email      = request.POST['email']
            add_user   = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            add_user.save()
            return HttpResponse('User saved <br><br> add your response handler.py file')
    else:
       context = {'registerform':Rgform}
       return render(request,'register.html',context)
def login(request):
    Lgform = LoginForm(request.POST or None)
    if request.method == 'POST':
        if(Lgform.is_valid()):
              username= request.POST['username']
              password = request.POST['password']              
              user = auth.authenticate(username=username,password=password)
              context = {'loginform':Lgform,'cred':'invalid credentials'}

              if not user:
                  return render(request,'login.html',context)
              else:    
                auth.login(request, user)
                return HttpResponse('Logged in <br><br> add your response in handler.py')   
    else:
       context = {'loginform':Lgform}
       return render(request,'login.html',context)       


