from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreateForm, ProfileForm
from .decorators import unauthenticated_user
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.
@unauthenticated_user
def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {'form': form})

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('games:game_list')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    return redirect('games:game_list')

def user_profile(request, username):
    user = User.objects.get(username__iexact=username)
    return render(request, 'accounts/user_profile.html', {'target_user': user})

@login_required
def edit_profile(request, username):
    user = User.objects.get(username__iexact=username)
    form = ProfileForm(instance=user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', username=username)

    return render(request, 'accounts/edit_profile.html', {'form': form})

