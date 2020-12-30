from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('create_game/', views.create_game, name='create_game'),
    path('game_detail/<int:pk>/', views.game_detail, name='game_detail'),
    path('update_game/<int:pk>/', views.update_game, name='update_game'),
    path('delete_game/<int:pk>/', views.delete_game, name='delete_game'),
    path('update_item/', views.updateItem, name='update_item'),
    path('cart/', views.cart, name='cart'),
]