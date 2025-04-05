from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'location', 'working_hours', 'email']


User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
