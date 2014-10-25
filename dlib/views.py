from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from dlib.models import Book, Borrow
from django.contrib.auth.models import User
from dlib.forms import BookFormAdd


def user(request, user_id):
    user_p = User.objects.get(pk=user_id)
    books_owned_by_user = Book.objects.filter(owner = user_p) 
    books_borrowed_by_user = [b.book for b in Borrow.objects.filter(borrower = user_p)]
    
    d = {
        'books_owned': books_owned_by_user,
        'books_borrowed': books_borrowed_by_user,
        'next': request.path,
        'user': request.user,
        'user_p': user_p,
        'isRoot': False
    }
    d.update(csrf(request))
    return render_to_response('user.html', d)
 
def return_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    borrow = Borrow.objects.get(book=book)
    borrow.delete()
    return HttpResponseRedirect('/book/' + str(book_id) )
    
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
        'next': request.path,
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
            if book.title == u'\u0412\u0438\u0439':
                book.pic='viy.jpg'
            
            elif book.title == 'Clean Code':
                book.pic = 'cleancode.jpg'
            book.save()
            return HttpResponseRedirect('/book/' + str(book.id))

    else:
        form = BookFormAdd()

    arguments["form"] = form
    arguments.update(csrf(request))

    return render_to_response('add_book.html', arguments)
