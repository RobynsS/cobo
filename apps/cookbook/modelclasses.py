from .models import Recipe as RecipeModel
from .models import Label as LabelModel


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
        self.cuisine = recipe_query.cuisine_id.name

        # Fill in multi parameters of object into class
        labels = []
        for entry in recipe_query.recipelabel_set.all():
            labels.append(Label(entry.label.id))
        self.labels = labels


class Label:
    def __init__(self, label_id):
        label_query = LabelModel.objects.get(pk=label_id)
        self.name = label_query.name
        self.colour = label_query.colour
