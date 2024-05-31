from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.views import generic
import django.contrib.auth.views as auth_views

from . import forms


class UsersLogin(auth_views.LoginView):
    form_class = auth_views.AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация', 'content_name': 'Авторизация'}


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class UsersRegister(generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация', 'content_name': 'Регистрация'}

    success_url = reverse_lazy('users:login')
