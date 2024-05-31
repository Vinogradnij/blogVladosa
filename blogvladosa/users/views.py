from django.contrib.auth.views import LoginView, LogoutView, AuthenticationForm
from django.http import HttpResponse,  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


class UsersLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация', 'content_name': 'Авторизация'}


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
