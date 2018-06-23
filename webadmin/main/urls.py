from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('accounts/login/', views.login, name='Login'),
]