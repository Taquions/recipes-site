'''Module for the views of the recipes app.'''
import os
from django.db.models import Q
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http.response import Http404

from recipes.models import Recipe
from utils.pagination import make_pagination


PER_PAGE = os.environ.get('PER_PAGE', 6)  # take from .env


def home(request):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in project/settings.py.'''
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
    })


def category(request, category_id):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in project/settings.py.'''
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            # category__id is the way to access the foreign key field.
            is_published=True
        ).order_by('-id'),
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
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


def search(request):
    '''View for the search page.'''
    search_term = request.GET.get('q', '').strip()
    # request.GET.get('q') is used to get the value of the query parameter q
    # the second get is for return none if the parameter is not found
    # strip is used to remove the white spaces from the string

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        # __icontains is used to make the search using 'LIKE' in SQL
        # and the i means that doesn't matter if the string is upper or lower
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'q={search_term}&',
    })
