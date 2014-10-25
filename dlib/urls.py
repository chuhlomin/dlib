from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dlib.views.landing', name='landing'),
    url(r'^user$', 'dlib.views.user', name='user'),
    url(r'^book$', 'dlib.views.book', name='book'),
    url(r'^booklist$', 'dlib.views.booklist', name='booklist'),
    
    # url(r'^dlib/', include('dlib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
