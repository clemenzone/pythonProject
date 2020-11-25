from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.charField()
    password = forms.charField(widget=forms.PasswordInput)
