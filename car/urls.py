from django.urls import path, include

from car.views import home_view, create_ad_view, special_offers_view, edit_ad, delete_ad, car_ad_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_ad_view, name='create_ad'),
    path('special-offers/', special_offers_view, name='special_offers'),
    # path('cars/', car_list, name='car_list'),
    path('edit/<int:pk>/', edit_ad, name='edit_ad'),
    path('delete/<int:pk>/', delete_ad, name='delete_ad'),
    path('ad/<int:pk>/', car_ad_detail, name='car_ad_detail'),


]
