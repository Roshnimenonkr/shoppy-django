from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text='Your text'
            self.fields['password2'].help_text='Your text'

class signinform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)