from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render

from car.forms import CarAdForm
from car.models import CarAd
from owner.models import Favorite


def home_view(request):
    if request.user.is_authenticated:
        ads = CarAd.objects.all()
        return render(request, 'home.html', {'ads': ads})
    return render(request, 'home.html')

from django.contrib.auth.decorators import login_required

# @login_required
# def car_list(request):
#     cars = CarAd.objects.all()
#     return render(request, 'car_list.html', {'cars': cars})

@login_required
def create_ad_view(request):
    if request.method == 'POST':
        form = CarAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = request.user
            ad.save()
            return redirect('home')  # or whatever your list view is
    else:
        form = CarAdForm()
    return render(request, 'create_ad.html', {'form': form})

@login_required
def edit_ad(request, pk):
    ad = get_object_or_404(CarAd, pk=pk)

    if request.user != ad.owner and not request.user.is_superuser:
        raise PermissionDenied()

    if request.method == 'POST':
        form = CarAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarAdForm(instance=ad)

    return render(request, 'edit_ad.html', {'form': form})

@login_required
def delete_ad(request, pk):
    ad = get_object_or_404(CarAd, pk=pk)

    if request.user != ad.owner and not request.user.is_superuser:
        raise PermissionDenied()

    if request.method == 'POST':
        ad.delete()
        return redirect('home')

    return render(request, 'delete_ad_confirm.html', {'ad': ad})

def car_ad_detail(request, pk):
    ad = get_object_or_404(CarAd, pk=pk)
    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, car_ad=ad).exists()

    context = {
        'ad': ad,
        'is_favorite': is_favorite,
    }
    return render(request, 'car_ad_detail.html', context)

def special_offers_view(request):
    offers = CarAd.objects.filter(is_special_offer=True)
    return render(request, 'special_offers.html', {'offers': offers})

# @login_required
# def edit_ad(request, pk):
#     ad = get_object_or_404(CarAd, pk=pk)
#
#     # Owner, superuser, or has permission via group
#     if request.user != ad.owner and not request.user.is_superuser and not request.user.has_perm('car.change_carad'):
#         raise PermissionDenied()
#
#     if request.method == 'POST':
#         form = CarAdForm(request.POST, request.FILES, instance=ad)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CarAdForm(instance=ad)
#
#     return render(request, 'edit_ad.html', {'form': form})