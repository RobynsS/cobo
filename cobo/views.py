from django.shortcuts import render
from apps.cookbook.modelinterface import Recipe


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def search(request):
    return render(request, 'search.html')


def detail(request, recipe_id):
    recipe = Recipe(recipe_id)
    context = {
        'recipe': recipe
    }

    return render(request, 'detail.html', context)
