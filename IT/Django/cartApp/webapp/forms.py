from django import forms

class LoginForm(forms.Form):
    name=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=100,label="Name")
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")
    cash=forms.IntegerField(label="In hand Cash")
