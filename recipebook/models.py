from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class RecipeItem(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
