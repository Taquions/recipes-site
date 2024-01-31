'''Module for the views of the recipes app.'''
from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in projeto/settings.py.'''
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(6)],
    })


def recipe(request, recipe_id):
    '''View for the recipe page.'''
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
# Create your views here.
