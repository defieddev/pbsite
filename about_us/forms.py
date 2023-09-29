from django import forms 
from .models import Announcements, Profile, Profpic, Birthday, Occupation, Year_Joined, Height, Weight, Age, JerseyNumPic, TinNum, JerseyNum, GcashNum, Team
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class ProfpicForm(forms.ModelForm):
    class Meta:
        model = Profpic
        fields = ['image']

class JerseyNumPicForm(forms.ModelForm):
    class Meta:
        model = JerseyNumPic
        fields = ['image']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['birthday', 'occupation']

class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ['birthday']

class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ['occupation']

class YearJoinedForm(forms.ModelForm):
    class Meta:
        model = Year_Joined
        fields = ['year_joined']

class HeightForm(forms.ModelForm):
    class Meta:
        model = Height
        fields = ['height']

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight']

class AgeForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = ['age']

class TinNumForm(forms.ModelForm):
    class Meta:
        model = TinNum
        fields = ['tin']

class JerseyNumForm(forms.ModelForm):
    class Meta:
        model = JerseyNum
        fields = ['jerseynum']

class GcashNumForm(forms.ModelForm):
    class Meta:
        model = GcashNum
        fields = ['gcashnum']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team']

class AnnouncementsForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'description', 'picture']


class CustomRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        # Specify the model and fields to use for the form
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

