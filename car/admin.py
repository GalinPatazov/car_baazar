from django.contrib import admin
from .models import CarAd, CarImage, Reservation, Report

@admin.register(CarAd)
class CarAdAdmin(admin.ModelAdmin):
    pass

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass
