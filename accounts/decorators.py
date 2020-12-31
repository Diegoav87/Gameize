from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from games.models import Game


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('games:game_list')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def user_permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        username = kwargs.get('username')
        user = User.objects.get(username__iexact=username)
        
        if user != request.user:
            return HttpResponse('You can not perform this action.')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def action_permission(view_func):
    def wrapper_func(request, *args, **kwargs):
        pk = kwargs.get('pk')
        game = Game.objects.get(id=pk)
        
        if game.user != request.user:
            return HttpResponse('You can not perform this action.')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func