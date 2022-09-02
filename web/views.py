from django.shortcuts import render, get_object_or_404, redirect
from web.models import Simphony, Book, Women, Voice, Foto


def index(request):
    title = 'Виртуальный музей Андрея Белого'
    return render(request, 'index.html', {'title': title})


def muzy(request):
    title = 'Музы Андрея Белого'
    womens = Women.objects.all()
    return render(request, 'muzy.html', {'title': title, 'womens': womens})


def voices(request):
    title = 'Голоса серебрянного века'
    voices = Voice.objects.all()
    return render(request, 'golosa.html', {'title': title, 'voices': voices})


def osipov(request):
    title = 'Фильм Андрея Оиспова'
    return render(request, 'osipov.html', {'title': title})


def tropa(request):
    title = 'Аудиогид "Тропой Андрея Белого"'
    return render(request, 'tropa.html', {'title': title})


def foto(request):
    title = 'Фотогаллерея'
    fotos = Foto.objects.all()
    return render(request, 'foto.html', {'title': title, 'fotos': fotos})


def simphony(request):
    simfonii = Simphony.objects.all()
    title = 'Литературные симфонии Андрея Белого'
    return render(request, 'symphony.html', {'title': title, 'simfonii': simfonii})


def books(request):
    books = Book.objects.all()
    title = 'Произведения Андрея Белого'
    return render(request, 'books.html', {'title': title, 'books': books})





