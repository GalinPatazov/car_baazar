from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin, DeleteView

from car import models
from car.models import CarAd
from .forms import RegisterForm, LoginForm, CommentForm
from .models import Favorite, Comment


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


class CarAdDetailView(DetailView):
    model = CarAd
    template_name = 'car_ad_detail.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.object
        user = self.request.user

        is_favorite = False
        if user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=user, car_ad=ad).exists()

        comments = ad.comments.all().order_by('-created_at')

        context['is_favorite'] = is_favorite
        context['comments'] = comments
        context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        # Обработваме формата за нов коментар
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.ad = self.object
            comment.author = request.user
            comment.save()
            return redirect('car_ad_detail', pk=self.object.pk)
        else:
            # Ако формата не е валидна - пак рендерираме с грешките
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(CarAd, pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user, car_ad=ad)
        if not created:
            favorite.delete()
        return redirect('car_ad_detail', pk=pk)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    def get_success_url(self):
        ad = self.object.ad
        return reverse_lazy('car_ad_detail', kwargs={'pk': ad.pk})

    def test_func(self):

        user = self.request.user
        return user.is_staff or user.groups.filter(name='staff').exists()


def custom_404(request, exception):
    return render(request, '404.html', status=404)