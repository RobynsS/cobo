from django.shortcuts import render
from apps.cookbook.modelinterface import Recipe, CourseList, CuisineList, LabelList


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def search(request):
    courses = CourseList()
    cuisines = CuisineList()
    labels = LabelList()

    context = {
        'courses': courses,
        'cuisines': cuisines,
        'labels': labels
    }
    return render(request, 'search.html', context)


def detail(request, recipe_id):
    recipe = Recipe(recipe_id)
    context = {
        'recipe': recipe
    }

    return render(request, 'detail.html', context)
