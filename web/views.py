from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    title = 'Виртуальный музей Андрея Белого'
    return render(request, 'index.html', {'title': title})


