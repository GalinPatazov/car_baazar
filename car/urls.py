from django.urls import path, include

from car.views import home_view, create_ad_view, special_offers_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_ad_view, name='create_ad'),
    path('special-offers/', special_offers_view, name='special_offers'),
    # path('edit/<int:pk>/', edit_ad_view, name='edit_ad'),
    # path('delete/<int:pk>/', delete_ad_view, name='delete_ad'),
]