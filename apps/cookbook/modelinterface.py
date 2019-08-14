from .models import Recipe as RecipeModel
from .models import Label as LabelModel
from .models import Step as StepModel
from .models import IngredientList as ListModel
from .models import Course as CourseModel
from .models import Cuisine as CuisineModel


class Recipe:
    def __init__(self, recipe_id):
        # Get recipe object from database
        recipe_query = RecipeModel.objects.get(pk=recipe_id)

        # Fill in single parameters of object into class
        self.name = recipe_query.name
        self.servings = recipe_query.servings
        self.preparation_time = recipe_query.preparation_time
        self.cost = recipe_query.cost
        self.course = recipe_query.course_id.name
        self.cuisine = recipe_query.cuisine_id.initials
        self.id = recipe_id

        # Fill in multi parameters of object into class
        labels = []
        for entry in recipe_query.recipelabel_set.all():
            labels.append(Label(entry.label.id))
        self.labels = labels

        steps = []
        for entry in recipe_query.step_set.all().order_by('step_number'):
            steps.append(Step(entry.id))
        self.steps = steps

        ingredientlist = []
        for entry in recipe_query.ingredientlist_set.all():
            ingredientlist.append(IngredientList(entry.id))
        self.ingredientlist = ingredientlist


class Label:
    def __init__(self, label_id):
        label_query = LabelModel.objects.get(pk=label_id)
        self.name = label_query.name
        self.colour = label_query.colour


class Step:
    def __init__(self, step_id):
        step_query = StepModel.objects.get(pk=step_id)
        self.number = step_query.step_number
        self.instruction = step_query.instruction


class IngredientList:
    def __init__(self, list_id):
        list_query = ListModel.objects.get(pk=list_id)
        self.ingredient = list_query.ingredient

        if list_query.quantity:
            self.quantity = '%g' % (list_query.quantity)
        else:
            self.quantity = ""

        if list_query.unit:
            self.unit = list_query.unit
        else:
            self.unit = ""


class CourseList:
    def __init__(self):
        entries = []
        for entry in CourseModel.objects.all().order_by('name'):
            entries.append(entry)
        self.list = entries


# class Cuisine:
#     def __init__(self, id):
#         # Get cuisine object from database
#         cuisine_query = CuisineModel.objects.get(pk=id)
#         self.name = cuisine_query.name
#         self.initials = cuisine_query.initials


class CuisineList:
    def __init__(self):
        entries = []
        for entry in CuisineModel.objects.all().order_by('name'):
            entries.append(entry)
        self.list = entries

    def get_initials(self, name):
        initials = None

        for entry in self.list:
            if(name == entry.name):
                initials = entry.initials

        return initials


class LabelList:
    def __init__(self):
        entries = []
        for entry in LabelModel.objects.all().order_by('name'):
            entries.append(entry)
        self.list = entries


class RecipesList:
    def __init__(self):
        entries = []
        for entry in RecipeModel.objects.all().order_by('name'):
            entries.append(Recipe(entry.id))
        self.entries = entries
