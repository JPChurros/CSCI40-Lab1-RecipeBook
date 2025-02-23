from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def recipe_list(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def recipeListTemplate(request, num=1):
    if num == 1:
        number = "1"
    elif num == 2:
        number = "2"
    else:
        number = "0"
    return render(request, 'recipeListTemplate.html', {'number':number})
# Create your views here.
