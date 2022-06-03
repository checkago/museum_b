from django.shortcuts import render, get_object_or_404, redirect
from web.models import Simphony, Book


def index(request):
    title = 'Виртуальный музей Андрея Белого'
    return render(request, 'index.html', {'title': title})


def simphony(request):
    simfonii = Simphony.objects.all()
    title = 'Литературные симфонии Андрея Белого'
    return render(request, 'symphony.html', {'title': title, 'simfonii': simfonii})


def books(request):
    books = Book.objects.all()
    title = 'Произведения Андрея Белого'
    return render(request, 'books.html', {'title': title, 'books': books})





