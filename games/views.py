from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def game_list(request):
    games = Game.objects.all().order_by('-created_at')
    item_count = 0

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()

        for item in items:
            item_count += item.quantity

    return render(request, 'games/game_list.html', {'games': games, 'item_count': item_count})

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

def updateItem(request):
    data = json.loads(request.body)
    gameId = data['gameId']
    action = data['action']
    print(action, gameId)

    game = Game.objects.get(id=gameId)
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, game=game)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added', safe=False)

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()

    total = 0
    item_count = 0
    for item in items:
        total += (item.game.price) * item.quantity
        item_count += item.quantity

    return render(request, 'games/cart.html', {'items': items, 'total': total, 'item_count': item_count})

@login_required
def checkout(request):
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()

    total = 0
    item_count = 0
    for item in items:
        total += (item.game.price) * item.quantity
        item_count += item.quantity

    return render(request, 'games/checkout.html', {'items': items, 'total': total, 'item_count': item_count})

@login_required
def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    total = float(data['total'])
    order.transaction_id = transaction_id

    items = order.orderitem_set.all()
    check_total = 0
    for item in items:
        check_total += float(item.game.price) * float(item.quantity)

    if total == float(check_total):
        order.complete = True
    order.save()

    return JsonResponse('Payment complete', safe=False)