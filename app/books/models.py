from email.policy import default
from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models
from django.forms import JSONField


# Create your models here.
class Recipie(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    document = models.JSONField(default=dict)
    images = models.ManyToManyField("core.Image", blank=True)
    category = models.ManyToManyField("core.Category", blank=True)
    tags = models.ManyToManyField("core.Tag", blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=175)
    in_recipie = models.ManyToManyField("Recipie")

    def __str__(self):
        return self.name


class NutritionalFacts(models.Model):
    fat = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)


class RecipieDetails(models.Model):
    prep_time_minutes = models.IntegerField(default=0)
    cook_time_minutes = models.IntegerField(default=0)
    services = models.IntegerField(default=0)
    leftover_safe = models.BooleanField(default=False)
