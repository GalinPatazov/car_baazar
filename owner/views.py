from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from car.models import CarAd
from .forms import RegisterForm, LoginForm
from .models import Favorite


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def details_view(request):
    return render(request, 'details.html')


# @login_required
# def toggle_favorite(request, ad_id):
#     ad = get_object_or_404(CarAd, id=ad_id)
#     favorite = Favorite.objects.filter(user=request.user, car_ad=ad)
#
#     if favorite.exists():
#         favorite.delete()  # премахваме от любими
#     else:
#         Favorite.objects.create(user=request.user, car_ad=ad)  # добавяме в любими
#
#     return redirect('car_ad_detail', ad_id=ad.id)  # връща обратно към страницата на обявата
#
#
@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('car_ad')
    return render(request, 'favorites.html', {'favorites': favorites})

