from cProfile import label

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cinema_base import models
from cinema_base.models import UsersNotes


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        #model = models.User #обращение не работает из-за пользовательского User
        model = get_user_model()
        fields = ('photo', 'username', 'password1', 'password2')

class NoteForm(forms.ModelForm):
    rating = forms.IntegerField(label='Оценка', widget=forms.NumberInput(attrs={'class': 'form-imput'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}))
    class Meta:
        model = UsersNotes
        fields = ('rating', 'note',)