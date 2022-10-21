from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Supporting Data
class Image(models.Model):
    caption = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.caption


# Metata data for SEO and other Social Media Standings
class MetaData(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=160)
    url = models.CharField(max_length=100)
    default_image = models.ForeignKey("Image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


# Core Data
# Contributor adds new fields to the user model
class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_about = models.CharField(max_length=250, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Menu(models.Model):
    location = models.CharField(max_length=25)
    models.ManyToManyField("app.Model", blank=True, null=True)

    def __str__(self):
        return self.location


class MenuItem(models.Model):
    title = models.CharField(max_length=25)
    uri = models.URLField(max_length=220, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
