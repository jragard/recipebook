"""recipebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebook.views import recipe_view, individual_view, author_view, recipe_add, author_add, signup_view, login_view, logout_view
from recipebook.models import Author, RecipeItem

admin.site.register(Author)
admin.site.register(RecipeItem)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_view, name='homepage'),
    path('recipe/<int:recipe_pk>', individual_view),
    path('author/<int:author_pk>', author_view),
    path('recipeadd/', recipe_add),
    path('authoradd/', author_add),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view)
]
