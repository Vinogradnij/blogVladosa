from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
import django.contrib.auth.views as auth_views


class UsersLogin(auth_views.LoginView):
    form_class = auth_views.AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация', 'content_name': 'Авторизация'}


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))
