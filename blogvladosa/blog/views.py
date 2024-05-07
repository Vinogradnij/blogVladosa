from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import models


class BlogHome(generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
    }

    def get_queryset(self):
        return models.Post.published.all()


def category(request, cat_slug):
    return HttpResponse('CategoryPage')


def detail(request, post_pk):
    return render(request, 'blog/detail.html', context={'post_pk': post_pk})


class CreatePost(generic.CreateView):
    model = models.Post
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'content', 'category', 'is_published']
    extra_context = {
        'title': 'Создание поста'
    }


def archive(request):
    return HttpResponse('ArchivePage')


def login(request):
    return HttpResponse('LoginPage')


def logout(request):
    return HttpResponse('LogoutPage')
