from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    password_check = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите свой возраст')
