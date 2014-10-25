from django.forms import ModelForm
from dlib.models import Book

class BookFormAdd(ModelForm):
    class Meta:
         model = Book
         fields = [
             'title',
             'author',
             'year',
             'language',
             'isbn',
             'genre',
             'edition',
             'desc',
         ]

