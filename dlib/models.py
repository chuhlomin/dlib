from datetime import datetime, timedelta

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
    
        
    def borrowed_by(self):
        borrows = Borrow.objects.filter(book = self)
        if not borrows.count():
            return None
        else:
            return borrows[0].borrower
        
    def borrowed_on(self):
        borrows = Borrow.objects.filter(book = self)
        if not borrows.count():
            return None
        else:
            return borrows[0].rented_date
        
    def to_be_returned_on(self):
        borrows = Borrow.objects.filter(book = self)
        if not borrows.count():
            return None
        else:
            return borrows[0].rented_date + timedelta(days = borrows[0].term)
            
    
    def __unicode__(self):
        return self.title
    
class Borrow (models.Model):
    term = models.IntegerField(default = 30)
    book = models.ForeignKey(Book)
    rented_date = models.DateField()
    borrower = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.book.title + ' borrowed by ' + unicode(self.borrower) 
    
