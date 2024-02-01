'''Module for the views of the recipes app.'''
from django.shortcuts import render, get_list_or_404, get_object_or_404
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
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            # category__id is the way to access the foreign key field.
            is_published=True
        ).order_by('-id'),
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f"{recipes[0].category.name} | "
    })


def recipe(request, recipe_id):
    '''View for the recipe page.'''
    recipe_ = get_object_or_404(
        Recipe,
        id=recipe_id,
        is_published=True
        )
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe_,
        'is_detail_page': True,
    })
# Create your views here.
