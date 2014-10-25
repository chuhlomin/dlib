from django.contrib import admin
from django.contrib.sites.models import Site
from models import Book

admin.site.unregister(Site)
admin.site.register(Book)