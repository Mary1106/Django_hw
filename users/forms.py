from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'country', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять из цифр!')
        return phone_number

