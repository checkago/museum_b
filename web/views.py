from django.shortcuts import render, get_object_or_404, redirect
from web.models import Simphony


def index(request):
    title = 'Виртуальный музей Андрея Белого'
    return render(request, 'index.html', {'title': title})


def simphony(request):
    simfonii = Simphony.objects.all()
    title = 'Литературные симфонии Андрея Белого'
    return render(request, 'symphony.html', {'title': title, 'simfonii': simfonii})





