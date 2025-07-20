from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from car.models import CarAd


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    city = models.CharField(
        max_length=100,
        blank=True,
    )
    is_verified = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        blank=True,
    )

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages',
    )
    content = models.TextField()
    sent_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_read = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.sender.username} → {self.recipient.username}"


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    car_ad = models.ForeignKey(
        CarAd,
        on_delete=models.CASCADE,
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('user', 'car_ad')

    def __str__(self):
        return f"{self.user.username} favorited {self.car_ad.title}"


class Comment(models.Model):
    ad = models.ForeignKey('car.CarAd', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} rated {self.ad} - {self.rating}★'

