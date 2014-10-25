from django.db import models

class Book (models.Model):
    title    = models.CharField(max_length=100)
    author   = models.CharField(max_length=100)
    year     = models.IntegerField()
    language = models.CharField(max_length=2)
    isbn     = models.CharField(max_length=50, blank=True, null=True)
    genre    = models.CharField(max_length=50, blank=True, null=True)
    edition  = models.IntegerField(blank=True, null=True)
    pic      = models.CharField(max_length=50, blank=True, null=True)
