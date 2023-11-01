from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from remainder.models import Todos

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title"]


class TodoChangeForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","status"]
