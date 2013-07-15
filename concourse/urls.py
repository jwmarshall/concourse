from concourse.forms import ConcourseRegistrationForm
from concourse.views import *
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from registration.forms import RegistrationFormTermsOfService
from registration.views import register

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concourse.views.home', name='home'),
    # url(r'^concourse/', include('concourse.foo.urls')),

    url(r'^$', home, {}, 'home'), #direct_to_template, {'template': 'index.html'}, 'home'),

    url(r'^accounts/register/$', register, {
            'backend': 'registration.backends.default.DefaultBackend',
            'form_class': ConcourseRegistrationForm,
        }, 'registration_register'),

    url(r'^accounts/', include('registration.backends.default.urls')),

#    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {}, 'login'),
#    url(r'^accounts/logout/$', logout_user, {}, 'logout'),
#    url(r'^accounts/register/$', register, {}, 'register'),
#    url(r'^accounts/registration_complete/$', direct_to_template, {'template': 'registered.html'}, 'registration_complete'),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html'), name='privacy'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
