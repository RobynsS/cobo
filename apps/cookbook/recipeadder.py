from .models import Recipe as RecipeModel
from .models import Course as CourseModel
from .models import Cuisine as CuisineModel
from .models import Label as LabelModel
from .models import RecipeLabel as RecipeLabelModel
from .models import Step as StepModel
from .models import IngredientList as ListModel
from .models import Ingredient as IngredientModel
from .models import Unit as UnitModel


class RecipeAdder:
    def __init__(self, request):
        self.recipe = RecipeQuery(request)
        self.id = 0

    def addRecipeToDatabase(self):

        # Add a Recipe entry
        recipeEntry = RecipeModel()
        recipeEntry.name = self.recipe.name
        recipeEntry.servings = self.recipe.servings
        recipeEntry.preparation_time = self.recipe.preparation
        recipeEntry.cost = self.recipe.price

        # Search course entry based on it's name and add it to the recipe
        course = CourseModel.objects.get(name=self.recipe.course)
        recipeEntry.course_id = course

        # Search cuisine entry based on it's name and add it to the recipe
        cuisine = CuisineModel.objects.get(name=self.recipe.cuisine)
        recipeEntry.cuisine_id = cuisine

        recipeEntry.save()
        self.id = recipeEntry.pk

        # Add labels
        for entry in self.recipe.labels:
            recipeLabelEntry = RecipeLabelModel()
            label = LabelModel.objects.get(name=entry)
            recipeLabelEntry.recipe = recipeEntry
            recipeLabelEntry.label = label

            recipeLabelEntry.save()

        # Add steps
        for entry in self.recipe.steps:
            stepEntry = StepModel()
            stepEntry.recipe = recipeEntry
            stepEntry.instruction = entry["text"]
            stepEntry.step_number = entry["number"]

            stepEntry.save()

        # Add ingredients
        for entry in self.recipe.ingredients:
            ingredientListEntry = ListModel()

            # check if ingredient is known in database
            ingredient = IngredientModel.objects.filter(
                name=entry["ingredient"]).first()

            if not ingredient:
                # ingredient does not exist and should be created
                ingredient = IngredientModel()
                ingredient.name = name = entry["ingredient"]
                ingredient.save()

            # check if unit is known in  database
            unit = UnitModel.objects.filter(
                name=entry["unit"]).first()

            if not unit:
                # unit does not exist and should be created
                unit = UnitModel()
                unit.name = name = entry["unit"]
                unit.save()

            ingredientListEntry.ingredient = ingredient
            ingredientListEntry.recipe = recipeEntry
            ingredientListEntry.unit = unit
            ingredientListEntry.quantity = entry["quantity"]

            ingredientListEntry.save()

    def getRecipeID(self):
        return self.id


class RecipeQuery:

    def __init__(self, request):
        self.name = request.session.get('name')
        self.servings = int(request.session.get('servings'))
        self.preparation = int(request.session.get('preparation'))
        self.price = int(request.session.get('price'))
        self.course = request.session.get('course')
        self.cuisine = request.session.get('cuisine')
        self.labels = request.session.get('labels')

        self.steps = self.getSteps(request)
        self.ingredients = self.getIngredients(request)

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
                "quantity": float(request.POST['ingr_' + str(i + 1) + "_qty"]),
                "unit": request.POST['ingr_' + str(i + 1) + "_unit"].lower(),
                "ingredient": request.POST['ingr_' + str(i + 1)].capitalize()
            }
            ingr_list.append(dict(entry))

        return ingr_list
