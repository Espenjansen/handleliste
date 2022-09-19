from atexit import register
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('create', views.create_list, name="create"),
    path('<int:id>', views.shoppingdetail, name="shoppingdetail"),
    path('view', views.view, name="view"),
    path('', views.homepage, name="index"),
    
]