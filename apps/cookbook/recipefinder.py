from .modelinterface import RecipesList


class RecipeFinder:
    def __init__(self, request):
        self.recipes_all = RecipesList()
        self.recipes_filtered = []
        self.query = SearchQuery(request)

    def searchRecipe(self):

        filter = TextFilter(self.query.text)

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

        a = self.filter_text
        a = a.lower()
        b = recipe.name
        b = b.lower()
        c = a in b

        if(self.filter_text == ""):
            filter_boolean = True
        elif(self.filter_text.lower() in recipe.name.lower()):
            filter_boolean = True

        return filter_boolean
