from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from webapp.cdb import CatDataBase


def cat_view(request: WSGIRequest):
    action_from_form = request.POST.get('action')
    message = CatDataBase.action(action_from_form)
    CatDataBase.name = request.POST.get('name', CatDataBase.name)
    game_status = CatDataBase.get_status()
    if game_status:
        context = {
            'name': CatDataBase.name,
            'image': CatDataBase.image,
            'age': CatDataBase.age,
            'happiness': CatDataBase.happiness,
            'satiety': CatDataBase.satiety,
            'message': message
        }
        return render(request, 'cat.html', context=context)
    else:
        response = redirect('/')
        return response