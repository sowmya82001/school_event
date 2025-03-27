from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Event

# Signup Form
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

# Event Form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
