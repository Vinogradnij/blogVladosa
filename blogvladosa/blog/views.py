from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def home(request):
    return render(request, 'blog/home.html')


def category(request, cat_slug):
    return HttpResponse('CategoryPage')


def detail(request, post_pk):
    return render(request, 'blog/detail.html', context={'post_pk': post_pk})


def create(request):
    return render(request, 'blog/create.html')


def archive(request):
    return HttpResponse('ArchivePage')


def login(request):
    return HttpResponse('LoginPage')


def logout(request):
    return HttpResponse('LogoutPage')
