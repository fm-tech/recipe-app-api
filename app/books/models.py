from pyexpat import model
from django.db import models
from django.forms import JSONField


# Create your models here.
class Recipie(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    document = models.JSONField(default=dict)
    images = models.ManyToManyField("core.Image", blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=175)
    in_recipie = models.ManyToManyField("Recipie")

    def __str__(self):
        return self.name
