# forms.py

from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label='Enter username', max_length=100)