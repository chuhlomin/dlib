from django.db import models

class Book (models.Model):
    title    = models.CharField(max_length=100)
    author   = models.CharField(max_length=100)
    year     = models.IntegerField()
    language = models.CharField(max_length=2)
    # isbn     = models.CharField(max_length=50, blank=True)
    # genre    = models.CharField(max_length=50, blank=True)
    # edition  = models.IntegerField(blank=True)
    # pic      = models.CharField(max_length=50)#, blank=True)
