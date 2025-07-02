from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render

from car.forms import CarAdForm
from car.models import CarAd


def home_view(request):
    return render(request, 'home.html')


@login_required
def create_ad_view(request):
    if request.method == 'POST':
        form = CarAdForm(request.POST)
        if form.is_valid():
            car_ad = form.save(commit=False)
            car_ad.owner = request.user
            car_ad.save()
            return redirect('home')
    else:
        form = CarAdForm()
    return render(request, 'create_ad.html', {'form': form})

# @login_required
# def edit_ad_view(request, pk):
#     car_ad = get_object_or_404(CarAd, pk=pk, owner=request.user)  # само собственикът може да редактира
#
#     if request.method == 'POST':
#         form = CarAdForm(request.POST, instance=car_ad)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # след редакция връщаме на home
#     else:
#         form = CarAdForm(instance=car_ad)
#
#     return render(request, 'edit_ad.html', {'form': form, 'car_ad': car_ad})
#
#
# @login_required
# def delete_ad_view(request, pk):
#     car_ad = get_object_or_404(CarAd, pk=pk, owner=request.user)  # само собственик може да изтрива
#     if request.method == 'POST':
#         car_ad.delete()
#         return redirect('home')
#     return render(request, 'delete_ad_confirm.html', {'car_ad': car_ad})

def special_offers_view(request):
    offers = CarAd.objects.filter(is_special_offer=True)
    return render(request, 'special_offers.html', {'offers': offers})