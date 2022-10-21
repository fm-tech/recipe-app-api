from django.contrib import admin
from core.models import Image, Contributor, Tag, Category, Menu, MenuItem

# Register your models here.

core_models = [Image, Contributor, Tag, Category, Menu, MenuItem]

admin.site.register(core_models)
