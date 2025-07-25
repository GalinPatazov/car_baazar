from django import forms
from django.forms import inlineformset_factory

from .models import CarAd, CarImage


class CarAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


