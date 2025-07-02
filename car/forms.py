from django import forms
from .models import CarAd

class CarAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = [
            'title',
            'brand',
            'model',
            'year',
            'fuel_type',
            'mileage',
            'price',
            'description',
            'is_special_offer',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
