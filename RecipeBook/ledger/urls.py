from django.urls import path
from .views import recipe_list, recipeListTemplate

urlpatterns = {
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipeListTemplate, name='recipeListTemplate')
}

app_name = "ledger"