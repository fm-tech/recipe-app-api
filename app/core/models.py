from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Images(models.Model):
    caption = models.CharField(max_length=30)
    image = models.ImageField()
