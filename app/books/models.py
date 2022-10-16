from django.db import models
from django.forms import JSONField

# Create your models here.
class Recipie(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    document = models.JSONField(default={})
    images = models.ManyToManyField("Image")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=175)
    in_recipie = models.ManyToManyField("Recipie")

    def __str__(self):
        return self.name
