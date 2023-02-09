from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.cdb import CatDataBase


def index_view(request: WSGIRequest):
    game_status = CatDataBase.get_status()
    if game_status:
        context = {'end_game_message': 'Постарайтесь не убить вашего кота'}
    else:
        context = {'end_game_message': 'Ваш кот сдох, создайте нового кота, чтобы'
                                       ' продолжить игру'}
    return render(request, 'index.html', context=context)