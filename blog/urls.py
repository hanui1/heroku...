from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.blog, name='blog'),
    path('newblog/', views.blogpost, name="newblog")
]