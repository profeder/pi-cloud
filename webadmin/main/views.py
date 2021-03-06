from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout


@login_required
def home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET['next']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(next)
        else:
            context += {'error': 'Invalid login credentials'}
    return HttpResponse(template.render(context, request))


def logout(request):
    return auth_logout(request)
