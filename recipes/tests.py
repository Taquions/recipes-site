'''This file contains the tests for the recipes app.'''
from django.test import TestCase
from django.urls import reverse, resolve

from . import views


class RecipeURLTests(TestCase):
    '''Test that the urls are correctly mapped to the views.'''
    def test_recipe_home_url_is_correct(self):
        '''Test that the home url is correct.'''
        # reverse is used to get the url of the view
        home_url = reverse('recipes:home')
        # self.assertEqual is used to compare the expected url with the url
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        '''Test that the category url is correct.'''
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/category/1/')

    def test_recipe_detail_url_is_correct(self):
        '''Test that the detail url is correct.'''
        detail_url = reverse('recipes:recipe', kwargs={'recipe_id': 1})
        self.assertEqual(detail_url, '/recipes/1/')


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
