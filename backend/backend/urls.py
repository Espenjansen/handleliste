from django.contrib import admin
from django.urls import path, include
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('django.contrib.auth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
