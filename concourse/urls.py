from concourse.views import *
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concourse.views.home', name='home'),
    # url(r'^concourse/', include('concourse.foo.urls')),

    url(r'^$', home, {}, 'home'), #direct_to_template, {'template': 'index.html'}, 'home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {}, 'login'),
    url(r'^logout/$', logout_user, {}, 'logout'),
    url(r'^register/$', register, {}, 'register'),
    url(r'^terms/$', direct_to_template, {'template': 'terms.html'}, 'terms'),
    url(r'^privacy/$', direct_to_template, {'template': 'privacy.html'}, 'privacy'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
