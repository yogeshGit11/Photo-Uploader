from cProfile import label
from dataclasses import fields
from dis import dis
from email import message
from faulthandler import disable
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class signupform(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='New Password')

    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                label='Re-Type Password')

    class Meta:
        model=User
        fields=['username','email',]

        labels={'email':'Email'}

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            }

class signinform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class newphoto(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark '}))

    desc=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control border border-dark '}))

    class Meta:
        model=uppic
        fields=['username','pic','desc']
        labels={'desc':'Description'}

        
class contactpage(forms.ModelForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-dark'}),label='Your Name')
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control border border-dark'}))
    mob=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control border border-dark'}),label='Mobile Number')
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control border border-dark','rows':4}))

    class Meta:
        model=cont
        fields=['username','email','mob','message']

        #labels={'username':'Your Name','mob':'Mobile Number'}