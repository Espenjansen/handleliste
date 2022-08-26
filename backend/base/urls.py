from atexit import register
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('base/index.html', views.index, name="index")
]