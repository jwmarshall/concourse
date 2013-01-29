from concourse.forms import *
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

'''
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
'''

def home(request):
    return render_to_response('home.html', RequestContext(request))

'''
def register(request):
    if request.method == 'POST':
        form = ConcourseRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('registration_complete'));
    else:
        form = ConcourseRegistrationForm()

    return render_to_response('registration/registration_form.html', RequestContext(request, {'form': form}))
'''
