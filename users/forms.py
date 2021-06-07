from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.models import User


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput())
    email = forms.EmailField()
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
