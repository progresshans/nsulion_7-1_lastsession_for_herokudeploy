from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password = request.POST['password1']
            )

            auth.login(request, user)
            return redirect('/post')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect('/post')
        else:
            return render(request, 'signin.html', {'errors' : '아이디 or 비밀번호 오류'})
    return render(request, 'signin.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return redirect('/post')
    

# Create your views here.
