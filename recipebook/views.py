from django.shortcuts import render
from recipebook.models import RecipeItem, Author


def recipe_view(request):

    results = RecipeItem.objects.all()
    return render(request, 'recipe_view.html', {'data': results})


def individual_view(request, recipe_pk):

    filtered_result = RecipeItem.objects.all().filter(id=recipe_pk)
    recipe_id = filtered_result.values()[0]['id']
    author_id = filtered_result.values()[0]['author_id']
    # print(recipe_id)
    aut = Author.objects.all().values()
    # print(aut)

    for item in aut:
        if item['id'] == author_id:
            author = item['name']
            aut_id = item['id']
            bio = item['bio']

    # print(filtered_result.values()[0])

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


    print(aut.values())
    print('hey')
    results = RecipeItem.objects.all().values().filter(author_id=author_pk)
    print(results)

    # for item in results:
    #     if item.author_id == int(request.META['PATH_INFO'][-1]):
    #         filtered_result.append(item.title)

    return render(request, 'author_view.html', {'data': results,
                                                'author': aut.values()[id - 1]['name'],
                                                'bio': aut.values()[id - 1]['bio']})
