from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name','image']