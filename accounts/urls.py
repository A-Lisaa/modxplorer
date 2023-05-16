from django.urls import include, path

from . import views

app_name = "accounts"
urlpatterns = [
    path("login", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("", include("django.contrib.auth.urls")),
]
