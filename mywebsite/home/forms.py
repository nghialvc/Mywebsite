from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth import login
from . import models

class RegisterForm(forms.Form):
    fullname = forms.CharField(label="Full Name", max_length=500)
    username = forms.CharField(label="Userame", max_length=200)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",max_length=200,widget=forms.PasswordInput())
    repassword = forms.CharField(label="Repeat Password",max_length=200,widget=forms.PasswordInput())

    def clean_repassword(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            repassword = self.cleaned_data['repassword']
            if password==repassword and password:
                return repassword
        raise forms.ValidationError('Your password is unavailable!')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Your username has special character!')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Your username has existed!')

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password'])

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:",max_length=150)
    password = forms.CharField(label="Password:",widget=forms.PasswordInput())

class UploadForm(forms.ModelForm):
    class Meta:
        model = models.ChapInfo
        fields = ("name","chap","content")
    
