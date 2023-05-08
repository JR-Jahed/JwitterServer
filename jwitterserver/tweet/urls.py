from django.urls import path
from . import views

urlpatterns = [
    path('create_tweet/', views.create_tweet),
    path('get_tweets/', views.get_tweets),
]
