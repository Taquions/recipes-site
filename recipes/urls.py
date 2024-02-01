''' Module for URL routing. '''
from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:recipe_id>/', views.recipe, name='recipe'),
]
