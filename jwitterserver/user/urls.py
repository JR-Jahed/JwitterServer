from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users),
    path('create_user/', views.create_user),
    path('login/', views.login),
    path('get_users/', views.get_users),
]


