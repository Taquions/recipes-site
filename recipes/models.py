'''This module contains the models for the recipes app.'''

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    '''Model for the category object.'''
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    '''Model for the recipe object.'''
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True means that the field will be automatically set to now
    # when the object is first created.
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now=True means that the field will be automatically set to now
    # every time the object is saved.
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default=''
        )
    # upload_to is the directory where the file will be uploaded.
    # The directory will be created if it doesn't exist.
    # %Y, %m, %d are placeholders for the year, month, and day.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True,
        default=None
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        )
    # on_delete=models.SET_NULL means that if the author is deleted, the
    # author field will be set to NULL.
    # null=True means that the author field can be NULL.

    def __str__(self):
        return self.title
