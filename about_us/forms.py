from django import forms 
from .models import Announcements
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.admin.models import LogEntry
from django.db import models



class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'description', 'picture']


class CustomRegistrationForm(UserCreationForm):
    # Add your custom fields here
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        # Specify the model and fields to use for the form
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# CustomUser = get_user_model()

# class CustomLogEntry(LogEntry):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

#     class Meta:
#         proxy = True



