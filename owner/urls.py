from django.urls import path, include

from owner.views import register_view, login_view, logout_view, details_view, my_favorites

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('details/', details_view, name='details'),
    # path('toggle_favorite/<int:ad_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', my_favorites, name='favorites'),

]