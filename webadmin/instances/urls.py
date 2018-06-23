from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Instances'),
    path('<int:instanceId>/', views.detail, name='detail'),
]