from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from users.forms import RegistrationUserForm
from django.contrib.auth.models import User


# Create your views here.
def logout_view(request):
    """Класс авторизации"""
    logout(request)
    return redirect('index')


def register(request):
    """Класс регистрации"""
    if request.method != 'POST':
        form = RegistrationUserForm()
    else:
        if User.objects.filter(email=request.POST.get('email')):
            messages.error(request, 'Пользователь с данной электронной почтой уже существует!')
            return redirect('register')
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST.get('password1'))
            login(request, authenticated_user)
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
