from django.shortcuts import render
from django.http import HttpResponse
from recipebook.models import RecipeItem


def recipe_view(request):
    html = """
    oh I guess this maybe works?
    """

    return HttpResponse(html)