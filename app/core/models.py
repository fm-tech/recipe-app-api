from django.db import models
from django.contrib.auth.models import User

# Supporting Data
class Image(models.Model):
    caption = models.CharField(max_length=30)
    image = models.ImageField()


# Metata data for SEO and other Social Media Standings
class MetaData(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=160)
    url = models.CharField(max_length=100)
    default_image = models.ForeignKey("Image", on_delete=models.PROTECT)


# Core Data
# Contributor adds new fields to the user model
class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Categorie(models.Model):
    name = models.CharField(max_length=50)
