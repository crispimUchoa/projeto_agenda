from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
      required=True,
    )

    email = forms.EmailField(
      required=True
    )


    class Meta:
        model = User
        fields = (
              'first_name', 'last_name', 'email',
              'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
      required=True,
    )

    email = forms.EmailField(
      required=True
    )

    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False
    )

    password2 = forms.CharField(
        label='Confirmação de senha',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Digite a senha novamente',
        required=False
    )

    class Meta:
        model = User
        fields = (
              'first_name', 'last_name', 'email',
              'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        print(cleaned_data.get('email'))

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('As senhas não batem'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid ')
                )
        return email


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
           try:
               password_validation.validate_password(password1)
           except ValidationError as errors:
               self.add_error(
                   'password1',
                   ValidationError(errors)
               )
        return password1