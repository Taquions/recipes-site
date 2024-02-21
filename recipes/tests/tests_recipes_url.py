'''This file contains the tests for the recipes app.'''
from django.test import TestCase
from django.urls import reverse


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

    def test_recipe_search_url_is_correct(self):
        '''Test that the search url is correct.'''
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
