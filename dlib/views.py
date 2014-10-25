from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from dlib.models import Book, Borrow
from dlib.forms import BookFormAdd

def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    borrow = Borrow(book=book, borrower=user, term=30, rented_date = date.today())
    borrow.save()
    return HttpResponseRedirect('/book/' + str(book_id) )
    

def landing(request):
    d = {
        'books': Book.objects.order_by('-id')[:4],
        'user': request.user,
        'form': AuthenticationForm(),
        'next': request.path,
        'isRoot': True
    }
    d.update(csrf(request))
    return render_to_response('landing.html', d)

def user(request):
    return render_to_response('user.html')

def book(request, book_id):
    arguments = {
        'user': request.user,
        'book': Book.objects.get(pk=book_id),
        'next': request.path,
        'isRoot': False
    }
    return render_to_response('book.html', arguments)

def booklist(request):
    arguments = {
        'user': request.user,
        'books': Book.objects.all(),
        'isRoot': False
    }
    return render_to_response('booklist.html', arguments)

def book_add(request):

    arguments = {
        'user': request.user,
        'isRoot': False
    }

    if request.method == 'POST':

        form = BookFormAdd(request.POST)

        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return HttpResponseRedirect('/book/' + str(book.id))

    else:
        form = BookFormAdd()

    arguments["form"] = form
    arguments.update(csrf(request))

    return render_to_response('add_book.html', arguments)
