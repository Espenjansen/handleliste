from base import views
from django.urls import path

urlpatterns = [
    path("home", views.listcategoryview.as_view())
]