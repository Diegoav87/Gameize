from django.shortcuts import render

# Create your views here.
def game_list(request):
    return render(request, 'games/game_list.html')