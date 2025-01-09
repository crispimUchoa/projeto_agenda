from typing import Any
from django.core.exceptions import ValidationError
from django import forms

from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'aqui veio do init'
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuario'
    )


    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name', 'phone',
            'email', 'description', 'category',
            )
                
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Escreva aqui',
                },
                
            )
        }

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome deve ser diferente do segundo',
                code='invalid'
            )
            self.add_error(
                'first_name',
                msg
            )

            self.add_error(
                'last_name',
                msg
            )

        return super().clean()
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        
        return first_name