from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dlib.views.landing', name='landing'),
    url(r'^user$', 'dlib.views.user', name='user'),
    url(r'^book/(\d+)$', 'dlib.views.book', name='book'),
    url(r'^booklist$', 'dlib.views.booklist', name='booklist'),
    url(r'^add_book$', 'dlib.views.add_book', name='add_book'),
    url(r'^takeit/(\d+)$', 'dlib.views.borrow_book', name='borrow_book'),
    

    # url(r'^dlib/', include('dlib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
