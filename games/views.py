from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game
from django.contrib.auth.decorators import login_required

# Create your views here.
def game_list(request):
    games = Game.objects.all().order_by('-created_at')
    return render(request, 'games/game_list.html', {'games': games})

@login_required
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

@login_required
def game_detail(request, pk):
    game = Game.objects.get(id=pk)
    return render(request, 'games/game_detail.html', {'game': game})

@login_required
def update_game(request, pk):
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', username=request.user.username)

    return render(request, 'games/create_game.html', {'form': form})

@login_required
def delete_game(request, pk):
    game = Game.objects.get(id=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('accounts:user_profile', username=request.user.username)

    return render(request, 'games/delete_game.html', {'game': game})