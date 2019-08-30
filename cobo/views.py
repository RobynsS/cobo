from django.shortcuts import render
from apps.cookbook.modelinterface import Recipe, CourseList, CuisineList, LabelList
from apps.cookbook.recipefinder import RecipeFinder


def index(request):
    return render(request, 'index.html')


def add(request):
    courses = CourseList()
    cuisines = CuisineList()
    labels = LabelList()

    context = {
        'courses': courses,
        'cuisines': cuisines,
        'labels': labels
    }
    return render(request, 'add.html', context)


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


def result(request):
    recipe_finder = RecipeFinder(request)
    recipe_finder.searchRecipe()
    context = {
        'recipes': recipe_finder.getResult(),
    }
    return render(request, 'result.html', context)


def detail(request, recipe_id):
    recipe = Recipe(recipe_id)
    context = {
        'recipe': recipe
    }

    return render(request, 'detail.html', context)
