from .models import Notes, User, Group
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

class GroupForm(ModelForm):
    class Meta:
        model = Group
        widgets = {
            'group_name': forms.TextInput(attrs={'id': 'group_name', 'autocomplete': 'off'}),
            'group_password': forms.PasswordInput(attrs={'id': 'group_password', 'autocomplete': 'off'})
        }
        fields = ['group_password', 'group_name']

class LoginForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'id': 'username'}),
            'password': forms.PasswordInput(attrs={'id': 'password'})
        }
        exclude = ('group',)