from django.contrib import admin

from .models import Course, Label, Cuisine, Colour, Recipe, Step, Ingredient, Unit, IngredientList, RecipeLabel

# Register your models here.
admin.site.register(Course)
admin.site.register(Label)
admin.site.register(Cuisine)
admin.site.register(Colour)
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(IngredientList)
admin.site.register(RecipeLabel)
