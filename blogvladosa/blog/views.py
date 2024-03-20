from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def home(request):
    return HttpResponse('HomePage')


def detail(request):
    return HttpResponse('DetailPage')


def create(request):
    return HttpResponse('CreatePage')


def archive(request):
    return HttpResponse('ArchivePage')


def login(request):
    return HttpResponse('LoginPage')


def logout(request):
    return HttpResponse('LogoutPage')
