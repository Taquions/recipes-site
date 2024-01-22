'''Module for the views of the recipes app.'''
from django.shortcuts import render


def home(request):
    '''Fuction to View for the home page.
    Remember to add the app to the list of installed apps
    in projeto/settings.py.'''
    return render(request, 'recipes/pages/home.html')


# Create your views here.
