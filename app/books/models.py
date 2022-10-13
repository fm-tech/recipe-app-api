from email.policy import default
from django.db import models
from django.forms import JSONField

# Create your models here.
class Recipie(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    document = models.JSONField(default={})

    def __str__(self):
        return self.name
