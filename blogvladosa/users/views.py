from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse('LoginPage')


def logout(request):
    return HttpResponse('LogoutPage')
