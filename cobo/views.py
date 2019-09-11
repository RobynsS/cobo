from django.shortcuts import render
from apps.cookbook.modelinterface import Recipe, CourseList, CuisineList, LabelList
from apps.cookbook.recipefinder import RecipeFinder
from apps.cookbook.recipeadder import RecipeAdder
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def add_1(request):
    courses = CourseList()
    cuisines = CuisineList()
    labels = LabelList()

    context = {
        'courses': courses,
        'cuisines': cuisines,
        'labels': labels
    }
    return render(request, 'add_1.html', context)


def add_2(request):

    # Check if the POST comes from the first or second form page by checking the hidden variable of the second form
    form_finished = request.POST.get('end', False)

    if not form_finished:

        request.session['name'] = request.POST['name']
        request.session['servings'] = request.POST['servings']
        request.session['preparation'] = request.POST['preparation']
        request.session['price'] = request.POST['price']
        request.session['course'] = request.POST['courses']
        request.session['cuisine'] = request.POST['cuisines']
        request.session['steps'] = request.POST['steps']
        request.session['ingredients'] = request.POST['ingredients']
        request.session['labels'] = request.POST.getlist('labels')

        context = {
            'amount_steps': range(int(request.POST['steps'])),
            'amount_ingrs': range(int(request.POST['ingredients'])),
        }

        return render(request, 'add_2.html', context)

    else:

        recipe_adder = RecipeAdder(request)

        return HttpResponseRedirect(reverse('detail', args='1'))


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
