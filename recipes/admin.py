'''Module for registering models with the admin site.'''

from django.contrib import admin
from .models import Category, Recipe


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin class for the category model.'''
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    '''Admin class for the recipe model.'''
    ...
