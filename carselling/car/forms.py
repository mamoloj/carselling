from django import forms
from .models import Car , BuyCar

from django.contrib.auth.models import User  





class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name','mobile','make','model','year','condition','price']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control'}),
            'make' : forms.TextInput(attrs={'class': 'form-control'}),
            'model' : forms.TextInput(attrs={'class': 'form-control'}),
            'year' : forms.Select(attrs={'class': 'form-control'}),
            'condition' : forms.Select(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'})

        }



class BuyCarForm(forms.ModelForm):
    class Meta:
        model = BuyCar
        fields = ['name','mobile']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password' :  forms.PasswordInput(attrs={'class': 'form-control'}) ,
        }