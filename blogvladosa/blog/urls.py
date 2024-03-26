from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_pk>/', views.detail, name='detail'),
    path('category/<slug:cat_slug>', views.category, name='category'),
    path('create/', views.CreatePost.as_view(), name='create'),
    path('archive/', views.archive, name='archive'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logit'),
]
