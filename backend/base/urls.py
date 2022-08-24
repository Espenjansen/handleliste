from django.urls import path
from .views import listShoppingView

urlpatterns = [
    path("", listShoppingView.as_view())
]