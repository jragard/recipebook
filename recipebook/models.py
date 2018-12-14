from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=3000)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

