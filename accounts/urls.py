from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
    path('edit_profile/<str:username>/', views.edit_profile, name='edit_profile'),
]