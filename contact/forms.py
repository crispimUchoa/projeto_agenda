from typing import Any
from django.core.exceptions import ValidationError
from django import forms

from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name', 'phone',
            'email', 'description', 'category', 'picture',
            )
                
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui',
                },
                
            )
        }

     