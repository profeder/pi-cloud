from django.urls import path
from .views import natTest

urlpatterns = [
    path('<str:clientId>/<int:port>/test', natTest),
]