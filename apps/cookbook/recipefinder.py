from .modelinterface import RecipesList, CuisineList


class RecipeFinder:
    def __init__(self, request):
        self.recipes_all = RecipesList()
        self.recipes_filtered = []
        self.query = SearchQuery(request)

    def searchRecipe(self):

        filter = CombinedFilter(
            [TextFilter(self.query.text), CuisineFilter(self.query.cuisines)])

        # filter = TextFilter(self.query.text)

        for recipe in self.recipes_all.entries:
            if(filter.filter(recipe)):
                self.recipes_filtered.append(recipe)

    def getResult(self):
        return self.recipes_filtered


class SearchQuery:
    def __init__(self, request):
        self.text = request.POST['text']
        self.courses = request.POST.getlist('courses')
        self.cuisines = request.POST.getlist('cuisines')
        self.labels = request.POST.getlist('labels')


class TextFilter:
    def __init__(self, filter_text):
        self.filter_text = filter_text

    def filter(self, recipe):
        filter_boolean = False

        if(self.filter_text == ""):
            filter_boolean = True

        # Search on title
        elif(self.filter_text.lower() in recipe.name.lower()):
            filter_boolean = True

        # Search on ingredient
        for entry in recipe.ingredientlist:
            if(self.filter_text.lower() in entry.ingredient.name.lower()):
                filter_boolean = True

        return filter_boolean


class CuisineFilter:
    def __init__(self, filter_cuisines):
        self.filter_cuisines = filter_cuisines
        self.cuisine_list = CuisineList()

    def filter(self, recipe):
        filter_boolean = False

        if(self.filter_cuisines == []):
            filter_boolean = True

        else:
            for cuisine in self.filter_cuisines:
                if(self.cuisine_list.get_initials(cuisine) == recipe.cuisine):
                    filter_boolean = True

        return filter_boolean


class CombinedFilter:
    def __init__(self, filter_array):
        self.filters = filter_array

    def filter(self, recipe):
        filter_boolean = True

        for filter in self.filters:
            filter_boolean = filter_boolean & filter.filter(recipe)

        return filter_boolean
