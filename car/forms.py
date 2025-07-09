from django import forms
from django.forms import inlineformset_factory

from .models import CarAd, CarImage


class CarAdForm(forms.ModelForm):
    class Meta:
        model = CarAd
        fields = '__all__'  # or list fields manually if needed
        exclude = ['owner']  # owner will be set automatically in the view
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


