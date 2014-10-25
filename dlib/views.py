from django.http import HttpResponse
from django.shortcuts import render_to_response


def landing(request):
    images = [
        'cryptonomicon.jpg',
        'erlang.jpg',
        'hgttg.jpg',
        'thinking.jpg'
    ]

    return render_to_response('landing.html', {'images': images})


def user(request):
    return render_to_response('user.html')


def book(request):
    return render_to_response('book.html')


def booklist(request):
    return render_to_response('booklist.html')