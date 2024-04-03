from django import forms

class UsernameForm(forms.Form):
    username = forms.CharField(label='Enter Username', max_length=100)