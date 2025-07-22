from django.conf.urls.static import static
from django.urls import path, include

from car_baazar import settings
from owner.views import register_view, login_view, logout_view, details_view, my_favorites, CarAdDetailView, \
    CommentDeleteView, ToggleFavoriteView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('details/', details_view, name='details'),
    # path('toggle_favorite/<int:ad_id>/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', my_favorites, name='favorites'),
    path('ads/<int:pk>/', CarAdDetailView.as_view(), name='car_ad_detail'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('ad/<int:pk>/toggle_favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)