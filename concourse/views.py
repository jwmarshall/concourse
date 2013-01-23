from concourse.forms import *
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def home(request):
    return render_to_response('home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/account/");
    else:
        form = RegisterForm()
    return render_to_response('register.html', RequestContext(request, {'form': form}))
