from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from dlib.models import Book

def landing(request):
    images = [
        'cryptonomicon.jpg',
        'erlang.jpg',
        'hgttg.jpg',
        'thinking.jpg'
    ]
    d = {
        'images': images,
        'user': request.user,
        'form': AuthenticationForm(),
        'isRoot': True
    }
    d.update(csrf(request))
    return render_to_response('landing.html', d)


def user(request):
    return render_to_response('user.html')


def book(request):
    arguments = {
        'user': request.user,
        'books': Book.objects.all(),
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