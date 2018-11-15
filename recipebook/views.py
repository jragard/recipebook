from django.shortcuts import render
from django.http import HttpResponse
from recipebook.models import RecipeItem


def recipe_view(request):

    results = RecipeItem.objects.all()

    return render(request, 'recipe_view.html', {'data':results})