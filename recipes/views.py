'''Module for the views of the recipes app.'''
from django.shortcuts import render
from django.http import Http404
from recipes.models import Recipe


def home(request):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in projeto/settings.py.'''
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in projeto/settings.py.'''
    recipes = Recipe.objects.filter(
        category__id=category_id,
        # category__id is the way to access the foreign key field.
        is_published=True
        ).order_by('-id')

    if not recipes:
        raise Http404('Category not found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f"{recipes.first().category.name} | "
    })


def recipe(request, recipe_id):
    '''View for the recipe page.'''
    recipe_ = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe_,
        'is_detail_page': True,
    })
# Create your views here.
