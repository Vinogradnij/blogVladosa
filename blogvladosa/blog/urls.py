from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('post/<int:post_pk>/', views.BlogDetail.as_view(), name='detail'),
    path('category/<slug:cat_slug>', views.BlogCategory.as_view(), name='category'),
    path('create/', views.BlogCreate.as_view(), name='create'),
    path('archive/', views.archive, name='archive'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logit'),
]
