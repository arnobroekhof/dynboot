from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import re

# set the macc address regex
X = '([a-fA-F0-9]{2}[:|\-]?){6}'



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynboot.views.home', name='home'),
    # url(r'^dynboot/', include('dynboot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #pxe specific
    url(r'^pxelinux\.cfg/default/$','pxe.views.index'),
    url(r'^pxelinux\.cfg/default/(?P<macaddr>([0-9A-F]{2}[:-]){5}([0-9A-F]{2}))','pxe.views.macfilter'),
)
