from django.db import models
from django.contrib.auth.models import User

class Book (models.Model):
    title    = models.CharField(max_length=100)
    author   = models.CharField(max_length=100)
    year     = models.IntegerField()
    language = models.CharField(max_length=2)
    isbn     = models.CharField(max_length=50, blank=True, null=True)
    genre    = models.CharField(max_length=50, blank=True, null=True)
    edition  = models.IntegerField(blank=True, null=True)
    pic      = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField()
    owner = models.ForeignKey(User)
    
    
class Borrow (models.Model):
    term = models.IntegerField(default = 30)
    book = models.ForeignKey(Book)
    rented_date = models.DateField()
    borrower = models.ForeignKey(User)
    
