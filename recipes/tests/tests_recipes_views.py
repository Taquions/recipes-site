'''This file contains the tests for the recipes app.'''
from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views


class RecipeViewsTest(TestCase):
    '''Test that the views are correctly mapped to the urls.'''
    def test_recipe_home_view_function_is_correct(self):
        '''Test that the home view function is correctly mapped to the url.'''
        view = resolve(reverse('recipes:home'))
        # resolve is used to get the view function of the url
        self.assertIs(view.func, views.home)
        # self.assertIs is used to compare if the argument is the same object

    def test_recipe_category_view_function_is_correct(self):
        '''Test that the category view function is correctly
        mapped to the url'''
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        '''Test that the detail view function is correctly
        mapped to the url.'''
        view = resolve(
            reverse('recipes:recipe', kwargs={'recipe_id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_search_uses_correct_view_function(self):
        '''Test that the search view function is correctly'''
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
