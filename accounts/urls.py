from django.urls import include, path

from . import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("logout/", views.CustomLogoutView.as_view(), name='logout'),
    path("", include("django.contrib.auth.urls")),
]
