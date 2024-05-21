from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from . import models
from . import utils


class BlogHome(utils.DataMixin, generic.ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        return self.get_mixin_context(
            context=super().get_context_data(**kwargs),
            title='Главная страница',
        )

    def get_queryset(self):
        return models.Post.published.all()


class BlogCategory(utils.DataMixin, generic.ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'cat_slug'

    def get_context_data(self, **kwargs):
        category = models.Category.objects.get(slug=self.kwargs['cat_slug'])
        return self.get_mixin_context(
            context=super().get_context_data(**kwargs),
            title=f'Категория: {category}',
        )

    def get_queryset(self, **kwargs):
        return models.Post.published.filter(category__slug=self.kwargs['cat_slug'])


class BlogDetail(utils.DataMixin, generic.DetailView):
    model = models.Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            context=context,
            title=context['post'],
        )


class CreatePost(utils.DataMixin, generic.CreateView):
    model = models.Post
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:home')
    fields = ['title', 'content', 'category', 'is_published']

    def get_context_data(self, **kwargs):
        return self.get_mixin_context(
            context=super().get_context_data(**kwargs),
            title='Создание поста',
        )


def archive(request):
    return HttpResponse('ArchivePage')


def login(request):
    return HttpResponse('LoginPage')


def logout(request):
    return HttpResponse('LogoutPage')
