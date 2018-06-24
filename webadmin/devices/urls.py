from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Devices'),
    path('new', views.new, name='Add device'),
]