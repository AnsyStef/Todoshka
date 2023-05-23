from .models import *
from django import forms
from django.forms import ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = Note
        priority_list = (('1','2','3'),)
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
            'group_name': forms.TextInput(attrs={'id': 'group_name'}),
            'group_password': forms.PasswordInput(attrs={'id': 'group_password'})
        }
        fields = ['group_password', 'group_name']

class LoginForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'email': forms.TextInput(attrs={'id': 'username', 'placeholder':'Эл. почта', 'class':'input100'}),
            'password': forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Пароль', 'class':'input100'})
        }
        
        exclude = ('group',)


class UserChangeForm(ModelForm):
    class Meta:
        model = UserChange
        widgets = {
            'email': forms.TextInput(attrs={'id': 'email', 'placeholder':'Эл. почта', 'class':'input100'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Отоброжаемое имя', 'class': 'input100'}),
            'password': forms.PasswordInput(attrs={'id': 'password', 'placeholder': 'Пароль', 'class':'input100'})
        }
        fields = ['email', 'username', 'password']
