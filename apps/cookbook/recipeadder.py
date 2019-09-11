class RecipeAdder:
    def __init__(self, request):
        self.recipe = RecipeQuery(request)

    # def addRecipeToDatabase(self):

    # def getRecipeID(self):


class RecipeQuery:

    def __init__(self, request):
        self.name = request.session.get('name')
        self.servings = request.session.get('servings')
        self.preparation = request.session.get('preparation')
        self.price = request.session.get('price')
        self.course = request.session.get('course')
        self.cuisine = request.session.get('cuisine')
        self.labels = request.session.get('labels')

        self.steps = self.getSteps(request)
        self.ingredients = self.getIngredients(request)

        self.a = 1

    def getSteps(self, request):
        steps_list = []
        for i in range(int(request.session.get('steps'))):
            entry = {"number": i+1, "text": request.POST['step_' + str(i + 1)]}
            steps_list.append(dict(entry))

        return steps_list

    def getIngredients(self, request):
        ingr_list = []
        for i in range(int(request.session.get('ingredients'))):
            entry = {
                "quantity": request.POST['ingr_' + str(i + 1) + "_qty"],
                "unit": request.POST['ingr_' + str(i + 1) + "_unit"],
                "ingredient": request.POST['ingr_' + str(i + 1)]
            }
            ingr_list.append(dict(entry))

        return ingr_list
