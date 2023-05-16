from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('modpack/', include('modpack.urls')),
    path("rr/", lambda _: redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
]
