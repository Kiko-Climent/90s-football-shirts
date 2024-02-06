from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        labels = {
            'value': 'Rate this product:'
        }
        widgets = {
            'value': forms.Select(choices=Rating.VALUE_CHOICES),
        }
