from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post_slug>/', views.detail, name='detail'),
    path('category/<slug:cat_slug>', views.category, name='category'),
    path('create/', views.create, name='create'),
    path('archive/', views.archive, name='archive'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logit'),
]
