from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users),
    path('create/', views.create_user),
    path('get/', views.get_users),
]


