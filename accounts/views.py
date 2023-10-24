from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password1']

        if password == confirm_password:
           if User.objects.filter(username=username).exists():
               messages.info(request,'Username already exists')
               return redirect('register')

           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email already exists')
               return redirect('register')
           
           else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
           
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        
        return redirect('/')

    return render(request,'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')