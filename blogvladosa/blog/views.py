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
        'categories': models.Category.objects.all()
    }

    def get_queryset(self):
        return models.Post.published.all()


def category(request, cat_slug):
    return HttpResponse('CategoryPage')


def detail(request, post_pk):
    return render(request, 'blog/detail.html', context={'post_pk': post_pk})


class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['categories'] = models.Category.objects.all()
        return context


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
