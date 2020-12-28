from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all().order_by('-created_at')
    return render(request, 'games/game_list.html', {'games': games})

def create_game(request):
    form = GameForm()

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)

        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('games:game_list')

    return render(request, 'games/create_game.html', {'form': form})