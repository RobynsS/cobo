from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def search(request):
    return render(request, 'search.html')


def detail(request):
    return render(request, 'detail.html')
