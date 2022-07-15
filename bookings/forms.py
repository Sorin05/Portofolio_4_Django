from django import forms
from .models import Booking


class BookSessionForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__al__'