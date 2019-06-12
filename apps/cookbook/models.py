from django.db import models


class Cuisine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    servings = models.IntegerField()
    preparation_time = models.IntegerField()
    cost = models.IntegerField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    # TODO: to implement image later in this model

    def __str__(self):
        return self.name


class Step(models.Model):
    id = models.AutoField(primary_key=True)
    step_number = models.IntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'step_number')

    def __str__(self):
        return self.recipe.name + " - Step " + str(self.step_number)


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IngredientList(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.DecimalField(
        null=True, blank=True, max_digits=6, decimal_places=2)
    unit = models.ForeignKey(
        Unit, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return self.recipe.name + " - " + self.ingredient.name


class Colour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    hex = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    colour = models.ForeignKey(
        Colour, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class RecipeLabel(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'label')

    def __str__(self):
        return self.recipe.name + " - " + self.label.name
