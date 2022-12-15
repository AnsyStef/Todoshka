from .models import Notes, User
from django import forms
from django.forms import ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = Notes
        priority_list = (('1','2'),)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-class', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-class', 'id': 'descript'}),
            'priority': forms.Select(choices=priority_list, attrs={'class': 'form-class', 'id': 'priority'}),
            'is_public': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox', 'id': 'public'}),
            'creator': forms.HiddenInput(attrs={'class': 'form-class', 'id': 'creator'})
        }
        exclude = ('worker','date', 'status')


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username'}),
            'password': forms.TextInput(attrs={'id': 'password'})
        }