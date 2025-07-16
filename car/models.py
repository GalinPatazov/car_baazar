from django.db import models
from django.conf import settings

FUEL_CHOICES = [
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Electric', 'Electric'),
    ('Hybrid', 'Hybrid'),
]

class CarAd(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
    )
    brand = models.CharField(
        max_length=50,
    )
    model = models.CharField(
        max_length=50,
    )
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
    )
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    description = models.TextField()
    is_special_offer = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    class Meta:
        permissions = [
            ("can_edit_all_ads", "Can edit all ads"),
            ("can_delete_any_ad", "Can delete any car ad"),
        ]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarImage(models.Model):
    car_ad = models.ForeignKey(
        CarAd,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to='car_images/',
    )

    def __str__(self):
        return f"Image for {self.car_ad.title}"


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    car_ad = models.ForeignKey(
        CarAd,
        on_delete=models.CASCADE,
    )
    reservation_date = models.DateTimeField()
    message = models.TextField(
        blank=True,
    )
    is_confirmed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.user.username} reserved {self.car_ad.title}"


class Report(models.Model):
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    car_ad = models.ForeignKey(
        CarAd,
        on_delete=models.CASCADE,
    )
    reason = models.TextField()
    reported_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.reporter.username} reported {self.car_ad.title}"
