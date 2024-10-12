"""Urls for User API."""

from django.urls import path
from users import views


urlpatterns = [
    path('user/', views.CreateUserView.as_view(), name='create')
]