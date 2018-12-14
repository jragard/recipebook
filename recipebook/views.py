from recipebook.models import RecipeItem, Author
from recipebook.forms import RecipeAdd, AuthorAdd, SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import reverse, render, HttpResponseRedirect
from django.contrib.auth.models import User


def recipe_view(request):

        results = RecipeItem.objects.all()
        return render(request, 'recipe_view.html', {'data': results})


def individual_view(request, recipe_pk):

        filtered_result = RecipeItem.objects.all().filter(id=recipe_pk)
        author_id = filtered_result.values()[0]['author_id']
        aut = Author.objects.all().values()

        for item in aut:
                if item['id'] == author_id:
                        author = item['name']
                        aut_id = item['id']
                        bio = item['bio']

        return render(request, 'individual_view.html', {'title': filtered_result.values()[0]['title'],
                                                        'body': filtered_result.values()[0]['body'],
                                                        'time': filtered_result.values()[0]['time_required'],
                                                        'instructions': filtered_result.values()[0]['instructions'],
                                                        'author': author,
                                                        'recipe_id': filtered_result.values()[0]['id'],
                                                        'author_id': aut_id,
                                                        'bio': bio})


def author_view(request, author_pk):

        aut = Author.objects.all().values()
        id = int(request.META['PATH_INFO'][-1])
        author_pk = id

        results = RecipeItem.objects.all().values().filter(author_id=author_pk)

        return render(request, 'author_view.html', {'data': results,
                                                    'author': aut.values()[id - 1]['name'],
                                                    'bio': aut.values()[id - 1]['bio']})


@login_required()
def recipe_add(request):
        html = 'recipe_add.html'
        form = None

        if request.method == 'POST':
                # Take the information from the request and shove it into the database
                form = RecipeAdd(request.user, request.POST)

                if form.is_valid():
                        data = form.cleaned_data

                        RecipeItem.objects.create(
                                title=data['title'],
                                body=data['body'],
                                author=Author.objects.filter(id=data['author']).first(),
                                time_required=data['time_required'],
                                instructions=data['instructions']
                        )
                        return render(request, 'thanks.html')
        else:
                # everything we get here is going to be a GET request
                form = RecipeAdd(user=request.user)
        
        return render(request, html, {'form': form})


@staff_member_required
def author_add(request):
        html = 'author_add.html'
        form = None

        if request.method == 'POST':
                form = AuthorAdd(request.POST)

                if form.is_valid():
                        data = form.cleaned_data

                        Author.objects.create(
                                name=data['name'],
                                bio=data['bio'],
                        )
                        return render(request, 'thanks.html')
        else:
                form = AuthorAdd()
        
        return render(request, html, {'form': form})


def signup_view(request):

        html = 'signup.html'

        form = SignupForm(None or request.POST)

        if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                        data['username'], data['email'], data['password']
                )
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

        return render(request, html, {'form': form})


def login_view(request):
        html = 'login.html'

        form = LoginForm(None or request.POST)

        if form.is_valid():
                data = form.cleaned_data
                user = authenticate(username=data['username'], password=data['password'])
                if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse('homepage'))

        return render(request, html, {'form': form})


def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))